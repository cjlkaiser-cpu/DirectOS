---
id: documentador-fantasma
name: Documentador Fantasma
emoji: 👻
problem: Tu código funciona pero no tiene documentación.
flow:
  - python
  - claude
  - markdown
flowDesc: Código → AST extrae estructura → LLM documenta → docs/
---

# Documentador Fantasma

Tu código funciona pero no tiene documentación.

## Prompt

Actúa como Technical Writer. Lee este módulo Python usando AST y genera: 1) Docstrings en formato Google Style para cada función, 2) Un README.md con: descripción, instalación, uso básico, y ejemplos. 3) Un diagrama ASCII del flujo principal. No inventes funcionalidad - documenta solo lo que existe.

## Flujo

Código → AST extrae estructura → LLM documenta → docs/

## Stack técnico

python, claude, markdown
