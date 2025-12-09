---
category: robustez
emoji: "\U0001F6E1️"
flow:
- python
- loguru
flowDesc: Código frágil → Identificar fallos → try/except → Retry → Log
id: centinela-errores
name: Centinela de Errores
problem: Tu script se rompe si falta internet o un archivo.
prompt: 'Actúa como SRE (Site Reliability Engineer). Envuelve este código en estructura
  robusta de errores: Excepciones específicas (NetworkError, FileNotFoundError), retry
  con backoff exponencial (3 intentos: 1s→2s→4s), fallback graceful, Loguru para registrar
  timestamp/intento/error/contexto.'
---

# Centinela de Errores

Tu script se rompe si falta internet o un archivo.

## Prompt

Actúa como SRE (Site Reliability Engineer). Envuelve este código en estructura robusta de errores: Excepciones específicas (NetworkError, FileNotFoundError), retry con backoff exponencial (3 intentos: 1s→2s→4s), fallback graceful, Loguru para registrar timestamp/intento/error/contexto.

## Flujo

Código frágil → Identificar fallos → try/except → Retry → Log

## Stack técnico

python, loguru