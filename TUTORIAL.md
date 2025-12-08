# Tutorial DirectOS v10.9

> **Tu cockpit de desarrollo con IA integrada y Memoria Evolutiva**

DirectOS es una plataforma visual para diseñar y ejecutar pipelines de automatización con nodos de IA, procesamiento y flujo de control. La v10.9 introduce **MINEROS BRAIN & MEMORY**: sistema centralizado de IA con memoria evolutiva.

---

## Tabla de Contenidos

1. [Introduccion](#1-introduccion)
2. [Instalacion y Arranque](#2-instalacion-y-arranque)
3. [El Dashboard](#3-el-dashboard)
4. [Pipeline Builder](#4-pipeline-builder)
5. [Tipos de Nodos](#5-tipos-de-nodos)
6. [Tu Primer Pipeline](#6-tu-primer-pipeline)
7. [Claude CLI Integration](#7-claude-cli-integration)
8. [Claude Intelligence Suite](#8-claude-intelligence-suite)
9. [MINEROS BRAIN y MEMORY](#9-mineros-brain-y-memory)
10. [Human-in-the-Loop (HITL)](#10-human-in-the-loop-hitl)
11. [Prompt Builder Pro](#11-prompt-builder-pro)
12. [Casos de Uso Reales](#12-casos-de-uso-reales)
13. [Tips y Troubleshooting](#13-tips-y-troubleshooting)

---

## 1. Introduccion

### Que es DirectOS?

DirectOS es un **cockpit de desarrollo** que combina:

- **Pipeline Builder Visual**: Disena flujos de trabajo arrastrando nodos
- **36+ Herramientas**: Desde OCR hasta modelos de IA
- **Claude CLI Integration**: Usa tu suscripcion Pro/Max sin pagar API
- **Claude Intelligence Suite**: 7 funcionalidades de IA integradas
- **Ejecucion Real**: Los pipelines se ejecutan de verdad, no son solo diagramas

### Arquitectura

```
+-----------------------------------------------------+
|                    FRONTEND                          |
|   index.html (Single Page Application)              |
|   - Pipeline Builder (Canvas SVG)                   |
|   - Claude Intelligence Suite                       |
|   - Prompt Builder                                  |
+----------------------+------------------------------+
                       | REST API
+----------------------v------------------------------+
|                    BACKEND                           |
|   FastAPI + Uvicorn (Puerto 8000)                   |
|   - /api/tools, /api/patterns, /api/flows           |
|   - /api/claude/ask (Claude CLI)                    |
|   - /api/agent/execute (Pipeline Executor)          |
+-----------------------------------------------------+
```

---

## 2. Instalacion y Arranque

### Requisitos

- Python 3.9+
- Node.js (opcional, para desarrollo)
- Claude Code CLI (para integracion Claude)

### Pasos

```bash
# 1. Clonar o descargar DirectOS
cd ~/Desktop/DirectOS

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install fastapi uvicorn anthropic chromadb sentence-transformers

# 4. Arrancar (opcion A - script)
./start.sh

# 4. Arrancar (opcion B - manual)
cd backend && uvicorn main:app --reload --port 8000 &
open frontend/index.html
```

### Verificar que funciona

```bash
# El backend responde
curl http://localhost:8000/api/health
# {"status":"healthy","version":"10.8.0"}

# Claude CLI disponible
curl http://localhost:8000/api/claude/status
# {"available":true,"version":"2.0.60 (Claude Code)"}
```

---

## 3. El Dashboard

Al abrir DirectOS veras el dashboard principal con estas secciones en el sidebar:

| Icono | Seccion | Descripcion |
|-------|---------|-------------|
| Home | Dashboard | Vista general y estado del sistema |
| Zap | Automatizaciones | Vista de agentes y triggers activos |
| Wrench | Pipeline Builder | **El canvas principal** - disena pipelines |
| Edit | Prompt Builder | Constructor de slash commands |
| Book | Glosario | 36+ herramientas con fichas tecnicas |
| Palette | Patrones | 42 patrones de prompts |
| Folder | Proyectos | Portfolio de proyectos |

### Panel de Sistema (abajo derecha)

Muestra logs en tiempo real:
- Estado del backend
- Ejecucion de pipelines
- Errores y warnings

---

## 4. Pipeline Builder

El corazon de DirectOS. Un canvas visual estilo n8n donde disenas flujos.

### Controles del Canvas

| Accion | Como |
|--------|------|
| **Zoom** | Ctrl + Scroll |
| **Pan** | Arrastrar el fondo |
| **Anadir nodo** | Arrastra desde el toolbox izquierdo |
| **Mover nodo** | Arrastra el nodo (snap a grid 20px) |
| **Conectar** | Arrastra desde puerto azul (salida) a verde (entrada) |
| **Eliminar conexion** | Click en la linea |
| **Eliminar nodo** | Seleccionar + Delete |
| **Ejecutar** | Boton verde "Ejecutar" en toolbar |

### Barra de Herramientas (v10.8)

```
[Crear con IA] [Auto Layout] [Validar] [IA] [Exportar] [Limpiar]
```

**Nuevos botones v10.8:**
- **Crear con IA**: Genera pipeline desde descripcion en lenguaje natural
- **IA**: Validacion semantica del pipeline con Claude

### Barra Inferior (v10.8)

```
[Nodos: X] [Conexiones: Y] | [Simular] [Ejecutar] [Crear Proyecto] [Generar Codigo] [Documentar]
```

**Nuevo boton v10.8:**
- **Documentar**: Genera documentacion Markdown del pipeline

### Atajos de Teclado

- `Ctrl+Z` - Deshacer
- `Ctrl+Shift+Z` - Rehacer
- `Ctrl+E` - Exportar JSON
- `Ctrl+S` - Guardar arquitectura
- `Delete` - Eliminar nodo seleccionado

### Panel de Configuracion (derecha)

Al seleccionar un nodo aparece un panel con:
- Informacion del nodo
- Parametros configurables
- **Prompt personalizado** (para Claude Transform)
- Codigo de ejemplo
- Opciones HITL

---

## 5. Tipos de Nodos

DirectOS tiene **36 nodos** organizados en categorias:

### Triggers (Inicio del flujo)

| Nodo | Descripcion |
|------|-------------|
| **Trigger Manual** | Boton para ejecutar manualmente |
| **Trigger File** | Watch de carpeta (*.pdf, *.jpg) |
| **Trigger Cron** | Programacion horaria |
| **Trigger Webhook** | Endpoint HTTP POST |

### Proceso

| Nodo | Descripcion |
|------|-------------|
| **Whisper** | Transcripcion de audio |
| **Tesseract** | OCR de imagenes |
| **PDF Parser** | Extraer texto de PDFs |
| **BeautifulSoup** | Web scraping |

### IA Models

| Nodo | Descripcion |
|------|-------------|
| **Claude (CLI)** | Tu suscripcion Pro/Max |
| **Claude Transform** | **NUEVO v10.8** - Prompt personalizable |
| **Ollama** | Modelos locales (llama3, mistral) |
| **OpenAI** | GPT-4, embeddings |

### Storage

| Nodo | Descripcion |
|------|-------------|
| **ChromaDB** | Vector store local |
| **SQLite** | Base de datos SQL |
| **Redis** | Cache en memoria |

### Flow (Control de flujo)

| Nodo | Descripcion |
|------|-------------|
| **Flow If** | Bifurcacion condicional |
| **Flow Loop** | Repetir N veces o iterar lista |
| **Flow Delay** | Pausar X segundos |
| **Inspector** | Pausa HITL con panel didactico |

### Output (Salida)

| Nodo | Descripcion |
|------|-------------|
| **Output File** | Guardar en archivo |
| **Output Notify** | Notificacion macOS |
| **Output Email** | Enviar por email |
| **Output Slack** | Mensaje a Slack |

---

## 6. Tu Primer Pipeline

Vamos a crear un pipeline simple que use Claude para analizar texto.

### Paso 1: Anadir Trigger Manual

1. En el toolbox izquierdo, busca "Trigger Manual"
2. Arrastralo al canvas
3. Se posiciona automaticamente en el grid

### Paso 2: Anadir Nodo Claude

1. Busca "Claude (CLI)" en el toolbox
2. Arrastralo a la derecha del trigger

### Paso 3: Conectar

1. Haz click en el puerto azul (salida) del Trigger
2. Arrastra hasta el puerto verde (entrada) de Claude
3. Se crea una linea bezier conectandolos

### Paso 4: Anadir Output

1. Arrastra "Output Notify" a la derecha de Claude
2. Conecta Claude -> Output Notify

### Paso 5: Ejecutar

1. Click en boton verde "Ejecutar"
2. Veras los nodos iluminarse secuencialmente
3. Claude respondera (usando tu suscripcion)
4. Recibiras una notificacion del navegador

```
[Trigger Manual] --> [Claude (CLI)] --> [Output Notify]
```

---

## 7. Claude CLI Integration

### Que es?

DirectOS puede ejecutar Claude usando tu suscripcion Pro/Max via Claude Code CLI. **Sin coste de API**.

### Requisitos

1. Tener Claude Code instalado (`npm install -g @anthropic-ai/claude-code`)
2. Estar autenticado (`claude login`)
3. Tener suscripcion Pro o Max activa

### Como funciona

Internamente, DirectOS ejecuta:

```bash
claude -p "tu prompt aqui" --output-format json
```

Y parsea la respuesta JSON.

### Endpoint API

```bash
# Hacer pregunta a Claude
curl -X POST http://localhost:8000/api/claude/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explica que es Python", "system_prompt": "Se conciso"}'

# Respuesta
{
  "success": true,
  "content": "Python es un lenguaje de programacion...",
  "model": "claude"
}
```

---

## 8. Claude Intelligence Suite

**NUEVO en v10.8** - Suite completa de funcionalidades potenciadas por Claude.

### 8.1 Pipeline Assistant (Crear con IA)

Crea pipelines completos desde lenguaje natural.

**Como usar:**
1. Click en boton "Crear con IA" en la barra de herramientas
2. Describe lo que necesitas: "Quiero procesar PDFs y guardar resumenes"
3. Claude genera el pipeline (nodos + conexiones)
4. Click "Aplicar" para crearlo en el canvas

**Ejemplos de descripciones:**
- "Procesar PDFs y extraer informacion clave"
- "Transcribir audios y generar resumenes"
- "Monitorear carpeta y procesar archivos nuevos"
- "Crear un RAG para buscar en mis documentos"

### 8.2 Claude Transform

Nodo especial con prompt personalizable.

**Como usar:**
1. Arrastra "Claude Transform" al canvas
2. Click en el nodo para abrir configuracion
3. Escribe tu prompt: "Extrae todos los emails del texto"
4. El contenido del nodo anterior se procesa con tu prompt

**Casos de uso:**
- Extraer emails/telefonos de texto
- Resumir en 3 bullets
- Traducir a otro idioma
- Formatear como JSON
- Clasificar contenido

### 8.3 Debug Inteligente

Cuando un nodo falla, Claude sugiere soluciones.

**Como funciona:**
1. El pipeline falla en un nodo
2. Automaticamente aparece el modal de Debug
3. Muestra: Error + Contexto del pipeline
4. Click "Preguntar a Claude" para obtener sugerencias
5. Claude explica la causa y como solucionarlo

### 8.4 Validacion Semantica

Claude analiza si tu pipeline tiene sentido logico.

**Como usar:**
1. Disena tu pipeline
2. Click en boton "IA" en la barra de herramientas
3. Claude analiza:
   - Flujo logico
   - Nodos faltantes
   - Optimizaciones posibles
   - Compatibilidad entre nodos
4. Resultado aparece en panel de validacion

### 8.5 Auto-documentacion

Genera documentacion Markdown del pipeline.

**Como usar:**
1. Disena tu pipeline
2. Click en boton "Documentar" (barra inferior)
3. Claude genera README con:
   - Titulo y descripcion
   - Flujo de datos (ASCII)
   - Tabla de nodos
   - Configuracion necesaria
   - Casos de uso
4. Copia o guarda la documentacion

### 8.6 Sugerencias Proactivas

Al anadir nodos, Claude sugiere complementos.

**Como funciona:**
1. Anade un nodo (ej: Whisper)
2. Aparece toast: "Whisper genera texto largo. Resumir?"
3. Click "Anadir" para agregar el nodo sugerido
4. O "Ignorar" para descartarlo

**Sugerencias incluidas:**
- Whisper -> Claude Transform (resumir)
- PDF Parser -> Claude Transform (procesar)
- Claude -> SQLite (guardar respuesta)
- ChromaDB -> Claude (usar contexto)

### 8.7 Chat Contextual

Chat flotante que conoce tu pipeline.

**Como usar:**
1. Click en el FAB azul/morado (esquina inferior derecha)
2. Pregunta sobre tu pipeline:
   - "Que hace este pipeline?"
   - "Como puedo optimizarlo?"
   - "Que nodo deberia anadir?"
3. Claude responde con conocimiento del estado actual

**Preguntas rapidas:**
- Botones predefinidos para preguntas comunes

---

## 9. MINEROS BRAIN y MEMORY

La v10.9 introduce un sistema centralizado de IA con memoria evolutiva que mejora con el uso.

### 9.1 MINEROS BRAIN - Claude Intelligence Core

Sistema que unifica todas las interacciones con Claude:

| Componente | Descripcion |
|------------|-------------|
| **MINEROS_SYSTEM_PROMPT** | Prompt maestro con identidad del asistente DirectOS |
| **buildClaudeContext()** | Construye contexto dinamico (pipeline, historial, nodos) |
| **parseClaudeResponse()** | Parser robusto que auto-repara JSON malformado |
| **askClaudeUnified()** | API unica para todas las llamadas Claude |

**Contexto incluido automaticamente:**
- Estado del pipeline actual (nodos + conexiones)
- Ultimos 5 mensajes del chat
- Pipelines guardados
- Resultados de ejecucion
- Memoria evolutiva

### 9.2 MINEROS MEMORY - Memoria Evolutiva

Sistema de aprendizaje continuo basado en localStorage:

```
+-------------------+     +-----------------+     +------------------+
|   Usuario usa     | --> |    MEMORIA      | --> |  Claude conoce   |
|   DirectOS        |     |    guarda       |     |  tus patrones    |
+-------------------+     +-----------------+     +------------------+
         ^                                                  |
         |                                                  |
         +------ Sugerencias cada vez mas relevantes <------+
```

**Que trackea:**

| Metrica | Descripcion |
|---------|-------------|
| **Nodos usados** | Frecuencia de uso de cada tipo de nodo |
| **Flujos favoritos** | Secuencias de nodos que repites (ej: Trigger -> Claude -> SQLite) |
| **Pipelines creados** | Total de pipelines guardados |
| **Pipelines ejecutados** | Total de ejecuciones exitosas |
| **Sugerencias** | Aceptadas vs rechazadas (tasa de aceptacion) |
| **Chat history** | Ultimas 50 conversaciones |

**El efecto flywheel:**

```
     Usas DirectOS
           |
           v
    Memoria aprende
           |
           v
  Claude te conoce mejor
           |
           v
  Sugerencias mas utiles
           |
           v
   Trabajas mas rapido
           |
           v
     Usas mas DirectOS --> (repite)
```

**Como ver la memoria:**

En la consola del navegador:
```javascript
console.log(MinerosMemory.load())
// Muestra toda tu memoria guardada

console.log(MinerosMemory.getSummaryForClaude())
// Muestra lo que Claude ve de ti
```

**Resetear memoria:**
```javascript
MinerosMemory.reset()
// Borra toda la memoria (nuevo comienzo)
```

---

## 10. Human-in-the-Loop (HITL)

DirectOS permite supervisar y controlar la ejecucion de pipelines con multiples mecanismos HITL.

### Nodo Inspector

El nodo **Inspector** pausa el pipeline y muestra un panel didactico:

```
[Trigger] -> [PDF Parser] -> [Inspector] -> [Claude] -> [Output]
                                 ^
                    Pausa aqui y muestra:
                    - Origen: de donde vienen los datos
                    - Proceso: quien los proceso
                    - Datos: que se extrajo (editable)
                    - Destino: a donde van
```

### Dry Run (Simulacion)

Boton **"Simular"** (naranja) que muestra que haria el pipeline sin ejecutar:

| Informacion | Descripcion |
|-------------|-------------|
| Nodos | Total de nodos a ejecutar |
| Tiempo | Estimacion basada en tipo de nodo |
| Pausas HITL | Cuantas veces se detendra |
| Warnings | Advertencias (auth, config, etc.) |

### Pausas por Nodo

Cada nodo puede configurarse para pausar:

1. Click en un nodo del canvas
2. Panel derecho -> seccion "Human-in-the-Loop"
3. Activar:
   - [ ] **Pausar antes de ejecutar**: Ver datos de entrada
   - [ ] **Pausar despues de ejecutar**: Ver/editar resultado

Los nodos con pausas muestran un **indicador cyan pulsante**.

### Logs Inline por Nodo (v10.7)

Ver el output de cada nodo ejecutado:

1. Ejecuta el pipeline
2. Los nodos completados muestran indicador azul
3. Click en el icono de terminal o doble-click en el nodo
4. Modal muestra el output completo
5. Boton "Copiar" para copiar al portapapeles

---

## 11. Prompt Builder Pro

Constructor visual para crear slash commands de Claude Code.

### Acceso

Click en "Prompt Builder" en el sidebar.

### El Patron de 6 Secciones

Los mejores prompts agenticos siguen esta estructura:

```markdown
---
description: Que hace el comando
allowed-tools: Herramientas permitidas
argument-hint: Como usar argumentos
---

# Variables
$VARIABLE: descripcion

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

- `/code-review` - Revision de codigo
- `/doc` - Generar documentacion
- `/test` - Analizar y crear tests
- `/security` - Auditoria de seguridad
- `/refactor` - Sugerir refactorizaciones
- `/vault` - Actualizar knowledge base
- `/scan-projects` - Escanear proyectos
- `/update-context` - Actualizar CLAUDE.md

---

## 12. Casos de Uso Reales

### Pipeline: Crear con IA

```
Usuario: "Quiero procesar PDFs, resumirlos y guardar en base de datos"
     |
     v
[Pipeline Assistant genera:]
[Trigger File] -> [PDF Parser] -> [Claude Transform] -> [SQLite]
```

### Pipeline: Analizar PDFs con IA

```
[Trigger File: *.pdf] --> [PDF Parser] --> [Claude Transform: "Resume"] --> [Output File]
```

**Uso**: Watch de carpeta "Documentos". Cada PDF nuevo se parsea, Claude lo resume, y se guarda.

### Pipeline: Transcribir y Analizar Audio

```
[Trigger File: *.mp3] --> [Whisper] --> [Claude Transform: "Puntos clave"] --> [Output Notify]
```

**Uso**: Subir grabaciones de reuniones, obtener transcripcion y resumen automatico.

### Pipeline: RAG Local

```
[Trigger Manual] --> [PDF Parser] --> [ChromaDB: store] --> [Claude: "Responde con contexto"]
```

**Uso**: Indexar documentos y hacer preguntas sobre ellos.

---

## 13. Tips y Troubleshooting

### El backend no arranca

```bash
# Ver si el puerto esta ocupado
lsof -i :8000

# Matar proceso anterior
kill -9 $(lsof -ti:8000)

# Arrancar de nuevo
cd backend && uvicorn main:app --reload --port 8000
```

### Claude CLI no responde

```bash
# Verificar instalacion
claude --version

# Re-autenticar
claude login

# Probar manualmente
claude -p "Hola" --output-format json
```

### Pipeline Assistant no genera bien

- Se mas especifico en la descripcion
- Menciona tipos de archivo (PDF, audio, etc.)
- Indica el destino (guardar, notificar, etc.)

### El Chat no responde

- Verifica que el backend esta corriendo
- Revisa la consola del navegador para errores
- Asegurate de tener conexion con Claude CLI

---

## Resumen de Versiones

| Version | Caracteristicas principales |
|---------|---------------------------|
| v10.8 | Claude Intelligence Suite (7 funcionalidades IA) |
| v10.7 | Persistencia pipelines, Logs inline |
| v10.5 | Dry Run, Pausas por nodo, HITL completo |
| v10.4 | Inspector (Human-in-the-Loop didactico) |
| v10.3 | Claude CLI Integration |
| v10.2 | Output nodes, Flow nodes, Snap to Grid |
| v10.1 | Pipeline Builder Pro, ejecucion real |
| v10.0 | Trigger nodes |

---

## Enlaces

- **CHANGELOG.md**: Historial completo de cambios
- **README.md**: Informacion general del proyecto
- **MEJORAS.md**: Roadmap y proximas versiones

---

*Tutorial creado para DirectOS v10.8 - Diciembre 2025*
