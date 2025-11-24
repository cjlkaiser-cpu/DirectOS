---
id: docker
name: Docker
category: DevOps
icon: fa-brands fa-docker
color: text-blue-400
tag: Contenedores
status: new
level: exploring
next: Docker Compose multi-container
---

# Docker

Empaqueta tu aplicación para que funcione en cualquier servidor.

## Por qué en minerOS

Tu app funciona en tu Mac pero falla en producción? Docker asegura que el entorno sea idéntico en todas partes.

## Casos de uso

- Desplegar minerOS en servidor
- Entornos reproducibles
- CI/CD

## Código ejemplo

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app"]
```

## Proyectos que lo usan

- DirectOS v8.0 (planeado - deploy en VPS)
- PhotoMine v2.0 (futuro - compartir con equipo)
