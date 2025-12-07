# Changelog

Todos los cambios notables en DirectOS están documentados aquí.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

---

## [10.5.0] - 2025-12-07

### Added - Dry Run (Simulación)
- **Botón "Simular"**: Nuevo botón naranja en toolbar del Pipeline Builder
- **Modal de simulación** con:
  - Número de nodos a ejecutar
  - Tiempo estimado total
  - Contador de pausas HITL
  - Lista detallada de pasos con iconos y tiempos
  - Warnings contextuales (Claude necesita auth, etc.)
- **Ejecutar desde simulación**: Botón para pasar directamente a ejecución real

### Added - Configuración HITL por Nodo
- **Checkboxes en panel de configuración**:
  - "Pausar antes de ejecutar"
  - "Pausar después de ejecutar"
- **Indicador visual**: Nodos con HITL muestran borde cyan y punto pulsante
- **Ejecución inteligente**: Cada nodo respeta sus flags de pausa
- **Edición de datos**: Modificar datos durante pausas antes de continuar

### Technical
- Tiempos estimados por tipo de nodo (Claude ~10s, Whisper ~30s, etc.)
- CSS animations para indicador HITL
- toggleNodePause() para gestionar estado
- Integración con Inspector modal existente

---

## [10.4.0] - 2025-12-07

### Added - Inspector (Human-in-the-Loop)
- **Nodo "Inspector"**: Pausa el pipeline y muestra panel didactico
- **Panel visual** con 4 secciones:
  - **Origen**: De donde vienen los datos (nodo anterior, fuente)
  - **Proceso**: Quien lo hizo (herramienta, accion)
  - **Datos**: Que se extrajo (preview editable)
  - **Destino**: A donde van (siguiente nodo, accion)
- **Tips didacticos**: Explicaciones contextuales de cada herramienta
- **Acciones**: Continuar, Parar, Editar datos
- **Edicion en linea**: Modifica datos antes de continuar

### Technical
- Promise-based modal para pausar ejecucion
- Contexto completo del pipeline (previous/next node)
- 20+ tips didacticos por herramienta
- Total nodos: 36 (35 + Inspector)

---

## [10.3.0] - 2025-12-07

### Added - Claude CLI Integration
- **Endpoint `/api/claude/ask`**: Ejecuta Claude usando suscripción Pro/Max
- **Endpoint `/api/claude/status`**: Verifica disponibilidad de Claude CLI
- **Nodo "Claude (CLI)"**: Disponible en Pipeline Builder (categoría IA Model)
- **Sin coste API**: Usa tu suscripción existente, no créditos de API

### Added - Tutorial Interactivo
- **TUTORIAL.md**: Documentación completa en markdown (10 secciones)
- **tutorial.html**: Tutorial interactivo con animaciones y demos
- Cobertura: Arquitectura, Pipeline Builder, Nodos, Claude CLI, Prompt Builder
- Demo interactiva de ejecución de pipeline

### Technical
- Subprocess con timeout de 3 minutos
- Output format JSON para parsing
- Manejo de errores robusto

---

## [10.2.0] - 2025-12-07

### Added - Nodos Output
- **Output File**: Guardar resultado en archivo (JSON, CSV, TXT)
- **Output Notify**: Notificación nativa de macOS
- **Output Email**: Enviar resultado por email
- **Output Slack**: Mensaje a canal de Slack via webhook

### Added - Nodos Control de Flujo
- **Flow If**: Bifurcación condicional del pipeline
- **Flow Loop**: Repetir sección N veces o iterar lista
- **Flow Delay**: Pausar pipeline X segundos (rate limiting)

### Added - UX Improvements
- **Snap to Grid**: Nodos se alinean automáticamente a cuadrícula de 20px
- **Validación de conexiones**:
  - No conectar trigger → trigger
  - No conectar output → output
  - Detección de ciclos
  - Máximo 1 entrada por nodo (excepto flow-if)
- **Botón Ejecutar**: En barra de herramientas del Pipeline Builder

### Changed
- Nueva categoría **Output** (naranja) con 4 nodos
- Nueva categoría **Flow** (púrpura) con 3 nodos
- Total herramientas: 28 → 35

---

## [10.1.0] - 2025-12-07

### Added - Pipeline Builder Pro
- **Canvas con Grid**: Fondo con cuadrícula visual estilo n8n
- **Zoom y Pan**: Ctrl+Scroll para zoom, arrastra fondo para mover
- **Nodos Draggables**: Arrastra nodos libremente por el canvas
- **Conexiones Draggables**: Arrastra desde puerto de salida a entrada
- **Puertos de Conexión**: Verde (entrada) y Azul (salida) con hover effects
- **Eliminar Conexiones**: Click en línea para eliminar
- **Auto Layout**: Botón para reorganizar nodos automáticamente
- **Controles de Zoom**: Botones +/- y reset en barra de herramientas

### Added - Panel de Configuración de Nodo
- **Panel lateral derecho** al seleccionar un nodo
- **Información del nodo**: icono, nombre, descripción, código
- **Parámetros dinámicos** según tipo de nodo (triggers, storage, IA)
- **Contador de conexiones**: entradas y salidas
- **Acciones rápidas**: Duplicar nodo, eliminar nodo
- **Copiar código** al portapapeles

### Added - Ejecución Real de Pipelines
- **Conexión con API backend** `/api/agent/execute`
- **Polling de estado** en tiempo real
- **Estados visuales**: idle, running, success, error
- **Log de ejecución** en el panel de sistema
- **Parámetros del nodo** enviados al backend

### Changed
- Canvas ahora usa posiciones libres en vez de grid fijo
- Conexiones se definen manualmente (no secuenciales)
- Nodos con clase `pipeline-node-pro` con estilos mejorados

---

## [10.0.0] - 2025-12-07

### Added - Trigger Nodes (Automatizaciones v10)
- **Nueva categoría Trigger**: 4 tipos de nodos activadores de pipeline
  - **Trigger Manual**: Botón "Ejecutar Pipeline" con estado visual
  - **Trigger File**: Watch de carpeta con patrones (*.pdf, *.jpg)
  - **Trigger Cron**: Programación horaria (diario, semanal, por hora)
  - **Trigger Webhook**: Endpoint HTTP POST para integraciones
- **Ejecución visual desde canvas**: Click en trigger ejecuta todo el pipeline
- **Indicadores de estado por nodo**: Círculos de color (idle/running/success/error)
- **Animación de progreso**: Los nodos se iluminan secuencialmente al ejecutar
- **Leyenda actualizada**: Nueva categoría "Trigger" en barra del canvas

### Changed
- Nodos trigger no tienen puerto de entrada (son el inicio del flujo)
- Icono de trigger con animación pulse para destacar
- Fondo con gradiente verde para nodos trigger

### Fixed
- Archivos markdown creados para triggers (trigger-manual.md, trigger-file.md, trigger-cron.md, trigger-webhook.md)
- Triggers ahora visibles en toolbox después de refresh de cache del backend

---

## [9.1.0] - 2025-12-07

### Added - Pipeline Builder v9.1
- **Undo/Redo en canvas**: Sistema de historial con hasta 50 estados
  - `Ctrl+Z` / `Cmd+Z` para deshacer
  - `Ctrl+Shift+Z` / `Cmd+Shift+Z` para rehacer
  - Botones visuales en la barra del canvas
- **Exportar pipeline como JSON**: Descarga el pipeline completo en formato JSON portable
  - Incluye nodos, conexiones y metadata
  - Botón en barra + atajo `Ctrl+E` / `Cmd+E`
- **Atajos de teclado globales**:
  - `Ctrl+S` / `Cmd+S` - Guardar arquitectura
  - `Ctrl+E` / `Cmd+E` - Exportar JSON
  - `Delete` / `Backspace` - Eliminar último nodo
- **Detección de duplicados**: Validación que alerta si hay nodos duplicados
- **Validación de compatibilidad**: Nuevas validaciones para LangChain + ChromaDB

### Changed - Renaming Agent Mode → Automatizaciones
- **Sidebar**: Nuevo icono bolt y nombre "Automatizaciones"
- **Vista Agent Mode**: Título actualizado a "Automatizaciones"
- **Toasts**: Mensajes actualizados ("Automatizaciones iniciadas/detenidas")
- **Badge versión**: Actualizado a v9.1 con color amarillo
- **Título página**: "DirectOS v9.1 - Automatizaciones"

### Improved
- Historial de canvas con persistencia entre acciones
- UI de botones undo/redo con estados disabled cuando no aplica
- Separador visual en barra de herramientas del canvas

---

## [9.0.0] - 2025-12-06

### Added - Prompt Builder Pro
- **Constructor visual de prompts agénticos** con patrón de 6 secciones:
  - Metadata (description, allowed-tools, argument-hint)
  - Variables (dinámicas y estáticas)
  - Workflow (S-TIER - pasos secuenciales)
  - Instructions (reglas y guías)
  - Report (formato de salida)
- **8 plantillas precargadas**: code-review, doc, test, security, refactor, vault, scan-projects, update-context
- **Validación en tiempo real** con checklist de calidad
- **Drag & drop** para reordenar pasos del workflow
- **Instalar directo** a `~/.claude/commands/` desde el UI
- **Cargar/editar comandos existentes** con parsing de markdown
- **Parser de secciones** para importar comandos y editarlos
- **Biblioteca de prompts agénticos** en `data/content/patterns/agentic-prompts-library.md`

### Added - API Commands
- `GET /api/commands` - Listar slash commands de ~/.claude/commands/
- `GET /api/commands/{name}` - Obtener comando específico
- `POST /api/commands` - Guardar/actualizar comando
- `DELETE /api/commands/{name}` - Eliminar comando

### Added - Agent Mode Backend
- **Pipeline Executor**: Ejecutar pipelines diseñados como código real
- **Watchdog Service**: Detectar archivos nuevos y procesarlos automáticamente
- **Scheduler Service**: Programar tareas con cron expressions o intervalos
- **Notifier Service**: Notificaciones macOS nativas
- **25+ endpoints REST** para Agent Mode completo

### Changed
- 8 slash commands refactorizados con patrón de 6 secciones
- README actualizado con Agent Mode y Prompt Builder
- Total plantillas: 5 → 8

---

## [8.1.0] - 2025-11-25

### Added - Portfolio de Proyectos
- **Sección Proyectos** en el dashboard con navegación en sidebar
- **11 proyectos documentados** en markdown con formato estructurado:
  - Production (6): farmaIA, DirectOS, PhotoMine, DocMine-Fiscal, Web Scraper IA, Simulaciones MAZ
  - Active (1): Dashboard Seguimiento
  - Prototype (2): Portfolio Dibujo, minerOS v2
  - Archived (2): DocMine, Limpiador PDFs
- **Backend endpoint** `/api/projects` con GET list y GET by ID
- **Modal interactivo** con stack técnico, repositorio y contenido completo
- **Copiar documentación** al portapapeles desde modal
- **Grid responsivo** con tarjetas de proyecto y badges de estado

### Added - Comando /vault Inteligente
- **Auto-detección de contenido**: Identifica si es herramienta, proyecto o patrón
- **Plantillas integradas**: Templates para crear nuevos archivos
- **Lógica condicional**: Crea o actualiza según exista el archivo
- **Refresh automático**: Invalida cache tras actualizar
- **Prompt para commit**: Sugiere commitear cambios
- Documentación completa en FASE6-VAULT.md

### Added - Migración a Markdown
- **28 herramientas** migradas de JavaScript a markdown con frontmatter
- **33 patrones** extraídos y documentados en archivos individuales
- **12 flows** migrados con metadata completa
- **6 presets** documentados
- **ContentManager** con cache para performance
- **API endpoints**: /api/tools, /api/patterns, /api/flows, /api/presets, /api/projects
- **Dual-load pattern**: API + fallback para robustez

### Fixed
- **Información inventada corregida** en 4 proyectos:
  - farmaia.md: Corregido de Python a Node.js + Express
  - dashboard-seguimiento.md: Corregido a HTML + localStorage
  - docmine-fiscal.md: Removido ChromaDB/Ollama inventado
  - directos.md: Versión corregida a v8.0
- **Modal de herramientas**: Fix para mostrar detalles correctamente
- **Pipeline Builder**: Fix herramientas y recetas no visibles

### Changed
- **Total archivos markdown**: 85 (28 tools + 33 patterns + 12 flows + 6 presets + 6 projects)
- **Backend modular**: ContentManager con reload dinámico
- **Frontend arquitectura**: MERGE strategy para combinar API + fallback
- **Getter pattern**: Todos los accesos a datos vía `getTools()`, `getPatterns()`, etc.

---

## [8.0.0] - 2025-11-23

### Added - Pipeline Builder
- **Canvas Visual**: Nodos posicionados en grid con conexiones SVG bezier
- **Panel de Validación**: Análisis en tiempo real del stack (checks, warnings, errors)
- **Score de Arquitectura**: Puntuación 0-100 basada en completitud del pipeline
- **Compilar a Python**: Genera código completo desde el diagrama
- **Scaffold de Proyecto**: Crea estructura de carpetas + script ejecutable
  - Vista previa de estructura
  - Opciones: git init, crear venv
  - Genera requirements.txt automático
  - Descarga script .sh

### Added - App Store de Flujos
- **12 recetas de arquitectura** organizadas en 4 categorías:
  - Knowledge: DocMine Classic, Knowledge Graph, Multi-Agent Research
  - Media: Video Search Engine, Audio Transcriptor, Content Moderator
  - Automation: Smart Scraper Pro, Data Pipeline ETL, Workflow Orchestrator
  - DevOps: CI/CD Local, Log Analyzer, Infra Monitor
- Filtros por categoría, complejidad (🟢🟡🔴), y coste (💻 Local / 💸 API)
- Modal con detalles, caso de uso y prompt táctico
- Clonar a Arquitecto con un click

### Added - Glosario Mejorado
- Filtros por categoría y estado de maestría
- Búsqueda en tiempo real
- Progreso visual con círculo SVG animado
- Cambiar estado desde el modal
- Persistencia en localStorage
- **6 nuevas herramientas**: Docker, Pytest, HTTPX, jq, Typer, Rich

### Added - Patrones
- **Pack 14 - RAG Avanzado** (3 patrones):
  - Hybrid Search Optimizer
  - Reranking Pipeline
  - Chunking Strategist
- **Pack 15 - DevOps CI/CD** (3 patrones):
  - GitHub Actions Generator
  - Dockerfile Optimizer
  - Pre-commit Setup

### Changed
- Total herramientas: 22 → 28
- Total patrones: 33 → 42
- Arquitecto Pro renombrado a Pipeline Builder
- UI actualizada con nuevo branding v8.0

---

## [7.2.0] - 2025-11-23

### Added
- Pack 14: RAG Avanzado (3 patrones)
- Pack 15: DevOps CI/CD (3 patrones)
- Documento PATRONES.md completo

---

## [7.1.0] - 2025-11-22

### Added
- **18 nuevos patrones** organizados en 8 packs adicionales
- Documento PATRONES.md como referencia
- Packs: Debug, Data, UI, Robustez, Automation, Docs Visual
- Patrones Comodín: Meta-patrón, Auditor, Simplificador KISS

### Changed
- Total patrones: 15 → 33

---

## [7.0.0] - 2025-11-22

### Added
- **Knowledge Base (RAG)**: Búsqueda semántica en documentos
  - Indexación automática de archivos .md
  - Embeddings con sentence-transformers
  - ChromaDB como vector store
- **Scout**: Análisis de errores con Claude API
- **Glosario Interactivo**: 22 herramientas con fichas técnicas
  - Estado de maestría por herramienta
  - Snippets de código copiables
  - Integración con Arquitecto

### Changed
- Arquitectura cliente-servidor completa
- Backend FastAPI persistente

---

## [6.0.0] - 2025-11-21

### Added
- **Backend FastAPI** con Uvicorn
- **Monitor de Sistema**: Health check en tiempo real
- Logs del sistema con timestamps
- API REST documentada con Swagger

### Changed
- De single-file a arquitectura modular
- Soporte para modo offline (sin backend)

---

## [5.0.0] - 2025-11-20

### Added
- **Arquitecto Visual**: Drag & drop de herramientas
- **6 Presets de arquitectura**: RAG Chatbot, Video Search, etc.
- Validación de dependencias entre herramientas
- Exportar diagrama a PNG
- Guardar/cargar arquitecturas en localStorage

### Changed
- UI completamente rediseñada con Tailwind CSS

---

## [4.0.0] - 2025-11-19

### Added
- **Generador de Prompts** con biblioteca de patrones
- 15 patrones iniciales organizados en 5 packs
- Modo Biblioteca + Modo Libre

---

## [3.0.0] - 2025-11-18

### Added
- Interfaz con pestañas (Arquitecto, Generador, Monitor)
- Sistema de navegación entre vistas

---

## [2.0.0] - 2025-11-17

### Added
- Canvas básico para arquitectura
- Lista de herramientas arrastrables

---

## [1.0.0] - 2025-11-16

### Added
- Versión inicial single-file
- HTML + CSS + JS básico
- Concepto de cockpit de desarrollo

---

## Leyenda

- **Added**: Nuevas funcionalidades
- **Changed**: Cambios en funcionalidades existentes
- **Deprecated**: Funcionalidades que serán eliminadas
- **Removed**: Funcionalidades eliminadas
- **Fixed**: Corrección de bugs
- **Security**: Mejoras de seguridad
