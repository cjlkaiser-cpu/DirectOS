
# DirectOS v10.10 - Pipeline Builder Pro

> Tu cockpit de desarrollo con IA integrada, Human-in-the-Loop y Memoria Evolutiva

## Qué es

DirectOS es tu **cockpit de desarrollo** para el ecosistema minerOS. Diseña pipelines visualmente, ejecútalos con IA real (Claude CLI), supervisa cada paso con HITL, y aprende cómo funcionan las automatizaciones.

## Novedades v10.10

### Canvas Pro - UX Mejorada
| Feature | Descripción |
|---------|-------------|
| **Insertar en conexión** | Arrastra un nodo sobre una línea → se inserta automáticamente |
| **Conectar en puertos** | Suelta cerca de un puerto → se conecta automáticamente |
| **Minimap funcional** | Vista miniatura del canvas con colores por categoría |
| **Animación de flujo** | Pulso animado en conexiones durante ejecución |
| **Preview visual** | Botón para simular ejecución paso a paso |
| **Estados de nodos** | Visual: ejecutando (amarillo), success (✓), error (✗) |
| **Colores por tipo** | Conexiones coloreadas según tipo de dato |

### Atajos de Teclado
| Atajo | Acción |
|-------|--------|
| `Ctrl/Cmd+Z` | Deshacer |
| `Ctrl/Cmd+Shift+Z` | Rehacer |
| `Ctrl/Cmd+S` | Guardar pipeline |
| `Ctrl/Cmd+C/V` | Copiar/Pegar nodo |
| `Ctrl/Cmd+L` | Auto-layout |
| `Supr/Backspace` | Eliminar nodo |
| `Escape` | Deseleccionar |
| `+/-/0` | Zoom in/out/reset |

### Sistema Educativo
| Feature | Descripción |
|---------|-------------|
| **Tooltips en conexiones** | Hover sobre línea → explica qué datos fluyen y por qué |
| **Panel de nodo mejorado** | "Qué hace", Input/Output, "Cuándo usarlo" |
| **Learning Path export** | Genera guía paso a paso con prompts para Claude Code |

### 7 Nuevos Nodos
| Nodo | Categoría | Descripción |
|------|-----------|-------------|
| **Telegram Bot** | Output | Envía mensajes, fotos o archivos a Telegram |
| **Telegram Trigger** | Trigger | Recibe mensajes y comandos desde Telegram |
| **REST API Call** | Proceso | Llama a cualquier API REST externa |
| **Text Splitter** | Proceso | Divide textos largos en chunks para RAG |
| **Notion** | Storage | Crea páginas y bases de datos en Notion |
| **Airtable** | Storage | Lee y escribe en bases de datos Airtable |
| **Spreadsheet** | Storage | Lee y escribe archivos CSV y Excel |

---

## Novedades v10.9

### MINEROS BRAIN - Claude Intelligence Core
Sistema centralizado para todas las interacciones con Claude:

| Componente | Descripción |
|------------|-------------|
| **System Prompt** | Identidad consistente de DirectOS Assistant |
| **Context Builder** | Construye contexto dinámico (pipeline, historial, nodos) |
| **JSON Parser** | Parser robusto que auto-repara respuestas |
| **API Unificada** | `askClaudeUnified()` para todas las llamadas |

### MINEROS MEMORY - Memoria Evolutiva
Sistema de aprendizaje continuo basado en localStorage:

| Feature | Descripción |
|---------|-------------|
| **Tracking de Nodos** | Registra qué nodos usas más frecuentemente |
| **Flujos Favoritos** | Detecta secuencias de nodos que repites |
| **Sugerencias** | Trackea aceptadas/rechazadas para mejorar |
| **Chat Persistente** | Historial entre sesiones (últimos 50 msgs) |
| **Resumen para Claude** | Contexto de memoria para el LLM |

### Claude Intelligence Suite (v10.8)
| Feature | Descripción |
|---------|-------------|
| **Crear con IA** | Describe tu pipeline en lenguaje natural → Claude lo genera |
| **Claude Transform** | Nodo para procesar datos con prompts personalizados |
| **Debug Inteligente** | Claude sugiere soluciones cuando hay errores |
| **Validación Semántica** | Claude analiza y optimiza tu pipeline |
| **Auto-documentación** | Genera documentación Markdown del pipeline |
| **Sugerencias Proactivas** | Sugiere nodos al añadir otros |
| **Chat Contextual** | Chat flotante que conoce tu pipeline |

## Novedades v10.7

### Human-in-the-Loop Completo
| Feature | Descripción |
|---------|-------------|
| **Nodo Inspector** | Pausa didáctica mostrando origen → proceso → datos → destino |
| **Dry Run** | Simula el pipeline sin ejecutar, muestra tiempo estimado y pausas |
| **Pausas por Nodo** | Checkbox para pausar antes/después de cada nodo |
| **Tips Didácticos** | Explicaciones contextuales para aprender automatización |
| **Edición en Pausa** | Modifica datos intermedios antes de continuar |

### Claude CLI Integration (v10.3)
| Feature | Descripción |
|---------|-------------|
| **Sin coste API** | Usa tu suscripción Pro/Max directamente |
| **Nodo Claude** | Arrastra al canvas y conecta |
| **Endpoint REST** | `/api/claude/ask` para integración |

### Pipeline Execution Real (v10.1)
| Feature | Descripción |
|---------|-------------|
| **36 Nodos** | Triggers, Proceso, IA, Storage, Flow, Output |
| **Conexiones SVG** | Bezier curves arrastrables |
| **Ejecución Secuencial** | Los pipelines se ejecutan de verdad |
| **Snap to Grid** | Alineación automática 20px |

### Prompt Builder Pro
| Feature | Descripción |
|---------|-------------|
| **Constructor Visual** | Crea prompts agénticos con el patrón de 6 secciones |
| **8 Plantillas** | code-review, doc, test, security, refactor, vault, scan-projects, update-context |
| **Instalar Directo** | Guarda en `~/.claude/commands/` con un click |

### Versiones anteriores

| v8.x | Descripción |
|---------|-------------|
| **Portfolio de Proyectos** | 11 proyectos documentados con stack, estado y métricas |
| **Pipeline Builder** | Canvas visual con conexiones SVG entre nodos |
| **App Store de Flujos** | 12 recetas de arquitectura listas para clonar |
| **42 Patrones** | Biblioteca completa de prompt patterns |
| **Glosario** | Filtros, búsqueda, progreso visual |

### Persistencia & Logs (v10.7)
| Feature | Descripción |
|---------|-------------|
| **Mis Pipelines** | Guarda, carga y elimina pipelines desde sidebar |
| **Logs Inline** | Click o doble-click en nodo para ver output |
| **Copy Output** | Copia resultado de cualquier nodo al portapapeles |

### Historial de versiones

| Versión | Highlights |
|---------|------------|
| **v10.10** | Canvas Pro + 7 nuevos nodos + Sistema Educativo |
| **v10.9** | MINEROS BRAIN & MEMORY (Memoria Evolutiva) |
| **v10.8** | Claude Intelligence Suite (7 funcionalidades IA) |
| **v10.7** | Persistencia de pipelines + Logs inline por nodo |
| **v10.5** | Human-in-the-Loop: Dry Run + Pausas por nodo |
| **v10.4** | Inspector didáctico (origen → proceso → datos → destino) |
| **v10.3** | Claude CLI Integration (sin coste API) |
| **v10.2** | Output nodes, Flow nodes, Snap to Grid |
| **v10.1** | Pipeline Builder Pro, ejecución real |
| **v10.0** | Trigger nodes (Manual, File, Cron, Webhook) |
| **v9.0** | Prompt Builder Pro + Agent Mode Backend |
| **v8.0** | Pipeline Builder + App Store Flujos |
| **v7.0** | Knowledge Base (RAG) + Scout + Glosario |

## El problema que resuelve

```
ANTES                              DESPUÉS
──────                             ───────
Planificas en tu cabeza       →    Pipeline visual con conexiones
Escribes prompt desde 0       →    33 patrones listos para copiar
No sabes qué herramienta usar →    Glosario con 28 herramientas
Copias errores a Claude       →    Scout analiza automáticamente
Configuras proyecto a mano    →    Scaffold genera todo en 1 click
```

## Posición en el Workflow minerOS

```
1. ENTENDER    → Claude navegador
2. PLANIFICAR  → Claude navegador
3. DISEÑAR     → DirectOS ← AQUÍ (Pipeline Builder + Patrones)
4. CONSTRUIR   → Claude Code (con scaffold de DirectOS)
5. PROBAR      → Terminal
6. EVALUAR     → ¿Aporta valor?
7. DOCUMENTAR  → Knowledge Base (DirectOS)
8. APRENDER    → Glosario Interactivo (DirectOS)
```

## Inicio rápido

```bash
# 1. Configurar API key (opcional, para Scout)
cp .env.example .env
# Editar .env y añadir ANTHROPIC_API_KEY

# 2. Arrancar
./start.sh

# 3. Abrir
# → Frontend: http://localhost:8000
# → API Docs: http://localhost:8000/docs
```

## Funcionalidades

### Pipeline Builder (v8.0) ⭐ NUEVO

**Canvas Visual:**
- Drag & drop de 35 nodos al canvas
- **Conexiones SVG** automáticas entre nodos (bezier curves)
- Layout automático en grid
- Indicadores de posición en pipeline

**Validación en Tiempo Real:**
- Panel lateral con análisis del stack
- ✅ Checks: API presente, persistencia, procesamiento
- ⚠️ Warnings: Sugerencias de mejora
- ❌ Errors: Dependencias faltantes
- Score de arquitectura (0-100)

**Compilar a Código:**
- Genera Python completo desde el diagrama
- Imports dinámicos según stack seleccionado
- Funciones helper para cada componente
- Copy to clipboard integrado

**Scaffold de Proyecto:**
- Vista previa de estructura de carpetas
- Opciones: `git init`, crear `venv`
- Genera `requirements.txt` automático
- Descarga script `.sh` ejecutable

### App Store de Flujos (v8.0) ⭐ NUEVO

- **12 recetas de arquitectura** probadas y documentadas
- **4 categorías**: Knowledge, Media, Automation, DevOps
- **Filtros** por categoría, complejidad, coste
- **Badges**: 🟢 Fácil / 🟡 Medio / 🔴 Avanzado
- **Modal detalle** con caso de uso y prompt táctico
- **Clonar a Arquitecto** con un click

**Flujos incluidos:**
| Flujo | Categoría | Complejidad |
|-------|-----------|-------------|
| DocMine Classic | Knowledge | 🟢 Fácil |
| Knowledge Graph | Knowledge | 🔴 Avanzado |
| Multi-Agent Research | Knowledge | 🔴 Avanzado |
| Video Search Engine | Media | 🟡 Medio |
| Audio Transcriptor | Media | 🟢 Fácil |
| Content Moderator | Media | 🟡 Medio |
| Smart Scraper Pro | Automation | 🟡 Medio |
| Data Pipeline ETL | Automation | 🟡 Medio |
| Workflow Orchestrator | Automation | 🔴 Avanzado |
| CI/CD Local | DevOps | 🟡 Medio |
| Log Analyzer | DevOps | 🟢 Fácil |
| Infra Monitor | DevOps | 🟡 Medio |

### Glosario Interactivo (v8.0 mejorado)

- **28 herramientas** organizadas en 6 categorías
- **Filtros** por categoría y estado de maestría
- **Búsqueda** en tiempo real
- **Progreso visual** con círculo SVG animado
- **Cambiar estado** desde el modal
- **Persistencia** en localStorage
- **6 nuevas herramientas**: Docker, Pytest, HTTPX, jq, Typer, Rich

### Biblioteca de Patrones (v8.1 - 33 patrones)

**Packs organizados:**

| Pack | Patrones | Tema |
|------|----------|------|
| 1. Refactoring | 3 | Código limpio |
| 2. Contenido | 1 | Multi-formato |
| 3. Seguridad | 1 | Privacidad |
| 4. Knowledge | 1 | RAG y síntesis |
| 5. Aprendizaje | 3 | Estudiar y traducir |
| 6. DevOps | 3 | Calidad código |
| 7. Debug | 2 | Errores y velocidad |
| 8. Data & API | 2 | Esquemas y endpoints |
| 9. Meta | 2 | Prompts y watchdog |
| 10. UI | 3 | Frontend bonito |
| 11. Robustez | 3 | Sistema sólido |
| 12. Data Eng | 3 | Limpieza datos |
| 13. Docs Visual | 3 | Diagramas |
| 14. RAG Avanzado | 3 | Hybrid search, reranking |
| 15. DevOps CI/CD | 3 | GitHub Actions, Docker |
| Bonus | 3 | Meta-patrón, Auditor, KISS |

**Ver `PATRONES.md` para referencia completa**

### Knowledge Base (RAG)

- Indexa automáticamente tus archivos `.md` del Desktop
- Búsqueda semántica: "¿cómo funciona RAG?"
- Usa embeddings (sentence-transformers) + ChromaDB
- Tu propio "Perplexity" local

### Scout

- Pega un error en el Monitor
- Scout lo analiza con Claude API
- Sugiere la solución directamente
- Contexto de tu stack (minerOS)

## Nodos disponibles (43)

| Categoría | Nodos |
|-----------|-------|
| **Trigger** | Manual, File Watch, Cron, Webhook, **Telegram** |
| **Proceso** | Whisper, Tesseract OCR, PDF Parser, BeautifulSoup, **REST API**, **Text Splitter** |
| **IA** | Claude (CLI), Claude Transform, Ollama, OpenAI |
| **Storage** | ChromaDB, SQLite, Redis, **Notion**, **Airtable**, **Spreadsheet** |
| **Flow** | If, Loop, Delay, Inspector |
| **Output** | File, Notify, Email, Slack, **Telegram** |

## Arquitectura

```
DirectOS/
├── frontend/
│   └── index.html          ← UI completa (Tailwind + JS vanilla)
├── backend/
│   ├── main.py             ← FastAPI server
│   ├── modules/
│   │   ├── knowledge.py    ← RAG: embeddings + ChromaDB
│   │   └── scout.py        ← Análisis con Claude
│   └── requirements.txt
├── data/
│   ├── vectors/            ← ChromaDB persistence
│   └── logs/               ← Logs del sistema
├── versions/               ← Histórico de versiones
├── PATRONES.md             ← 33 patrones documentados
├── MEJORAS.md              ← Roadmap y mejoras futuras
├── start.sh                ← Script de arranque
├── .env.example            ← Variables de entorno
└── README.md
```

## Stack técnico

### Frontend
- HTML5 + Tailwind CSS (CDN)
- JavaScript vanilla (sin frameworks)
- SVG para conexiones del pipeline
- html2canvas (exportación PNG)
- Font Awesome (iconos)

### Backend
- FastAPI + Uvicorn
- sentence-transformers (all-MiniLM-L6-v2)
- ChromaDB (vector database)
- Anthropic SDK (Claude API)
- Loguru (logging)

## API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/api/health` | GET | Estado del sistema |
| `/api/tools` | GET | Lista de 35 nodos |
| `/api/claude/ask` | POST | Ejecutar Claude CLI |
| `/api/claude/status` | GET | Verificar Claude disponible |
| `/api/agent/execute` | POST | Ejecutar pipeline |
| `/api/search` | POST | Búsqueda semántica |
| `/api/scout/analyze` | POST | Analizar error con Claude |

## Requisitos

- Python 3.9+
- Claude Code CLI (para nodo Claude)
- ~2GB RAM (para embeddings)
- ANTHROPIC_API_KEY (opcional, para Scout)

## Documentación

- **TUTORIAL.md**: Guía paso a paso de todas las funcionalidades
- **CHANGELOG.md**: Historial detallado de cambios
- **tutorial.html**: Tutorial interactivo con demos

## Filosofía

- **minerOS style**: Herramienta que aporta valor real
- **Local-first**: Tu data en tu máquina
- **Incremental**: Funciona sin backend (modo básico)
- **KISS**: Simple, debuggeable, modular
- **Visual-first**: Diseña antes de escribir código

---

## Screenshots

### Pipeline Builder
```
┌─────────────────────────────────────────────────────────────┐
│  [FastAPI] ──→ [ChromaDB] ──→ [Ollama] ──→ [SQLite]        │
│     │              │              │            │            │
│  Validación: ✅ API  ✅ Storage  ✅ LLM  Score: 85/100     │
└─────────────────────────────────────────────────────────────┘
```

### App Store de Flujos
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ 📄 DocMine   │  │ 🎬 Video     │  │ 🤖 Multi     │
│    Classic   │  │    Search    │  │    Agent     │
│ 🟢 Easy      │  │ 🟡 Medium    │  │ 🔴 Advanced  │
│ 💻 Local     │  │ 💻 Local     │  │ 💸 API       │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

Parte del ecosistema **minerOS** | Creado por Carlos | Dic 2024
