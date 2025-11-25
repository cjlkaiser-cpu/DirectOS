---
id: limpiador-pdfs
name: Limpiador PDFs
version: v1.0
status: archived
stack:
  - python
  - tkinter
  - pymupdf
  - pypdf
repo: ~
description: Herramienta de automatización para limpieza y procesamiento de archivos PDF. Interfaz gráfica con tkinter para operaciones batch sobre PDFs.
---

# Limpiador PDFs v1.0

Herramienta de automatización para limpieza y procesamiento de archivos PDF con interfaz gráfica en tkinter.

## Flujo de trabajo

1. **Interfaz Gráfica (tkinter)**
   - Selección de archivos PDF
   - Configuración de opciones
   - Preview de resultados
   - Procesamiento batch

2. **Operaciones sobre PDFs**
   - Limpieza de metadatos
   - Compresión de archivos
   - Extracción de páginas
   - Merge de múltiples PDFs
   - Conversión de formatos

3. **Procesamiento Automatizado**
   - Operaciones en lote
   - Progress bar visual
   - Logs de operaciones
   - Gestión de errores

## Comandos principales

```bash
# Ejecutar aplicación
python limpiador_pdfs.py

# O simplemente doble-click en el archivo .py
# (si tienes Python configurado en tu sistema)
```

## Arquitectura

```
limpiador-pdfs/
├── limpiador_pdfs.py        # Script principal con GUI
├── utils/
│   ├── pdf_operations.py    # Operaciones sobre PDFs
│   └── file_manager.py      # Gestión de archivos
└── output/                  # PDFs procesados
```

### Stack técnico

- **GUI:** tkinter (built-in Python)
- **PDF Processing:** PyMuPDF o PyPDF2
- **Automatización:** Python scripts
- **Deploy:** Ejecutable local (sin instalación)

## Aprendizajes clave

### Lo que funcionó bien

1. **tkinter:** Interfaz gráfica simple sin dependencias externas
2. **Batch processing:** Procesar múltiples archivos de una vez
3. **Preview:** Ver resultados antes de confirmar
4. **Python puro:** Sin framework pesado
5. **Portable:** Funciona en cualquier sistema con Python

### Casos de uso

**Limpieza de metadatos:**
- Eliminar información personal de PDFs
- Limpiar propiedades de autor/creador
- Remover comentarios y anotaciones

**Compresión:**
- Reducir tamaño de PDFs grandes
- Optimizar imágenes embebidas
- Eliminar elementos innecesarios

**Organización:**
- Extraer páginas específicas
- Unir múltiples PDFs en uno
- Separar PDF por páginas

## Operaciones principales

```python
# Ejemplo de código (pseudocódigo)
def limpiar_metadata(pdf_path):
    """Elimina metadata del PDF"""
    doc = open_pdf(pdf_path)
    doc.remove_metadata()
    doc.save("cleaned_" + pdf_path)

def comprimir_pdf(pdf_path, quality=75):
    """Comprime imágenes del PDF"""
    doc = open_pdf(pdf_path)
    doc.compress_images(quality)
    doc.save("compressed_" + pdf_path)

def extraer_paginas(pdf_path, pages):
    """Extrae páginas específicas"""
    doc = open_pdf(pdf_path)
    new_doc = doc.extract_pages(pages)
    new_doc.save("extract_" + pdf_path)
```

## Interfaz GUI

```
┌─────────────────────────────────────────┐
│  Limpiador de PDFs v1.0                │
├─────────────────────────────────────────┤
│                                         │
│  Seleccionar archivos: [Explorar...]   │
│                                         │
│  Operación:                             │
│  ○ Limpiar metadata                     │
│  ○ Comprimir                            │
│  ○ Extraer páginas                      │
│  ○ Unir PDFs                            │
│                                         │
│  Carpeta salida: [Explorar...]          │
│                                         │
│  [────────────────────] 0%              │
│                                         │
│  [Procesar]  [Cancelar]                 │
└─────────────────────────────────────────┘
```

## Filosofía KISS

**¿Por qué tkinter?**
- Viene con Python (sin instalar nada)
- Suficiente para operaciones simples
- Ligero y rápido
- Multiplataforma (Windows, Mac, Linux)

**Principio:** Si tkinter resuelve el problema, ¿para qué PyQt o Electron?

## Estado del proyecto

**Versión:** v1.0
**Estado:** Archivado
**Motivo:** Funcionalidad básica completada

Proyecto pequeño de automatización que cumplió su propósito: procesar PDFs de forma batch con interfaz gráfica simple.

Archivado tras completar las funcionalidades básicas. No requiere mantenimiento activo.

## Comparativa

| Feature | Limpiador PDFs | Adobe Acrobat | PyMuPDF CLI |
|---------|----------------|---------------|-------------|
| Interfaz | ✅ GUI simple | Compleja | Terminal |
| Gratis | ✅ | ❌ | ✅ |
| Batch | ✅ | ✅ | ✅ |
| Portable | ✅ | ❌ | ✅ |
| Learning curve | ✅ Fácil | Difícil | Medio |

## Métricas

- **Líneas de código:** ~200-300 líneas Python
- **Dependencias:** 2 (PyMuPDF/PyPDF2 + tkinter built-in)
- **Tamaño:** <100 KB
- **Operaciones:** 4-5 funciones principales

## Casos de uso reales

### Limpiar metadatos antes de compartir

```bash
# Seleccionar PDF con información personal
# Ejecutar "Limpiar metadata"
# Resultado: PDF sin autor, fecha de creación, software usado
```

### Comprimir PDFs para email

```bash
# PDF original: 15 MB
# Comprimir con calidad 75%
# PDF resultante: 3 MB (80% reducción)
```

### Extraer capítulo de libro

```bash
# Libro completo: 300 páginas
# Extraer páginas 45-67
# Resultado: PDF con solo capítulo 3
```

## Enlaces útiles

- [tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [PyMuPDF Docs](https://pymupdf.readthedocs.io/)
- [PyPDF2 Docs](https://pypdf2.readthedocs.io/)
