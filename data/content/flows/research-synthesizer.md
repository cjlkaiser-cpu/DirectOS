---
category: knowledge
complexity: high
cost: api
desc: Genera informes a partir de múltiples fuentes. Deep research.
emoji: "\U0001F52C"
flowDesc: Tema → Multi-query ChromaDB → Reranking → Claude sintetiza → Markdown
id: research-synthesizer
prompt: 'Actúa como Research Engineer. Crea un sintetizador que:

  1. Reciba un tema de investigación

  2. Genere 5 queries diferentes (Multi-Query RAG)

  3. Busque en ChromaDB con cada query

  4. Reordene por relevancia (cross-encoder)

  5. Pase contexto a Claude con prompt estructurado

  6. Genere informe Markdown con citas

  Output: Informe con secciones, bullet points y fuentes.'
stack:
- python
- chroma
- claude
- markdown
title: Research Synthesizer
useCase: Estado del arte de una tecnología, comparativas, investigación.
---

# Research Synthesizer

Genera informes a partir de múltiples fuentes. Deep research.

## Descripción

Sistema de investigación profunda que genera informes estructurados combinando múltiples fuentes y técnicas de RAG avanzadas.

## Stack técnico

- **Python**: orquestación
- **ChromaDB**: búsqueda vectorial
- **Claude API**: síntesis y generación
- **Markdown**: formato de salida

## Flujo

1. Recibe tema de investigación
2. Genera 5 queries diferentes (Multi-Query RAG)
3. Busca en ChromaDB con cada query
4. Reordena por relevancia (cross-encoder)
5. Pasa contexto a Claude con prompt estructurado
6. Genera informe Markdown con secciones, bullet points y fuentes

## Casos de uso reales

- Knowledge base de minerOS (análisis de tecnologías)
- Comparativas de herramientas
- Informes técnicos para decisiones