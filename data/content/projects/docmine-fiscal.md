---
id: docmine-fiscal
name: DocMine Fiscal
version: v2.1
status: prototype
stack:
  - fastapi
  - ollama
  - chroma
  - python
  - ocr
repo: https://github.com/yourusername/docmine-fiscal
description: Sistema RAG local para consultar documentación fiscal y contratos. Embeddings con Sentence-BERT, LLM con Ollama (llama3).
---

# DocMine Fiscal v2.1

Sistema RAG 100% local para consultar documentación fiscal, contratos y manuales técnicos. Sin llamadas a APIs externas.

## Flujo de trabajo

1. **Ingesta de documentos**
   - Soporte: PDF, DOCX, TXT, MD
   - OCR para PDFs escaneados (Tesseract)
   - Extracción de texto con PyMuPDF
   - Detección automática de idioma

2. **Procesamiento RAG**
   - Chunking semántico (respeta párrafos)
   - Embeddings con Sentence-BERT (all-MiniLM-L6-v2)
   - Indexado en ChromaDB persistente
   - Metadata: archivo, página, fecha, tipo

3. **Motor de consultas**
   - Multi-query RAG para mejor cobertura
   - Reranking con cross-encoder
   - Contexto ventana deslizante
   - Ollama llama3 para respuestas

4. **Interfaz**
   - Chat conversacional con historial
   - Citas a documentos originales
   - Exportación de respuestas a MD/PDF
   - Modo "solo buscar" (sin LLM)

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3

# Ingerir documentos
python main.py ingest --input ~/Documents/Fiscal --recursive

# Modo servidor
python main.py serve --port 8000

# Consulta desde CLI
python main.py query "¿Cuáles son los plazos de IVA trimestral?"

# Dashboard web
open http://localhost:8000
```

## Arquitectura

```
docmine-fiscal/
├── main.py                  # CLI entry point
├── app.py                   # FastAPI server
├── modules/
│   ├── ingestion.py         # Document loaders
│   ├── chunking.py          # Semantic chunking
│   ├── embeddings.py        # Sentence-BERT
│   ├── vector_store.py      # ChromaDB wrapper
│   ├── rag_engine.py        # Multi-query + rerank
│   └── llm.py               # Ollama interface
├── templates/
│   ├── chat.html            # Chat interface
│   └── documents.html       # Document manager
└── data/
    ├── chroma/              # Vector DB
    └── uploads/             # Original docs
```

### Stack técnico

- **LLM:** Ollama llama3 (8B params, local)
- **Embeddings:** Sentence-BERT (all-MiniLM-L6-v2)
- **Vector DB:** ChromaDB con persistencia
- **OCR:** Tesseract para PDFs escaneados
- **Backend:** FastAPI + Python 3.11
- **Frontend:** HTML5 + HTMX + TailwindCSS

## Aprendizajes clave

### Lo que funcionó bien

1. **100% local = sin costos:** Procesar 500 docs sin pagar APIs
2. **Chunking semántico:** Respeta párrafos, mejor que fixed-size
3. **Multi-query RAG:** 5 queries diferentes mejoran recall
4. **Reranking:** Cross-encoder reduce respuestas irrelevantes

### Problemas resueltos

- **PDFs escaneados:** OCR con Tesseract + limpieza de ruido
- **Documentos mixtos (ES/EN):** Detección de idioma por chunk
- **Respuestas genéricas:** Añadir "SOLO responde basándote en el contexto"
- **ChromaDB locks:** Usar PersistentClient con paths absolutos

### Optimizaciones

- **Embeddings cacheados:** Evitar recomputar docs existentes
- **Batch ingestion:** Procesar 100 docs en paralelo
- **Query expansion:** Sinónimos automáticos para términos fiscales
- **Filtrado por metadata:** Búsqueda solo en docs del año X

### Siguientes pasos

- [ ] Soporte para tablas en PDFs (Camelot)
- [ ] Fine-tuning de embeddings con términos fiscales
- [ ] Sistema de alertas (notificar cambios BOE)
- [ ] Multi-tenant (un ChromaDB por cliente)

## Métricas

- **Documentos indexados:** 487 archivos
- **Chunks totales:** 12,456 fragmentos
- **Tamaño ChromaDB:** 340 MB
- **Tiempo consulta:** ~3s (búsqueda + LLM)
- **Precisión:** 82% (evaluación manual 50 queries)
- **Líneas código:** 1,847 líneas Python

## Casos de uso reales

### Consultor fiscal
```bash
# Buscar información sobre IVA
python main.py query "¿Cuál es el tipo reducido de IVA en 2024?"

# Filtrar solo por documentos AEAT
python main.py query "retenciones autónomos" --source AEAT

# Exportar respuesta con citas
python main.py query "calendario fiscal 2024" --export respuesta.md
```

### Abogado contratista
```bash
# Buscar cláusulas en contratos
python main.py query "cláusula de confidencialidad" --doctype contrato

# Comparar versiones
python main.py compare contrato_v1.pdf contrato_v2.pdf

# Extraer todas las fechas
python main.py extract dates --input contratos/
```

## Configuración avanzada

```yaml
# config.yaml
chunk_size: 500
chunk_overlap: 50
embedding_model: "all-MiniLM-L6-v2"
llm_model: "llama3"
llm_temperature: 0.1
max_context_chunks: 5
rerank_top_k: 3
```

## Comparativa con alternativas

| Feature | DocMine Fiscal | ChatPDF | DocuChat |
|---------|---------------|----------|----------|
| Local | ✅ | ❌ | ❌ |
| Gratis | ✅ | Límites | Límites |
| OCR | ✅ | ✅ | ❌ |
| Multi-query | ✅ | ❌ | ✅ |
| Rerank | ✅ | ❌ | ❌ |
| API | ✅ | ✅ | ❌ |

## Deploy

```bash
# Docker
docker build -t docmine-fiscal .
docker run -p 8000:8000 -v $(pwd)/data:/app/data docmine-fiscal

# Systemd
sudo cp scripts/docmine.service /etc/systemd/system/
sudo systemctl enable docmine
sudo systemctl start docmine
```

## Enlaces útiles

- [Ollama](https://ollama.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
