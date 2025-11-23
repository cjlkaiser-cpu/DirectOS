# DirectOS v6.0

> Arquitecto visual de pipelines + Knowledge Base + Scout para el ecosistema minerOS

## Qué es

DirectOS es tu centro de operaciones para diseñar arquitecturas visualmente, buscar en tu knowledge base con IA, y analizar errores automáticamente. Evolución de una herramienta de un archivo a una aplicación con backend.

## Novedades v6.0

| Feature | Descripción |
|---------|-------------|
| **Knowledge Base (RAG)** | Búsqueda semántica en tus notas markdown |
| **Scout** | Analiza errores y sugiere soluciones con Claude |
| **Backend FastAPI** | API para embeddings y análisis |
| **Health Monitor** | Estado del sistema en tiempo real |

## El problema que resuelve

```
ANTES                          DESPUÉS
──────                         ───────
Planificas en tu cabeza   →    Planificas visualmente
Escribes prompt desde 0   →    Generas desde diagrama
Buscas en archivos        →    Búsqueda semántica con IA
Copias errores a Claude   →    Scout analiza automáticamente
```

## Posición en el Workflow minerOS

```
1. ENTENDER    → Claude navegador
2. PLANIFICAR  → Claude navegador
3. DISEÑAR     → DirectOS ← AQUÍ
4. CONSTRUIR   → Claude Code
5. PROBAR      → Terminal
6. EVALUAR     → ¿Aporta valor?
7. DOCUMENTAR  → Knowledge base
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

### Arquitecto Pro
- Drag & drop de herramientas al canvas
- Validación de dependencias (ej: "Whisper necesita FFmpeg")
- Compilar a prompt estructurado
- Guardar/cargar arquitecturas
- Exportar diagrama a PNG

### Knowledge Base (RAG) 🆕
- Indexa automáticamente tus archivos `.md` del Desktop
- Búsqueda semántica: "¿cómo funciona RAG?"
- Usa embeddings (sentence-transformers) + ChromaDB
- Tu propio "Perplexity" local

### Scout 🆕
- Pega un error en el Monitor
- Scout lo analiza con Claude API
- Sugiere la solución directamente
- Contexto de tu stack (minerOS)

### Monitor Sistema
- Health check del backend en tiempo real
- Logs del sistema
- Estado de módulos (Knowledge ✓ / Scout ✓)

### Flujos Tácticos
- Diagrama interactivo del pipeline
- Click en nodos para ver detalles y código
- Saltar al Generador con contexto

### Generador de Prompts
- Seleccionar rol y objetivo
- Seleccionar stack
- Generar prompt formateado

### Glosario
- Catálogo de herramientas con tips
- Integrado con Knowledge Base

## Arquitectura

```
DirectOS/
├── frontend/
│   └── index.html          ← UI (Tailwind + JS)
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
├── start.sh                ← Script de arranque
├── .env.example            ← Variables de entorno
└── README.md
```

## Stack técnico

### Frontend
- HTML5 + Tailwind CSS (CDN)
- JavaScript vanilla
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

- Python 3.11+
- ~2GB RAM (para embeddings)
- ANTHROPIC_API_KEY (opcional, para Scout)

## Filosofía

- **minerOS style**: Herramienta que aporta valor real
- **Local-first**: Tu data en tu máquina
- **Incremental**: Funciona sin backend (modo básico)
- **KISS**: Simple, debuggeable, modular

---

Parte del ecosistema **minerOS** | Creado por Carlos | Nov 2025
