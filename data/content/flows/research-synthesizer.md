---
id: research-synthesizer
title: Research Synthesizer
emoji: 🔬
category: knowledge
stack:
  - python
  - chroma
  - claude
  - markdown
complexity: high
cost: api
useCase: Estado del arte de una tecnología, comparativas, investigación.
flowDesc: Tema → Multi-query ChromaDB → Reranking → Claude sintetiza → Markdown
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
