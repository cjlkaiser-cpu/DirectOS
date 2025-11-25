---
id: refactorizador-modular
name: Refactorizador Modular
emoji: 🏗️
problem: Tienes un script prueba.py de 300 líneas que funciona, pero es un caos.
flow:
  - python
  - fastapi
  - loguru
flowDesc: Script → Analiza → Separa módulos → Estructura limpia
---

# Refactorizador Modular

Tienes un script prueba.py de 300 líneas que funciona, pero es un caos.

## Prompt

Actúa como Arquitecto de Software. Toma este código monolítico y refactorízalo siguiendo la arquitectura limpia de minerOS. Sepáralo en: routers/ (endpoints), services/ (lógica pura), y core/ (configuración). Usa inyección de dependencias y Pydantic para validación. Entrégame la estructura de archivos final.

## Flujo

Script → Analiza → Separa módulos → Estructura limpia

## Stack técnico

python, fastapi, loguru
