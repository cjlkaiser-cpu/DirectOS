"""
DirectOS Backend v6.0
=====================
FastAPI server para Knowledge Base (RAG) y Scout (análisis de logs)

Ejecutar:
    uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from loguru import logger
import time

# Importar módulos (se crearán después)
from modules.knowledge import KnowledgeBase
from modules.scout import Scout

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

app = FastAPI(
    title="DirectOS API",
    description="Backend para Knowledge Base y Scout",
    version="6.0.0"
)

# CORS para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = Path(__file__).parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
DATA_DIR = BASE_DIR / "data"

# Inicializar módulos
knowledge = KnowledgeBase(data_dir=DATA_DIR / "vectors")
scout = Scout()

# Configurar logging
logger.add(DATA_DIR / "logs" / "directos.log", rotation="1 MB")

# =============================================================================
# MODELOS
# =============================================================================

class SearchQuery(BaseModel):
    query: str
    limit: int = 5

class SearchResult(BaseModel):
    text: str
    source: str
    score: float

class ScoutRequest(BaseModel):
    error_text: str
    context: str = ""

class ScoutResponse(BaseModel):
    analysis: str
    suggestion: str
    confidence: str

# =============================================================================
# ENDPOINTS - HEALTH
# =============================================================================

@app.get("/api/health")
async def health_check():
    """Health check del servidor"""
    return {
        "status": "online",
        "timestamp": time.time(),
        "version": "6.0.0",
        "modules": {
            "knowledge": knowledge.is_ready(),
            "scout": scout.is_ready()
        }
    }

# =============================================================================
# ENDPOINTS - KNOWLEDGE BASE
# =============================================================================

@app.post("/api/search", response_model=list[SearchResult])
async def semantic_search(query: SearchQuery):
    """Búsqueda semántica en la knowledge base"""
    if not knowledge.is_ready():
        raise HTTPException(status_code=503, detail="Knowledge base no inicializada")

    results = knowledge.search(query.query, limit=query.limit)
    return results

@app.post("/api/index")
async def index_documents(folder_path: str = None):
    """Indexar documentos markdown"""
    # Por defecto, indexar archivos del Desktop relacionados con aprendizaje
    if folder_path is None:
        folder_path = str(Path.home() / "Desktop")

    count = knowledge.index_folder(folder_path)
    return {"indexed": count, "path": folder_path}

@app.get("/api/stats")
async def knowledge_stats():
    """Estadísticas de la knowledge base"""
    return knowledge.get_stats()

# =============================================================================
# ENDPOINTS - SCOUT
# =============================================================================

@app.post("/api/scout/analyze", response_model=ScoutResponse)
async def analyze_error(request: ScoutRequest):
    """Analizar error con Claude y sugerir solución"""
    if not scout.is_ready():
        raise HTTPException(status_code=503, detail="Scout no configurado (falta API key)")

    result = await scout.analyze(request.error_text, request.context)
    return result

# =============================================================================
# FRONTEND (SERVIR ARCHIVOS ESTÁTICOS)
# =============================================================================

@app.get("/")
async def serve_frontend():
    """Servir el frontend"""
    return FileResponse(FRONTEND_DIR / "index.html")

# Montar archivos estáticos si los hubiera
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    logger.info("Iniciando DirectOS Backend v6.0")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
