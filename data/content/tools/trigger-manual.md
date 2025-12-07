---
id: trigger-manual
name: Trigger Manual
category: Trigger
icon: fa-play-circle
color: text-emerald-400
tag: Ejecutar Ahora
status: used
level: solid
next: Trigger File para automatización
isTrigger: true
---

# Trigger Manual

Ejecuta el pipeline manualmente con un clic.

## Por qué en minerOS

El punto de entrada más simple para ejecutar pipelines. Ideal para testing, demos y ejecución bajo demanda.

## Casos de uso

- Testing de pipelines
- Ejecución bajo demanda
- Demos y presentaciones
- Debugging de flujos

## Código ejemplo

```python
# Click en el botón "Ejecutar Pipeline" para iniciar
# El trigger manual no requiere configuración

def on_manual_trigger():
    """Se ejecuta cuando el usuario hace click en Ejecutar"""
    pipeline = get_current_pipeline()
    return execute_pipeline(pipeline)
```

## Tips aprendidos

- Usar para probar pipelines antes de automatizarlos
- Ideal para flujos que se ejecutan esporádicamente
- Combinar con logs para debugging

## Proyectos que lo usan

- DirectOS v10.0 (Automatizaciones)
