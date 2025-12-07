---
id: trigger-file
name: Trigger File
category: Trigger
icon: fa-folder-open
color: text-emerald-400
tag: Watch Carpeta
status: used
level: solid
next: Trigger Cron para programación
isTrigger: true
---

# Trigger File

Detecta archivos nuevos en una carpeta y ejecuta el pipeline.

## Por qué en minerOS

Automatiza el procesamiento de archivos. Cuando llega un PDF, imagen o documento, el pipeline se ejecuta automáticamente.

## Casos de uso

- Procesar PDFs al llegar a una carpeta
- Transcribir audios automáticamente
- Indexar documentos nuevos
- Convertir formatos de imagen

## Código ejemplo

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def __init__(self, pattern="*.pdf"):
        self.pattern = pattern

    def on_created(self, event):
        if fnmatch(event.src_path, self.pattern):
            execute_pipeline(event.src_path)

# Configuración
watch_path = "/path/to/watch"
pattern = "*.pdf"  # *.mp3, *.jpg, etc.
```

## Tips aprendidos

- Usar patrones específicos (*.pdf, *.mp3) para filtrar
- Configurar debounce para evitar ejecuciones duplicadas
- Mover archivos procesados a carpeta "done"

## Proyectos que lo usan

- DirectOS v10.0 (Automatizaciones)
- DocMine (procesamiento de documentos)
