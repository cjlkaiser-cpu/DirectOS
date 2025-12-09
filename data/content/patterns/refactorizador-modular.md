---
category: refactoring
emoji: "\U0001F3D7️"
flow:
- python
- fastapi
- loguru
flowDesc: Script → Analiza → Separa módulos → Estructura limpia
id: refactorizador-modular
name: Refactorizador Modular
problem: Tienes un script prueba.py de 300 líneas que funciona, pero es un caos.
prompt: 'Actúa como Arquitecto de Software. Toma este código monolítico y refactorízalo
  siguiendo la arquitectura limpia de minerOS. Sepáralo en: routers/ (endpoints),
  services/ (lógica pura), y core/ (configuración). Usa inyección de dependencias
  y Pydantic para validación. Entrégame la estructura de archivos final.'
---

# Refactorizador Modular

Tienes un script prueba.py de 300 líneas que funciona, pero es un caos.

## Prompt

Actúa como Arquitecto de Software. Toma este código monolítico y refactorízalo siguiendo la arquitectura limpia de minerOS. Sepáralo en: routers/ (endpoints), services/ (lógica pura), y core/ (configuración). Usa inyección de dependencias y Pydantic para validación. Entrégame la estructura de archivos final.

## Flujo

Script → Analiza → Separa módulos → Estructura limpia

## Stack técnico

python, fastapi, loguru