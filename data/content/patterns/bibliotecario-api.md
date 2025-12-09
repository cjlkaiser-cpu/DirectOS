---
category: docs-visual
emoji: "\U0001F4DA"
flow:
- fastapi
- python
- markdown
flowDesc: Código → Extraer endpoints → OpenAPI YAML → /docs automático
id: bibliotecario-api
name: Bibliotecario de API
problem: Tu API funciona pero no tiene documentación para otros devs.
prompt: 'Actúa como API Documentation Specialist. Genera documentación OpenAPI 3.0
  (Swagger) en YAML: Paths con métodos HTTP, Request/Response schemas, Códigos de
  error (400, 404, 500), Ejemplos realistas, Tags por recurso. Bonus: docstring para
  que FastAPI auto-genere /docs.'
---

# Bibliotecario de API

Tu API funciona pero no tiene documentación para otros devs.

## Prompt

Actúa como API Documentation Specialist. Genera documentación OpenAPI 3.0 (Swagger) en YAML: Paths con métodos HTTP, Request/Response schemas, Códigos de error (400, 404, 500), Ejemplos realistas, Tags por recurso. Bonus: docstring para que FastAPI auto-genere /docs.

## Flujo

Código → Extraer endpoints → OpenAPI YAML → /docs automático

## Stack técnico

fastapi, python, markdown