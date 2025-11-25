---
id: text-to-sql
name: 🔮 Oráculo de Datos
useCase: Farmacia, Fiscalidad
tools:
  - fastapi
  - claude
  - python
  - sqlite
  - htmx
flow: Pregunta → LLM genera SQL → Ejecuta → Muestra
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
