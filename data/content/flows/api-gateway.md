---
category: devops
complexity: mid
cost: local
desc: Unifica todos tus microservicios locales en un solo punto.
emoji: "\U0001F6AA"
flowDesc: Request → Auth → Route → Proxy al servicio → Log → Response
id: api-gateway
prompt: 'Actúa como API Architect. Gateway unificado:

  1. FastAPI como punto de entrada único

  2. Rutas: /photos/* → PhotoMine, /docs/* → DocMine, etc.

  3. Middleware de autenticación (API key simple)

  4. Rate limiting por IP

  5. Loguru registra cada request

  6. Health checks a cada servicio

  7. Swagger unificado en /docs

  Incluye docker-compose para orquestar.'
stack:
- fastapi
- pydantic
- loguru
title: API Gateway
useCase: Exponer herramientas minerOS de forma segura, API unificada.
---

# API Gateway

Unifica todos tus microservicios locales en un solo punto.

## Descripción

Gateway unificado que expone todos los servicios minerOS (PhotoMine, DocMine, etc.) a través de un punto de entrada único con autenticación.

## Stack técnico

- **FastAPI**: punto de entrada único
- **Pydantic**: validación de requests
- **Loguru**: logging de accesos

## Flujo

1. FastAPI como punto de entrada único
2. Rutas: /photos/* → PhotoMine, /docs/* → DocMine, etc.
3. Middleware de autenticación (API key simple)
4. Rate limiting por IP
5. Proxy requests a servicios internos
6. Logging centralizado de todo

## Casos de uso reales

- DirectOS v8.0 (unificar módulos)
- Exposición segura de herramientas
- Dashboard centralizado

Incluye health checks de todos los servicios