---
id: httpx
name: HTTPX
category: Backend
icon: fa-globe
color: text-cyan-400
tag: HTTP Client
status: new
level: exploring
next: HTTPX connection pooling
---

# HTTPX

Cliente HTTP moderno y asíncrono para Python.

## Por qué en minerOS

requests es síncrono y lento. HTTPX es async, soporta HTTP/2 y tiene API idéntica a requests.

## Casos de uso

- Llamadas a APIs externas
- Web scraping async
- Testing de endpoints

## Código ejemplo

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get('https://api.example.com/data')
    data = response.json()
```

## Proyectos que lo usan

- DirectOS v8.0 (planeado - Scout async)
- Web Scraper IA (futuro - scraping paralelo)
