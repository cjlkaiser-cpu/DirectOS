---
id: flow-loop
name: Flow Loop
category: Flow
icon: fa-repeat
color: text-purple-400
tag: Repetir
status: new
level: solid
next: Flow Delay para pausas
isFlow: true
---

# Flow Loop

Repite una sección del pipeline N veces o hasta condición.

## Por qué en minerOS

Procesamiento por lotes. Iterar sobre lista de archivos, reintentar operaciones fallidas, o polling.

## Casos de uso

- Procesar cada archivo de una carpeta
- Reintentar hasta 3 veces si falla
- Polling cada 5 segundos hasta respuesta
- Iterar páginas de API paginada

## Código ejemplo

```python
def flow_loop(data, mode='count', count=3, condition=None):
    """Repite nodos del pipeline"""

    results = []

    if mode == 'count':
        # Repetir N veces
        for i in range(count):
            result = execute_next_nodes(data, iteration=i)
            results.append(result)

    elif mode == 'foreach':
        # Iterar sobre lista
        items = data.get('items', [])
        for item in items:
            result = execute_next_nodes(item)
            results.append(result)

    elif mode == 'until':
        # Repetir hasta condición
        while not eval(condition):
            result = execute_next_nodes(data)
            results.append(result)
            if len(results) > 100:  # Safety limit
                break

    return results
```

## Tips aprendidos

- Siempre poner límite máximo de iteraciones
- Loggear progreso (procesando 5/20...)
- Considerar procesamiento paralelo para listas grandes

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
