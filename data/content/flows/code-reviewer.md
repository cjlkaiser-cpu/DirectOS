---
id: code-reviewer
title: Code Reviewer
emoji: 👀
category: devops
stack:
  - git
  - python
  - claude
  - loguru
complexity: low
cost: api
useCase: CI/CD local, pre-commit hook, code quality.
flowDesc: git diff → Claude analiza → Reporte severidad → Aprueba/Rechaza
---

# Code Reviewer

Revisa tu código antes de hacer commit.

## Descripción

Sistema automatizado de revisión de código que detecta problemas antes del commit usando Claude.

## Stack técnico

- **Git**: captura de cambios
- **Python**: orquestación
- **Claude API**: análisis de código
- **Loguru**: logging de revisiones

## Flujo

1. `git diff --staged` captura cambios
2. Claude analiza buscando:
   - Vulnerabilidades de seguridad
   - Code smells
   - Falta de type hints
   - Complejidad ciclomática
3. Genera reporte con severidad (critical/warning/info)
4. Exit code 1 si hay críticos (bloquea commit)

## Casos de uso reales

- Pre-commit hooks en minerOS
- CI/CD local antes de push
- Code quality automático

Integrable como pre-commit hook
