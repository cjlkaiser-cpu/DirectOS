"""
Scheduler Service - DirectOS v9.0 Agent Mode
=============================================
Ejecuta pipelines en horarios programados (estilo cron).

Casos de uso:
- Ejecutar backup cada día a las 3am
- Procesar logs cada hora
- Limpiar archivos temporales semanalmente
- Sincronizar datos cada 15 minutos

Formato de horarios (cron-like):
- "0 9 * * *" = cada día a las 9am
- "*/15 * * * *" = cada 15 minutos
- "0 0 * * 0" = cada domingo a medianoche
"""

import json
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Callable, Optional
from dataclasses import dataclass, field
from loguru import logger

try:
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from apscheduler.triggers.cron import CronTrigger
    from apscheduler.triggers.interval import IntervalTrigger
    SCHEDULER_AVAILABLE = True
except ImportError:
    SCHEDULER_AVAILABLE = False
    logger.warning("apscheduler no instalado - pip install apscheduler")


@dataclass
class ScheduledTask:
    """Tarea programada"""
    id: str
    name: str
    pipeline_id: str
    schedule_type: str  # "cron" o "interval"
    schedule: str  # cron expression o intervalo en segundos
    enabled: bool = True
    last_run: float = 0
    next_run: float = 0
    run_count: int = 0
    last_status: str = ""  # success, error, pending
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "pipeline_id": self.pipeline_id,
            "schedule_type": self.schedule_type,
            "schedule": self.schedule,
            "enabled": self.enabled,
            "last_run": self.last_run,
            "last_run_formatted": datetime.fromtimestamp(self.last_run).isoformat() if self.last_run else None,
            "next_run": self.next_run,
            "next_run_formatted": datetime.fromtimestamp(self.next_run).isoformat() if self.next_run else None,
            "run_count": self.run_count,
            "last_status": self.last_status,
            "created_at": self.created_at
        }


class SchedulerService:
    """
    Servicio de programación de tareas.

    Uso:
        scheduler = SchedulerService()
        scheduler.add_task(ScheduledTask(...))
        scheduler.start()

        # Cuando se ejecute:
        scheduler.on_task_run = lambda task: executor.execute(task.pipeline_id)
    """

    def __init__(self, config_path: Path = None):
        self.config_path = config_path or Path.home() / ".directos" / "schedules.json"
        self.tasks: Dict[str, ScheduledTask] = {}
        self.scheduler: Optional[AsyncIOScheduler] = None
        self.running = False

        # Callback cuando se ejecuta una tarea
        self.on_task_run: Optional[Callable[[ScheduledTask], None]] = None

        # Cargar config
        self._load_config()

        logger.info(f"SchedulerService inicializado. Tareas: {len(self.tasks)}")

    def _load_config(self):
        """Carga tareas programadas desde archivo"""
        if self.config_path.exists():
            try:
                data = json.loads(self.config_path.read_text())
                for t in data.get("tasks", []):
                    task = ScheduledTask(**t)
                    self.tasks[task.id] = task
            except Exception as e:
                logger.error(f"Error cargando schedules: {e}")

    def _save_config(self):
        """Guarda configuración"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        data = {"tasks": [t.to_dict() for t in self.tasks.values()]}
        self.config_path.write_text(json.dumps(data, indent=2))

    def _create_trigger(self, task: ScheduledTask):
        """Crea trigger de APScheduler según tipo"""
        if task.schedule_type == "cron":
            # Parse cron expression: "min hour day month dow"
            parts = task.schedule.split()
            if len(parts) == 5:
                return CronTrigger(
                    minute=parts[0],
                    hour=parts[1],
                    day=parts[2],
                    month=parts[3],
                    day_of_week=parts[4]
                )
            else:
                logger.error(f"Cron expression inválida: {task.schedule}")
                return None

        elif task.schedule_type == "interval":
            # Intervalo en segundos
            try:
                seconds = int(task.schedule)
                return IntervalTrigger(seconds=seconds)
            except ValueError:
                # Intentar parsear como "15m", "1h", "1d"
                value = task.schedule[:-1]
                unit = task.schedule[-1].lower()
                multipliers = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
                if unit in multipliers:
                    return IntervalTrigger(seconds=int(value) * multipliers[unit])
                logger.error(f"Intervalo inválido: {task.schedule}")
                return None

        return None

    async def _run_task(self, task_id: str):
        """Ejecuta una tarea programada"""
        task = self.tasks.get(task_id)
        if not task:
            return

        logger.info(f"[SCHEDULER] Ejecutando tarea: {task.name}")

        task.last_run = time.time()
        task.run_count += 1

        try:
            if self.on_task_run:
                await self.on_task_run(task)
                task.last_status = "success"
            else:
                task.last_status = "no_handler"
                logger.warning("No hay handler configurado para tareas")
        except Exception as e:
            logger.error(f"Error ejecutando tarea {task.name}: {e}")
            task.last_status = "error"

        self._save_config()

    def _schedule_task(self, task: ScheduledTask):
        """Programa una tarea en el scheduler"""
        if not self.scheduler or not task.enabled:
            return

        trigger = self._create_trigger(task)
        if not trigger:
            return

        # Añadir job
        job = self.scheduler.add_job(
            self._run_task,
            trigger=trigger,
            args=[task.id],
            id=task.id,
            name=task.name,
            replace_existing=True
        )

        # Actualizar next_run
        if job.next_run_time:
            task.next_run = job.next_run_time.timestamp()

        logger.info(f"Tarea programada: {task.name} ({task.schedule})")

    def add_task(self, task: ScheduledTask) -> bool:
        """Añade una nueva tarea programada"""
        self.tasks[task.id] = task
        self._save_config()

        if self.running:
            self._schedule_task(task)

        logger.info(f"Tarea añadida: {task.name}")
        return True

    def remove_task(self, task_id: str) -> bool:
        """Elimina una tarea"""
        if task_id not in self.tasks:
            return False

        # Remover del scheduler
        if self.scheduler:
            try:
                self.scheduler.remove_job(task_id)
            except Exception:
                pass

        del self.tasks[task_id]
        self._save_config()

        logger.info(f"Tarea eliminada: {task_id}")
        return True

    def update_task(self, task_id: str, **kwargs) -> bool:
        """Actualiza una tarea"""
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

        self._save_config()

        # Reprogramar si está corriendo
        if self.running:
            try:
                self.scheduler.remove_job(task_id)
            except Exception:
                pass
            if task.enabled:
                self._schedule_task(task)

        return True

    def get_tasks(self) -> List[Dict]:
        """Lista todas las tareas"""
        return [t.to_dict() for t in self.tasks.values()]

    def get_task(self, task_id: str) -> Optional[Dict]:
        """Obtiene una tarea específica"""
        task = self.tasks.get(task_id)
        return task.to_dict() if task else None

    def run_now(self, task_id: str) -> bool:
        """Ejecuta una tarea inmediatamente (fuera de horario)"""
        task = self.tasks.get(task_id)
        if not task:
            return False

        import asyncio
        asyncio.create_task(self._run_task(task_id))
        return True

    def start(self):
        """Inicia el scheduler"""
        if not SCHEDULER_AVAILABLE:
            logger.error("No se puede iniciar: apscheduler no instalado")
            return False

        if self.running:
            logger.warning("Scheduler ya está corriendo")
            return False

        self.scheduler = AsyncIOScheduler()

        # Programar todas las tareas habilitadas
        for task in self.tasks.values():
            if task.enabled:
                self._schedule_task(task)

        self.scheduler.start()
        self.running = True

        logger.info(f"SchedulerService iniciado con {len(self.tasks)} tareas")
        return True

    def stop(self):
        """Detiene el scheduler"""
        if self.scheduler:
            self.scheduler.shutdown(wait=False)
            self.scheduler = None

        self.running = False
        logger.info("SchedulerService detenido")

    def get_status(self) -> Dict:
        """Estado del servicio"""
        pending_jobs = 0
        if self.scheduler:
            pending_jobs = len(self.scheduler.get_jobs())

        return {
            "running": self.running,
            "scheduler_available": SCHEDULER_AVAILABLE,
            "tasks_count": len(self.tasks),
            "enabled_tasks": len([t for t in self.tasks.values() if t.enabled]),
            "pending_jobs": pending_jobs
        }


# ========================================
# Presets de schedules comunes
# ========================================

SCHEDULE_PRESETS = {
    "daily_morning": {
        "name": "Cada día a las 9am",
        "schedule_type": "cron",
        "schedule": "0 9 * * *"
    },
    "daily_night": {
        "name": "Cada día a las 11pm",
        "schedule_type": "cron",
        "schedule": "0 23 * * *"
    },
    "hourly": {
        "name": "Cada hora",
        "schedule_type": "cron",
        "schedule": "0 * * * *"
    },
    "every_15min": {
        "name": "Cada 15 minutos",
        "schedule_type": "interval",
        "schedule": "15m"
    },
    "weekly_sunday": {
        "name": "Cada domingo a medianoche",
        "schedule_type": "cron",
        "schedule": "0 0 * * 0"
    },
    "monthly": {
        "name": "Primer día del mes",
        "schedule_type": "cron",
        "schedule": "0 0 1 * *"
    }
}


def parse_human_schedule(text: str) -> Optional[Dict]:
    """
    Parsea expresiones de horario en lenguaje natural.

    Ejemplos:
        "cada día a las 9am" -> {"type": "cron", "schedule": "0 9 * * *"}
        "cada 15 minutos" -> {"type": "interval", "schedule": "15m"}
        "los lunes a las 10am" -> {"type": "cron", "schedule": "0 10 * * 1"}
    """
    text = text.lower().strip()

    # Patrones simples
    if "cada hora" in text:
        return {"schedule_type": "cron", "schedule": "0 * * * *"}

    if "cada día" in text or "diario" in text or "daily" in text:
        # Buscar hora
        import re
        hour_match = re.search(r'(\d{1,2})\s*(am|pm)?', text)
        if hour_match:
            hour = int(hour_match.group(1))
            if hour_match.group(2) == 'pm' and hour < 12:
                hour += 12
            return {"schedule_type": "cron", "schedule": f"0 {hour} * * *"}
        return {"schedule_type": "cron", "schedule": "0 9 * * *"}

    if "cada" in text and "minuto" in text:
        import re
        min_match = re.search(r'cada\s+(\d+)\s*minuto', text)
        if min_match:
            mins = int(min_match.group(1))
            return {"schedule_type": "interval", "schedule": f"{mins}m"}

    if "semanal" in text or "cada semana" in text:
        return {"schedule_type": "cron", "schedule": "0 9 * * 1"}  # Lunes 9am

    return None
