---
id: docmine
name: DocMine
version: v0.3.0
status: archived
stack:
  - python
  - flask
  - sqlite
  - spacy
  - bs4
  - pdfminer
  - python-docx
  - loguru
repo: ~/Desktop/Mineria de BD/DocMine-OLD
description: Organizador inteligente de documentos legales con clasificación automática, búsqueda full-text y dashboard web. 3 fases completadas con metodología minerOS (ORO-GEMAS-TESORO).
---

# DocMine v0.3.0

Organizador inteligente de documentos legales con clasificación automática y dashboard web. Parte de la filosofía **minerOS**: aplicaciones independientes que convierten datos en **oro organizado**.

## Flujo de trabajo

1. **Tunnels (Descubrimiento)**
   - Escaneo recursivo de carpetas
   - Detección de tipos de archivo
   - Extracción de texto (PDF, Word, Excel)
   - Hash SHA-256 para duplicados
   - Metadata EXIF/propiedades

2. **GemaEngine (Análisis)**
   - Clasificación automática por contenido
   - NLP con spaCy
   - Detección de tipo de documento
   - Categorización legal (fiscal, mercantil, civil, laboral)
   - Extracción de año fiscal
   - Identificación de cliente
   - Score de confianza

3. **Vault (Persistencia)**
   - Base de datos SQLite con 9 tablas
   - Esquema relacional optimizado
   - Backups automáticos con timestamp
   - Índices para búsquedas rápidas

4. **Dashboard Web**
   - Flask con Jinja2 templates
   - Búsqueda full-text con highlighting
   - Tabla interactiva con DataTables
   - Gráficos de distribución (Chart.js)
   - Filtros por tipo/categoría/año/cliente
   - Tema claro/oscuro con persistencia
   - API REST con 9 endpoints

## Comandos principales

```bash
# Instalación
cd "/Users/carlos/Desktop/Mineria de BD/DocMine-OLD"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Escanear documentos
python main.py scan /ruta/a/documentos

# Escanear sin procesar (solo registrar)
python main.py scan /ruta/carpeta --no-process

# Clasificar documentos automáticamente
python main.py classify

# Clasificar con límite
python main.py classify --limit 100

# Reclasificar documentos ya clasificados
python main.py classify --reclassify

# Ver estadísticas
python main.py stats

# Crear backup de base de datos
python main.py backup

# Iniciar web dashboard
python main.py web
# Abre: http://localhost:5002
```

## Arquitectura

```
DocMine/
├── main.py                    # CLI principal
├── config.yaml                # Configuración
├── requirements.txt           # Dependencias
├── documentos.db              # Base de datos SQLite
│
├── core/                      # Tunnels (descubrimiento)
│   ├── scanner.py             # Encuentra documentos
│   ├── extractor.py           # Extrae texto/metadata
│   └── hasher.py              # Detecta duplicados
│
├── intelligence/              # GemaEngine (análisis)
│   ├── classifier.py          # Clasificación automática
│   ├── nlp_analyzer.py        # NLP y embeddings
│   └── date_extractor.py      # Fechas críticas
│
├── storage/                   # Vault (persistencia)
│   ├── database.py            # Gestor SQLite
│   └── models.py              # Esquema de tablas
│
├── web/                       # Dashboard
│   ├── app.py                 # Flask app
│   ├── routes/
│   ├── templates/
│   └── static/
│
└── analizar_130.py            # Script análisis Modelo 130
```

### Stack técnico

- **Backend:** Python 3.11 + Flask
- **Base de datos:** SQLite con FTS5 (full-text search)
- **Extracción:** PyMuPDF (PDF), python-docx (Word), openpyxl (Excel)
- **NLP:** spaCy (análisis lingüístico)
- **Frontend:** HTML5 + Jinja2 + DataTables + Chart.js
- **Logging:** Loguru
- **CLI:** argparse
- **Hashing:** hashlib (SHA-256)

## Aprendizajes clave

### Lo que funcionó bien

1. **Metodología minerOS:** Pipeline claro ORO→GEMAS→TESORO
2. **Clasificación automática:** Alta precisión sin entrenamiento
3. **SQLite con FTS5:** Búsqueda full-text instantánea
4. **Flask simple:** Dashboard funcional sin complejidad
5. **Hash para duplicados:** Detecta archivos repetidos

### Problemas resueltos

- **Múltiples formatos:** Extractores específicos por tipo
- **Clasificación sin ML:** Keywords + reglas heurísticas
- **Búsqueda rápida:** Índices SQLite optimizados
- **Duplicados:** SHA-256 hash único
- **Backups:** Automáticos con timestamp

### Tipos de documentos soportados

**Formatos:**
- PDF (.pdf)
- Word (.docx, .doc)
- Excel (.xlsx, .xls)
- Texto (.txt, .rtf)

**Clasificación automática:**
- Facturas (IRPF, IVA, comerciales)
- Contratos (alquiler, compraventa, prestación servicios)
- Escrituras (públicas, notariales)
- Sentencias (civiles, penales, contencioso-administrativas)
- Requerimientos (AEAT, tribunales)
- Modelos Tributarios (303, 347, 390, etc.)

**Categorías:**
- Fiscal (impuestos, tributación)
- Mercantil (sociedades, BORME)
- Civil (herencias, propiedad)
- Laboral (contratos, nóminas)

### Fases completadas

**✅ FASE 0 (Completada):**
- Escaneo de carpetas
- Extracción de texto (PDF, Word, Excel)
- Base de datos SQLite con 9 tablas
- CLI funcional
- Detección de duplicados por hash

**✅ FASE 1 (Completada):**
- Clasificación automática por contenido
- Detección de tipo de documento
- Categorización legal (fiscal, mercantil, civil, laboral)
- Extracción de año fiscal
- Identificación de cliente
- Score de confianza

**✅ FASE 2 (Completada):**
- Dashboard web en Flask (http://localhost:5002)
- Búsqueda full-text con highlighting
- Tabla interactiva con DataTables
- Gráficos de distribución (Chart.js)
- Filtros por tipo/categoría/año/cliente
- Tema claro/oscuro con persistencia
- Vista detallada de documentos
- API REST con 9 endpoints

**📅 FASE 3 (Planificado - No implementado):**
- Análisis NLP con spaCy
- Extracción de entidades (nombres, empresas)
- Búsqueda semántica con embeddings
- Extracción de fechas críticas
- Expedientes virtuales
- Alertas de vencimientos

## Esquema de base de datos

**Tabla: `documentos`**
```sql
id, ruta_archivo, nombre_archivo, extension, tamanio_kb,
fecha_creacion, fecha_modificacion, hash_sha256,
fecha_agregado
```

**Tabla: `contenido`**
```sql
id, documento_id, texto_extraido, num_palabras,
num_paginas, idioma_detectado
```

**Tabla: `clasificacion`**
```sql
id, documento_id, tipo_documento, categoria,
año_fiscal, cliente, confianza
```

**Tabla: `metadata`**
```sql
id, documento_id, autor, titulo, asunto,
fecha_documento, palabras_clave
```

**Tabla: `duplicados`**
```sql
id, hash_sha256, documento_id_original, documento_id_duplicado
```

**Tabla: `backups`**
```sql
id, fecha_backup, ruta_backup, tamanio_mb
```

## Configuración

Edita `config.yaml` para personalizar:

```yaml
# Tipos de documentos y keywords
document_types:
  factura:
    keywords: ["factura", "IRPF", "IVA", "base imponible"]
  contrato:
    keywords: ["contrato", "arrendamiento", "compraventa"]

# Formatos soportados
supported_formats:
  - pdf
  - docx
  - xlsx
  - txt

# Límites
max_file_size_mb: 50
scan_recursive: true

# Dashboard
web_port: 5002
web_host: "127.0.0.1"

# Logging
log_level: INFO
log_file: docmine.log
```

## Casos de uso reales

### Escaneo de documentos

```bash
$ python main.py scan ~/Documents/Legal
Escaneando /Users/carlos/Documents/Legal...
✓ Procesado: Contrato_Arrendamiento_2024.pdf (137 KB)
✓ Procesado: Factura_IRPF_Q3_2024.pdf (89 KB)
✓ Duplicado detectado: Copia_de_Factura.pdf
✓ Procesado: Escritura_Pública.docx (245 KB)

Total: 4 documentos escaneados
Duplicados: 1
Tiempo: 12.3s
```

### Clasificación automática

```bash
$ python main.py classify
Clasificando documentos...
✓ Contrato_Arrendamiento_2024.pdf → Contrato (Civil) [95% confianza]
✓ Factura_IRPF_Q3_2024.pdf → Factura (Fiscal) [98% confianza]
✓ Escritura_Pública.docx → Escritura (Civil) [92% confianza]

Clasificados: 3 documentos
Promedio confianza: 95%
```

### Dashboard web

```
Documentos por tipo:
┌──────────────┬─────────┐
│ Tipo         │ Cantidad│
├──────────────┼─────────┤
│ Facturas     │ 45      │
│ Contratos    │ 23      │
│ Escrituras   │ 12      │
│ Sentencias   │ 8       │
└──────────────┴─────────┘

Documentos por categoría:
┌──────────────┬─────────┐
│ Categoría    │ Cantidad│
├──────────────┼─────────┤
│ Fiscal       │ 52      │
│ Civil        │ 28      │
│ Mercantil    │ 7       │
│ Laboral      │ 1       │
└──────────────┴─────────┘
```

## Filosofía minerOS

```
DATOS BRUTOS → [Tunnels] → ORO (metadata)
                    ↓
              [GemaEngine]
                    ↓
            GEMAS (análisis IA)
                    ↓
              [Vault + UI]
                    ↓
            TESORO (organizado)
```

## API REST Endpoints

```
GET  /api/documents              # Listar todos los documentos
GET  /api/documents/:id          # Detalle de documento
GET  /api/search?q=query         # Búsqueda full-text
GET  /api/stats                  # Estadísticas generales
GET  /api/types                  # Tipos de documentos
GET  /api/categories             # Categorías
GET  /api/clients                # Clientes identificados
GET  /api/years                  # Años fiscales
POST /api/classify/:id           # Reclasificar documento
```

## Estado del proyecto

**Versión:** v0.3.0
**Estado:** Archivado (FASE 2 completada)
**Motivo:** Integrado en DirectOS como módulo de Knowledge Base

El proyecto alcanzó un estado funcional completo en FASE 2. Fue archivado tras integrar su funcionalidad principal (búsqueda de documentos + clasificación) en DirectOS v8.0 como parte del módulo Knowledge Base RAG.

## Integración en DirectOS

DocMine se integró en DirectOS como:
- **Knowledge Base (RAG):** Búsqueda semántica en documentos markdown
- **Scout:** Análisis de código con Claude API
- Arquitectura modular reutilizada

## Enlaces útiles

- [spaCy Docs](https://spacy.io/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [SQLite FTS5](https://www.sqlite.org/fts5.html)
- [DataTables](https://datatables.net/)
- [Chart.js](https://www.chartjs.org/)
