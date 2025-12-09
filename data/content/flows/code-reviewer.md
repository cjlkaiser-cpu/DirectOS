---
category: devops
complexity: low
cost: api
desc: Revisa tu código antes de hacer commit.
emoji: "\U0001F440"
flowDesc: git diff → Claude analiza → Reporte severidad → Aprueba/Rechaza
id: code-reviewer
prompt: "Actúa como Code Review Bot. Sistema de revisión:\n1. git diff --staged captura
  cambios\n2. Claude analiza buscando:\n   - Vulnerabilidades de seguridad\n   - Code
  smells\n   - Falta de type hints\n   - Complejidad ciclomática\n3. Genera reporte
  con severidad (critical/warning/info)\n4. Exit code 1 si hay críticos (bloquea commit)\nIntegrable
  como pre-commit hook."
stack:
- git
- python
- claude
- loguru
title: Code Reviewer
useCase: CI/CD local, pre-commit hook, code quality.
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