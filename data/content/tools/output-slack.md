---
id: output-slack
name: Output Slack
category: Output
icon: fa-hashtag
color: text-orange-400
tag: Mensaje Slack
status: new
level: learning
next: Flow If para control de flujo
isOutput: true
---

# Output Slack

Envía el resultado del pipeline a un canal de Slack.

## Por qué en minerOS

Integración con equipos. Notificaciones en tiempo real a canales de proyecto o alertas.

## Casos de uso

- Notificar deploys exitosos
- Alertar errores al canal #ops
- Compartir métricas diarias
- Avisar de tareas completadas

## Código ejemplo

```python
import requests

def send_slack(channel, message, webhook_url):
    """Envía mensaje a Slack via webhook"""
    payload = {
        "channel": channel,
        "text": message,
        "username": "DirectOS Pipeline",
        "icon_emoji": ":robot_face:"
    }

    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200

# Uso
send_slack(
    "#pipelines",
    "Pipeline completado: 42 documentos procesados",
    SLACK_WEBHOOK_URL
)
```

## Tips aprendidos

- Crear webhook en Slack App settings
- Usar emojis para categorizar mensajes
- Incluir links a resultados

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
