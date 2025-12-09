---
category: knowledge
complexity: mid
cost: local
desc: Convierte audios en notas estructuradas para Obsidian.
emoji: "\U0001F3A4"
flowDesc: Audio → Whisper transcribe → Ollama limpia/resume → Obsidian .md
id: voice-to-knowledge
prompt: 'Actúa como Knowledge Engineer. Pipeline de voz a notas:

  1. Watchdog detecta .mp3/.m4a en carpeta inbox/

  2. Whisper (base) transcribe a texto raw

  3. Ollama (llama3) limpia muletillas y estructura

  4. Genera YAML frontmatter (fecha, tags inferidos)

  5. Guarda en vault/diario/ con nombre fecha-hora.md

  Incluye manejo de errores y logs con Loguru.'
stack:
- whisper
- python
- ollama
- markdown
title: Voice-to-Knowledge
useCase: Diario personal hablado, ideas al conducir, reuniones.
---

# Voice-to-Knowledge

Convierte audios en notas estructuradas para Obsidian.

## Descripción

Pipeline automático que procesa notas de voz y las convierte en documentos markdown limpios y estructurados.

## Stack técnico

- **Whisper**: transcripción de voz a texto
- **Python**: orquestación y watchdog
- **Ollama (llama3)**: limpieza y estructuración
- **Markdown**: formato de salida

## Flujo

1. Watchdog detecta archivos .mp3/.m4a en inbox/
2. Whisper (base) transcribe a texto raw
3. Ollama limpia muletillas y estructura el contenido
4. Genera YAML frontmatter (fecha, tags inferidos)
5. Guarda en vault/diario/ con nombre fecha-hora.md

## Casos de uso reales

- Diario personal hablado
- Captura de ideas rápidas
- Transcripción de reuniones y entrevistas