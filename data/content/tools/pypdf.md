---
id: pypdf
name: PyPDF
category: Process
icon: fa-file-pdf
color: text-red-300
tag: PDF Tools
status: used
level: working
next: PyMuPDF para más velocidad
---

# PyPDF (pypdf2)

Librería Python pura para manipular PDFs. Sin dependencias externas.

## Por qué en minerOS

Combinar, dividir, rotar PDFs. Más simple que PyMuPDF para tareas básicas.

## Casos de uso

- Combinar múltiples PDFs
- Extraer páginas específicas
- Rotar páginas
- Añadir marcas de agua

## Código ejemplo

```python
from pypdf import PdfReader, PdfWriter

# Leer PDF
reader = PdfReader("documento.pdf")
print(f"Páginas: {len(reader.pages)}")

# Extraer texto
for page in reader.pages:
    print(page.extract_text())

# Combinar PDFs
writer = PdfWriter()
for pdf in ["doc1.pdf", "doc2.pdf"]:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)
writer.write("combinado.pdf")
```

## Proyectos que lo usan

- Limpiador PDFs (operaciones batch)
