---
id: guardian-calidad
name: Guardián de Calidad
emoji: 🛡️
problem: Tienes miedo de tocar el código porque se puede romper.
flow:
  - python
  - sqlite
  - loguru
flowDesc: Código → Analiza → Genera tests → conftest.py + tests/
---

# Guardián de Calidad

Tienes miedo de tocar el código porque se puede romper.

## Prompt

Actúa como Ingeniero de QA experto en Pytest. Genera una suite de tests completa para este módulo. Incluye conftest.py con fixtures para mockear la base de datos y las llamadas a APIs externas (como OpenAI). Cubre casos de éxito, casos de error y casos borde.

## Flujo

Código → Analiza → Genera tests → conftest.py + tests/

## Stack técnico

python, sqlite, loguru
