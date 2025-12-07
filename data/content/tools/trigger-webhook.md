---
id: trigger-webhook
name: Trigger Webhook
category: Trigger
icon: fa-globe
color: text-emerald-400
tag: HTTP POST
status: used
level: solid
next: Integración con servicios externos
isTrigger: true
---

# Trigger Webhook

Endpoint HTTP POST que ejecuta el pipeline al recibir una petición.

## Por qué en minerOS

Integración con servicios externos: GitHub, Slack, Zapier, n8n. Cuando ocurre un evento externo, el pipeline se activa.

## Casos de uso

- GitHub push → ejecutar tests
- Slack comando → generar reporte
- Formulario web → procesar datos
- Zapier/n8n → orquestar flujos

## Código ejemplo

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/api/trigger/{workflow_id}")
async def webhook_trigger(workflow_id: str, request: Request):
    """Endpoint para activar pipelines via HTTP"""
    payload = await request.json()

    # Ejecutar pipeline con datos del webhook
    result = execute_pipeline(
        workflow_id=workflow_id,
        input_data=payload
    )

    return {"status": "triggered", "workflow": workflow_id}

# Uso externo:
# curl -X POST http://localhost:8000/api/trigger/mi-pipeline \
#      -H "Content-Type: application/json" \
#      -d '{"file": "documento.pdf"}'
```

## Tips aprendidos

- Validar payload antes de ejecutar
- Usar tokens de autenticación para seguridad
- Responder rápido y procesar en background

## Proyectos que lo usan

- DirectOS v10.0 (Automatizaciones)
