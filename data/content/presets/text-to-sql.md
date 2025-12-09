---
desc: Text-to-SQL - Pregunta a tu BD en lenguaje natural
flow: Pregunta → LLM genera SQL → Ejecuta → Muestra
id: text-to-sql
name: "\U0001F52E Oráculo de Datos"
tools:
- fastapi
- claude
- python
- sqlite
- htmx
useCase: Farmacia, Fiscalidad
---

# Text-to-SQL - Pregunta a tu BD en lenguaje natural

Interfaz en lenguaje natural para bases de datos SQL que permite hacer consultas complejas sin conocer SQL.

## Descripción

Escribe "¿cuántas facturas recibí en enero?" y el sistema genera el SQL, lo ejecuta y muestra los resultados en formato legible.

## Casos de uso

- Consultas a base de datos de farmacia
- Análisis de facturas y gastos
- Reporting automático

## Stack técnico

1. **FastAPI**: Backend y API
2. **Claude API**: Generación de SQL desde lenguaje natural
3. **Python**: Validación y ejecución segura
4. **SQLite**: Base de datos
5. **HTMX**: Interfaz dinámica

## Proyectos que lo usan

- farmaIA v6.0 (planeado - consultas naturales)
- DocMine-Fiscal v2.0 (futuro - analytics)