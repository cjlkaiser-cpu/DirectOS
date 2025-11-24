---
id: api-gateway
title: API Gateway
emoji: 🚪
category: devops
stack:
  - fastapi
  - pydantic
  - loguru
complexity: mid
cost: local
useCase: Exponer herramientas minerOS de forma segura, API unificada.
flowDesc: Request → Auth → Route → Proxy al servicio → Log → Response
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
