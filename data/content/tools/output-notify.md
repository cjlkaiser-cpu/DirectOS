---
id: output-notify
name: Output Notify
category: Output
icon: fa-bell
color: text-orange-400
tag: Notificación
status: new
level: solid
next: Output Email para emails
isOutput: true
---

# Output Notify

Envía una notificación del sistema cuando el pipeline termina.

## Por qué en minerOS

Feedback inmediato al usuario. Cuando un pipeline largo termina, recibes una notificación en macOS.

## Casos de uso

- Notificar fin de procesamiento
- Alertar de errores
- Confirmar backup completado
- Avisar de nuevo archivo detectado

## Código ejemplo

```python
import subprocess

def notify(title, message, sound=True):
    """Envía notificación nativa de macOS"""
    script = f'''
    display notification "{message}" with title "{title}"
    '''
    if sound:
        script += ' sound name "default"'

    subprocess.run(['osascript', '-e', script])

# Uso
notify("Pipeline Completado", "Se procesaron 15 documentos")
```

## Tips aprendidos

- Usar sonido para notificaciones importantes
- Mantener mensajes cortos (máx 2 líneas)
- Incluir conteo o resumen en el mensaje

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
