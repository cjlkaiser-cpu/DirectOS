# DirectOS - Claude Context

> Pipeline Builder Pro con IA integrada y Human-in-the-Loop

## Quick Start

```bash
./start.sh
# Frontend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Arquitectura

```
DirectOS/
├── frontend/index.html    # UI completa (434KB, Tailwind + JS vanilla)
├── backend/
│   ├── main.py            # FastAPI server (endpoints + ejecución pipelines)
│   └── modules/
│       ├── knowledge.py   # RAG: embeddings + ChromaDB
│       └── scout.py       # Análisis con Claude API
├── data/                  # ChromaDB persistence + logs
└── versions/              # Histórico de versiones
```

## Estado Actual: v10.9

### Implementado
- [x] Pipeline Builder (36 nodos, conexiones SVG, ejecución real)
- [x] Claude CLI Integration (sin coste API)
- [x] Human-in-the-Loop (Inspector, Dry Run, Pausas por nodo)
- [x] Prompt Builder Pro (8 plantillas, instalar en ~/.claude/commands/)
- [x] App Store de Flujos (12 recetas)
- [x] Knowledge Base (RAG local)
- [x] Scout (análisis de errores)
- [x] **Persistencia de Pipelines** (guardar/cargar/eliminar en localStorage)
- [x] **Logs Inline por Nodo** (ver output, copiar, indicador visual)
- [x] **Claude Intelligence Suite v10.8:**
  - Claude Transform (nodo con prompt personalizable)
  - Debug Inteligente (Claude sugiere soluciones)
  - Validación Semántica (análisis de pipeline)
  - Auto-documentación (genera README)
  - Sugerencias Proactivas (al añadir nodos)
  - Chat Contextual (FAB flotante)
  - Pipeline Assistant (crear con lenguaje natural)
- [x] **MINEROS BRAIN v10.9:**
  - MINEROS_SYSTEM_PROMPT (identidad consistente)
  - buildClaudeContext() (contexto dinámico)
  - parseClaudeResponse() (parser JSON robusto)
  - askClaudeUnified() (API unificada)
- [x] **MINEROS MEMORY v10.9:**
  - MinerosMemory object (persistencia localStorage)
  - Tracking: nodos, pipelines, sugerencias
  - Chat history persistente (50 msgs)
  - getSummaryForClaude() (contexto memoria)

### Categorías de Nodos (36 total)
| Categoría | Nodos |
|-----------|-------|
| Trigger | Manual, File Watch, Cron, Webhook |
| Proceso | Whisper, Tesseract OCR, PDF Parser, BeautifulSoup |
| IA | Claude (CLI), Ollama, OpenAI |
| Storage | ChromaDB, SQLite, Redis |
| Flow | If, Loop, Delay, Inspector |
| Output | File, Notify, Email, Slack |

## Endpoints API

| Endpoint | Descripción |
|----------|-------------|
| `GET /api/health` | Estado del sistema |
| `GET /api/tools` | Lista de nodos |
| `POST /api/claude/ask` | Ejecutar Claude CLI |
| `POST /api/agent/execute` | Ejecutar pipeline |
| `POST /api/search` | Búsqueda semántica |

## Stack

- **Frontend**: HTML5 + Tailwind CSS + JS vanilla + SVG
- **Backend**: FastAPI + sentence-transformers + ChromaDB
- **Dependencias**: Python 3.9+, Claude Code CLI

## Convenciones

- Single HTML file para frontend (todo inline)
- JS vanilla, sin frameworks
- Funciones globales expuestas en window
- CSS con Tailwind utility classes
- IDs descriptivos para elementos del DOM

## Próximos Pasos

<!-- Actualizar según avance del proyecto -->
- [x] ~~Persistencia de pipelines (guardar/cargar)~~ v10.7
- [x] ~~Logs inline por nodo~~ v10.7
- [x] ~~MINEROS BRAIN (Context + System Prompt)~~ v10.9
- [x] ~~MINEROS MEMORY (Memoria evolutiva)~~ v10.9
- [ ] Export/Import JSON mejorado (metadata)
- [ ] Historial de ejecuciones
- [ ] Auto-save de pipelines
- [ ] Triggers automáticos (File Watch activo, Cron real)

## Notas de Desarrollo

- El frontend es un monolito HTML por diseño (fácil distribución)
- Los nodos del pipeline usan data attributes para configuración
- Las conexiones SVG se recalculan en cada render
- HITL usa Promise-based modals para pausar ejecución
- **MINEROS BRAIN**: Todas las llamadas Claude usan `askClaudeUnified()`
- **MINEROS MEMORY**: Persistencia en localStorage key `mineros_memory`
- Funciones refactorizadas: sendChatMessage, generatePipelineFromDescription, askClaudeForHelp, generateDocumentation, validateWithAI
