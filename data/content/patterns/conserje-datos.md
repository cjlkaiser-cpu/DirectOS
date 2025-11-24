---
id: conserje-datos
name: Conserje de Datos
emoji: 🧹
problem: Tienes un CSV/JSON sucio con fechas mixtas, nulos y duplicados.
flow:
  - python
  - sqlite
flowDesc: CSV sucio → Pandas → Limpieza → CSV limpio + reporte
---

# Conserje de Datos

Tienes un CSV/JSON sucio con fechas mixtas, nulos y duplicados.

## Prompt

Actúa como Data Engineer. Genera script de limpieza con Pandas: 1) Estandarizar fechas a ISO 8601, 2) Manejar nulos (media para numéricos, "UNKNOWN" para strings), 3) Eliminar duplicados por columnas clave, 4) Detectar outliers (>3 std), 5) Exportar CSV limpio + quality_report.json.

## Flujo

CSV sucio → Pandas → Limpieza → CSV limpio + reporte

## Stack técnico

python, sqlite
