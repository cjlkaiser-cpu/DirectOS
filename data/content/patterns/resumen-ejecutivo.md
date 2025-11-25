---
id: resumen-ejecutivo
name: Resumen Ejecutivo
emoji: 📋
problem: Al final del día no recuerdas qué guardaste en tus carpetas.
flow:
  - python
  - watchdog
  - ocr
  - clip
  - claude
  - markdown
flowDesc: Watchdog → Clasifica archivos → IA resume → DIARIO.md
---

# Resumen Ejecutivo

Al final del día no recuerdas qué guardaste en tus carpetas.

## Prompt

Actúa como Asistente Personal. Escanea los archivos creados/modificados en las últimas 24 horas en la carpeta especificada. Para cada archivo, extrae su "esencia" (título, tipo, tema principal). Genera un resumen narrativo de 1 párrafo: "Hoy guardaste 3 facturas, 2 notas de voz sobre X, y 1 snippet de código para Y".

## Flujo

Watchdog → Clasifica archivos → IA resume → DIARIO.md

## Stack técnico

python, watchdog, ocr, clip, claude, markdown
