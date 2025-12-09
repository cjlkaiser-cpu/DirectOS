---
category: media
complexity: mid
cost: local
desc: Organiza 10.000 fotos automáticamente sin tocarlas.
emoji: "\U0001F5BC️"
flowDesc: Watchdog detecta → CLIP analiza → SQLite metadata → HTML5 galería
id: smart-gallery
prompt: 'Actúa como Photo Engineer. Sistema Smart Gallery:

  1. Watchdog monitorea carpeta de fotos

  2. CLIP genera tags automáticos (top 10 conceptos)

  3. SQLite guarda: path, hash, tags, fecha EXIF, GPS

  4. HTML5 galería estática con filtros por tag

  5. Búsqueda semántica por texto

  6. No mueve archivos, solo indexa

  Incluye detección de duplicados por hash perceptual.'
stack:
- python
- clip
- sqlite
- html
- watchdog
title: Smart Gallery
useCase: PhotoMine v2, organizar biblioteca familiar, portfolio.
---

# Smart Gallery

Organiza 10.000 fotos automáticamente sin tocarlas.

## Descripción

Sistema de organización automática de fotos que indexa sin mover archivos, usando tags automáticos generados por IA.

## Stack técnico

- **Python**: orquestación
- **CLIP**: generación de tags automáticos
- **SQLite**: metadata (path, hash, tags, EXIF, GPS)
- **HTML5**: galería estática con filtros
- **Watchdog**: monitoreo de nuevas fotos

## Flujo

1. Watchdog monitorea carpeta de fotos
2. CLIP genera tags automáticos (top 10 conceptos)
3. SQLite guarda metadata sin mover archivos
4. HTML5 galería estática con filtros por tag
5. Búsqueda semántica por texto
6. Detección de duplicados por hash perceptual

## Casos de uso reales

- PhotoMine v1.4 (1,361 fotos procesadas)
- Organización de biblioteca familiar
- Portfolio de fotografía