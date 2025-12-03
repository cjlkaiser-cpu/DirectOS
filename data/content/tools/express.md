---
id: express
name: Express.js
category: Backend
icon: fa-server
color: text-gray-400
tag: Web Framework
status: used
level: working
next: Middleware avanzado
---

# Express.js

Framework web minimalista para Node.js. El estándar de facto para APIs.

## Por qué en minerOS

Simple, flexible y con enorme ecosistema de middleware. Perfecto para APIs REST rápidas.

## Casos de uso

- APIs REST
- Servidores web
- Middleware de autenticación
- Proxy y routing

## Código ejemplo

```javascript
const express = require('express');
const app = express();

app.use(express.json());

app.get('/api/items', (req, res) => {
  res.json({ items: ['a', 'b', 'c'] });
});

app.post('/api/items', (req, res) => {
  const { name } = req.body;
  res.status(201).json({ created: name });
});

app.listen(3000);
```

## Proyectos que lo usan

- farmaIA v5.0 (API + SSE streaming)
