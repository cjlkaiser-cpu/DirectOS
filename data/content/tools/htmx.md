---
id: htmx
name: HTMX
category: Frontend
icon: fa-bolt
color: text-yellow-400
tag: Interactividad
status: learning
level: working
next: WebSockets con HTMX
---

# HTMX

Superpoderes para HTML. AJAX sin JavaScript complejo.

## Por qué en minerOS

Convierte tus botones y formularios en dinámicos (sin recargar página) conectando directo con Python. Es la alternativa KISS a React.

## Casos de uso

- Búsqueda en vivo
- Carga infinita de fotos
- Edición inline de datos

## Código ejemplo

```html
<button hx-post='/api/procesar' hx-target='#resultado' hx-swap='innerHTML'>
  Analizar Imagen
</button>
```

## Proyectos que lo usan

- DirectOS v7.0 (búsqueda dinámica - futuro)
- PhotoMine v2.0 (planeado para validación)
