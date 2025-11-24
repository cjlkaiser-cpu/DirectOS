---
id: sintetizador-conocimiento
name: Sintetizador de Conocimiento
emoji: 📚
problem: Tienes 50 PDFs sobre un tema y necesitas un resumen coherente.
flow:
  - fastapi
  - chroma
  - python
  - claude
  - html
flowDesc: Tema → ChromaDB busca → Reranking → LLM sintetiza → Informe HTML
---

# Sintetizador de Conocimiento

Tienes 50 PDFs sobre un tema y necesitas un resumen coherente.

## Prompt

Actúa como Investigador Senior. Genera un "Estado del Arte" sobre el tema especificado basándote únicamente en los fragmentos recuperados de mi Knowledge Base local. Estructura el ensayo con: Introducción, Conceptos clave, Evolución histórica, Estado actual, y Conclusiones. Cita las fuentes originales.

## Flujo

Tema → ChromaDB busca → Reranking → LLM sintetiza → Informe HTML

## Stack técnico

fastapi, chroma, python, claude, html
