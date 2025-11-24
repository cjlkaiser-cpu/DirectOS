---
id: alpine
name: Alpine.js
category: Frontend
icon: fa-code
color: text-teal-400
tag: Reactividad
status: new
level: exploring
next: Aprende basics de Alpine
---

# Alpine.js

JavaScript minimalista para interacciones en el navegador.

## Por qué en minerOS

Para cuando necesitas abrir un modal, un menú desplegable o pestañas sin llamar al servidor. Pesa poquísimo.

## Casos de uso

- Modales de confirmación
- Tabs del Dashboard
- Toggles de visibilidad

## Código ejemplo

```html
<div x-data='{ open: false }'>
  <button @click='open = true'>Abrir</button>
  <span x-show='open'>Hola!</span>
</div>
```

## Proyectos que lo usan

- DirectOS v7.0 (planeado para v8.0)
- PhotoMine v2.0 (alternativa a vanilla JS)
