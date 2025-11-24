---
id: bs4
name: BeautifulSoup
category: Backend
icon: fa-code
color: text-green-300
tag: Scraper
status: learning
level: working
next: Scraping ético y legal
---

# BeautifulSoup

Parser HTML para extraer datos de webs.

## Por qué en minerOS

Cuando necesitas sacar información de páginas web (precios, artículos, datos públicos) de forma estructurada.

## Casos de uso

- Scraping de precios
- Extracción de artículos
- Monitoreo de cambios web

## Código ejemplo

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
titulo = soup.find('h1').text
```

## Proyectos que lo usan

- farmaIA v5.0 (scraping CIMA AEMPS)
- Web Scraper IA (experimental)
