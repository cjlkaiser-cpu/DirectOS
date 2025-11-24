---
id: debugger-sherlock
name: Debugger Sherlock
emoji: 🔍
problem: Tienes un error críptico y no sabes por dónde empezar.
flow:
  - python
  - loguru
  - claude
flowDesc: Traceback → Analiza contexto → Hipótesis → Plan de acción
---

# Debugger Sherlock

Tienes un error críptico y no sabes por dónde empezar.

## Prompt

Actúa como Detective de Bugs Senior. Analiza este traceback como Sherlock Holmes. Identifica: 1) La línea exacta del fallo y tipo de excepción, 2) El contexto (qué datos entraron), 3) 3 hipótesis ordenadas por probabilidad, 4) Plan de debugging paso a paso con prints/breakpoints estratégicos. No asumas - deduce desde la evidencia.

## Flujo

Traceback → Analiza contexto → Hipótesis → Plan de acción

## Stack técnico

python, loguru, claude
