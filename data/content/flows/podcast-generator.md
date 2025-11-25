---
id: podcast-generator
title: Podcast Generator
emoji: 🎙️
category: media
stack:
  - python
  - ollama
  - ffmpeg
complexity: mid
cost: local
useCase: Consumir noticias mientras cocinas, artículos largos, newsletters.
flowDesc: URL/Texto → Scraper → Ollama guioniza → TTS local → MP3
---

# Podcast Generator

Convierte artículos en audio para escuchar.

## Descripción

Pipeline que transforma artículos de texto en episodios de podcast con voz natural, ideal para consumo en movimiento.

## Stack técnico

- **Python**: orquestación
- **Ollama**: reescritura conversacional
- **FFmpeg**: procesamiento de audio

## Flujo

1. BeautifulSoup extrae texto limpio de URL
2. Ollama reescribe como guión de podcast (más conversacional)
3. TTS local (piper/kokoro) genera audio
4. FFmpeg añade intro/outro music
5. Guarda en podcast/ con metadata ID3
6. Genera feed RSS opcional

## Casos de uso reales

- Newsletters técnicos en audio
- Artículos largos para escuchar
- Consumo de noticias en multitarea

Target: 10 minutos de lectura → 8 min audio
