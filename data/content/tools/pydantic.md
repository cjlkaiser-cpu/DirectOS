---
id: pydantic
name: Pydantic
category: Backend
icon: fa-shield-halved
color: text-red-400
tag: Validación
status: new
level: exploring
next: Pydantic v2 avanzado
---

# Pydantic

Control de calidad para tus datos.

## Por qué en minerOS

Define cómo deben ser tus datos (ej: 'La edad debe ser un número'). Si algo falla, te avisa antes de romper la base de datos.

## Casos de uso

- Validar JSON de entrada
- Configuración (.env)
- Esquemas de DB

## Código ejemplo

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    email: str
    es_admin: bool = False
```

## Proyectos que lo usan

- DirectOS v6.0 (modelos de API)
- farmaIA v5.0 (validación de medicamentos)
