---
id: videonotes
name: VideoNotes
version: v1.0
status: production
stack:
  - python
  - flask
  - ollama
  - whisper
repo: ~/Projects/videonotes
description: Herramienta para transcribir y resumir videos de YouTube usando IA local.
---

# VideoNotes v1.0

Herramienta KISS para transcribir videos de YouTube y generar notas resumidas usando IA local (Ollama) o Claude Code.

## Flujo de trabajo

1. Arrastrar URL de YouTube a la interfaz web
2. Extraer subtitulos (o transcribir con Whisper si no hay)
3. Resumir con Ollama (llama3.2) automaticamente o con Claude Code (manual)
4. Guardar nota en HTML con formato didactico
5. Indice de videos vistos con opciones de exportar/borrar

## Comandos principales

```bash
# Iniciar servidor
python videonotes.py --server

# Procesar video manual
python videonotes.py "https://youtube.com/watch?v=..."

# App nativa (Desktop)
open ~/Desktop/VideoNotes.app
```

## Arquitectura

```
videonotes/
├── videonotes.py         # CLI + logica principal
├── server.py             # Flask REST API
├── templates/
│   ├── index.html        # Interfaz web drag&drop
│   └── nota.html         # Template nota individual
├── output/
│   ├── index.html        # Indice generado
│   ├── videos.json       # Base de datos
│   └── *.html            # Notas individuales
└── VideoNotes.app        # App nativa macOS (Desktop)
```

### Stack tecnico

- **Backend:** Python + Flask
- **Extraccion:** yt-dlp (subtitulos) + Whisper (audio)
- **IA:** Ollama (llama3.2 local) o Claude Code (manual HITL)
- **Frontend:** HTML + JS vanilla + CSS dark theme
- **Persistencia:** JSON + HTML estatico

## Aprendizajes clave

### Lo que funciono bien

1. Motor dual: Ollama para automatico, Claude Code para mejor calidad
2. Drag&drop simplifica mucho el UX
3. App nativa macOS con notificaciones = experiencia pro

### Problemas resueltos

- PATH de yt-dlp: usar ruta completa de Python
- Servidor en background: usar `&` y `wait $PID`
- Traduccion de transcripciones: integrar Ollama para traducir

### Siguientes pasos

- [ ] Soporte para playlists
- [ ] Busqueda en notas
- [ ] Tags/categorias

## Metricas

- **Videos procesados:** 2+
- **Tiempo por video:** ~30s (subtitulos) / ~2min (Whisper)
- **Formatos export:** HTML, Markdown
