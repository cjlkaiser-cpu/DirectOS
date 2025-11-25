---
id: smart-gallery
title: Smart Gallery
emoji: 🖼️
category: media
stack:
  - python
  - clip
  - sqlite
  - html
  - watchdog
complexity: mid
cost: local
useCase: PhotoMine v2, organizar biblioteca familiar, portfolio.
flowDesc: Watchdog detecta → CLIP analiza → SQLite metadata → HTML5 galería
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
