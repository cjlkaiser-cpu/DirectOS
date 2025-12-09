---
desc: RAG Chatbot - Chatea con tus PDFs/Apuntes
flow: Pregunta → Vector → Busca contexto → LLM responde
id: rag-chatbot
name: "\U0001F9E0 Cerebro de Segunda Memoria"
tools:
- fastapi
- sbert
- chroma
- claude
- htmx
useCase: farmaIA, DocMine
---

# RAG Chatbot - Chatea con tus PDFs/Apuntes

Arquitectura de chatbot inteligente que puede responder preguntas sobre tus documentos usando Retrieval-Augmented Generation.

## Descripción

Sistema que combina búsqueda semántica con un LLM para crear un asistente que "conoce" tu documentación personal o de trabajo.

## Casos de uso

- Consultar base de conocimiento de farmacia
- Buscar en documentos fiscales
- Asistente personal de apuntes

## Stack técnico

1. **FastAPI**: Servidor backend
2. **Sentence-BERT**: Vectorización de preguntas y documentos
3. **ChromaDB**: Base de datos vectorial
4. **Claude API**: Generación de respuestas
5. **HTMX**: Interfaz dinámica sin recargar

## Proyectos que lo usan

- farmaIA v5.0 (consulta de interacciones)
- DocMine-Fiscal (búsqueda en facturas)
- DirectOS v6.0 (Knowledge Base)