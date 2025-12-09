---
desc: Video Search - Encuentra momentos por texto o imagen
flow: Video → Escenas + Audio → Indexa → Busca
id: video-search
name: "\U0001F985 Ojo de Halcón"
tools:
- ffmpeg
- whisper
- clip
- sqlite
- fastapi
useCase: VideoMine, PhotoMine++
---

# Video Search - Encuentra momentos por texto o imagen

Sistema de búsqueda multimodal que permite encontrar escenas específicas en videos usando descripción textual o imágenes de referencia.

## Descripción

Combina análisis de audio (transcripción) y visual (embeddings de frames) para hacer vídeos completamente buscables.

## Casos de uso

- Encontrar escena específica en entrevista larga
- Buscar momentos en vlogs personales
- Localizar referencias en cursos en vídeo

## Stack técnico

1. **FFmpeg**: Extracción de frames y audio
2. **Whisper**: Transcripción de audio
3. **CLIP**: Vectorización de frames
4. **SQLite**: Índice de timestamps y metadata
5. **FastAPI**: API de búsqueda

## Proyectos que lo usan

- VideoMine (proyecto futuro)
- PhotoMine v2.0 (extensión para vídeos)