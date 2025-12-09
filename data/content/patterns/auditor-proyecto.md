---
category: comodin
emoji: "\U0001F50E"
flow:
- python
- loguru
- markdown
flowDesc: Proyecto → Escanear → Analizar → Informe ejecutivo
id: auditor-proyecto
name: Auditor de Proyecto
problem: Heredas un proyecto y no sabes por dónde empezar.
prompt: 'Actúa como Tech Lead haciendo due diligence. Escanea este proyecto y genera
  informe: 1) Stack detectado (lenguajes, frameworks, DBs), 2) Estructura de carpetas,
  3) Puntos de entrada (main.py, index.html), 4) Dependencias críticas, 5) Red flags:
  código muerto, secrets expuestos, deuda técnica, 6) Siguiente paso recomendado.'
---

# Auditor de Proyecto

Heredas un proyecto y no sabes por dónde empezar.

## Prompt

Actúa como Tech Lead haciendo due diligence. Escanea este proyecto y genera informe: 1) Stack detectado (lenguajes, frameworks, DBs), 2) Estructura de carpetas, 3) Puntos de entrada (main.py, index.html), 4) Dependencias críticas, 5) Red flags: código muerto, secrets expuestos, deuda técnica, 6) Siguiente paso recomendado.

## Flujo

Proyecto → Escanear → Analizar → Informe ejecutivo

## Stack técnico

python, loguru, markdown