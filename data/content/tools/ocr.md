---
id: ocr
name: Tesseract OCR
category: Process
icon: fa-font
color: text-cyan-400
tag: OCR
status: learning
level: working
next: OCR fine-tuning español
---

# Tesseract OCR

Extrae texto de imágenes y PDFs escaneados.

## Por qué en minerOS

Para digitalizar documentos físicos (facturas, recibos) y hacerlos buscables.

## Casos de uso

- Escanear facturas
- Digitalizar notas a mano
- Extraer texto de capturas

## Código ejemplo

```python
import pytesseract
from PIL import Image
texto = pytesseract.image_to_string(Image.open('scan.png'))
```

## Proyectos que lo usan

- DocMine-Fiscal (OCR facturas escaneadas)
- farmaIA v4.0 (experimento - leer prospectos)
