---
id: jq
name: jq
category: Process
icon: fa-filter
color: text-amber-400
tag: JSON Parser
status: new
level: exploring
next: jq scripting avanzado
---

# jq

El grep/sed/awk para JSON. Filtra y transforma JSON desde terminal.

## Por qué en minerOS

Tienes un JSON gigante y solo necesitas un campo? jq lo extrae en una línea.

## Casos de uso

- Filtrar respuestas de API
- Transformar datos
- Pipelines de shell

## Código ejemplo

```bash
# Extraer nombres de un JSON
cat data.json | jq '.users[].name'

# Filtrar por condición
jq '.items | map(select(.price < 100))'
```

## Proyectos que lo usan

- Scripts de automatización minerOS
- Debugging de APIs (farmaIA, DirectOS)
