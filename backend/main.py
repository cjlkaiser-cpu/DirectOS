"""
DirectOS Backend v9.0 - Agent Mode
==================================
FastAPI server con:
- Knowledge Base (RAG)
- Scout (análisis de logs)
- Agent Mode: Pipeline Executor, Watchdog, Scheduler, Notifier

Ejecutar:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from loguru import logger
from typing import Optional, List
import time
import json
import uuid
import asyncio

# Importar módulos
from modules.knowledge import KnowledgeBase
from modules.scout import Scout
from modules.content import ContentManager

# Agent Mode v9.0
from modules.executor import PipelineExecutor, PipelineRun
from modules.watchdog_service import WatchdogService, WatchConfig, WATCH_PRESETS
from modules.scheduler import SchedulerService, ScheduledTask, SCHEDULE_PRESETS
from modules.notifier import NotifierService

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

app = FastAPI(
    title="DirectOS API",
    description="Backend para Knowledge Base, Scout y Agent Mode",
    version="9.0.0"
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
content = ContentManager(base_dir=DATA_DIR / "content")

# Agent Mode v9.0
executor = PipelineExecutor(work_dir=DATA_DIR / "runs")
watchdog = WatchdogService(config_path=DATA_DIR / "agent" / "watches.json")
scheduler = SchedulerService(config_path=DATA_DIR / "agent" / "schedules.json")
notifier = NotifierService(config_path=DATA_DIR / "agent" / "notifier.json")

# Configurar logging
logger.add(DATA_DIR / "logs" / "directos.log", rotation="1 MB")

# Crear directorio agent si no existe
(DATA_DIR / "agent").mkdir(exist_ok=True)

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

# Modelos para Offline-First Sync
class ToolStatusUpdate(BaseModel):
    status: str  # 'used' | 'learning' | 'new'

class ProjectCreate(BaseModel):
    name: str
    description: str = ""
    status: str = "active"  # 'production' | 'active' | 'archived' | 'learning'
    stack: list[str] = []
    version: str = "v1.0"
    repo: str = ""

class ProjectUpdate(BaseModel):
    name: str = None
    description: str = None
    status: str = None
    stack: list[str] = None
    version: str = None
    repo: str = None

class ArchitectureCreate(BaseModel):
    name: str
    description: str = ""
    nodes: list[dict] = []  # Lista de nodos del canvas
    projectId: str = None

class ArchitectureUpdate(BaseModel):
    name: str = None
    description: str = None
    nodes: list[dict] = None
    projectId: str = None

# Modelos para Sync con minerOS móvil
class InboxItem(BaseModel):
    """Idea/captura desde minerOS móvil"""
    type: str = "idea"  # 'idea' | 'bug' | 'todo' | 'duda'
    content: str
    project: str = None  # ID del proyecto relacionado
    priority: str = "normal"  # 'low' | 'normal' | 'high'
    tags: list[str] = []
    deviceId: str = None  # Identificador del dispositivo móvil

class InboxBatch(BaseModel):
    """Lote de items para sync"""
    items: list[InboxItem]
    deviceId: str
    lastSync: float = None  # Timestamp del último sync

class SyncStatus(BaseModel):
    """Estado del sync"""
    deviceId: str
    lastSync: float
    pendingItems: int = 0

# Modelos para Agent Mode v9.0
class PipelineExecuteRequest(BaseModel):
    """Request para ejecutar un pipeline"""
    name: str = "Pipeline"
    nodes: List[dict]
    connections: List[dict] = []

class WatchCreateRequest(BaseModel):
    """Crear un watch de archivos"""
    name: str
    directory: str
    patterns: List[str]  # ["*.pdf", "*.jpg"]
    pipeline_id: str = ""
    recursive: bool = False

class ScheduleCreateRequest(BaseModel):
    """Crear una tarea programada"""
    name: str
    pipeline_id: str
    schedule_type: str  # "cron" o "interval"
    schedule: str  # "0 9 * * *" o "15m"

class NotificationSettingsRequest(BaseModel):
    """Actualizar settings de notificaciones"""
    desktop_enabled: Optional[bool] = None
    sound_enabled: Optional[bool] = None
    in_app_enabled: Optional[bool] = None

# =============================================================================
# ENDPOINTS - HEALTH
# =============================================================================

@app.get("/api/health")
async def health_check():
    """Health check del servidor"""
    return {
        "status": "online",
        "timestamp": time.time(),
        "version": "9.0.0",
        "modules": {
            "knowledge": knowledge.is_ready(),
            "scout": scout.is_ready(),
            "content": content.get_stats()
        },
        "agent": {
            "executor": len(executor.runs),
            "watchdog": watchdog.get_status(),
            "scheduler": scheduler.get_status(),
            "notifier": notifier.get_status()
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
# ENDPOINTS - CONTENT (Herramientas, Patrones, Flows)
# =============================================================================

@app.get("/api/tools")
async def get_tools():
    """Obtener todas las herramientas desde archivos .md"""
    tools = content.get_tools()
    return {"tools": tools, "count": len(tools)}

@app.get("/api/tools/states")
async def get_tool_states():
    """Obtener todos los estados de herramientas (sync)"""
    store = load_json_store("tool_states.json")
    return {"states": store}

@app.get("/api/tools/{tool_id}")
async def get_tool(tool_id: str):
    """Obtener una herramienta específica por ID"""
    tool = content.get_tool(tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail=f"Herramienta '{tool_id}' no encontrada")
    return tool

@app.get("/api/patterns")
async def get_patterns():
    """Obtener todos los patrones de prompts"""
    patterns = content.get_patterns()
    return {"patterns": patterns, "count": len(patterns)}

@app.get("/api/flows")
async def get_flows():
    """Obtener todos los flows del App Store"""
    flows = content.get_flows()
    return {"flows": flows, "count": len(flows)}

@app.get("/api/presets")
async def get_presets():
    """Obtener todos los presets de arquitectura"""
    presets = content.get_presets()
    return {"presets": presets, "count": len(presets)}

@app.get("/api/projects")
async def get_projects():
    """Obtener todos los proyectos documentados"""
    projects = content.get_projects()
    return {"projects": projects, "count": len(projects)}

@app.get("/api/projects/sync")
async def get_projects_sync():
    """Obtener proyectos para sync (desde JSON store)"""
    store = load_json_store("projects.json")
    return {"projects": list(store.values()), "count": len(store)}

@app.get("/api/projects/{project_id}")
async def get_project(project_id: str):
    """Obtener un proyecto específico por ID"""
    project = content.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail=f"Proyecto '{project_id}' no encontrado")
    return project

@app.post("/api/content/refresh")
async def refresh_content():
    """Refrescar cache de contenido (recargar desde disco)"""
    content.refresh_cache()
    stats = content.get_stats()
    return {"status": "refreshed", "stats": stats}

@app.get("/api/content/stats")
async def content_stats():
    """Estadísticas del contenido"""
    return content.get_stats()

# =============================================================================
# ENDPOINTS - SLASH COMMANDS (Claude Code)
# =============================================================================

COMMANDS_DIR = Path.home() / ".claude" / "commands"

class CommandCreate(BaseModel):
    """Crear/actualizar un slash command"""
    name: str
    description: str
    allowed_tools: List[str] = []
    argument_hint: str = ""
    content: str  # Markdown completo del comando

class CommandResponse(BaseModel):
    """Respuesta de un comando"""
    name: str
    description: str
    allowed_tools: List[str]
    argument_hint: str
    content: str
    path: str

@app.get("/api/commands")
async def list_commands():
    """
    Listar todos los slash commands de ~/.claude/commands/
    """
    if not COMMANDS_DIR.exists():
        return {"commands": [], "count": 0, "path": str(COMMANDS_DIR)}

    commands = []
    for file in COMMANDS_DIR.glob("*.md"):
        try:
            content = file.read_text()
            # Parsear frontmatter básico
            meta = {"name": file.stem, "description": "", "allowed_tools": [], "argument_hint": ""}

            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    for line in frontmatter.split("\n"):
                        if ":" in line:
                            key, value = line.split(":", 1)
                            key = key.strip().replace("-", "_")
                            value = value.strip()
                            if key == "description":
                                meta["description"] = value
                            elif key == "allowed_tools":
                                meta["allowed_tools"] = [t.strip() for t in value.split(",")]
                            elif key == "argument_hint":
                                meta["argument_hint"] = value

            commands.append({
                "name": file.stem,
                "description": meta["description"],
                "allowed_tools": meta["allowed_tools"],
                "argument_hint": meta["argument_hint"],
                "path": str(file)
            })
        except Exception as e:
            logger.error(f"Error parsing command {file}: {e}")

    return {"commands": commands, "count": len(commands), "path": str(COMMANDS_DIR)}

@app.get("/api/commands/{name}")
async def get_command(name: str):
    """
    Obtener un slash command específico
    """
    file_path = COMMANDS_DIR / f"{name}.md"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Comando '{name}' no encontrado")

    content = file_path.read_text()

    # Parsear frontmatter
    meta = {"description": "", "allowed_tools": [], "argument_hint": ""}

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            for line in frontmatter.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip().replace("-", "_")
                    value = value.strip()
                    if key == "description":
                        meta["description"] = value
                    elif key == "allowed_tools":
                        meta["allowed_tools"] = [t.strip() for t in value.split(",")]
                    elif key == "argument_hint":
                        meta["argument_hint"] = value

    return {
        "name": name,
        "description": meta["description"],
        "allowed_tools": meta["allowed_tools"],
        "argument_hint": meta["argument_hint"],
        "content": content,
        "path": str(file_path)
    }

@app.post("/api/commands")
async def save_command(command: CommandCreate):
    """
    Guardar un slash command en ~/.claude/commands/

    Crea o sobrescribe el archivo {name}.md
    """
    # Asegurar que existe el directorio
    COMMANDS_DIR.mkdir(parents=True, exist_ok=True)

    file_path = COMMANDS_DIR / f"{command.name}.md"

    # Guardar contenido
    file_path.write_text(command.content)

    logger.info(f"Command saved: {command.name} → {file_path}")

    return {
        "name": command.name,
        "path": str(file_path),
        "status": "saved",
        "message": f"Comando /{command.name} guardado correctamente"
    }

@app.delete("/api/commands/{name}")
async def delete_command(name: str):
    """
    Eliminar un slash command
    """
    file_path = COMMANDS_DIR / f"{name}.md"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"Comando '{name}' no encontrado")

    file_path.unlink()
    logger.info(f"Command deleted: {name}")

    return {"deleted": name, "message": f"Comando /{name} eliminado"}

# =============================================================================
# HELPERS - PERSISTENCIA JSON (para offline-first)
# =============================================================================

SYNC_DIR = DATA_DIR / "sync"
SYNC_DIR.mkdir(exist_ok=True)

def load_json_store(filename: str) -> dict:
    """Cargar store JSON desde disco"""
    filepath = SYNC_DIR / filename
    if filepath.exists():
        return json.loads(filepath.read_text())
    return {}

def save_json_store(filename: str, data: dict):
    """Guardar store JSON en disco"""
    filepath = SYNC_DIR / filename
    filepath.write_text(json.dumps(data, indent=2, ensure_ascii=False))

# =============================================================================
# ENDPOINTS - TOOLS STATUS (Offline-First)
# =============================================================================

@app.put("/api/tools/{tool_id}/status")
async def update_tool_status(tool_id: str, update: ToolStatusUpdate):
    """Actualizar status de una herramienta (used/learning/new)"""
    store = load_json_store("tool_states.json")
    store[tool_id] = {
        "status": update.status,
        "updatedAt": time.time()
    }
    save_json_store("tool_states.json", store)
    logger.info(f"Tool {tool_id} status → {update.status}")
    return {"id": tool_id, "status": update.status}

# =============================================================================
# ENDPOINTS - PROJECTS CRUD (Offline-First)
# =============================================================================

@app.post("/api/projects")
async def create_project(project: ProjectCreate):
    """Crear nuevo proyecto"""
    store = load_json_store("projects.json")
    project_id = str(uuid.uuid4())[:8]

    store[project_id] = {
        "id": project_id,
        "name": project.name,
        "description": project.description,
        "status": project.status,
        "stack": project.stack,
        "version": project.version,
        "repo": project.repo,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }
    save_json_store("projects.json", store)
    logger.info(f"Project created: {project.name} ({project_id})")
    return store[project_id]

@app.put("/api/projects/{project_id}")
async def update_project(project_id: str, update: ProjectUpdate):
    """Actualizar proyecto existente"""
    store = load_json_store("projects.json")

    if project_id not in store:
        raise HTTPException(status_code=404, detail=f"Proyecto '{project_id}' no encontrado")

    # Actualizar solo campos proporcionados
    for field, value in update.model_dump(exclude_none=True).items():
        store[project_id][field] = value
    store[project_id]["updatedAt"] = time.time()

    save_json_store("projects.json", store)
    logger.info(f"Project updated: {project_id}")
    return store[project_id]

@app.delete("/api/projects/{project_id}")
async def delete_project(project_id: str):
    """Eliminar proyecto"""
    store = load_json_store("projects.json")

    if project_id not in store:
        raise HTTPException(status_code=404, detail=f"Proyecto '{project_id}' no encontrado")

    deleted = store.pop(project_id)
    save_json_store("projects.json", store)
    logger.info(f"Project deleted: {project_id}")
    return {"deleted": project_id, "name": deleted["name"]}

# =============================================================================
# ENDPOINTS - ARCHITECTURES CRUD (Offline-First)
# =============================================================================

@app.get("/api/architectures")
async def get_architectures():
    """Listar todas las arquitecturas"""
    store = load_json_store("architectures.json")
    return {"architectures": list(store.values()), "count": len(store)}

@app.get("/api/architectures/{arch_id}")
async def get_architecture(arch_id: str):
    """Obtener una arquitectura específica"""
    store = load_json_store("architectures.json")

    if arch_id not in store:
        raise HTTPException(status_code=404, detail=f"Arquitectura '{arch_id}' no encontrada")

    return store[arch_id]

@app.post("/api/architectures")
async def create_architecture(arch: ArchitectureCreate):
    """Crear nueva arquitectura"""
    store = load_json_store("architectures.json")
    arch_id = str(uuid.uuid4())[:8]

    store[arch_id] = {
        "id": arch_id,
        "name": arch.name,
        "description": arch.description,
        "nodes": arch.nodes,
        "projectId": arch.projectId,
        "createdAt": time.time(),
        "updatedAt": time.time()
    }
    save_json_store("architectures.json", store)
    logger.info(f"Architecture created: {arch.name} ({arch_id})")
    return store[arch_id]

@app.put("/api/architectures/{arch_id}")
async def update_architecture(arch_id: str, update: ArchitectureUpdate):
    """Actualizar arquitectura existente"""
    store = load_json_store("architectures.json")

    if arch_id not in store:
        raise HTTPException(status_code=404, detail=f"Arquitectura '{arch_id}' no encontrada")

    for field, value in update.model_dump(exclude_none=True).items():
        store[arch_id][field] = value
    store[arch_id]["updatedAt"] = time.time()

    save_json_store("architectures.json", store)
    logger.info(f"Architecture updated: {arch_id}")
    return store[arch_id]

@app.delete("/api/architectures/{arch_id}")
async def delete_architecture(arch_id: str):
    """Eliminar arquitectura"""
    store = load_json_store("architectures.json")

    if arch_id not in store:
        raise HTTPException(status_code=404, detail=f"Arquitectura '{arch_id}' no encontrada")

    deleted = store.pop(arch_id)
    save_json_store("architectures.json", store)
    logger.info(f"Architecture deleted: {arch_id}")
    return {"deleted": arch_id, "name": deleted["name"]}

# =============================================================================
# ENDPOINTS - SYNC CON MINEROS MÓVIL
# =============================================================================

@app.post("/api/inbox")
async def receive_inbox(item: InboxItem):
    """
    Recibir una idea/captura desde minerOS móvil.

    El móvil envía ideas cuando detecta WiFi.
    DirectOS las guarda en el inbox para procesarlas.
    """
    store = load_json_store("inbox.json")
    item_id = f"inbox_{int(time.time() * 1000)}"

    store[item_id] = {
        "id": item_id,
        "type": item.type,
        "content": item.content,
        "project": item.project,
        "priority": item.priority,
        "tags": item.tags,
        "deviceId": item.deviceId,
        "receivedAt": time.time(),
        "processed": False
    }

    save_json_store("inbox.json", store)
    logger.info(f"📥 Inbox: {item.type} recibido desde {item.deviceId}")

    return {"id": item_id, "status": "received"}

@app.post("/api/inbox/batch")
async def receive_inbox_batch(batch: InboxBatch):
    """
    Recibir múltiples ideas en un solo request (más eficiente).

    El móvil acumula ideas offline y las envía todas juntas.
    """
    store = load_json_store("inbox.json")
    received = []

    for item in batch.items:
        item_id = f"inbox_{int(time.time() * 1000)}_{len(received)}"
        store[item_id] = {
            "id": item_id,
            "type": item.type,
            "content": item.content,
            "project": item.project,
            "priority": item.priority,
            "tags": item.tags,
            "deviceId": batch.deviceId,
            "receivedAt": time.time(),
            "processed": False
        }
        received.append(item_id)

    save_json_store("inbox.json", store)

    # Actualizar estado de sync del dispositivo
    sync_store = load_json_store("sync_status.json")
    sync_store[batch.deviceId] = {
        "deviceId": batch.deviceId,
        "lastSync": time.time(),
        "itemsReceived": len(received)
    }
    save_json_store("sync_status.json", sync_store)

    logger.info(f"📥 Inbox batch: {len(received)} items desde {batch.deviceId}")

    return {"received": len(received), "ids": received}

@app.get("/api/inbox")
async def get_inbox(processed: bool = None):
    """
    Obtener items del inbox.

    - Sin filtro: todos los items
    - processed=false: solo pendientes
    - processed=true: solo procesados
    """
    store = load_json_store("inbox.json")
    items = list(store.values())

    if processed is not None:
        items = [i for i in items if i.get("processed") == processed]

    # Ordenar por fecha (más recientes primero)
    items.sort(key=lambda x: x.get("receivedAt", 0), reverse=True)

    return {"items": items, "count": len(items)}

@app.put("/api/inbox/{item_id}/process")
async def mark_inbox_processed(item_id: str):
    """Marcar un item del inbox como procesado."""
    store = load_json_store("inbox.json")

    if item_id not in store:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' no encontrado")

    store[item_id]["processed"] = True
    store[item_id]["processedAt"] = time.time()
    save_json_store("inbox.json", store)

    return {"id": item_id, "processed": True}

@app.delete("/api/inbox/{item_id}")
async def delete_inbox_item(item_id: str):
    """Eliminar un item del inbox."""
    store = load_json_store("inbox.json")

    if item_id not in store:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' no encontrado")

    deleted = store.pop(item_id)
    save_json_store("inbox.json", store)

    return {"deleted": item_id}

@app.get("/api/sync")
async def get_sync_data(since: float = 0):
    """
    Obtener datos para sincronizar con minerOS móvil.

    El móvil llama aquí para obtener:
    - Proyectos (para el selector)
    - Herramientas (para referencia)
    - Último timestamp de sync

    Args:
        since: Timestamp desde el cual obtener cambios (0 = todo)
    """
    projects = content.get_projects()
    tools = content.get_tools()

    # Simplificar datos para el móvil (solo lo necesario)
    projects_lite = [
        {
            "id": p.get("id"),
            "name": p.get("name"),
            "status": p.get("status"),
            "version": p.get("version"),
            "description": p.get("description", "")[:100]
        }
        for p in projects
    ]

    tools_lite = [
        {
            "id": t.get("id"),
            "name": t.get("name"),
            "category": t.get("category")
        }
        for t in tools
    ]

    return {
        "timestamp": time.time(),
        "projects": projects_lite,
        "tools": tools_lite,
        "counts": {
            "projects": len(projects_lite),
            "tools": len(tools_lite)
        }
    }

@app.get("/api/sync/status")
async def get_sync_status(deviceId: str = None):
    """
    Obtener estado de sync de un dispositivo o todos.
    """
    store = load_json_store("sync_status.json")

    if deviceId:
        if deviceId in store:
            return store[deviceId]
        return {"deviceId": deviceId, "lastSync": None, "message": "Nunca sincronizado"}

    return {"devices": list(store.values())}

@app.get("/api/sync/discover")
async def discover_directos():
    """
    Endpoint de descubrimiento para minerOS móvil.

    El móvil puede hacer broadcast en la red local y buscar
    este endpoint para encontrar DirectOS automáticamente.
    """
    import socket
    hostname = socket.gethostname()

    return {
        "service": "DirectOS",
        "version": "8.1.0",
        "hostname": hostname,
        "endpoints": {
            "inbox": "/api/inbox",
            "sync": "/api/sync",
            "health": "/api/health"
        }
    }

# =============================================================================
# ENDPOINTS - AGENT MODE: EXECUTOR
# =============================================================================

@app.post("/api/agent/execute")
async def execute_pipeline(request: PipelineExecuteRequest, background_tasks: BackgroundTasks):
    """
    Ejecutar un pipeline.

    El pipeline se ejecuta en background y retorna un run_id
    para consultar el progreso.
    """
    pipeline_def = {
        "name": request.name,
        "nodes": request.nodes,
        "connections": request.connections
    }

    # Callback para notificar al completar
    def on_complete(run: PipelineRun):
        notifier.pipeline_completed(
            run.pipeline_name,
            run.status,
            run.finished_at - run.started_at if run.finished_at else 0,
            run.id
        )

    run_id = await executor.execute(pipeline_def, on_complete=on_complete)

    return {
        "run_id": run_id,
        "status": "started",
        "message": f"Pipeline '{request.name}' iniciado"
    }

@app.get("/api/agent/runs")
async def get_pipeline_runs(limit: int = 10):
    """Listar ejecuciones de pipelines"""
    return {"runs": executor.get_runs(limit)}

@app.get("/api/agent/runs/{run_id}")
async def get_pipeline_run(run_id: str):
    """Obtener estado de una ejecución específica"""
    run = executor.get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail=f"Run '{run_id}' no encontrado")
    return run

@app.post("/api/agent/runs/{run_id}/cancel")
async def cancel_pipeline_run(run_id: str):
    """Cancelar una ejecución en progreso"""
    success = executor.cancel_run(run_id)
    if not success:
        raise HTTPException(status_code=400, detail="No se puede cancelar (no existe o ya terminó)")
    return {"cancelled": run_id}

# =============================================================================
# ENDPOINTS - AGENT MODE: WATCHDOG
# =============================================================================

@app.get("/api/agent/watches")
async def get_watches():
    """Listar todos los watches configurados"""
    return {"watches": watchdog.get_watches(), "presets": WATCH_PRESETS}

@app.get("/api/agent/watches/{watch_id}")
async def get_watch(watch_id: str):
    """Obtener un watch específico"""
    watch = watchdog.get_watch(watch_id)
    if not watch:
        raise HTTPException(status_code=404, detail=f"Watch '{watch_id}' no encontrado")
    return watch

@app.post("/api/agent/watches")
async def create_watch(request: WatchCreateRequest):
    """Crear un nuevo watch de archivos"""
    config = WatchConfig(
        id=f"watch_{int(time.time())}",
        name=request.name,
        directory=request.directory,
        patterns=request.patterns,
        pipeline_id=request.pipeline_id,
        recursive=request.recursive
    )
    success = watchdog.add_watch(config)
    if not success:
        raise HTTPException(status_code=400, detail="Error creando watch (¿directorio existe?)")
    return config.to_dict()

@app.delete("/api/agent/watches/{watch_id}")
async def delete_watch(watch_id: str):
    """Eliminar un watch"""
    success = watchdog.remove_watch(watch_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Watch '{watch_id}' no encontrado")
    return {"deleted": watch_id}

@app.put("/api/agent/watches/{watch_id}/toggle")
async def toggle_watch(watch_id: str):
    """Activar/desactivar un watch"""
    watch = watchdog.get_watch(watch_id)
    if not watch:
        raise HTTPException(status_code=404, detail=f"Watch '{watch_id}' no encontrado")

    new_state = not watch.get("enabled", True)
    watchdog.update_watch(watch_id, enabled=new_state)
    return {"id": watch_id, "enabled": new_state}

@app.post("/api/agent/watchdog/start")
async def start_watchdog():
    """Iniciar el servicio de watchdog"""
    success = watchdog.start()
    return {"started": success, "status": watchdog.get_status()}

@app.post("/api/agent/watchdog/stop")
async def stop_watchdog():
    """Detener el servicio de watchdog"""
    watchdog.stop()
    return {"stopped": True, "status": watchdog.get_status()}

# =============================================================================
# ENDPOINTS - AGENT MODE: SCHEDULER
# =============================================================================

@app.get("/api/agent/schedules")
async def get_schedules():
    """Listar todas las tareas programadas"""
    return {"tasks": scheduler.get_tasks(), "presets": SCHEDULE_PRESETS}

@app.get("/api/agent/schedules/{task_id}")
async def get_schedule(task_id: str):
    """Obtener una tarea programada específica"""
    task = scheduler.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Tarea '{task_id}' no encontrada")
    return task

@app.post("/api/agent/schedules")
async def create_schedule(request: ScheduleCreateRequest):
    """Crear una nueva tarea programada"""
    task = ScheduledTask(
        id=f"task_{int(time.time())}",
        name=request.name,
        pipeline_id=request.pipeline_id,
        schedule_type=request.schedule_type,
        schedule=request.schedule
    )
    scheduler.add_task(task)
    return task.to_dict()

@app.delete("/api/agent/schedules/{task_id}")
async def delete_schedule(task_id: str):
    """Eliminar una tarea programada"""
    success = scheduler.remove_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Tarea '{task_id}' no encontrada")
    return {"deleted": task_id}

@app.put("/api/agent/schedules/{task_id}/toggle")
async def toggle_schedule(task_id: str):
    """Activar/desactivar una tarea"""
    task = scheduler.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Tarea '{task_id}' no encontrada")

    new_state = not task.get("enabled", True)
    scheduler.update_task(task_id, enabled=new_state)
    return {"id": task_id, "enabled": new_state}

@app.post("/api/agent/schedules/{task_id}/run")
async def run_schedule_now(task_id: str):
    """Ejecutar una tarea inmediatamente (fuera de horario)"""
    success = scheduler.run_now(task_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Tarea '{task_id}' no encontrada")
    return {"triggered": task_id}

@app.post("/api/agent/scheduler/start")
async def start_scheduler():
    """Iniciar el servicio de scheduler"""
    success = scheduler.start()
    return {"started": success, "status": scheduler.get_status()}

@app.post("/api/agent/scheduler/stop")
async def stop_scheduler():
    """Detener el servicio de scheduler"""
    scheduler.stop()
    return {"stopped": True, "status": scheduler.get_status()}

# =============================================================================
# ENDPOINTS - AGENT MODE: NOTIFICATIONS
# =============================================================================

@app.get("/api/agent/notifications")
async def get_notifications(limit: int = 50, unread_only: bool = False):
    """Listar notificaciones"""
    return {
        "notifications": notifier.get_notifications(limit, unread_only),
        "unread_count": notifier.get_unread_count()
    }

@app.put("/api/agent/notifications/{notif_id}/read")
async def mark_notification_read(notif_id: str):
    """Marcar notificación como leída"""
    success = notifier.mark_read(notif_id)
    return {"id": notif_id, "read": success}

@app.post("/api/agent/notifications/read-all")
async def mark_all_notifications_read():
    """Marcar todas las notificaciones como leídas"""
    notifier.mark_all_read()
    return {"status": "all read"}

@app.delete("/api/agent/notifications")
async def clear_notifications():
    """Limpiar historial de notificaciones"""
    notifier.clear()
    return {"status": "cleared"}

@app.get("/api/agent/notifications/settings")
async def get_notification_settings():
    """Obtener settings de notificaciones"""
    return notifier.get_settings()

@app.put("/api/agent/notifications/settings")
async def update_notification_settings(request: NotificationSettingsRequest):
    """Actualizar settings de notificaciones"""
    updates = {k: v for k, v in request.model_dump().items() if v is not None}
    return notifier.update_settings(**updates)

@app.post("/api/agent/notifications/test")
async def test_notification():
    """Enviar notificación de prueba"""
    notifier.success(
        title="DirectOS v9.0",
        message="Sistema de notificaciones funcionando correctamente"
    )
    return {"sent": True}

# =============================================================================
# ENDPOINTS - AGENT MODE: STATUS GENERAL
# =============================================================================

@app.get("/api/agent/status")
async def get_agent_status():
    """Estado general del Agent Mode"""
    return {
        "executor": {
            "active_runs": len([r for r in executor.runs.values() if r.status == "running"]),
            "total_runs": len(executor.runs)
        },
        "watchdog": watchdog.get_status(),
        "scheduler": scheduler.get_status(),
        "notifier": notifier.get_status()
    }

@app.post("/api/agent/start-all")
async def start_all_agents():
    """Iniciar todos los servicios del Agent Mode"""
    results = {
        "watchdog": watchdog.start(),
        "scheduler": scheduler.start()
    }
    notifier.info("Agent Mode", "Todos los servicios iniciados")
    return results

@app.post("/api/agent/stop-all")
async def stop_all_agents():
    """Detener todos los servicios del Agent Mode"""
    watchdog.stop()
    scheduler.stop()
    notifier.info("Agent Mode", "Todos los servicios detenidos")
    return {"stopped": True}

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
    logger.info("Iniciando DirectOS Backend v9.0 - Agent Mode")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
