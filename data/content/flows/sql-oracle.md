---
category: automation
complexity: mid
cost: api
desc: Pregunta a tu base de datos en lenguaje natural.
emoji: "\U0001F52E"
flowDesc: Pregunta → Claude genera SQL → Valida → Ejecuta → Formatea respuesta
id: sql-oracle
prompt: 'Actúa como Data Engineer. Sistema Text-to-SQL:

  1. FastAPI recibe pregunta en español

  2. Inyecta schema de tablas en prompt

  3. Claude genera SQL (solo SELECT, no modificaciones)

  4. Regex valida que no haya DROP/DELETE/UPDATE

  5. Ejecuta query y formatea resultado

  6. Cachea queries frecuentes

  Incluye ejemplos few-shot en el prompt.'
stack:
- fastapi
- claude
- pydantic
- sqlite
title: SQL Oracle
useCase: Dashboard de ventas sin saber SQL, reportes ad-hoc.
---

# SQL Oracle

Pregunta a tu base de datos en lenguaje natural.

## Descripción

Sistema text-to-SQL que permite hacer consultas complejas a bases de datos usando lenguaje natural en español.

## Stack técnico

- **FastAPI**: API de consultas
- **Claude API**: generación de SQL
- **Pydantic**: validación de queries
- **SQLite**: base de datos

## Flujo

1. FastAPI recibe pregunta en español
2. Inyecta schema de tablas en prompt
3. Claude genera SQL (solo SELECT, no modificaciones)
4. Regex valida que no haya DROP/DELETE/UPDATE
5. Ejecuta query y formatea resultado
6. Cachea queries frecuentes

## Casos de uso reales

- farmaIA v6.0 (consultas a inventario)
- DocMine-Fiscal (analytics de gastos)
- Dashboards sin conocimiento SQL

Incluye ejemplos few-shot en el prompt