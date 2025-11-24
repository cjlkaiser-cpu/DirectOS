---
id: opencv
name: OpenCV / Pillow
category: Process
icon: fa-eye
color: text-red-400
tag: Visión
status: used
level: solid
next: OpenCV filtros avanzados
---

# OpenCV / Pillow

Librerías para manipular imágenes píxel a píxel.

## Por qué en minerOS

Necesarias para preparar las imágenes antes de pasarlas a la IA (redimensionar, recortar, convertir formato).

## Casos de uso

- Generar miniaturas
- Detectar caras
- Normalizar para CLIP

## Código ejemplo

```python
from PIL import Image
img = Image.open('foto.jpg').resize((224, 224))
img.save('thumb.jpg')
```

## Proyectos que lo usan

- PhotoMine v1.4 (procesamiento 1,361 fotos)
- farmaIA v5.0 (recorte logos medicamentos)
