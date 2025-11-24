---
id: prompt-optimizer
name: Prompt Optimizer
emoji: 🎯
problem: Tu prompt funciona a medias, a veces da respuestas inconsistentes.
flow:
  - claude
  - markdown
flowDesc: Prompt débil → Análisis → Aplicar técnicas → Prompt robusto
---

# Prompt Optimizer

Tu prompt funciona a medias, a veces da respuestas inconsistentes.

## Prompt

Actúa como Prompt Engineer Senior. Analiza este prompt y mejóralo aplicando: 1) Rol específico con expertise, 2) Formato de salida estructurado (JSON, Markdown), 3) Ejemplos few-shot si el patrón es complejo, 4) Restricciones explícitas (qué NO hacer), 5) Pensamiento paso a paso si requiere razonamiento. Devuelve: versión original vs mejorada.

## Flujo

Prompt débil → Análisis → Aplicar técnicas → Prompt robusto

## Stack técnico

claude, markdown
