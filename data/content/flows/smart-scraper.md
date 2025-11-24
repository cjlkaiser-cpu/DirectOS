---
id: smart-scraper
title: Smart Scraper
emoji: 🕷️
category: automation
stack:
  - python
  - bs4
  - claude
  - sqlite
  - loguru
complexity: mid
cost: api
useCase: Comparador de precios, monitor de BOE, tracking de productos.
flowDesc: URL → HTTPX fetch → Claude extrae JSON → Valida → SQLite
---

# Smart Scraper

Extrae datos estructurados de cualquier web con IA.

## Descripción

Web scraper inteligente que usa LLM para extraer datos sin necesidad de escribir selectores CSS manuales.

## Stack técnico

- **Python**: orquestación
- **BeautifulSoup**: parsing HTML
- **Claude API**: extracción inteligente
- **SQLite**: almacenamiento con histórico
- **Loguru**: logging completo

## Flujo

1. HTTPX con retry y rate limiting
2. BeautifulSoup parsea HTML
3. Claude extrae datos según schema Pydantic definido
4. Validación estricta antes de guardar
5. SQLite con histórico (tracking de cambios)
6. Loguru registra cada operación

## Casos de uso reales

- farmaIA (scraping CIMA AEMPS)
- Monitor de precios
- Tracking de cambios en webs oficiales

Incluye modo --dry-run para testing
