---
id: sqlite
name: SQLite
category: Storage
icon: fa-table
color: text-blue-300
tag: Relacional
status: used
level: solid
next: PostgreSQL para concurrencia
---

# SQLite

Base de datos SQL en un archivo único.

## Por qué en minerOS

Perfecta para metadatos estructurados (fechas, nombres, rutas). Es robusta, rápida y no necesita servidor.

## Casos de uso

- Índice de archivos
- Registro de usuarios
- Logs estructurados

## Código ejemplo

```python
import sqlite3
con = sqlite3.connect('mineros.db')
con.execute('SELECT * FROM docs WHERE fecha > ?', ('2024-01-01',))
```

## Proyectos que lo usan

- PhotoMine v1.4 (8 tablas relacionadas)
- DocMine-Fiscal (5 tablas, 93K€ procesados)
- farmaIA v5.0 (99 medicamentos + 79 interacciones)
- Factoria Demo (12 tablas + vistas + indices, sistema gestion escuela)
