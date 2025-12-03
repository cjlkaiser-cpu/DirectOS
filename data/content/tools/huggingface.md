---
id: huggingface
name: HuggingFace
category: IA Model
icon: fa-face-smile
color: text-yellow-400
tag: ML Hub
status: learning
level: working
next: Fine-tuning modelos
---

# HuggingFace

Plataforma y librería para modelos de ML. El "GitHub de la IA".

## Por qué en minerOS

Acceso a miles de modelos pre-entrenados. Transformers, embeddings, LLMs open source.

## Casos de uso

- Descargar modelos pre-entrenados
- Embeddings con sentence-transformers
- Modelos de lenguaje (LLaMA, Mistral)
- Fine-tuning de modelos

## Código ejemplo

```python
from transformers import pipeline

# Clasificación de texto
classifier = pipeline("sentiment-analysis")
result = classifier("I love using HuggingFace!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99}]

# Embeddings
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(['Hello world', 'Hola mundo'])
```

## Proyectos que lo usan

- BioMistral Validation (modelos biomédicos)
- DirectOS Knowledge Base (embeddings)
