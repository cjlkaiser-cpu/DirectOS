---
desc: Voice-to-Knowledge - Notas de voz a texto estructurado
flow: Audio → Transcribe → LLM resume → Guarda .md
id: voice-notes
name: "\U0001F3A4 Escriba Silencioso"
tools:
- whisper
- python
- claude
- markdown
useCase: Diario, ideas, reuniones
---

# Voice-to-Knowledge - Notas de voz a texto estructurado

Pipeline automático que convierte notas de voz en documentos markdown estructurados y resumidos.

## Descripción

Graba una idea, reunión o reflexión y el sistema la transcribe, resume y guarda como nota estructurada en formato markdown.

## Casos de uso

- Diario personal hablado
- Captura rápida de ideas
- Transcripción de reuniones

## Stack técnico

1. **Whisper**: Transcripción de voz a texto
2. **Python**: Orquestación del pipeline
3. **Claude API**: Resumen y estructuración
4. **Markdown**: Formato de salida

## Proyectos que lo usan

- Experimentos personales (diario)
- VideoMine (transcripción de entrevistas - futuro)