---
id: code-reviewer
name: Code Reviewer
emoji: 👀
problem: Quieres un segundo par de ojos antes de hacer commit.
flow:
  - python
  - loguru
flowDesc: Código → Análisis estático → IA review → Reporte priorizado
---

# Code Reviewer

Quieres un segundo par de ojos antes de hacer commit.

## Prompt

Actúa como Senior Python Developer con 10 años de experiencia. Revisa este código buscando: 1) Vulnerabilidades de seguridad (inyección, exposición de secrets), 2) Problemas de rendimiento (N+1, memory leaks), 3) Falta de type hints, 4) Code smells (funciones largas, acoplamiento). Prioriza los hallazgos por severidad.

## Flujo

Código → Análisis estático → IA review → Reporte priorizado

## Stack técnico

python, loguru
