---
category: knowledge
complexity: low
cost: local
desc: Chat con tus PDFs y documentos. RAG simple pero efectivo.
emoji: "\U0001F4C4"
flowDesc: Documento → Chunking → Embeddings → ChromaDB → Query → LLM responde
id: docmine-classic
prompt: 'Actúa como Arquitecto RAG. Implementa un pipeline DocMine:

  1. FastAPI endpoint para subir PDFs

  2. PyMuPDF para extraer texto

  3. Chunking con overlap (500 chars, 50 overlap)

  4. Sentence-BERT para embeddings

  5. ChromaDB para persistencia

  6. Ollama (llama3) para respuestas

  Entrega código modular en services/, routers/.'
stack:
- fastapi
- python
- chroma
- ollama
title: DocMine Classic
useCase: Consultar manuales técnicos, contratos, documentación interna.
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