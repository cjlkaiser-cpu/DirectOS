---
id: ollama
name: Ollama
category: IA Model
icon: fa-robot
color: text-pink-400
tag: Local LLM
status: new
level: exploring
next: Deploy Llama 3 localmente
---

# Ollama

Ejecuta modelos tipo ChatGPT (Llama 3, Mistral) en tu Mac.

## Por qué en minerOS

Privacidad total. Te permite tener un asistente inteligente que lee tus documentos privados sin subirlos a la nube.

## Casos de uso

- Resumir documentos sensibles
- Chatbot offline
- Extracción de datos privados

## Código ejemplo

```bash
# En terminal:
ollama run llama3
```

```python
# O desde Python:
import ollama
ollama.chat(model='llama3', messages=[...])
```

## Proyectos que lo usan

- Experimentos privados (análisis fiscal personal)
- DirectOS v8.0 (planeado - modo offline)
