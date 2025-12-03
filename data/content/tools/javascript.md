---
id: javascript
name: JavaScript
category: Frontend
icon: fa-js
color: text-yellow-300
tag: Language
status: used
level: working
next: ES2024 features
---

# JavaScript

El lenguaje de la web. Funciona en navegadores y servidores (Node.js).

## Por qué en minerOS

Ubicuo en desarrollo web. Permite crear interfaces interactivas sin frameworks pesados.

## Casos de uso

- Interactividad web
- Manipulación del DOM
- Fetch API para llamadas HTTP
- localStorage para persistencia
- Event handling

## Código ejemplo

```javascript
// Fetch + async/await
async function loadData() {
  try {
    const res = await fetch('/api/items');
    const data = await res.json();

    data.items.forEach(item => {
      const el = document.createElement('div');
      el.textContent = item.name;
      document.body.appendChild(el);
    });
  } catch (err) {
    console.error('Error:', err);
  }
}

// Event listener
document.getElementById('btn').addEventListener('click', loadData);
```

## Proyectos que lo usan

- DirectOS (frontend completo)
- farmaIA (frontend interactivo)
- Dashboard Seguimiento
