---
category: data-eng
emoji: "\U0001F52E"
flow:
- python
- loguru
flowDesc: Texto → Identificar patrón → Regex → Extraer → Lista limpia
id: susurrador-regex
name: Susurrador de Regex
problem: Necesitas extraer información de texto no estructurado (logs, emails).
prompt: 'Actúa como experto en Expresiones Regulares de Python. Necesito extraer [PATRÓN:
  IBANs, referencias catastrales, fechas, etc] de este texto. Para cada patrón: 1)
  Regex comentada paso a paso, 2) Código Python con re.findall(), 3) Tests con casos
  borde (qué matchea y qué no).'
---

# Susurrador de Regex

Necesitas extraer información de texto no estructurado (logs, emails).

## Prompt

Actúa como experto en Expresiones Regulares de Python. Necesito extraer [PATRÓN: IBANs, referencias catastrales, fechas, etc] de este texto. Para cada patrón: 1) Regex comentada paso a paso, 2) Código Python con re.findall(), 3) Tests con casos borde (qué matchea y qué no).

## Flujo

Texto → Identificar patrón → Regex → Extraer → Lista limpia

## Stack técnico

python, loguru