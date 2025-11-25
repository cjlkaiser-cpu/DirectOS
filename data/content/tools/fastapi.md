---
id: fastapi
name: FastAPI
category: Backend
icon: fa-server
color: text-green-400
tag: API Server
status: learning
level: working
next: WebSockets en FastAPI
---

# FastAPI

El servidor web más rápido y moderno para Python.

## Por qué en minerOS

Es asíncrono (no se bloquea mientras la IA piensa). Genera documentación automática (/docs) para que pruebes tus funciones.

## Casos de uso

- Backend de DirectOS
- API de búsqueda
- Endpoint de ingesta de archivos

## Código ejemplo

```python
from fastapi import FastAPI
app = FastAPI()

@app.get('/items/{id}')
async def read_item(id: int):
    return {'item_id': id}
```

## Proyectos que lo usan

- DirectOS v8.0 (backend completo)
