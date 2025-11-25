---
id: videomine-search
title: VideoMine Search
emoji: 🎬
category: media
stack:
  - ffmpeg
  - clip
  - whisper
  - chroma
  - fastapi
complexity: high
cost: local
useCase: Buscar en videos familiares, tutoriales, conferencias grabadas.
flowDesc: Video → FFmpeg (frames+audio) → CLIP+Whisper → ChromaDB → API búsqueda
---

# VideoMine Search

Busca el momento exacto en cualquier video por texto.

## Descripción

Sistema de búsqueda multimodal en vídeos que combina análisis visual y de audio para encontrar escenas específicas.

## Stack técnico

- **FFmpeg**: extracción de frames y audio
- **CLIP**: vectorización de frames
- **Whisper**: transcripción de audio con timestamps
- **ChromaDB**: índice multimodal (visual + texto)
- **FastAPI**: API de búsqueda

## Flujo

1. FFmpeg extrae frame cada 5 segundos + audio completo
2. CLIP genera embeddings de cada frame
3. Whisper transcribe audio con timestamps
4. ChromaDB indexa ambos (visual + texto)
5. FastAPI endpoint de búsqueda multimodal
6. Retorna timestamp exacto + thumbnail

## Casos de uso reales

- VideoMine (proyecto futuro)
- Búsqueda en vídeos familiares
- Localización de momentos en cursos
