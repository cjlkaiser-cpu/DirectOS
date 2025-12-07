---
id: flow-delay
name: Flow Delay
category: Flow
icon: fa-clock
color: text-purple-400
tag: Esperar
status: new
level: solid
next: Output File para guardar
isFlow: true
---

# Flow Delay

Pausa el pipeline durante un tiempo especificado.

## Por qué en minerOS

Rate limiting y sincronización. Esperar entre llamadas a APIs, dar tiempo a procesos externos, o programar secuencias.

## Casos de uso

- Esperar 1s entre llamadas a API (rate limit)
- Dar 5s para que archivo se escriba completamente
- Pausa de 30s antes de verificar resultado
- Debounce para evitar duplicados

## Código ejemplo

```python
import asyncio
import time

def flow_delay(data, seconds=1, mode='fixed'):
    """Pausa el pipeline"""

    if mode == 'fixed':
        # Espera fija
        time.sleep(seconds)

    elif mode == 'random':
        # Espera aleatoria (anti-bot)
        import random
        wait = random.uniform(seconds * 0.5, seconds * 1.5)
        time.sleep(wait)

    elif mode == 'exponential':
        # Backoff exponencial (para retries)
        attempt = data.get('_retry_count', 0)
        wait = seconds * (2 ** attempt)
        time.sleep(min(wait, 60))  # Max 60s

    return data  # Pass through
```

## Tips aprendidos

- Usar delays cortos (1-5s) para rate limiting
- Exponential backoff para retries
- Loggear cuánto tiempo se esperó

## Proyectos que lo usan

- DirectOS v10.1 (Pipeline Builder)
