---
desc: Auto-Tagging - Organiza archivos por contenido
flow: Detecta archivo → Analiza → Clasifica → Mueve
id: auto-tagger
name: "\U0001F47B Clasificador Fantasma"
tools:
- watchdog
- clip
- ocr
- chroma
- python
useCase: Descargas, Escritorio
---

# Auto-Tagging - Organiza archivos por contenido

Sistema que monitorea carpetas y clasifica automáticamente archivos (imágenes, PDFs) según su contenido visual y textual.

## Descripción

Observa carpetas como Descargas y automáticamente analiza, clasifica y organiza archivos nuevos en carpetas temáticas.

## Casos de uso

- Organización automática de Descargas
- Clasificación de capturas de pantalla
- Limpieza del Escritorio

## Stack técnico

1. **Watchdog**: Monitoreo de carpetas
2. **CLIP**: Análisis visual de imágenes
3. **Tesseract OCR**: Extracción de texto de imágenes
4. **ChromaDB**: Búsqueda semántica de categorías
5. **Python**: Lógica de clasificación y movimiento

## Proyectos que lo usan

- PhotoMine v2.0 (planeado - auto-ingesta)
- Experimento de organización Desktop (prueba de concepto)