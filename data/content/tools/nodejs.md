---
id: nodejs
name: Node.js
category: Backend
icon: fa-node-js
color: text-green-500
tag: Runtime
status: used
level: working
next: Streams y Workers
---

# Node.js

JavaScript en el servidor. Runtime asíncrono y orientado a eventos.

## Por qué en minerOS

Permite usar JavaScript tanto en frontend como backend. NPM tiene el ecosistema de paquetes más grande del mundo.

## Casos de uso

- Servidor backend con Express
- Scripts de automatización
- APIs REST y WebSockets
- Herramientas CLI

## Código ejemplo

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello from Node.js!');
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});
```

## Proyectos que lo usan

- farmaIA v5.0 (backend completo)
- Web Scraper IA
