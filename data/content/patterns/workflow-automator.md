---
category: meta
emoji: "\U0001F916"
flow:
- python
- watchdog
- loguru
flowDesc: Describir flujo → Watchdog detecta → Acción → Log
id: workflow-automator
name: Workflow Automator
problem: Haces lo mismo manualmente cada día (renombrar, mover, procesar).
prompt: 'Actúa como Automation Engineer. Dado este flujo manual, genera un script
  Python con Watchdog que: 1) Detecte archivos nuevos por patrón (*.pdf, *.jpg), 2)
  Ejecute la acción automáticamente, 3) Loguee cada operación con Loguru, 4) Tenga
  modo --dry-run para probar. Sin dependencias innecesarias. Local-first.'
---

# Workflow Automator

Haces lo mismo manualmente cada día (renombrar, mover, procesar).

## Prompt

Actúa como Automation Engineer. Dado este flujo manual, genera un script Python con Watchdog que: 1) Detecte archivos nuevos por patrón (*.pdf, *.jpg), 2) Ejecute la acción automáticamente, 3) Loguee cada operación con Loguru, 4) Tenga modo --dry-run para probar. Sin dependencias innecesarias. Local-first.

## Flujo

Describir flujo → Watchdog detecta → Acción → Log

## Stack técnico

python, watchdog, loguru