---
id: gestor-entorno
name: Gestor de Entorno
emoji: ⚙️
problem: Tienes API keys y rutas hardcodeadas en el código.
flow:
  - python
  - fastapi
  - loguru
flowDesc: Código → Identificar config → .env + Settings → Validación
---

# Gestor de Entorno

Tienes API keys y rutas hardcodeadas en el código.

## Prompt

Actúa como DevOps Engineer. Analiza este script e identifica variables de configuración: API Keys, rutas, URLs, puertos, feature flags. Refactoriza usando python-dotenv + Pydantic Settings. Genera .env.example con placeholders. Añade validación (app no arranca si falta ANTHROPIC_API_KEY).

## Flujo

Código → Identificar config → .env + Settings → Validación

## Stack técnico

python, fastapi, loguru
