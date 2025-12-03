---
id: uvicorn
name: Uvicorn
category: Backend
icon: fa-bolt
color: text-green-400
tag: ASGI Server
status: used
level: working
next: Gunicorn + Uvicorn workers
---

# Uvicorn

Servidor ASGI ultrarrápido para Python. El estándar para FastAPI.

## Por qué en minerOS

Servidor de producción para apps async. Hot-reload en desarrollo.

## Casos de uso

- Servir FastAPI/Starlette
- Hot-reload en desarrollo
- Websockets
- HTTP/2

## Código ejemplo

```python
# Ejecutar desde terminal
# uvicorn main:app --reload --port 8000

# O programáticamente
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
```

## Proyectos que lo usan

- DirectOS (backend)
- minerOS v2 Backend
