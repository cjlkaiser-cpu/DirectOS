---
category: devops
emoji: "\U0001F331"
flow:
- fastapi
- claude
- python
- sqlite
flowDesc: Esquema → LLM genera JSON → Valida Pydantic → Inserta SQLite
id: semilla-datos
name: Semilla de Datos
problem: Necesitas datos de prueba realistas sin usar datos reales de producción.
prompt: 'Actúa como Ingeniero de Datos. Genera un dataset de prueba con el esquema
  especificado. Los datos deben ser: 1) Coherentes entre sí (edades realistas, nombres
  plausibles), 2) Diversos (cubrir casos borde), 3) En formato JSON/CSV. Incluye al
  menos 100 registros.'
---

# Semilla de Datos

Necesitas datos de prueba realistas sin usar datos reales de producción.

## Prompt

Actúa como Ingeniero de Datos. Genera un dataset de prueba con el esquema especificado. Los datos deben ser: 1) Coherentes entre sí (edades realistas, nombres plausibles), 2) Diversos (cubrir casos borde), 3) En formato JSON/CSV. Incluye al menos 100 registros.

## Flujo

Esquema → LLM genera JSON → Valida Pydantic → Inserta SQLite

## Stack técnico

fastapi, claude, python, sqlite