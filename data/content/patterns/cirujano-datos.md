---
category: robustez
emoji: "\U0001F52C"
flow:
- sqlite
- python
flowDesc: Schema + Query → EXPLAIN → Índices → Query optimizada
id: cirujano-datos
name: Cirujano de Datos
problem: Tus consultas a SQLite empiezan a ir lentas.
prompt: 'Actúa como DBA experto en SQLite. Analiza este esquema y consulta SQL lenta.
  Tareas: 1) Identificar cuellos de botella (table scans, joins sin índice), 2) Sugerir
  índices (CREATE INDEX), 3) Normalizar si hay redundancia, 4) Reescribir query optimizada,
  5) Explicar con EXPLAIN QUERY PLAN.'
---

# Cirujano de Datos

Tus consultas a SQLite empiezan a ir lentas.

## Prompt

Actúa como DBA experto en SQLite. Analiza este esquema y consulta SQL lenta. Tareas: 1) Identificar cuellos de botella (table scans, joins sin índice), 2) Sugerir índices (CREATE INDEX), 3) Normalizar si hay redundancia, 4) Reescribir query optimizada, 5) Explicar con EXPLAIN QUERY PLAN.

## Flujo

Schema + Query → EXPLAIN → Índices → Query optimizada

## Stack técnico

sqlite, python