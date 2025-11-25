---
id: smart-scraper
name: 🕵️ Agente Curador
useCase: Investigación, precios
tools:
  - python
  - bs4
  - claude
  - sqlite
  - loguru
flow: URL → HTML → LLM extrae JSON → Guarda
---

# Smart Scraper - Extrae datos limpios de webs

Web scraper inteligente que usa LLM para extraer datos estructurados de páginas HTML sin necesidad de selectores CSS manuales.

## Descripción

En lugar de escribir selectores CSS frágiles, el scraper usa Claude para entender la estructura de la página y extraer la información relevante.

## Casos de uso

- Monitoreo de precios de productos
- Extracción de datos de investigación
- Agregación de noticias

## Stack técnico

1. **Python**: Orquestación
2. **BeautifulSoup**: Parsing HTML
3. **Claude API**: Extracción inteligente de datos
4. **SQLite**: Almacenamiento estructurado
5. **Loguru**: Logging de errores y cambios

## Proyectos que lo usan

- Web Scraper IA (experimental)
- farmaIA v5.0 (scraping CIMA AEMPS)
