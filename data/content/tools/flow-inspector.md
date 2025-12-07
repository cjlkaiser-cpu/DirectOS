---
id: flow-inspector
name: Inspector
category: Flow
icon: fa-magnifying-glass
color: text-cyan-400
tag: HITL
status: new
level: solid
next: Cualquier nodo de proceso
isFlow: true
---

# Inspector (Human-in-the-Loop)

Pausa el pipeline y muestra un panel didactico con toda la informacion del flujo.

## Por que en DirectOS

Entender como funcionan las automatizaciones. Ver de donde vienen los datos, que se extrae, quien lo hace, y a donde van. Aprender para diseñar mejores flujos.

## Que muestra

- **Origen**: Nodo anterior, carpeta/archivo fuente
- **Proceso**: Herramienta usada, metodo, accion
- **Datos**: Preview del contenido extraido
- **Destino**: Siguiente nodo, que hara con los datos
- **Tip**: Explicacion didactica contextual

## Casos de uso

- Debuggear pipelines paso a paso
- Aprender como funciona cada herramienta
- Validar datos antes de guardarlos
- Editar datos intermedios manualmente

## Codigo ejemplo

```python
def inspector_node(data, context):
    """Pausa y muestra informacion del flujo"""

    # Recopilar info del contexto
    info = {
        "origen": {
            "nodo": context.get("previous_node", "Inicio"),
            "fuente": context.get("source_path", "N/A"),
        },
        "proceso": {
            "herramienta": context.get("tool_name", "N/A"),
            "accion": context.get("action", "N/A"),
        },
        "datos": data[:500] if isinstance(data, str) else str(data)[:500],
        "destino": {
            "nodo": context.get("next_node", "Fin"),
            "accion": context.get("next_action", "N/A"),
        }
    }

    # Mostrar modal y esperar aprobacion
    approved, edited_data = show_inspector_modal(info)

    if not approved:
        raise PipelineStoppedByUser()

    return edited_data if edited_data else data
```

## Tips aprendidos

- Coloca Inspector despues de nodos criticos (extraccion, IA)
- Usa para validar antes de escribir a BD o enviar emails
- El tip didactico te ayuda a elegir mejores herramientas

## Proyectos que lo usan

- DirectOS v10.4 (Pipeline Builder)
