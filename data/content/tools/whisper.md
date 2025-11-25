---
id: whisper
name: Whisper
category: IA Model
icon: fa-ear-listen
color: text-indigo-400
tag: Audio
status: learning
level: working
next: Fine-tuning Whisper
---

# Whisper

Reconocimiento de voz a texto de alta precisión.

## Por qué en minerOS

Convierte el audio (vídeos, notas de voz) en texto que luego puedes buscar, resumir o procesar.

## Casos de uso

- Transcribir reuniones
- Subtítulos automáticos
- Notas de voz a Obsidian

## Código ejemplo

```python
import whisper
model = whisper.load_model('base')
result = model.transcribe('audio.mp3')
print(result['text'])
```

## Proyectos que lo usan

- VideoMine (planeado - transcripción automática)
- DocMine v2.0 (futuro - procesar entrevistas)
