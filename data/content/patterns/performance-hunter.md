---
category: debug
emoji: ⚡
flow:
- python
- loguru
flowDesc: Código lento → Profiling mental → Identificar hotspots → Optimizar
id: performance-hunter
name: Performance Hunter
problem: Tu script funciona pero tarda demasiado.
prompt: 'Actúa como Performance Engineer. Analiza este código Python buscando: 1)
  Loops O(n²) convertibles a O(n) con sets/dicts, 2) Operaciones I/O bloqueantes que
  podrían ser async, 3) Memory allocations innecesarias en loops, 4) Candidatos para
  caching (@lru_cache). Prioriza por impacto/esfuerzo. Dame el código optimizado.'
---

# Performance Hunter

Tu script funciona pero tarda demasiado.

## Prompt

Actúa como Performance Engineer. Analiza este código Python buscando: 1) Loops O(n²) convertibles a O(n) con sets/dicts, 2) Operaciones I/O bloqueantes que podrían ser async, 3) Memory allocations innecesarias en loops, 4) Candidatos para caching (@lru_cache). Prioriza por impacto/esfuerzo. Dame el código optimizado.

## Flujo

Código lento → Profiling mental → Identificar hotspots → Optimizar

## Stack técnico

python, loguru