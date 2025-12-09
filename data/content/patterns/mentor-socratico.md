---
category: aprendizaje
emoji: "\U0001F393"
flow:
- python
- claude
- htmx
- markdown
flowDesc: PDF/MD → LLM genera quiz → JSON → Interfaz Flashcards
id: mentor-socratico
name: Mentor Socrático
problem: Quieres comprobar si realmente entendiste un documento técnico.
prompt: 'Actúa como profesor universitario experto en evaluación. Lee este documento
  técnico y genera un test de 10 preguntas tipo test (4 opciones, solo 1 correcta).
  Incluye preguntas de comprensión, aplicación y análisis. Devuelve un JSON con: pregunta,
  opciones[], respuesta_correcta, explicacion.'
---

# Mentor Socrático

Quieres comprobar si realmente entendiste un documento técnico.

## Prompt

Actúa como profesor universitario experto en evaluación. Lee este documento técnico y genera un test de 10 preguntas tipo test (4 opciones, solo 1 correcta). Incluye preguntas de comprensión, aplicación y análisis. Devuelve un JSON con: pregunta, opciones[], respuesta_correcta, explicacion.

## Flujo

PDF/MD → LLM genera quiz → JSON → Interfaz Flashcards

## Stack técnico

python, claude, htmx, markdown