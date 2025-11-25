---
id: clip
name: OpenAI CLIP
category: IA Model
icon: fa-brain
color: text-purple-400
tag: Visión
status: used
level: solid
next: Fine-tuning CLIP
---

# OpenAI CLIP

Modelo multimodal que entiende imágenes y texto.

## Por qué en minerOS

Es el corazón de PhotoMine. Permite buscar "perro en la playa" y encontrar la foto sin que nadie la haya etiquetado.

## Casos de uso

- Búsqueda semántica visual
- Clasificación automática
- Detección de duplicados

## Código ejemplo

```python
inputs = processor(text=['gato', 'perro'], images=image, return_tensors='pt')
probs = model(**inputs).logits_per_image.softmax(dim=1)
```

## Proyectos que lo usan

- PhotoMine v1.4 (1,361 fotos clasificadas)
