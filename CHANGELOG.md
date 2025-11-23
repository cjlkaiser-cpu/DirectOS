# Changelog

Todos los cambios notables en DirectOS están documentados aquí.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/).

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
