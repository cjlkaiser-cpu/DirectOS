---
category: media
complexity: mid
cost: local
desc: Convierte artículos en audio para escuchar.
emoji: "\U0001F399️"
flowDesc: URL/Texto → Scraper → Ollama guioniza → TTS local → MP3
id: podcast-generator
prompt: 'Actúa como Audio Content Engineer. Pipeline podcast:

  1. BeautifulSoup extrae texto limpio de URL

  2. Ollama reescribe como guión de podcast (más conversacional)

  3. TTS local (piper/kokoro) genera audio

  4. FFmpeg añade intro/outro music

  5. Guarda en podcast/ con metadata ID3

  6. Genera feed RSS opcional

  Target: 10 minutos de lectura → 8 min audio.'
stack:
- python
- ollama
- ffmpeg
title: Podcast Generator
useCase: Consumir noticias mientras cocinas, artículos largos, newsletters.
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