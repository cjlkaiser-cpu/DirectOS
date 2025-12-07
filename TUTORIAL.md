# Tutorial DirectOS v10.5

> **Tu cockpit de desarrollo con IA integrada**

DirectOS es una plataforma visual para diseñar y ejecutar pipelines de automatización con nodos de IA, procesamiento y flujo de control.

---

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Instalación y Arranque](#2-instalación-y-arranque)
3. [El Dashboard](#3-el-dashboard)
4. [Pipeline Builder](#4-pipeline-builder)
5. [Tipos de Nodos](#5-tipos-de-nodos)
6. [Tu Primer Pipeline](#6-tu-primer-pipeline)
7. [Claude CLI Integration](#7-claude-cli-integration)
8. [Human-in-the-Loop (HITL)](#8-human-in-the-loop-hitl)
9. [Prompt Builder Pro](#9-prompt-builder-pro)
10. [Casos de Uso Reales](#10-casos-de-uso-reales)
11. [Tips y Troubleshooting](#11-tips-y-troubleshooting)

---

## 1. Introducción

### ¿Qué es DirectOS?

DirectOS es un **cockpit de desarrollo** que combina:

- **Pipeline Builder Visual**: Diseña flujos de trabajo arrastrando nodos
- **35+ Herramientas**: Desde OCR hasta modelos de IA
- **Claude CLI Integration**: Usa tu suscripción Pro/Max sin pagar API
- **Ejecución Real**: Los pipelines se ejecutan de verdad, no son solo diagramas

### Arquitectura

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND                          │
│   index.html (Single Page Application)              │
│   - Pipeline Builder (Canvas SVG)                   │
│   - Prompt Builder                                  │
│   - Dashboard y Glosario                            │
└──────────────────────┬──────────────────────────────┘
                       │ REST API
┌──────────────────────▼──────────────────────────────┐
│                    BACKEND                           │
│   FastAPI + Uvicorn (Puerto 8000)                   │
│   - /api/tools, /api/patterns, /api/flows           │
│   - /api/claude/ask (Claude CLI)                    │
│   - /api/agent/execute (Pipeline Executor)          │
└─────────────────────────────────────────────────────┘
```

---

## 2. Instalación y Arranque

### Requisitos

- Python 3.9+
- Node.js (opcional, para desarrollo)
- Claude Code CLI (para integración Claude)

### Pasos

```bash
# 1. Clonar o descargar DirectOS
cd ~/Desktop/DirectOS

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install fastapi uvicorn anthropic chromadb sentence-transformers

# 4. Arrancar (opción A - script)
./start.sh

# 4. Arrancar (opción B - manual)
cd backend && uvicorn main:app --reload --port 8000 &
open frontend/index.html
```

### Verificar que funciona

```bash
# El backend responde
curl http://localhost:8000/api/health
# {"status":"healthy","version":"10.3.0"}

# Claude CLI disponible
curl http://localhost:8000/api/claude/status
# {"available":true,"version":"2.0.60 (Claude Code)"}
```

---

## 3. El Dashboard

Al abrir DirectOS verás el dashboard principal con estas secciones en el sidebar:

| Icono | Sección | Descripción |
|-------|---------|-------------|
| 🏠 | Dashboard | Vista general y estado del sistema |
| ⚡ | Automatizaciones | Vista de agentes y triggers activos |
| 🔧 | Pipeline Builder | **El canvas principal** - diseña pipelines |
| 📝 | Prompt Builder | Constructor de slash commands |
| 📚 | Glosario | 35+ herramientas con fichas técnicas |
| 🎨 | Patrones | 42 patrones de prompts |
| 📁 | Proyectos | Portfolio de proyectos |

### Panel de Sistema (abajo derecha)

Muestra logs en tiempo real:
- Estado del backend
- Ejecución de pipelines
- Errores y warnings

---

## 4. Pipeline Builder

El corazón de DirectOS. Un canvas visual estilo n8n donde diseñas flujos.

### Controles del Canvas

| Acción | Cómo |
|--------|------|
| **Zoom** | Ctrl + Scroll |
| **Pan** | Arrastrar el fondo |
| **Añadir nodo** | Arrastra desde el toolbox izquierdo |
| **Mover nodo** | Arrastra el nodo (snap a grid 20px) |
| **Conectar** | Arrastra desde puerto azul (salida) a verde (entrada) |
| **Eliminar conexión** | Click en la línea |
| **Eliminar nodo** | Seleccionar + Delete |
| **Ejecutar** | Botón verde "Ejecutar" en toolbar |

### Barra de Herramientas

```
[Undo] [Redo] | [Zoom -] [Reset] [Zoom +] | [Auto Layout] [Exportar JSON] | [Ejecutar]
```

### Atajos de Teclado

- `Ctrl+Z` - Deshacer
- `Ctrl+Shift+Z` - Rehacer
- `Ctrl+E` - Exportar JSON
- `Ctrl+S` - Guardar arquitectura
- `Delete` - Eliminar nodo seleccionado

### Panel de Configuración (derecha)

Al seleccionar un nodo aparece un panel con:
- Información del nodo
- Parámetros configurables
- Código de ejemplo
- Botones: Duplicar, Eliminar

---

## 5. Tipos de Nodos

DirectOS tiene **35 nodos** organizados en categorías:

### 🟢 Triggers (Inicio del flujo)

| Nodo | Descripción |
|------|-------------|
| **Trigger Manual** | Botón para ejecutar manualmente |
| **Trigger File** | Watch de carpeta (*.pdf, *.jpg) |
| **Trigger Cron** | Programación horaria |
| **Trigger Webhook** | Endpoint HTTP POST |

### 🔵 Proceso

| Nodo | Descripción |
|------|-------------|
| **Whisper** | Transcripción de audio |
| **Tesseract** | OCR de imágenes |
| **PDF Parser** | Extraer texto de PDFs |
| **BeautifulSoup** | Web scraping |

### 🟡 IA Models

| Nodo | Descripción |
|------|-------------|
| **Claude (CLI)** | Tu suscripción Pro/Max |
| **Ollama** | Modelos locales (llama3, mistral) |
| **OpenAI** | GPT-4, embeddings |

### 🟣 Storage

| Nodo | Descripción |
|------|-------------|
| **ChromaDB** | Vector store local |
| **SQLite** | Base de datos SQL |
| **Redis** | Cache en memoria |

### 🟣 Flow (Control de flujo)

| Nodo | Descripción |
|------|-------------|
| **Flow If** | Bifurcación condicional |
| **Flow Loop** | Repetir N veces o iterar lista |
| **Flow Delay** | Pausar X segundos |

### 🟠 Output (Salida)

| Nodo | Descripción |
|------|-------------|
| **Output File** | Guardar en archivo |
| **Output Notify** | Notificación macOS |
| **Output Email** | Enviar por email |
| **Output Slack** | Mensaje a Slack |

---

## 6. Tu Primer Pipeline

Vamos a crear un pipeline simple que use Claude para analizar texto.

### Paso 1: Añadir Trigger Manual

1. En el toolbox izquierdo, busca "Trigger Manual"
2. Arrástralo al canvas
3. Se posiciona automáticamente en el grid

### Paso 2: Añadir Nodo Claude

1. Busca "Claude (CLI)" en el toolbox
2. Arrástralo a la derecha del trigger

### Paso 3: Conectar

1. Haz click en el puerto azul (salida) del Trigger
2. Arrastra hasta el puerto verde (entrada) de Claude
3. Se crea una línea bezier conectándolos

### Paso 4: Añadir Output

1. Arrastra "Output Notify" a la derecha de Claude
2. Conecta Claude → Output Notify

### Paso 5: Ejecutar

1. Click en botón verde "Ejecutar"
2. Verás los nodos iluminarse secuencialmente
3. Claude responderá (usando tu suscripción)
4. Recibirás una notificación del navegador

```
[Trigger Manual] ──► [Claude (CLI)] ──► [Output Notify]
```

---

## 7. Claude CLI Integration

### ¿Qué es?

DirectOS puede ejecutar Claude usando tu suscripción Pro/Max via Claude Code CLI. **Sin coste de API**.

### Requisitos

1. Tener Claude Code instalado (`npm install -g @anthropic-ai/claude-code`)
2. Estar autenticado (`claude login`)
3. Tener suscripción Pro o Max activa

### Cómo funciona

Internamente, DirectOS ejecuta:

```bash
claude -p "tu prompt aquí" --output-format json
```

Y parsea la respuesta JSON.

### Endpoint API

```bash
# Hacer pregunta a Claude
curl -X POST http://localhost:8000/api/claude/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explica qué es Python", "system_prompt": "Sé conciso"}'

# Respuesta
{
  "success": true,
  "content": "Python es un lenguaje de programación...",
  "model": "claude"
}
```

### En el Pipeline

Cuando añades el nodo "Claude (CLI)" al pipeline:
1. Recibe como input la salida del nodo anterior
2. Envía ese texto como prompt a Claude
3. Devuelve la respuesta al siguiente nodo

---

## 8. Human-in-the-Loop (HITL)

DirectOS permite supervisar y controlar la ejecución de pipelines con múltiples mecanismos HITL.

### Nodo Inspector

El nodo **Inspector** pausa el pipeline y muestra un panel didáctico:

```
[Trigger] → [PDF Parser] → [🔍 Inspector] → [Claude] → [Output]
                                ↑
                    Pausa aquí y muestra:
                    - Origen: de dónde vienen los datos
                    - Proceso: quién los procesó
                    - Datos: qué se extrajo (editable)
                    - Destino: a dónde van
```

### Dry Run (Simulación)

Botón **"Simular"** (naranja) que muestra qué haría el pipeline sin ejecutar:

| Información | Descripción |
|-------------|-------------|
| Nodos | Total de nodos a ejecutar |
| Tiempo | Estimación basada en tipo de nodo |
| Pausas HITL | Cuántas veces se detendrá |
| Warnings | Advertencias (auth, config, etc.) |

### Pausas por Nodo

Cada nodo puede configurarse para pausar:

1. Click en un nodo del canvas
2. Panel derecho → sección "Human-in-the-Loop"
3. Activar:
   - ☐ **Pausar antes de ejecutar**: Ver datos de entrada
   - ☐ **Pausar después de ejecutar**: Ver/editar resultado

Los nodos con pausas muestran un **indicador cyan pulsante**.

### Flujo de trabajo recomendado

1. **Diseñar** el pipeline en el canvas
2. **Simular** para ver qué pasará
3. **Configurar pausas** en nodos críticos
4. **Ejecutar** y revisar en cada pausa
5. **Editar datos** si es necesario antes de continuar

---

## 9. Prompt Builder Pro

Constructor visual para crear slash commands de Claude Code.

### Acceso

Click en "Prompt Builder" en el sidebar.

### El Patrón de 6 Secciones

Los mejores prompts agénticos siguen esta estructura:

```markdown
---
description: Qué hace el comando
allowed-tools: Herramientas permitidas
argument-hint: Cómo usar argumentos
---

# Variables
$VARIABLE: descripción

# Workflow (S-TIER)
1. Primer paso
2. Segundo paso
3. ...

# Instructions
- Regla 1
- Regla 2

# Report
Formato de salida esperado
```

### Plantillas Incluidas

- `/code-review` - Revisión de código
- `/doc` - Generar documentación
- `/test` - Analizar y crear tests
- `/security` - Auditoría de seguridad
- `/refactor` - Sugerir refactorizaciones
- `/vault` - Actualizar knowledge base
- `/scan-projects` - Escanear proyectos
- `/update-context` - Actualizar CLAUDE.md

### Crear Nuevo Comando

1. Selecciona una plantilla o empieza en blanco
2. Rellena cada sección
3. Click "Instalar" para guardar en `~/.claude/commands/`
4. Usa con `/nombre-comando` en Claude Code

---

## 10. Casos de Uso Reales

### Pipeline: Analizar PDFs con IA

```
[Trigger File: *.pdf] ──► [PDF Parser] ──► [Claude: "Resume este documento"] ──► [Output File: resumen.txt]
```

**Uso**: Watch de carpeta "Documentos". Cada PDF nuevo se parsea, Claude lo resume, y se guarda el resumen.

### Pipeline: Transcribir y Analizar Audio

```
[Trigger File: *.mp3] ──► [Whisper] ──► [Claude: "Extrae los puntos clave"] ──► [Output Notify]
```

**Uso**: Subir grabaciones de reuniones, obtener transcripción y resumen automático.

### Pipeline: Web Scraping Inteligente

```
[Trigger Cron: 9am] ──► [BeautifulSoup: url] ──► [Claude: "¿Hay noticias importantes?"] ──► [Output Slack]
```

**Uso**: Cada mañana scrapea una web de noticias y envía resumen a Slack.

### Pipeline: Rate-Limited API Calls

```
[Trigger Manual] ──► [Flow Loop: 10x] ──► [API Call] ──► [Flow Delay: 1s] ──► [Output File]
```

**Uso**: Hacer 10 llamadas a una API con 1 segundo entre cada una para respetar rate limits.

---

## 11. Tips y Troubleshooting

### El backend no arranca

```bash
# Ver si el puerto está ocupado
lsof -i :8000

# Matar proceso anterior
kill -9 $(lsof -ti:8000)

# Arrancar de nuevo
cd backend && uvicorn main:app --reload --port 8000
```

### Claude CLI no responde

```bash
# Verificar instalación
claude --version

# Re-autenticar
claude login

# Probar manualmente
claude -p "Hola" --output-format json
```

### Los nodos no aparecen en el toolbox

1. Verifica que los archivos `.md` existen en `data/content/tools/`
2. Reinicia el backend para recargar el cache
3. Recarga la página (Ctrl+Shift+R)

### Las conexiones no se crean

Validaciones que pueden bloquear:
- No puedes conectar Trigger → Trigger
- No puedes conectar Output → Output
- No puedes crear ciclos
- Máximo 1 entrada por nodo (excepto Flow If)

### El pipeline no ejecuta

1. Verifica que hay al menos un Trigger
2. Verifica que todos los nodos están conectados
3. Revisa el panel de logs para errores

---

## Resumen de Versiones

| Versión | Características principales |
|---------|---------------------------|
| v10.5 | Dry Run, Pausas por nodo, HITL completo |
| v10.4 | Inspector (Human-in-the-Loop didáctico) |
| v10.3 | Claude CLI Integration |
| v10.2 | Output nodes, Flow nodes, Snap to Grid |
| v10.1 | Pipeline Builder Pro, ejecución real |
| v10.0 | Trigger nodes |
| v9.0 | Prompt Builder Pro |
| v8.0 | Pipeline Builder, App Store de Flujos |

---

## Enlaces

- **CHANGELOG.md**: Historial completo de cambios
- **README.md**: Información general del proyecto
- **data/content/**: Archivos markdown de tools, patterns, flows

---

*Tutorial creado para DirectOS v10.5 - Diciembre 2024*
