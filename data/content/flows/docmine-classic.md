---
id: docmine-classic
title: DocMine Classic
emoji: 📄
category: knowledge
stack:
  - fastapi
  - python
  - chroma
  - ollama
complexity: low
cost: local
useCase: Consultar manuales técnicos, contratos, documentación interna.
flowDesc: Documento → Chunking → Embeddings → ChromaDB → Query → LLM responde
---

# DocMine Classic

Chat con tus PDFs y documentos. RAG simple pero efectivo.

## Descripción

Sistema de Retrieval-Augmented Generation que te permite hacer preguntas a tu documentación en PDF como si hablaras con un experto.

## Stack técnico

- **FastAPI**: endpoint para subir PDFs
- **Python**: orquestación y chunking
- **ChromaDB**: base de datos vectorial
- **Ollama (llama3)**: generación de respuestas

## Flujo

1. Subir PDFs via FastAPI
2. PyMuPDF extrae texto
3. Chunking con overlap (500 chars, 50 overlap)
4. Sentence-BERT genera embeddings
5. ChromaDB persiste vectors
6. Query → búsqueda semántica → LLM responde con contexto

## Casos de uso reales

- DocMine-Fiscal (consulta de facturas)
- farmaIA (búsqueda en prospectos)
- Manuales técnicos de minerOS
