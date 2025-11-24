---
id: escudo-privacidad
name: Escudo de Privacidad
emoji: 🔒
problem: Necesitas compartir logs o documentos pero contienen datos sensibles.
flow:
  - python
  - ocr
  - loguru
flowDesc: Archivos → OCR si es imagen → Regex/Spacy detecta → Copia censurada
---

# Escudo de Privacidad

Necesitas compartir logs o documentos pero contienen datos sensibles.

## Prompt

Actúa como Ingeniero de Seguridad. Crea un script Python que escanee archivos recursivamente, detecte datos sensibles (DNI, Email, Teléfono, API Keys, IBANs) usando regex y opcionalmente Spacy NER, y genere una copia censurada con [REDACTED]. Usa Loguru para alertar cada hallazgo. Sin APIs externas - todo local.

## Flujo

Archivos → OCR si es imagen → Regex/Spacy detecta → Copia censurada

## Stack técnico

python, ocr, loguru
