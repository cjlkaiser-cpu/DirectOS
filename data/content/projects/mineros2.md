---
id: mineros2
name: minerOS v2 Backend
version: v0.1.0
status: prototype
stack:
  - fastapi
  - chroma
  - python
  - pydantic
  - loguru
  - uvicorn
repo: ~/Desktop/MinerOs2
description: Backend API scaffold para minerOS v2. Sistema local-first de organización y búsqueda de archivos multimedia con IA. FastAPI + ChromaDB persistente con arquitectura ORO-GEMAS-TESORO.
---

# minerOS v2 Backend v0.1.0

Backend API scaffold para minerOS v2, sistema local-first de organización y búsqueda de archivos multimedia con IA.

## Flujo de trabajo

1. **API REST con FastAPI**
   - Endpoints asíncronos
   - Auto-documentación (Swagger)
   - Validación con Pydantic
   - CORS habilitado para desarrollo

2. **Base de Datos Vectorial**
   - ChromaDB persistente en disco
   - Colección: `mineros_vectors`
   - Embeddings para búsqueda semántica
   - Persistencia en `./data/chroma_db`

3. **Health Check**
   - Estado de API
   - Estado de base de datos
   - Conteo de documentos
   - Validación de conexión

4. **Ingesta de Archivos**
   - POST /ingest con FormData
   - Recepción de archivos multimedia
   - Placeholder para procesamiento IA
   - Confirmación de recepción

## Comandos principales

```bash
# Instalación
cd /Users/carlos/Desktop/MinerOs2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Ejecutar API (opción 1)
python -m app.main

# Ejecutar API (opción 2)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Probar health check
curl http://localhost:8000/health

# Probar ingesta de archivo
curl -X POST http://localhost:8000/ingest \
  -F "file=@/ruta/a/archivo.jpg"

# Ver documentación Swagger
open http://localhost:8000/docs

# Ver documentación ReDoc
open http://localhost:8000/redoc
```

## Arquitectura

```
MinerOs2/
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── config.py            # Configuración con pydantic-settings
│   ├── core/
│   │   ├── db.py            # Cliente ChromaDB persistente
│   │   └── logger.py        # Configuración Loguru
│   ├── routers/
│   │   ├── health.py        # GET /health
│   │   └── ingest.py        # POST /ingest
│   └── services/
│       └── vector_store.py  # Lógica de negocio ChromaDB
├── data/
│   └── chroma_db/           # Base de datos ChromaDB persistente
├── .env.example             # Ejemplo de variables de entorno
├── requirements.txt         # Dependencias Python
├── README.md
├── ARQUITECTURA_VISUAL.md
├── GUIA_ARCHIVOS.md
└── RESUMEN_Y_PROXIMOS_PASOS.md
```

### Stack técnico

- **Framework:** FastAPI (async)
- **Base de datos:** ChromaDB (vectorial persistente)
- **Validación:** Pydantic v2 + pydantic-settings
- **Logging:** Loguru (colorizado)
- **Servidor:** Uvicorn (ASGI)
- **Config:** Variables de entorno (.env)
- **Deploy:** Local-first (sin dependencias externas)

## Aprendizajes clave

### Lo que funcionó bien

1. **FastAPI:** Auto-documentación instantánea
2. **ChromaDB persistente:** Datos guardados en disco
3. **Pydantic-settings:** Configuración con variables de entorno
4. **Loguru:** Logging colorizado y claro
5. **Scaffold modular:** Estructura escalable

### Problemas resueltos

- **Persistencia ChromaDB:** Configuración de `persist_directory`
- **Async FastAPI:** Endpoints no bloqueantes
- **CORS:** Habilitado para desarrollo frontend
- **Logging colorizado:** Loguru con formato custom
- **Configuración centralizada:** Settings con Pydantic

### Endpoints disponibles

**GET /health**
```json
{
  "api": "online",
  "database": {
    "status": "healthy",
    "collection_name": "mineros_vectors",
    "document_count": 0
  }
}
```

**POST /ingest**
```bash
curl -X POST http://localhost:8000/ingest \
  -F "file=@archivo.jpg"

# Respuesta:
{
  "status": "received",
  "filename": "archivo.jpg",
  "size_bytes": 123456,
  "message": "Archivo 'archivo.jpg' recibido y procesado correctamente"
}
```

**GET /docs**
- Documentación Swagger UI interactiva
- Probar endpoints en navegador
- Ver schemas Pydantic

**GET /redoc**
- Documentación ReDoc alternativa
- Más legible para documentación formal

### Siguientes pasos (Roadmap)

**📅 ORO (Extracción):**
- Módulo para extraer metadata de archivos (EXIF, texto, etc.)
- Hashing para detectar duplicados
- Clasificación por tipo de archivo

**📅 GEMAS (IA):**
- Integración con modelos de embeddings
- Análisis visual (CLIP) para imágenes
- Análisis textual para documentos
- Generación de descripciones con LLM

**📅 TESORO (Búsqueda):**
- Búsqueda semántica usando embeddings
- Filtros avanzados
- Ranking de resultados
- API de búsqueda

## Variables de entorno

Configurar en `.env`:

```bash
# API
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true

# ChromaDB
CHROMA_PERSIST_DIR=./data/chroma_db
CHROMA_COLLECTION_NAME=mineros_vectors

# Logging
LOG_LEVEL=DEBUG
```

## Casos de uso (Planificados)

### Ingesta de fotos

```bash
# Subir una foto
curl -X POST http://localhost:8000/ingest \
  -F "file=@vacaciones/playa.jpg"

# El sistema debería:
# 1. Extraer EXIF (GPS, fecha, cámara)
# 2. Analizar con CLIP (contenido visual)
# 3. Generar embedding
# 4. Guardar en ChromaDB
```

### Búsqueda semántica

```bash
# Buscar fotos por descripción
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "playa al atardecer", "limit": 10}'

# Respuesta esperada:
{
  "results": [
    {
      "file": "playa.jpg",
      "score": 0.92,
      "metadata": {
        "date": "2024-08-15",
        "location": "Valencia"
      }
    }
  ]
}
```

### Organización automática

```bash
# El sistema debería agrupar fotos automáticamente:
# - Por evento (boda, cumpleaños)
# - Por ubicación (Madrid, Barcelona)
# - Por personas (si hay reconocimiento facial)
# - Por temporada (verano 2024)
```

## Filosofía minerOS

```
ARCHIVOS BRUTOS → [ORO] → Metadata extraída
                     ↓
                 [GEMAS]
                     ↓
            Análisis con IA
                     ↓
                 [TESORO]
                     ↓
        Búsqueda inteligente
```

**Principios:**
- **Local-first:** Datos en tu máquina
- **IA como herramienta:** No como caja negra
- **Organización automática:** Sin carpetas manuales
- **Búsqueda natural:** "fotos de la playa" en vez de navegar carpetas

## Estructura de código

**main.py:**
```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: conectar ChromaDB
    logger.info("🚀 Iniciando minerOS Backend...")
    db.connect()
    yield
    # Shutdown: cerrar conexiones
    logger.info("👋 Cerrando minerOS Backend...")

app = FastAPI(lifespan=lifespan)
```

**db.py:**
```python
import chroma

class ChromaManager:
    def __init__(self):
        self.client = None
        self.collection = None

    def connect(self):
        self.client = chroma.PersistentClient(
            path=settings.CHROMA_PERSIST_DIR
        )
        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION_NAME
        )
```

## Debugging

Los logs usan Loguru y tienen formato colorizado:

```
2024-01-15 10:30:45 | INFO     | app.main:lifespan:25 - 🚀 Iniciando minerOS Backend...
2024-01-15 10:30:45 | SUCCESS  | app.core.db:connect:34 - ✅ ChromaDB conectado
2024-01-15 10:30:46 | INFO     | uvicorn.server:serve:76 - Started server on http://0.0.0.0:8000
```

Cambiar nivel de logs editando `LOG_LEVEL` en `.env`.

## Estado del proyecto

**Versión:** v0.1.0 (Scaffold inicial)
**Estado:** Prototype
**Motivo:** Base arquitectónica para minerOS v2

Este es el scaffold inicial que establece la arquitectura base. Las fases ORO, GEMAS y TESORO están planificadas pero no implementadas.

El proyecto sirve como:
- Proof of concept de FastAPI + ChromaDB
- Base arquitectónica para expandir
- Referencia de estructura modular

## Diferencias con PhotoMine v1.4

| Feature | PhotoMine v1.4 | minerOS v2 |
|---------|----------------|------------|
| Framework | Flask | FastAPI |
| DB Vectorial | No | ChromaDB |
| Búsqueda | SQL | Semántica |
| IA | CLIP local | CLIP + LLM |
| Frontend | Templates | API REST |
| Deploy | Monolítico | Microservicios |

## Enlaces útiles

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Loguru Docs](https://loguru.readthedocs.io/)
- [Uvicorn Docs](https://www.uvicorn.org/)
