"""
Watchdog Service - DirectOS v9.0 Agent Mode
============================================
Monitorea directorios y ejecuta pipelines cuando detecta archivos nuevos.

Casos de uso:
- Detectar PDFs nuevos en ~/Downloads → ejecutar OCR pipeline
- Detectar imágenes en ~/Photos/Import → procesar con CLIP
- Detectar .mp3 en ~/Podcasts → transcribir con Whisper

Arquitectura:
1. Configurar watches (directorio + patrón + pipeline)
2. Watchdog detecta eventos del filesystem
3. Filtra por patrón (*.pdf, *.mp3, etc.)
4. Encola archivo para procesamiento
5. Ejecuta pipeline asociado
"""

import asyncio
import fnmatch
import json
import time
import threading
from pathlib import Path
from typing import Dict, List, Callable, Optional
from dataclasses import dataclass, field
from queue import Queue
from loguru import logger

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileMovedEvent
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False
    Observer = None
    FileSystemEventHandler = object  # Dummy base class
    FileCreatedEvent = None
    FileMovedEvent = None
    logger.warning("watchdog no instalado - pip install watchdog")


@dataclass
class WatchConfig:
    """Configuración de un watch"""
    id: str
    name: str
    directory: str
    patterns: List[str]  # ["*.pdf", "*.jpg"]
    pipeline_id: str
    enabled: bool = True
    recursive: bool = False
    debounce_seconds: int = 2  # Evitar duplicados
    created_at: float = field(default_factory=time.time)

    def matches(self, filename: str) -> bool:
        """Verifica si un archivo coincide con los patrones"""
        for pattern in self.patterns:
            if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                return True
        return False

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "directory": self.directory,
            "patterns": self.patterns,
            "pipeline_id": self.pipeline_id,
            "enabled": self.enabled,
            "recursive": self.recursive,
            "debounce_seconds": self.debounce_seconds,
            "created_at": self.created_at
        }


@dataclass
class FileEvent:
    """Evento de archivo detectado"""
    path: str
    watch_id: str
    event_type: str  # created, moved
    timestamp: float = field(default_factory=time.time)


class DirectOSEventHandler(FileSystemEventHandler):
    """Handler de eventos de watchdog"""

    def __init__(self, watch: WatchConfig, queue: Queue, seen: Dict):
        self.watch = watch
        self.queue = queue
        self.seen = seen  # Para debouncing
        super().__init__()

    def _should_process(self, path: str) -> bool:
        """Verifica si debemos procesar este archivo"""
        filename = Path(path).name

        # Ignorar archivos temporales y ocultos
        if filename.startswith('.') or filename.startswith('~'):
            return False

        # Verificar patrón
        if not self.watch.matches(filename):
            return False

        # Debouncing - evitar procesar mismo archivo múltiples veces
        now = time.time()
        last_seen = self.seen.get(path, 0)
        if now - last_seen < self.watch.debounce_seconds:
            return False

        self.seen[path] = now
        return True

    def on_created(self, event):
        if event.is_directory:
            return

        if self._should_process(event.src_path):
            logger.info(f"[WATCH] Archivo creado: {event.src_path}")
            self.queue.put(FileEvent(
                path=event.src_path,
                watch_id=self.watch.id,
                event_type="created"
            ))

    def on_moved(self, event):
        if event.is_directory:
            return

        # Para movimientos, nos interesa el destino
        if self._should_process(event.dest_path):
            logger.info(f"[WATCH] Archivo movido a: {event.dest_path}")
            self.queue.put(FileEvent(
                path=event.dest_path,
                watch_id=self.watch.id,
                event_type="moved"
            ))


class WatchdogService:
    """
    Servicio de monitoreo de archivos.

    Uso:
        service = WatchdogService()
        service.add_watch(WatchConfig(...))
        service.start()

        # Cuando se detecte archivo:
        service.on_file_detected = lambda event: executor.execute(...)
    """

    def __init__(self, config_path: Path = None):
        self.config_path = config_path or Path.home() / ".directos" / "watches.json"
        self.watches: Dict[str, WatchConfig] = {}
        self.observers: Dict[str, Observer] = {}
        self.event_queue: Queue = Queue()
        self.seen_files: Dict[str, float] = {}  # path -> timestamp
        self.running = False
        self.processor_thread: Optional[threading.Thread] = None

        # Callbacks
        self.on_file_detected: Optional[Callable[[FileEvent], None]] = None

        # Cargar config guardada
        self._load_config()

        logger.info(f"WatchdogService inicializado. Watches: {len(self.watches)}")

    def _load_config(self):
        """Carga configuración de watches desde archivo"""
        if self.config_path.exists():
            try:
                data = json.loads(self.config_path.read_text())
                for w in data.get("watches", []):
                    config = WatchConfig(**w)
                    self.watches[config.id] = config
            except Exception as e:
                logger.error(f"Error cargando watches: {e}")

    def _save_config(self):
        """Guarda configuración de watches"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"watches": [w.to_dict() for w in self.watches.values()]}
        self.config_path.write_text(json.dumps(data, indent=2))

    def add_watch(self, config: WatchConfig) -> bool:
        """Añade un nuevo watch"""
        # Verificar directorio existe
        watch_dir = Path(config.directory).expanduser()
        if not watch_dir.exists():
            logger.error(f"Directorio no existe: {config.directory}")
            return False

        self.watches[config.id] = config
        self._save_config()

        # Si ya está corriendo, iniciar observer
        if self.running:
            self._start_observer(config)

        logger.info(f"Watch añadido: {config.name} -> {config.directory}")
        return True

    def remove_watch(self, watch_id: str) -> bool:
        """Elimina un watch"""
        if watch_id not in self.watches:
            return False

        # Parar observer si existe
        if watch_id in self.observers:
            self.observers[watch_id].stop()
            del self.observers[watch_id]

        del self.watches[watch_id]
        self._save_config()

        logger.info(f"Watch eliminado: {watch_id}")
        return True

    def update_watch(self, watch_id: str, **kwargs) -> bool:
        """Actualiza configuración de un watch"""
        if watch_id not in self.watches:
            return False

        watch = self.watches[watch_id]
        for key, value in kwargs.items():
            if hasattr(watch, key):
                setattr(watch, key, value)

        self._save_config()

        # Reiniciar observer si está corriendo
        if self.running and watch_id in self.observers:
            self.observers[watch_id].stop()
            del self.observers[watch_id]
            if watch.enabled:
                self._start_observer(watch)

        return True

    def get_watches(self) -> List[Dict]:
        """Lista todos los watches"""
        return [w.to_dict() for w in self.watches.values()]

    def get_watch(self, watch_id: str) -> Optional[Dict]:
        """Obtiene un watch específico"""
        watch = self.watches.get(watch_id)
        return watch.to_dict() if watch else None

    def _start_observer(self, config: WatchConfig):
        """Inicia observer para un watch"""
        if not WATCHDOG_AVAILABLE:
            logger.error("watchdog no disponible")
            return

        if not config.enabled:
            return

        watch_dir = Path(config.directory).expanduser()
        if not watch_dir.exists():
            logger.error(f"Directorio no existe: {config.directory}")
            return

        handler = DirectOSEventHandler(config, self.event_queue, self.seen_files)
        observer = Observer()
        observer.schedule(handler, str(watch_dir), recursive=config.recursive)
        observer.start()

        self.observers[config.id] = observer
        logger.info(f"Observer iniciado para: {config.name}")

    def _process_events(self):
        """Procesa eventos de la cola (thread separado)"""
        while self.running:
            try:
                # Esperar evento con timeout para poder salir
                event = self.event_queue.get(timeout=1.0)

                if self.on_file_detected:
                    try:
                        self.on_file_detected(event)
                    except Exception as e:
                        logger.error(f"Error procesando evento: {e}")

            except Exception:
                # Queue vacía, continuar
                pass

    def start(self):
        """Inicia el servicio de monitoreo"""
        if not WATCHDOG_AVAILABLE:
            logger.error("No se puede iniciar: watchdog no instalado")
            return False

        if self.running:
            logger.warning("Servicio ya está corriendo")
            return False

        self.running = True

        # Iniciar observers para cada watch habilitado
        for config in self.watches.values():
            if config.enabled:
                self._start_observer(config)

        # Iniciar thread procesador
        self.processor_thread = threading.Thread(target=self._process_events, daemon=True)
        self.processor_thread.start()

        logger.info(f"WatchdogService iniciado con {len(self.observers)} observers")
        return True

    def stop(self):
        """Detiene el servicio"""
        self.running = False

        # Parar todos los observers
        for observer in self.observers.values():
            observer.stop()
            observer.join(timeout=2)

        self.observers.clear()

        # Esperar thread procesador
        if self.processor_thread:
            self.processor_thread.join(timeout=2)

        logger.info("WatchdogService detenido")

    def get_status(self) -> Dict:
        """Estado del servicio"""
        return {
            "running": self.running,
            "watchdog_available": WATCHDOG_AVAILABLE,
            "watches_count": len(self.watches),
            "active_observers": len(self.observers),
            "pending_events": self.event_queue.qsize()
        }


# ========================================
# Presets de watches comunes
# ========================================

WATCH_PRESETS = {
    "downloads_pdf": {
        "name": "PDFs en Descargas",
        "directory": "~/Downloads",
        "patterns": ["*.pdf"],
        "description": "Detecta PDFs nuevos en la carpeta de Descargas"
    },
    "downloads_images": {
        "name": "Imágenes en Descargas",
        "directory": "~/Downloads",
        "patterns": ["*.jpg", "*.jpeg", "*.png", "*.webp"],
        "description": "Detecta imágenes nuevas en Descargas"
    },
    "audio_transcription": {
        "name": "Audio para transcribir",
        "directory": "~/Downloads",
        "patterns": ["*.mp3", "*.wav", "*.m4a", "*.ogg"],
        "description": "Detecta archivos de audio para transcribir con Whisper"
    },
    "screenshots": {
        "name": "Capturas de pantalla",
        "directory": "~/Desktop",
        "patterns": ["Screenshot*.png", "Captura*.png"],
        "description": "Detecta capturas de pantalla en el Escritorio"
    }
}
