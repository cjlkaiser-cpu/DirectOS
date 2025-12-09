---
category: seguridad
emoji: "\U0001F512"
flow:
- python
- ocr
- loguru
flowDesc: Archivos → OCR si es imagen → Regex/Spacy detecta → Copia censurada
id: escudo-privacidad
name: Escudo de Privacidad
problem: Necesitas compartir logs o documentos pero contienen datos sensibles.
prompt: Actúa como Ingeniero de Seguridad. Crea un script Python que escanee archivos
  recursivamente, detecte datos sensibles (DNI, Email, Teléfono, API Keys, IBANs)
  usando regex y opcionalmente Spacy NER, y genere una copia censurada con [REDACTED].
  Usa Loguru para alertar cada hallazgo. Sin APIs externas - todo local.
---

# Escudo de Privacidad

Necesitas compartir logs o documentos pero contienen datos sensibles.

## Prompt

Actúa como Ingeniero de Seguridad. Crea un script Python que escanee archivos recursivamente, detecte datos sensibles (DNI, Email, Teléfono, API Keys, IBANs) usando regex y opcionalmente Spacy NER, y genere una copia censurada con [REDACTED]. Usa Loguru para alertar cada hallazgo. Sin APIs externas - todo local.

## Flujo

Archivos → OCR si es imagen → Regex/Spacy detecta → Copia censurada

## Stack técnico

python, ocr, loguru