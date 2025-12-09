---
category: data-api
emoji: "\U0001F5C2️"
flow:
- python
- fastapi
- sqlite
flowDesc: JSON/CSV → Inferir tipos → Generar Pydantic → models.py
id: schema-detective
name: Schema Detective
problem: Recibes un JSON/CSV gigante y necesitas entender su estructura.
prompt: 'Actúa como Data Analyst. Analiza este dataset (JSON/CSV) y genera: 1) Modelo
  Pydantic con tipos inferidos automáticamente, 2) Campos opcionales (Optional[])
  vs requeridos detectados, 3) Valores únicos que deberían ser Enums, 4) Relaciones
  entre entidades si existen. Formato listo para copiar a models.py.'
---

# Schema Detective

Recibes un JSON/CSV gigante y necesitas entender su estructura.

## Prompt

Actúa como Data Analyst. Analiza este dataset (JSON/CSV) y genera: 1) Modelo Pydantic con tipos inferidos automáticamente, 2) Campos opcionales (Optional[]) vs requeridos detectados, 3) Valores únicos que deberían ser Enums, 4) Relaciones entre entidades si existen. Formato listo para copiar a models.py.

## Flujo

JSON/CSV → Inferir tipos → Generar Pydantic → models.py

## Stack técnico

python, fastapi, sqlite