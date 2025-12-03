---
id: web-scraper-ia
name: Web Scraper IA
version: v1.0
status: production
stack:
  - python
  - claude
  - pydantic
  - httpx
  - bs4
  - sqlite
  - rich
  - loguru
repo: ~/Desktop/obtener datos de web
description: Sistema de web scraping inteligente que usa Claude para extraer datos estructurados según schemas Pydantic. CLI completo con histórico de cambios y validación estricta.
---

# Web Scraper IA v1.0

Sistema de web scraping que utiliza **Claude** para extraer datos estructurados de páginas web según schemas **Pydantic** definidos.

## Flujo de trabajo

1. **Cliente HTTP Robusto**
   - HTTPX con retry automático
   - Rate limiting configurable
   - Gestión de headers y cookies
   - Timeout inteligente

2. **Parsing HTML**
   - BeautifulSoup para extracción
   - Selector CSS específico opcional
   - Limpieza de HTML
   - Preservación de estructura

3. **Extracción Inteligente**
   - Claude API para interpretar contenido
   - Schema Pydantic para validación
   - Contexto adicional opcional
   - Extracción estructurada

4. **Persistencia y Tracking**
   - SQLite con histórico completo
   - Detección automática de cambios
   - Versionado de datos
   - Exportación JSON/CSV

## Comandos principales

```bash
# Instalación
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configurar API key
cp .env.example .env
# Editar .env y añadir ANTHROPIC_API_KEY

# Extraer datos de una URL
python main.py scrape "https://tienda.com/producto/123" -s product

# Modo dry-run (sin API ni guardar)
python main.py scrape "https://example.com" -s product --dry-run

# Ver histórico de cambios
python main.py history "https://tienda.com/producto/123" -s product

# Estadísticas
python main.py stats

# Exportar datos
python main.py export -s product -o products.json
python main.py export --format csv -o all_data.csv

# Previsualizar URL
python main.py preview "https://example.com"

# Ver schemas disponibles
python main.py schemas
python main.py schemas -s product
```

## Arquitectura

```
obtener datos de web/
├── main.py              # CLI principal
├── dashboard.py         # Dashboard Flask
├── src/
│   ├── http_client.py   # Cliente HTTPX con retry
│   ├── html_parser.py   # Parser BeautifulSoup
│   ├── extractor.py     # Extractor Claude + Pydantic
│   └── database.py      # SQLite con histórico
├── schemas/
│   ├── product.py       # Schema producto
│   ├── article.py       # Schema artículo
│   ├── company.py       # Schema empresa
│   ├── job_posting.py   # Schema empleo
│   └── real_estate.py   # Schema inmueble
├── data/                # Base de datos SQLite
└── logs/                # Archivos de log
```

### Stack técnico

- **Backend:** Python 3.11
- **HTTP:** HTTPX (async con retry)
- **Parsing:** BeautifulSoup4
- **IA:** Claude 3.5 Sonnet (Anthropic API)
- **Validación:** Pydantic v2
- **Base de datos:** SQLite
- **CLI:** Click + Rich (output elegante)
- **Logging:** Loguru
- **Dashboard:** Flask (opcional)

## Aprendizajes clave

### Lo que funcionó bien

1. **Schemas Pydantic:** Validación estricta asegura datos limpios
2. **Claude para extracción:** Más robusto que XPath/CSS selectors
3. **Histórico automático:** Detecta cambios sin código adicional
4. **CLI con Rich:** Output profesional en terminal
5. **Dry-run mode:** Pruebas sin consumir API calls

### Problemas resueltos

- **Rate limiting:** Control de requests por periodo
- **Retry automático:** Manejo de fallos temporales de red
- **Validación de schemas:** Pydantic rechaza datos inválidos
- **Tracking de cambios:** Diff automático entre versiones
- **Contexto para Claude:** Mejora precisión de extracción

### Schemas incluidos

**product:**
- Producto individual de e-commerce
- Campos: titulo, precio, descripcion, disponible, rating, sku, imagenes

**article:**
- Artículo de blog o noticia
- Campos: titulo, autor, fecha, contenido, tags, categoria

**company:**
- Información empresarial
- Campos: nombre, sector, descripcion, telefono, email, web, direccion

**job:**
- Oferta de empleo
- Campos: titulo, empresa, ubicacion, salario, tipo_contrato, requisitos

**property:**
- Inmueble (vivienda, local, terreno)
- Campos: tipo, precio, superficie, habitaciones, ubicacion, descripcion

### Siguientes pasos

- [ ] Scraping programado (cron jobs)
- [ ] Notificaciones de cambios (email/Telegram)
- [ ] Proxy rotation para scraping masivo
- [ ] Dashboard con gráficos de evolución
- [ ] Exportación a Google Sheets

## Métricas

- **Schemas:** 6 predefinidos (product, article, company, job, property, product_list)
- **Líneas de código:** ~1,200 líneas Python
- **Endpoints CLI:** 6 comandos principales
- **Tasa éxito:** Alta confianza en extracción estructurada

## Flujo de datos

```
URL → HTTPX (fetch) → BeautifulSoup (parse) → Claude (extract) → Pydantic (validate) → SQLite (save)
```

## Tracking de cambios

El sistema detecta automáticamente cambios entre extracciones:

```bash
$ python main.py scrape "https://tienda.com/producto" -s product
# Primera vez: "Nuevos datos guardados"

$ python main.py scrape "https://tienda.com/producto" -s product
# Si cambió el precio: "Datos actualizados - 1 cambios detectados"
#   • price: 99.99 → 89.99

$ python main.py history "https://tienda.com/producto" -s product
# Ver todas las versiones
```

## Configuración

Variables en `.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-xxxxx  # Requerido

# Rate limiting
RATE_LIMIT_REQUESTS=10
RATE_LIMIT_PERIOD=60

# Retry
MAX_RETRIES=3
RETRY_DELAY=1.0

# Database
DATABASE_PATH=./data/scraper.db

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/scraper.log
```

## Casos de uso reales

### Monitoreo de precios

```bash
# Extraer precio de producto
python main.py scrape "https://amazon.com/product/B08X..." -s product

# Repetir periódicamente con cron
# Ver histórico de cambios de precio
python main.py history "https://amazon.com/product/B08X..." -s product
```

### Agregación de noticias

```bash
# Extraer artículos de diferentes fuentes
python main.py scrape "https://blog.com/articulo-1" -s article
python main.py scrape "https://news.com/noticia-2" -s article

# Exportar todo a CSV
python main.py export -s article -o articles.csv
```

### Directorio de empresas

```bash
# Extraer info de múltiples empresas
python main.py scrape "https://directorio.com/empresa-a" -s company

# Exportar base de datos completa
python main.py export -s company -o companies.json
```

## Opciones avanzadas

```bash
# Verbose mode
python main.py -v scrape URL -s schema

# Selector CSS específico
python main.py scrape URL -s product --selector ".product-card"

# Guardar HTML parseado
python main.py scrape URL -s article --save-html output.html

# Contexto adicional para Claude
python main.py scrape URL -s product --context "Es una tienda española, precios en EUR"
```

## Crear schema personalizado

```python
# schemas/mi_schema.py
from pydantic import BaseModel, Field

class MiSchema(BaseModel):
    titulo: str = Field(..., description="Título del contenido")
    precio: float = Field(..., description="Precio en euros")
    disponible: bool = Field(True, description="Si está disponible")
    tags: list[str] = Field(default_factory=list)
```

Luego añádelo a `schemas/__init__.py` y al diccionario `SCHEMAS` en `main.py`.

## Enlaces útiles

- [Anthropic API Docs](https://docs.anthropic.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [HTTPX Docs](https://www.python-httpx.org/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/)
