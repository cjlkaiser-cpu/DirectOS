# DirectOS v8.1 - Portfolio & Projects

> Centro de operaciones para diseñar arquitecturas, aprender herramientas y dominar tu stack

## Qué es

DirectOS es tu **cockpit de desarrollo** para el ecosistema minerOS. Diseña pipelines visualmente, aprende nuevas herramientas con contexto, genera código automáticamente, y documenta tus proyectos.

## Novedades v8.1

| Feature | Descripción |
|---------|-------------|
| **Portfolio de Proyectos** | 11 proyectos documentados con stack, estado y métricas |
| **Comando /vault Inteligente** | Auto-detecta y actualiza herramientas/proyectos/patrones |
| **Migración a Markdown** | 85 archivos (tools, patterns, flows, presets, projects) |
| **Backend API REST** | Endpoints para todos los tipos de contenido |
| **ContentManager** | Cache inteligente con reload dinámico |

### Novedades v8.0

| Feature | Descripción |
|---------|-------------|
| **Pipeline Builder** | Canvas visual con conexiones SVG entre nodos |
| **Validación Real-time** | Panel lateral con warnings/errors del stack |
| **Compilar a Python** | Genera código completo desde el diagrama |
| **Scaffold Proyecto** | Crea estructura de carpetas + script ejecutable |
| **App Store de Flujos** | 12 recetas de arquitectura listas para clonar |
| **33 Patrones** | Biblioteca completa de prompt patterns |
| **Glosario Mejorado** | Filtros, búsqueda, progreso visual, 28 herramientas |

### Historial de versiones

| Versión | Highlights |
|---------|------------|
| **v8.1** | Portfolio de 11 proyectos + Comando /vault + Migración Markdown |
| **v8.0** | Pipeline Builder + Scaffold + App Store Flujos |
| **v7.2** | 42 Patrones (Pack 14-15: RAG Avanzado, DevOps CI/CD) |
| **v7.1** | 33 Patrones en 13 packs |
| **v7.0** | Knowledge Base (RAG) + Scout + Glosario Interactivo |
| **v6.0** | Backend FastAPI + Monitor |
| **v5.x** | Arquitecto Visual + Generador de Prompts |

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
- Drag & drop de 28 herramientas al canvas
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

## Herramientas incluidas (28)

| Categoría | Herramientas |
|-----------|--------------|
| **Frontend** | HTML5, Tailwind, HTMX, Alpine.js |
| **Backend** | Python, FastAPI, Pydantic, Loguru, BeautifulSoup, Watchdog, HTTPX, Typer, Rich |
| **IA Model** | CLIP, Whisper, Sentence-BERT, Claude API, Ollama |
| **Storage** | ChromaDB, SQLite, Markdown |
| **Process** | OpenCV/Pillow, FFmpeg, Tesseract OCR, jq |
| **DevOps** | Git, Ruff/Black, Docker, Pytest |

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
| `/api/search` | POST | Búsqueda semántica |
| `/api/index` | POST | Indexar archivos markdown |
| `/api/stats` | GET | Estadísticas de la KB |
| `/api/scout/analyze` | POST | Analizar error con Claude |

## Requisitos

- Python 3.9+
- ~2GB RAM (para embeddings)
- ANTHROPIC_API_KEY (opcional, para Scout)

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

Parte del ecosistema **minerOS** | Creado por Carlos | Nov 2025
