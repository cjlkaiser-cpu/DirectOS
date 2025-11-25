---
id: traductor-formatos
name: Traductor de Formatos
emoji: 🔄
problem: Necesitas mover datos entre sistemas incompatibles (XML→SQLite).
flow:
  - python
  - sqlite
  - fastapi
flowDesc: Origen → Parse → Transform → Validate → Load → Log
---

# Traductor de Formatos

Necesitas mover datos entre sistemas incompatibles (XML→SQLite).

## Prompt

Actúa como Integration Engineer. Genera script de migración en Python: 1) Parsear origen (lxml para XML, openpyxl para Excel), 2) Transformar al esquema destino, 3) Validar con Pydantic antes de insertar, 4) Manejar errores por registro (no fallar todo por uno), 5) Log de migración: exitosos/fallidos/warnings.

## Flujo

Origen → Parse → Transform → Validate → Load → Log

## Stack técnico

python, sqlite, fastapi
