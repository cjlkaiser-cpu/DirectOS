---
id: factoria-demo
name: Factoria Demo
version: v1.0
status: demo
stack:
  - flask
  - sqlite
  - faker
  - jinja2
  - bootstrap
repo: github.com/cjlkaiser-cpu/factoria-demo
description: Demo de sistema de gestion para escuela de artes con datos sinteticos (alumnos) y reales (profesores/actividades).
---

# Factoria Demo v1.0

Sistema de gestion completo para Factoria Estudio (escuela de artes). Mezcla datos reales extraidos de la web (profesores, actividades, sedes) con datos sinteticos generados con Faker (alumnos, tutores, inscripciones).

## Origen

Datos reales de https://factoriaestudio.es/ - escuela con 2 sedes (Valdemarín, Conde Orgaz), 11 areas (Musica, Danza, Robotica...), 81 actividades y 30 profesores.

## Features

- **Dashboard** con metricas en tiempo real
- **Gestion de alumnos** con tutores vinculados
- **Inscripciones** por actividad/horario
- **Control de ausencias** con justificaciones
- **Sistema de pagos** con 7 tipos de calculo
- **Motor de facturacion** mensual
- **50 estudiantes sinteticos** con Faker (locale ES)

## Arquitectura

```
factoria-demo/
├── database/
│   ├── schema.sql       # 12 tablas + vistas + índices
│   └── seed_real_data.sql  # Datos reales de la web
├── scripts/
│   ├── init_database.py    # Inicializa BD
│   └── generate_students.py  # Genera 50 alumnos sintéticos
├── app/
│   ├── main.py          # Flask con todas las rutas
│   ├── templates/       # 8 plantillas Jinja2
│   └── static/          # CSS
└── docs/
    └── index.html       # Guia de implementacion (GitHub Pages)
```

### Modelo de datos

12 tablas relacionadas:
- sedes, areas, actividades, profesores
- alumnos, tutores, alumno_tutor
- inscripciones, ausencias
- proveedores_config, pagos_mensuales, facturas

### 7 tipos de pago

```python
tipo_pago = ['hora', 'alumno', 'fijo', 'mixto_alumno',
             'mixto_porcentaje', 'mixto_hora_alumno']
```

## Stack tecnico

- **Backend:** Flask + Jinja2
- **Database:** SQLite (12 tablas)
- **Frontend:** Bootstrap 5
- **Datos sinteticos:** Faker (ES locale)
- **Deploy demo:** Local (127.0.0.1:5000)
- **Deploy docs:** GitHub Pages

## Aprendizajes clave

### Lo que funciono bien

1. **Mezcla datos reales + sinteticos** - realismo sin exponer datos personales
2. **Faker con locale ES** - nombres, DNI, direcciones españolas realistas
3. **Flask host='127.0.0.1'** - evita error 403 en algunos navegadores

### Problemas resueltos

- **HTTP 403 en localhost:5000**: Cambiar `app.run()` a `host='127.0.0.1', use_reloader=False`
- **Datos realistas**: Extraer profesores/actividades de web real vs inventar todo

### Siguientes pasos (produccion)

- [ ] Migrar a PostgreSQL/Supabase
- [ ] Añadir autenticacion (Flask-Login)
- [ ] Panel admin con permisos
- [ ] Notificaciones email (ausencias, pagos)
- [ ] Backup automatico

## Metricas

- **Sedes:** 2
- **Areas:** 11
- **Actividades:** 81
- **Profesores:** 30
- **Alumnos sinteticos:** 50
- **Tutores:** 60
- **Inscripciones:** 78
- **Tablas BD:** 12
