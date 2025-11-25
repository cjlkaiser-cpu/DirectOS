---
id: claude
name: Claude API
category: IA Model
icon: fa-comments
color: text-orange-400
tag: LLM Cloud
status: used
level: solid
next: Prompt engineering avanzado
---

# Claude API

Razonamiento y generación de texto avanzado.

## Por qué en minerOS

Para tareas complejas: resumir, analizar errores, generar código. Scout usa Claude para diagnosticar problemas.

## Casos de uso

- Análisis de errores (Scout)
- Resúmenes inteligentes
- Generación de código

## Código ejemplo

```python
from anthropic import Anthropic
client = Anthropic()
response = client.messages.create(
  model='claude-sonnet-4-20250514',
  messages=[{'role': 'user', 'content': prompt}]
)
```

## Proyectos que lo usan

- DirectOS v6.0 (Scout - análisis errores)
- Todos los proyectos minerOS (asistente desarrollo)
