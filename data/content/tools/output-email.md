---
id: output-email
name: Output Email
category: Output
icon: fa-envelope
color: text-orange-400
tag: Enviar Email
status: new
level: learning
next: Output Slack para mensajería
isOutput: true
---

# Output Email

Envía el resultado del pipeline por email.

## Por qué en minerOS

Distribución automática de resultados. Reportes semanales, alertas, o notificaciones a equipos.

## Casos de uso

- Enviar reporte diario
- Alertar de errores críticos
- Compartir resultados con equipo
- Notificar clientes

## Código ejemplo

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, body, attachments=None):
    """Envía email con resultado del pipeline"""
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = 'pipeline@directos.local'

    msg.attach(MIMEText(body, 'html'))

    # Configurar SMTP (usar variables de entorno)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

    return f"Email enviado a {to}"
```

## Tips aprendidos

- Usar variables de entorno para credenciales
- Validar email antes de enviar
- Incluir resumen en subject

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
