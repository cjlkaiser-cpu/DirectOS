---
category: data-api
emoji: "\U0001F3DB️"
flow:
- fastapi
- python
- sqlite
flowDesc: Dominio → Identificar recursos → Diseñar rutas → Schemas
id: api-architect
name: API Architect
problem: Sabes qué necesitas pero no cómo diseñar los endpoints.
prompt: 'Actúa como API Designer experto en REST. Dado este dominio de negocio, diseña
  una API RESTful completa: 1) Recursos y rutas (GET/POST/PUT/DELETE), 2) Esquemas
  Pydantic de request/response, 3) Códigos HTTP específicos (201, 204, 404, 422),
  4) Ejemplo curl de cada endpoint. Estilo FastAPI, listo para implementar.'
---

# API Architect

Sabes qué necesitas pero no cómo diseñar los endpoints.

## Prompt

Actúa como API Designer experto en REST. Dado este dominio de negocio, diseña una API RESTful completa: 1) Recursos y rutas (GET/POST/PUT/DELETE), 2) Esquemas Pydantic de request/response, 3) Códigos HTTP específicos (201, 204, 404, 422), 4) Ejemplo curl de cada endpoint. Estilo FastAPI, listo para implementar.

## Flujo

Dominio → Identificar recursos → Diseñar rutas → Schemas

## Stack técnico

fastapi, python, sqlite