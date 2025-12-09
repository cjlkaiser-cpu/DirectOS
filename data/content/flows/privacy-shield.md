---
category: devops
complexity: low
cost: local
desc: Censura datos sensibles en documentos automáticamente.
emoji: "\U0001F6E1️"
flowDesc: Documento → OCR si necesario → Regex/Spacy detecta → Censura → Copia limpia
id: privacy-shield
prompt: 'Actúa como Security Engineer. Redactor de PII:

  1. Detecta tipo de archivo (texto, PDF, imagen)

  2. OCR si es imagen/PDF escaneado

  3. Regex detecta: DNI, teléfonos, emails, IBANs, IPs

  4. Opcional: Spacy NER para nombres propios

  5. Genera copia con [REDACTED]

  6. Log de cada dato censurado (sin el dato)

  100% local, sin APIs externas.'
stack:
- python
- ocr
- loguru
title: Privacy Shield
useCase: Compartir logs sin exponer datos, anonimizar documentos.
---

# Privacy Shield

Censura datos sensibles en documentos automáticamente.

## Descripción

Redactor automático de información personal identificable (PII) en documentos.

## Stack técnico

- **Python**: orquestación
- **Tesseract OCR**: lectura de imágenes/PDFs
- **Loguru**: logging de censuras

## Flujo

1. Detecta tipo de archivo (texto, PDF, imagen)
2. OCR si es imagen/PDF escaneado
3. Regex detecta: DNI, teléfonos, emails, IBANs, IPs
4. Opcional: Spacy NER para nombres propios
5. Genera copia con [REDACTED]
6. Log de cada dato censurado (sin el dato)

## Casos de uso reales

- Compartir logs sin exponer datos personales
- Anonimizar documentos para compartir
- Compliance con RGPD

100% local, sin APIs externas