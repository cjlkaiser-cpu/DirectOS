---
id: docmine-fiscal
name: DocMine Fiscal
version: v1.0
status: production
stack:
  - python
  - ocr
  - flask
  - sqlite
repo: ~/Desktop/docmine-fiscal
description: Gestor de documentos fiscales. Procesa Modelo 130 con OCR + regex parser + Dashboard Flask. 93K€ procesados con 100% éxito.
---

# DocMine Fiscal v1.0

Precursor de la metodología minerOS. Sistema de procesamiento automático de documentos fiscales (Modelo 130).

## Flujo de trabajo

1. **Ingesta de PDFs**
   - Escaneado automático de carpeta
   - Detección de tipo de documento
   - OCR para PDFs escaneados (Tesseract)
   - Extracción de texto con PyMuPDF

2. **Parsing con regex**
   - Parser específico para formularios Modelo 130
   - Extracción de datos: trimestre, año, bases, cuotas
   - Validación de formato y cálculos
   - Normalización de clientes

3. **Almacenamiento**
   - SQLite con esquema fiscal
   - Histórico completo de declaraciones
   - Indexado por cliente y periodo
   - Queries SQL para análisis

4. **Dashboard Flask**
   - Visualización de datos procesados
   - Listado de clientes y totales
   - Gráficos de evolución IRPF
   - Exportación a CSV

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Instalar Tesseract (OCR)
brew install tesseract

# Procesar documentos
python main.py procesar --input ~/Documents/Fiscal/Modelo130/

# Iniciar dashboard
python main.py dashboard --port 5000

# Ver estadísticas
python main.py stats
```

## Arquitectura

```
docmine-fiscal/
├── main.py                  # CLI entry point
├── modules/
│   ├── scanner.py           # Escaner de PDFs
│   ├── ocr.py               # Tesseract wrapper
│   ├── parser_130.py        # Parser regex Modelo 130
│   └── database.py          # SQLite manager
├── templates/
│   ├── index.html           # Dashboard principal
│   ├── cliente.html         # Vista por cliente
│   └── stats.html           # Estadísticas
├── static/
│   └── style.css            # Estilos básicos
└── data/
    ├── fiscal.db            # Base de datos SQLite
    └── processed/           # PDFs procesados
```

### Stack técnico

- **Backend:** Python 3.11 + Flask
- **OCR:** Tesseract (open source)
- **Parsing:** Regex específico para Modelo 130
- **Base de datos:** SQLite
- **Frontend:** HTML + CSS + Jinja2 templates

## Aprendizajes clave

### Lo que funcionó bien

1. **OCR con Tesseract:** 100% de precisión en formularios escaneados
2. **Parser regex:** Extracción confiable de campos numéricos
3. **Normalización clientes:** Diferentes variantes → un solo ID
4. **Validación automática:** Detecta errores de cálculo en formularios
5. **Flask simple:** Dashboard funcional sin complejidad

### Problemas resueltos

- **PDFs escaneados vs digitales:** Detección automática y OCR condicional
- **Variantes de formato:** Parser robusto con múltiples patterns
- **Nombres inconsistentes:** Normalización con similitud de strings
- **Cálculos incorrectos:** Validación cruzada de cuotas
- **Escalabilidad:** Procesamiento por lotes con checkpoints

### Métricas reales

**Procesamiento completo:**
```
Total documentos: 107 Modelo 130
Éxito: 107 (100%)
Errores: 0

Total IRPF procesado: 93,029.46€
Clientes únicos: 18
Periodo: 2020-2024
Trimestres: Q1-Q4 de cada año
```

**Performance:**
- Tiempo por documento: ~2-3 segundos
- OCR (si necesario): +5 segundos
- Total 107 docs: ~8 minutos

### Siguientes pasos

- [ ] Soporte para más modelos fiscales (190, 303)
- [ ] Exportación a Excel con macros
- [ ] Alertas de plazos de presentación
- [ ] Integración con AEAT API

## Métricas

- **Documentos procesados:** 107 (Modelo 130)
- **Tasa éxito:** 100%
- **Total IRPF:** 93,029.46€
- **Clientes:** 18 únicos
- **Periodo:** 2020-2024
- **Líneas de código:** ~1,500 líneas Python

## Casos de uso reales

### Procesamiento automático
```bash
$ python main.py procesar --input ~/Fiscal/2024/Q3/

Procesando Modelo 130...
✓ Carlos_García_Q3_2024.pdf → 2,450.00€
✓ Ana_López_Q3_2024.pdf → 1,890.50€
✓ Juan_Martínez_Q3_2024.pdf → 3,120.75€

Total trimestre: 7,461.25€
Guardado en fiscal.db
```

### Dashboard Flask
```
IRPF por Cliente (2024):

Carlos García:
  Q1: 2,100.00€
  Q2: 2,350.50€
  Q3: 2,450.00€
  Q4: 2,200.00€
  ━━━━━━━━━━━━━━
  Total: 9,100.50€

Ana López:
  Q1-Q4: 7,560.00€

Total general 2024: 24,890.75€
```

### Query SQL directa
```sql
-- Total por cliente
SELECT cliente, SUM(cuota) as total
FROM modelo_130
WHERE year = 2024
GROUP BY cliente
ORDER BY total DESC;

-- Evolución trimestral
SELECT trimestre, SUM(cuota) as total
FROM modelo_130
WHERE cliente = 'Carlos García'
GROUP BY trimestre;
```

## Parser Regex (Ejemplo)

```python
import re

# Pattern para extraer cuota IRPF
PATTERN_CUOTA = r'Cuota\s+resultante.*?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))'

def extraer_cuota_130(texto):
    """
    Extrae la cuota de IRPF del Modelo 130
    """
    match = re.search(PATTERN_CUOTA, texto, re.DOTALL)
    if match:
        # Normalizar formato número
        cuota_str = match.group(1).replace('.', '').replace(',', '.')
        return float(cuota_str)
    return None

# Ejemplo
texto_pdf = "...Cuota resultante: 2.450,50..."
cuota = extraer_cuota_130(texto_pdf)  # 2450.50
```

## Esquema SQLite

```sql
CREATE TABLE modelo_130 (
    id INTEGER PRIMARY KEY,
    cliente TEXT NOT NULL,
    trimestre INTEGER,
    year INTEGER,
    base_imponible REAL,
    cuota REAL,
    retenciones REAL,
    resultado REAL,
    fecha_proceso TIMESTAMP,
    pdf_path TEXT,
    UNIQUE(cliente, trimestre, year)
);

CREATE INDEX idx_cliente ON modelo_130(cliente);
CREATE INDEX idx_periodo ON modelo_130(year, trimestre);
```

## Deploy

```bash
# Producción local
python main.py dashboard --port 5000 --host 0.0.0.0

# Systemd service
sudo cp docmine-fiscal.service /etc/systemd/system/
sudo systemctl enable docmine-fiscal
sudo systemctl start docmine-fiscal
```

## Lecciones aprendidas

**"Un sistema que funciona pero no aporta valor real no es un sistema completo."**

**Versión inicial (indexar):**
- "Encuentra el Modelo 130 de Carlos Q3"
- → "Aquí está el PDF"
- **Valor bajo:** Solo organiza

**Versión mejorada (responder):**
- "¿Cuánto IRPF pagó Carlos en 2024?"
- → "9,100.50€ en 4 trimestres"
- **Valor alto:** Genera insights

**El pivote crítico:**
> De buscar documentos → Responder preguntas

Esto marcó el inicio de la metodología minerOS: **el valor está en los insights, no en la organización**.

## Enlaces útiles

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Flask Docs](https://flask.palletsprojects.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [AEAT - Modelo 130](https://www.agenciatributaria.es/AEAT.internet/Inicio/La_Agencia_Tributaria/Campanas/IVA/Modelo_130/Modelo_130.shtml)
