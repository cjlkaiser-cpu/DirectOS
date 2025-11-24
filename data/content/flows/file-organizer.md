---
id: file-organizer
title: File Organizer
emoji: 📁
category: automation
stack:
  - python
  - ocr
  - ollama
  - loguru
  - watchdog
complexity: low
cost: local
useCase: Ordenar facturas, organizar documentos recibidos.
flowDesc: Watchdog detecta → OCR si es imagen → Ollama clasifica → Mueve
---

# File Organizer

Limpia la carpeta Descargas automáticamente con IA.

## Descripción

Organizador inteligente que clasifica y mueve archivos automáticamente basándose en su contenido.

## Stack técnico

- **Python**: orquestación
- **Tesseract OCR**: extracción de texto de imágenes
- **Ollama**: clasificación inteligente
- **Loguru**: logging de movimientos
- **Watchdog**: monitoreo de carpetas

## Flujo

1. Watchdog monitorea ~/Downloads
2. Por extensión: PDF/imágenes → OCR extrae texto
3. Ollama clasifica: factura, recibo, documento, imagen, otro
4. Mueve a carpetas: facturas/, recibos/, docs/, fotos/
5. Renombra con patrón: YYYY-MM-DD_tipo_descripcion
6. Log de cada movimiento

## Casos de uso reales

- Organización automática de Descargas
- Clasificación de facturas recibidas
- Limpieza de Escritorio

Modo --dry-run para probar antes de activar
