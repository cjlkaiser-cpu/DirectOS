---
id: flow-if
name: Flow If
category: Flow
icon: fa-code-branch
color: text-purple-400
tag: Condicional
status: new
level: solid
next: Flow Loop para repeticiones
isFlow: true
---

# Flow If

Bifurca el pipeline según una condición.

## Por qué en minerOS

Control de flujo inteligente. Procesar diferente según el contenido, tamaño, o tipo de archivo.

## Casos de uso

- Si es PDF → extraer texto, si es imagen → OCR
- Si tamaño > 10MB → comprimir primero
- Si contiene error → notificar, sino → continuar
- Si es urgente → procesar inmediato

## Código ejemplo

```python
def flow_if(data, condition, true_branch, false_branch):
    """Bifurca el flujo según condición"""

    # Evaluar condición
    if condition == 'is_pdf':
        result = data.get('file', '').endswith('.pdf')
    elif condition == 'has_error':
        result = 'error' in data
    elif condition == 'size_gt_10mb':
        result = data.get('size', 0) > 10_000_000
    else:
        result = eval(condition)  # Condición custom

    if result:
        return execute_node(true_branch, data)
    else:
        return execute_node(false_branch, data)
```

## Tips aprendidos

- Usar condiciones simples y claras
- Siempre definir rama else (aunque sea pass)
- Loggear qué rama se tomó

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
