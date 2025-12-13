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
├── index.html             # UI completa (~500KB, Tailwind + JS vanilla)
├── backend/
│   ├── main.py            # FastAPI server (endpoints + ejecución pipelines)
│   └── modules/
│       ├── knowledge.py   # RAG: embeddings + ChromaDB
│       └── scout.py       # Análisis con Claude API
├── data/                  # ChromaDB persistence + logs
└── versions/              # Histórico de versiones
```

## Estado Actual: v10.10

### Implementado
- [x] Pipeline Builder (43 nodos, conexiones SVG, ejecución real)
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
- [x] **Canvas Pro v10.10:**
  - Insertar nodo en conexión existente
  - Conectar arrastrando a puertos
  - Minimap funcional con colores
  - Animación de flujo en conexiones
  - Estados visuales de nodos (executing, success, error)
  - Atajos de teclado completos (Ctrl+C/V, Supr, etc.)
- [x] **Sistema Educativo v10.10:**
  - Tooltips en conexiones (qué datos fluyen)
  - Panel de nodo mejorado (Qué hace, Input/Output, Cuándo usarlo)
  - Learning Path export (guía + prompts para Claude Code)
- [x] **7 Nuevos Nodos v10.10:**
  - Telegram Bot, Telegram Trigger
  - REST API Call, Text Splitter
  - Notion, Airtable, Spreadsheet

### Categorías de Nodos (43 total)
| Categoría | Nodos |
|-----------|-------|
| Trigger | Manual, File Watch, Cron, Webhook, Telegram |
| Proceso | Whisper, Tesseract OCR, PDF Parser, BeautifulSoup, REST API, Text Splitter |
| IA | Claude (CLI), Claude Transform, Ollama, OpenAI |
| Storage | ChromaDB, SQLite, Redis, Notion, Airtable, Spreadsheet |
| Flow | If, Loop, Delay, Inspector |
| Output | File, Notify, Email, Slack, Telegram |

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
- **Canvas v10.10**: Funciones de flujo: `startFlowAnimation()`, `setNodeState()`, `simulateFlowExecution()`
- **Educativo v10.10**: `NODE_EDUCATION_DATA` con metadata de 43 nodos, `getNodeUsageTip()` para tips contextuales
- **Learning Path v10.10**: `exportLearningPath()` genera guía Markdown con prompts para Claude Code
