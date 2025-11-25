---
id: farmaia
name: farmaIA
version: v5.0
status: production
stack:
  - fastapi
  - claude
  - sqlite
  - htmx
  - python
repo: https://github.com/yourusername/farmaia
description: Sistema de análisis de prospectos farmacéuticos con IA para procesamiento de BOT Plus y CIMA.
---

# farmaIA v5.0

Sistema completo de análisis de prospectos farmacéuticos que integra datos de BOT Plus y CIMA, con motor de IA para responder consultas sobre medicamentos.

## Flujo de trabajo

1. **Ingesta de datos**
   - Descarga automática de CIMA (AEMPS)
   - Scraping inteligente de BOT Plus con rotación de proxies
   - Normalización de datos a esquema unificado

2. **Procesamiento IA**
   - Chunking de prospectos (500 chars, 50 overlap)
   - Embeddings con Sentence-BERT (all-MiniLM-L6-v2)
   - Indexado en ChromaDB con metadata

3. **API y Frontend**
   - Endpoints REST con FastAPI
   - Chat interactivo con HTMX (sin JavaScript)
   - Respuestas contextuales con Claude 3.5 Sonnet

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

# Iniciar backend
cd backend
uvicorn main:app --reload --port 8000

# Procesar datos (primera vez)
python scripts/ingest_cima.py
python scripts/scrape_botplus.py

# Abrir dashboard
open http://localhost:8000
```

## Arquitectura

```
farmaia/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── modules/
│   │   ├── rag.py           # RAG engine
│   │   ├── scraper.py       # Bot Plus scraper
│   │   └── database.py      # SQLite manager
│   └── routers/
│       ├── chat.py          # Chat endpoints
│       └── admin.py         # Admin panel
├── frontend/
│   └── index.html           # HTMX interface
├── data/
│   ├── farmaia.db           # SQLite database
│   └── chroma/              # Vector store
└── scripts/
    ├── ingest_cima.py       # CIMA downloader
    └── scrape_botplus.py    # Scraper
```

### Stack técnico

- **Backend:** FastAPI + Python 3.11
- **IA:** Claude 3.5 Sonnet (Anthropic API)
- **Embeddings:** Sentence-BERT local
- **Vector DB:** ChromaDB persistente
- **Frontend:** HTML5 + HTMX + TailwindCSS
- **Database:** SQLite con FTS5 para búsqueda

## Aprendizajes clave

### Lo que funcionó bien

1. **RAG local-first:** ChromaDB + Sentence-BERT = sin costos de embeddings
2. **HTMX para chat:** UI reactiva sin escribir JavaScript
3. **Scraping robusto:** Retry con backoff + rotación de headers
4. **Schema unificado:** Normalizar CIMA + BOT Plus simplificó el RAG

### Problemas resueltos

- **Rate limiting de CIMA:** Cache agresivo + requests con delays
- **Prospectos muy largos:** Chunking inteligente respetando párrafos
- **Respuestas inconsistentes:** Multi-query RAG + reranking mejoró precisión
- **SQLite locks:** Conexiones read-only para queries concurrentes

### Siguientes pasos

- [ ] Añadir OCR para PDFs escaneados (pytesseract)
- [ ] Sistema de alertas para nuevos prospectos
- [ ] Modo offline completo (descargar Claude en Ollama)
- [ ] API pública con rate limiting

## Métricas

- **Base de datos:** 15,432 medicamentos indexados
- **Prospectos:** 8,204 documentos completos
- **Tiempo de respuesta:** ~2.5s por consulta
- **Precisión RAG:** 87% (evaluación manual 100 queries)
- **Líneas de código:** 2,847 líneas Python

## Uso en producción

```bash
# Deploy con Docker
docker-compose up -d

# Actualizar datos semanalmente
0 2 * * 0 cd /app && python scripts/update_data.py
```

## Enlaces útiles

- [Documentación CIMA](https://cima.aemps.es/cima/publico/home.html)
- [BOT Plus](https://botplusweb.farmaceuticos.com/)
- [Claude API Docs](https://docs.anthropic.com/)
