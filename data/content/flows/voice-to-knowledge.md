---
id: voice-to-knowledge
title: Voice-to-Knowledge
emoji: 🎤
category: knowledge
stack:
  - whisper
  - python
  - ollama
  - markdown
complexity: mid
cost: local
useCase: Diario personal hablado, ideas al conducir, reuniones.
flowDesc: Audio → Whisper transcribe → Ollama limpia/resume → Obsidian .md
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
