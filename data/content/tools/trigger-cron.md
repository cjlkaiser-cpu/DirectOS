---
id: trigger-cron
name: Trigger Cron
category: Trigger
icon: fa-clock
color: text-emerald-400
tag: Programado
status: used
level: solid
next: Trigger Webhook para integraciones
isTrigger: true
---

# Trigger Cron

Ejecuta el pipeline en horarios programados.

## Por qué en minerOS

Automatiza tareas recurrentes: backups diarios, reportes semanales, sincronización cada hora.

## Casos de uso

- Backups diarios a las 3am
- Reportes semanales los lunes
- Sincronización cada hora
- Limpieza de logs mensual

## Código ejemplo

```python
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

scheduler = BackgroundScheduler()

# Ejemplos de programación
scheduler.add_job(
    execute_pipeline,
    CronTrigger(hour=3, minute=0),  # Diario a las 3:00
    id="daily_backup"
)

scheduler.add_job(
    execute_pipeline,
    CronTrigger(day_of_week='mon', hour=9),  # Lunes 9am
    id="weekly_report"
)

scheduler.add_job(
    execute_pipeline,
    CronTrigger(minute=0),  # Cada hora
    id="hourly_sync"
)
```

## Tips aprendidos

- Usar zonas horarias explícitas
- Evitar solapamiento de ejecuciones largas
- Logging de cada ejecución programada

## Proyectos que lo usan

- DirectOS v10.0 (Automatizaciones)
