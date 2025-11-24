---
id: loguru
name: Loguru
category: Backend
icon: fa-list-ul
color: text-slate-400
tag: Logging
status: learning
level: working
next: Loguru rotation avanzado
---

# Loguru

Logging simplificado y bonito para humanos.

## Por qué en minerOS

Deja de usar print(). Loguru te dice dónde, cuándo y por qué falló algo, con colores y guardado automático en archivo.

## Casos de uso

- Depuración de errores
- Historial de operaciones
- Alertas del sistema

## Código ejemplo

```python
from loguru import logger

logger.add('app.log', rotation='1 day')
logger.info('Iniciando proceso...')
logger.error('Error crítico en DB')
```

## Proyectos que lo usan

- DirectOS v6.0 (logs estructurados)
- PhotoMine v1.4 (tracking de procesamiento)
