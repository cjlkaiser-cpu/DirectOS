---
id: pymupdf
name: PyMuPDF
category: Process
icon: fa-file-pdf
color: text-red-400
tag: PDF Processing
status: used
level: working
next: OCR con PyMuPDF
---

# PyMuPDF (fitz)

Librería Python para manipular PDFs. Rápida y completa.

## Por qué en minerOS

Extrae texto, imágenes, metadata de PDFs. Más rápida que PyPDF2.

## Casos de uso

- Extraer texto de PDFs
- Limpiar y optimizar PDFs
- Extraer imágenes
- Combinar/dividir documentos

## Código ejemplo

```python
import fitz  # PyMuPDF

# Abrir PDF
doc = fitz.open("documento.pdf")

# Extraer texto de todas las páginas
for page in doc:
    text = page.get_text()
    print(text)

# Limpiar y guardar
doc.save("limpio.pdf", garbage=4, deflate=True)
doc.close()
```

## Proyectos que lo usan

- Limpiador PDFs (extracción y limpieza)
- DocMine (procesamiento documentos)
