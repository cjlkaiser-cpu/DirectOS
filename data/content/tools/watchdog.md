---
id: watchdog
name: Watchdog
category: Backend
icon: fa-eye
color: text-amber-400
tag: File Watcher
status: learning
level: working
next: Event handling avanzado
---

# Watchdog

Detecta cambios en carpetas automáticamente.

## Por qué en minerOS

Para pipelines automáticos: cuando guardas un archivo, se procesa solo. Ideal para ingesta continua.

## Casos de uso

- Auto-indexar Descargas
- Procesar fotos nuevas
- Backup automático

## Código ejemplo

```python
from watchdog.observers import Observer
observer = Observer()
observer.schedule(handler, path='./inbox')
```

## Proyectos que lo usan

- PhotoMine v2.0 (planeado - auto-ingesta)
- DocMine-Fiscal (futuro - monitoreo facturas)
