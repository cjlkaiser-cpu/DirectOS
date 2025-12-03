"""
Notifier Service - DirectOS v9.0 Agent Mode
============================================
Sistema de notificaciones para alertar sobre eventos del sistema.

Canales soportados:
- macOS Desktop notifications (nativo)
- In-app notifications (WebSocket/polling)
- Sonido de sistema

Eventos:
- Pipeline completado (éxito/error)
- Archivo detectado por watchdog
- Tarea programada ejecutada
"""

import subprocess
import asyncio
import json
import time
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from collections import deque
from loguru import logger


@dataclass
class Notification:
    """Notificación del sistema"""
    id: str
    type: str  # success, error, warning, info
    title: str
    message: str
    source: str  # executor, watchdog, scheduler
    timestamp: float = field(default_factory=time.time)
    read: bool = False
    data: Dict = field(default_factory=dict)  # Datos adicionales

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "message": self.message,
            "source": self.source,
            "timestamp": self.timestamp,
            "read": self.read,
            "data": self.data
        }


class NotifierService:
    """
    Servicio de notificaciones.

    Uso:
        notifier = NotifierService()
        notifier.notify(
            type="success",
            title="Pipeline completado",
            message="RAG Pipeline ejecutado en 45s"
        )
    """

    def __init__(self, config_path: Path = None):
        self.config_path = config_path or Path.home() / ".directos" / "notifier.json"
        self.notifications: deque = deque(maxlen=100)  # Últimas 100
        self.settings = {
            "desktop_enabled": True,
            "sound_enabled": True,
            "in_app_enabled": True
        }

        # Callbacks para diferentes canales
        self.on_notification: Optional[callable] = None  # Para WebSocket

        self._load_settings()
        logger.info("NotifierService inicializado")

    def _load_settings(self):
        """Carga settings de notificaciones"""
        if self.config_path.exists():
            try:
                data = json.loads(self.config_path.read_text())
                self.settings.update(data.get("settings", {}))
            except Exception as e:
                logger.error(f"Error cargando settings notifier: {e}")

    def _save_settings(self):
        """Guarda settings"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"settings": self.settings}
        self.config_path.write_text(json.dumps(data, indent=2))

    def _send_macos_notification(self, title: str, message: str, sound: bool = True):
        """Envía notificación nativa de macOS usando osascript"""
        try:
            sound_part = 'sound name "Ping"' if sound else ""
            script = f'''
            display notification "{message}" with title "{title}" {sound_part}
            '''
            subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                timeout=5
            )
            logger.debug(f"[NOTIFY] macOS: {title}")
        except Exception as e:
            logger.error(f"Error enviando notificación macOS: {e}")

    def _play_sound(self, sound_type: str = "success"):
        """Reproduce sonido de sistema"""
        sounds = {
            "success": "Glass",
            "error": "Basso",
            "warning": "Sosumi",
            "info": "Pop"
        }
        sound_name = sounds.get(sound_type, "Pop")

        try:
            subprocess.run(
                ["afplay", f"/System/Library/Sounds/{sound_name}.aiff"],
                capture_output=True,
                timeout=3
            )
        except Exception as e:
            logger.debug(f"Error reproduciendo sonido: {e}")

    def notify(
        self,
        type: str,
        title: str,
        message: str,
        source: str = "system",
        data: Dict = None,
        desktop: bool = None,
        sound: bool = None
    ) -> Notification:
        """
        Envía una notificación.

        Args:
            type: success, error, warning, info
            title: Título de la notificación
            message: Mensaje
            source: Origen (executor, watchdog, scheduler)
            data: Datos adicionales
            desktop: Forzar notificación desktop (o usar setting)
            sound: Forzar sonido (o usar setting)

        Returns:
            Notification creada
        """
        notification = Notification(
            id=f"notif_{int(time.time() * 1000)}",
            type=type,
            title=title,
            message=message,
            source=source,
            data=data or {}
        )

        # Guardar en historial
        self.notifications.append(notification)

        # Determinar canales
        send_desktop = desktop if desktop is not None else self.settings["desktop_enabled"]
        play_sound = sound if sound is not None else self.settings["sound_enabled"]

        # Enviar por canales activos
        if send_desktop:
            self._send_macos_notification(
                title,
                message,
                sound=play_sound
            )
        elif play_sound:
            self._play_sound(type)

        # Callback para in-app (WebSocket)
        if self.settings["in_app_enabled"] and self.on_notification:
            try:
                self.on_notification(notification)
            except Exception as e:
                logger.error(f"Error en callback notificación: {e}")

        logger.info(f"[NOTIFY] {type.upper()}: {title} - {message}")
        return notification

    # ========================================
    # Métodos de conveniencia
    # ========================================

    def success(self, title: str, message: str, **kwargs):
        """Notificación de éxito"""
        return self.notify("success", title, message, **kwargs)

    def error(self, title: str, message: str, **kwargs):
        """Notificación de error"""
        return self.notify("error", title, message, **kwargs)

    def warning(self, title: str, message: str, **kwargs):
        """Notificación de advertencia"""
        return self.notify("warning", title, message, **kwargs)

    def info(self, title: str, message: str, **kwargs):
        """Notificación informativa"""
        return self.notify("info", title, message, **kwargs)

    # ========================================
    # Notificaciones específicas de Agent Mode
    # ========================================

    def pipeline_completed(self, pipeline_name: str, status: str, duration: float, run_id: str = None):
        """Notifica que un pipeline terminó"""
        if status == "success":
            self.success(
                title=f"✓ {pipeline_name}",
                message=f"Completado en {duration:.1f}s",
                source="executor",
                data={"run_id": run_id}
            )
        else:
            self.error(
                title=f"✗ {pipeline_name}",
                message=f"Error después de {duration:.1f}s",
                source="executor",
                data={"run_id": run_id}
            )

    def file_detected(self, filename: str, watch_name: str):
        """Notifica archivo detectado por watchdog"""
        self.info(
            title=f"📁 {watch_name}",
            message=f"Nuevo archivo: {filename}",
            source="watchdog"
        )

    def task_executed(self, task_name: str, status: str):
        """Notifica ejecución de tarea programada"""
        if status == "success":
            self.success(
                title=f"⏰ {task_name}",
                message="Tarea ejecutada correctamente",
                source="scheduler"
            )
        else:
            self.error(
                title=f"⏰ {task_name}",
                message="Error ejecutando tarea",
                source="scheduler"
            )

    # ========================================
    # Gestión de notificaciones
    # ========================================

    def get_notifications(self, limit: int = 50, unread_only: bool = False) -> List[Dict]:
        """Lista notificaciones recientes"""
        notifs = list(self.notifications)
        if unread_only:
            notifs = [n for n in notifs if not n.read]
        return [n.to_dict() for n in notifs[-limit:]]

    def mark_read(self, notification_id: str) -> bool:
        """Marca una notificación como leída"""
        for notif in self.notifications:
            if notif.id == notification_id:
                notif.read = True
                return True
        return False

    def mark_all_read(self):
        """Marca todas como leídas"""
        for notif in self.notifications:
            notif.read = True

    def clear(self):
        """Limpia historial de notificaciones"""
        self.notifications.clear()

    def get_unread_count(self) -> int:
        """Cuenta notificaciones no leídas"""
        return sum(1 for n in self.notifications if not n.read)

    def update_settings(self, **kwargs) -> Dict:
        """Actualiza settings de notificaciones"""
        for key, value in kwargs.items():
            if key in self.settings:
                self.settings[key] = value
        self._save_settings()
        return self.settings

    def get_settings(self) -> Dict:
        """Obtiene settings actuales"""
        return self.settings.copy()

    def get_status(self) -> Dict:
        """Estado del servicio"""
        return {
            "notifications_count": len(self.notifications),
            "unread_count": self.get_unread_count(),
            "settings": self.settings
        }


# ========================================
# Test rápido
# ========================================

if __name__ == "__main__":
    notifier = NotifierService()

    # Probar notificación
    notifier.success(
        title="DirectOS v9.0",
        message="Sistema de notificaciones funcionando"
    )
