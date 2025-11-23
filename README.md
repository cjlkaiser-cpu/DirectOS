# DirectOS v7.1 - Patterns Expansion

> Centro de operaciones para diseñar arquitecturas, aprender herramientas y dominar tu stack

## Qué es

DirectOS es tu **cockpit de desarrollo** para el ecosistema minerOS. Diseña pipelines visualmente, aprende nuevas herramientas con contexto, y analiza errores automáticamente. De "herramienta de un archivo" a aplicación completa con backend.

## Novedades v7.1

| Feature | Descripción |
|---------|-------------|
| **33 Patrones de Prompts** | +18 nuevos patrones en 8 packs adicionales |
| **Documento PATRONES.md** | Referencia completa con todos los prompts |
| **Nuevos Packs** | Debug, Data, UI, Robustez, Automation, Docs Visual |
| **Patrones Comodín** | Meta-patrón, Auditor, Simplificador KISS |

### Lo que ya teníamos (v7.0)
| Feature | Descripción |
|---------|-------------|
| **Glosario Interactivo** | Click en herramientas → Ficha técnica completa |
| **Estado de Maestría** | ✅ Dominada · 🚧 En progreso · 🆕 Por descubrir |
| **22 Herramientas** | Ollama, Pydantic, Alpine.js, Git, Ruff... |
| **Knowledge Base (RAG)** | Búsqueda semántica en tus docs |
| **Scout** | Análisis de errores con Claude API |

### Versiones anteriores
- **v7.0**: Knowledge Base (RAG) + Scout + Glosario Interactivo
- **v6.0**: Backend FastAPI + Monitor
- **v5.x**: Arquitecto Visual + Generador de Prompts

## El problema que resuelve

```
ANTES                              DESPUÉS
──────                             ───────
Planificas en tu cabeza       →    Planificas visualmente
Escribes prompt desde 0       →    15 patrones listos para copiar
No sabes qué herramienta usar →    Glosario con contexto minerOS
Copias errores a Claude       →    Scout analiza automáticamente
No trackeas tu progreso       →    Estado de maestría por herramienta
```

## Posición en el Workflow minerOS

```
1. ENTENDER    → Claude navegador
2. PLANIFICAR  → Claude navegador
3. DISEÑAR     → DirectOS ← AQUÍ (Arquitecto + Patrones)
4. CONSTRUIR   → Claude Code
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

### Arquitecto Pro
- Drag & drop de 22 herramientas al canvas
- **6 Presets de arquitectura**: RAG Chatbot, Video Search, Smart Scraper...
- Validación de dependencias (ej: "Whisper necesita FFmpeg")
- Compilar a prompt estructurado
- Guardar/cargar arquitecturas
- Exportar diagrama a PNG

### Glosario Interactivo (v7.0)
- **22 herramientas** organizadas en 6 categorías
- **Estado de maestría**: Dominada / En progreso / Por descubrir
- **Ficha técnica** al hacer click:
  - Qué es (descripción)
  - Por qué me importa (contexto minerOS)
  - Casos de uso reales
  - Snippet de código copiable
- **Botón "Añadir al Arquitecto"** desde la ficha

### Biblioteca de Patrones (v7.1)
- **33 patrones de prompts** organizados en 13 packs:
  - 🔧 Refactoring (3) - Código limpio
  - 📝 Contenido (1) - Multi-formato
  - 🛡️ Seguridad (1) - Privacidad
  - 🧠 Knowledge (1) - RAG y síntesis
  - 📖 Aprendizaje (3) - Estudiar y traducir
  - 🔧 DevOps (3) - Calidad código
  - 🔍 Debug & Performance (2) - Errores y velocidad
  - 🗂️ Data & API (2) - Esquemas y endpoints
  - 🎯 Meta & Automation (2) - Prompts y watchdog
  - 🎨 Creatividad & UI (3) - Frontend bonito
  - 🛠️ Ingeniería & Robustez (3) - Sistema sólido
  - 🧹 Data Engineering (3) - Limpieza datos
  - 📐 Documentación Visual (3) - Diagramas y docs
  - 🃏 Comodín (3) - Meta-patrón, Auditor, KISS
- Cada patrón incluye: Problema, Prompt, Flujo Táctico
- Cargar en Generador o en Arquitecto con un click
- **Ver `PATRONES.md` para referencia completa**

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

### Monitor Sistema
- Health check del backend en tiempo real
- Logs del sistema con timestamps
- Estado de módulos (Knowledge ✓ / Scout ✓)

### Generador de Prompts
- **Modo Biblioteca**: Selecciona patrón predefinido
- **Modo Libre**: Rol + Objetivo + Stack personalizado
- Generar prompt formateado

## Herramientas incluidas (22)

| Categoría | Herramientas |
|-----------|--------------|
| **Frontend** | HTML5, Tailwind, HTMX, Alpine.js |
| **Backend** | Python, FastAPI, Pydantic, Loguru, BeautifulSoup, Watchdog |
| **IA Model** | CLIP, Whisper, Sentence-BERT, Claude API, Ollama |
| **Storage** | ChromaDB, SQLite, Markdown |
| **Process** | OpenCV/Pillow, FFmpeg, Tesseract OCR |
| **DevOps** | Git, Ruff/Black |

## Arquitectura

```
DirectOS/
├── frontend/
│   └── index.html          ← UI (Tailwind + JS vanilla)
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
- JavaScript vanilla (sin frameworks)
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
- **Aprender haciendo**: El Glosario es tu panel de progreso

---

## Roadmap v8.0+

Ver `MEJORAS.md` para el plan de evolución.

---

Parte del ecosistema **minerOS** | Creado por Carlos | Nov 2025
