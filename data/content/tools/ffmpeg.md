---
id: ffmpeg
name: FFmpeg
category: Process
icon: fa-film
color: text-pink-400
tag: Multimedia
status: learning
level: working
next: FFmpeg batch processing
---

# FFmpeg

La navaja suiza del vídeo y audio.

## Por qué en minerOS

Permite extraer el audio de un vídeo para Whisper, o sacar fotogramas cada 5 segundos para CLIP.

## Casos de uso

- Extraer audio de vídeo
- Comprimir vídeos
- Generar GIFs

## Código ejemplo

```python
import subprocess
subprocess.run(['ffmpeg', '-i', 'video.mp4', '-vn', 'audio.mp3'])
```

## Proyectos que lo usan

- VideoMine (planeado - extracción frames + audio)
- PhotoMine v2.0 (futuro - procesar vídeos)
