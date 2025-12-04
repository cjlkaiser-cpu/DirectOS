---
id: educacion-auditiva
name: Educación Auditiva
version: v1.0
status: production
stack:
  - html
  - css
  - javascript
  - tailwindcss
repo: ~/Desktop/curso_armonia/educacion_auditiva.html
description: Aplicación de entrenamiento auditivo para curso de armonía basado en bustena.com.
---

# Educación Auditiva v1.0

Aplicación web para entrenamiento auditivo musical. Parte del curso de armonía con ejercicios de identificación de acordes, intervalos y progresiones.

## Origen

Basado en materiales de bustena.com - Curso de Armonía.

## Features

- **Unidades temáticas**: Organización por conceptos armónicos
- **Ejercicios auditivos**: Audio cards con reproducción integrada
- **Teoría expandible**: Secciones de contenido teórico
- **Progreso trackeable**: Barra de progreso general
- **Responsive**: Sidebar colapsable en móvil
- **Reveal answers**: Sistema de mostrar/ocultar respuestas

## Arquitectura

```
curso_armonia/
└── educacion_auditiva.html  # Single-file app
```

## Stack técnico

- **Frontend:** HTML5 + Tailwind CSS + JavaScript
- **UI:** Dark theme (slate palette)
- **Icons:** Font Awesome 6
- **Fuente:** Inter (Google Fonts)
- **Audio:** HTML5 Audio API

## Aprendizajes clave

### Lo que funcionó bien

1. Tailwind CDN para prototipo rápido
2. Dark theme reduce fatiga visual en sesiones largas
3. Sidebar responsive con overlay

### Diseño

- **Theme:** Dark (slate-950 base)
- **Accent:** Blue-500 para interacciones
- **Success:** Green-500 para audio playing

## Métricas

- **Fuente contenido:** bustena.com
- **Estilo:** Dark mode profesional
- **Target:** Estudiantes de armonía
