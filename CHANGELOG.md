# Changelog

Todos los cambios notables en DirectOS están documentados aquí.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

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
