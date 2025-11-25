---
id: directos
name: DirectOS
version: v8.0
status: production
stack:
  - fastapi
  - python
  - htmx
  - markdown
  - sqlite
repo: ~/Desktop/DirectOS
description: Sistema operativo personal de conocimiento. Dashboard interactivo para navegación de herramientas, patrones, flows y proyectos minerOS.
---

# DirectOS v8.0

Sistema operativo personal de conocimiento. Dashboard interactivo para navegar herramientas, patrones, flows y proyectos del ecosistema minerOS.

## Flujo de trabajo

1. **Gestión de conocimiento**
   - Markdown como fuente de verdad
   - ContentManager con cache para performance
   - API REST para acceso programático
   - Sincronización bidireccional con Obsidian

2. **Interfaz interactiva**
   - Pipeline Builder: arrastra herramientas para diseñar arquitecturas
   - Architect Pro: visualización de flujos técnicos
   - Biblioteca de Patterns: 33 patrones de prompts listos
   - Flow Store: arquitecturas completas documentadas

3. **Sistema de documentación**
   - Tools: 28 herramientas técnicas documentadas
   - Patterns: 33 prompt patterns para casos comunes
   - Flows: 12 arquitecturas end-to-end
   - Presets: 6 configuraciones predefinidas
   - Projects: Documentación de proyectos reales

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

# Iniciar sistema completo
./start.sh

# Solo backend
cd backend && uvicorn main:app --reload

# Solo frontend
open frontend/index.html

# Refrescar cache después de editar markdown
curl -X POST http://localhost:8000/api/content/refresh

# Validar contenido
curl http://localhost:8000/api/tools | jq '.count'
curl http://localhost:8000/api/patterns | jq '.count'
```

## Arquitectura

```
DirectOS/
├── backend/
│   ├── main.py              # FastAPI app
│   └── modules/
│       └── content.py       # ContentManager (markdown → API)
├── frontend/
│   └── index.html           # Single-page dashboard
├── data/
│   └── content/
│       ├── tools/           # 28 herramientas
│       ├── patterns/        # 33 prompt patterns
│       ├── flows/           # 12 arquitecturas
│       ├── presets/         # 6 configuraciones
│       └── projects/        # Documentación proyectos
└── .claude/
    └── commands/
        └── vault.md         # Comando /vault inteligente
```

### Stack técnico

- **Backend:** FastAPI + Python 3.11
- **Frontend:** HTML5 + TailwindCSS + Alpine.js + HTMX
- **Content:** Markdown con YAML frontmatter
- **Parser:** python-frontmatter
- **Cache:** In-memory dict con timestamps
- **Deploy:** Local-first (no requiere internet)

## Aprendizajes clave

### Lo que funcionó bien

1. **Markdown como DB:** Editable en cualquier editor, git-friendly
2. **Dual-load pattern:** API + fallback para robustez
3. **ContentManager cache:** Cargar 79 archivos en 50ms
4. **HTMX + Alpine:** UI reactiva sin framework pesado
5. **Piano-piano migration:** 21 commits incrementales, sin romper nada

### Problemas resueltos

- **Modal roto tras migración:** Implementar MERGE strategy (API + fallback)
- **Referencias directas a arrays:** Usar getter pattern `getTools()`
- **Cache stale:** Endpoint `/api/content/refresh` para invalidar
- **Frontend no actualizado:** Documentar hard refresh (⌘+Shift+R)

### Decisiones de arquitectura

**¿Por qué markdown?**
- Git-friendly (track changes)
- Editable sin código
- Portable entre sistemas
- Searchable con grep/ripgrep

**¿Por qué FastAPI?**
- Type hints con Pydantic
- Auto-documentación en /docs
- Async nativo
- Ecosistema Python

**¿Por qué HTMX?**
- HTML-first (menos JavaScript)
- Progressive enhancement
- Servidor renderiza todo
- Compatible con Alpine para interactividad

### Siguientes pasos

- [x] FASE 5: Documentar proyectos en projects/
- [x] FASE 6: Comando /vault inteligente
- [ ] Sistema de búsqueda global (FTS5)
- [ ] Exportación a PDF/Notion/Obsidian
- [ ] Dashboard de métricas (proyectos, herramientas usadas)
- [ ] CLI para crear contenido: `directos new tool python`

## Métricas actuales

- **Herramientas:** 28 documentadas
- **Patterns:** 33 prompt patterns
- **Flows:** 12 arquitecturas
- **Presets:** 6 configuraciones
- **Projects:** 6 proyectos documentados
- **Total archivos:** 85 markdown (336KB)
- **Líneas código:** ~3,500 líneas Python + HTML

## Uso diario

### Buscar patrón para una tarea
```bash
# Desde CLI
grep -r "sobre-engineered" data/content/patterns/

# Desde dashboard
→ Ir a "Biblioteca de Patterns"
→ Buscar "KISS"
→ Copiar prompt
```

### Diseñar nueva arquitectura
```bash
# Desde Pipeline Builder
→ Arrastrar: FastAPI → Claude → ChromaDB
→ Generar prompt contextual
→ Exportar como flow markdown
```

### Documentar proyecto nuevo
```bash
# Crear archivo
touch data/content/projects/nuevo-proyecto.md

# Editar con plantilla
# (Ver cualquier archivo en projects/ como ejemplo)

# Refrescar cache
curl -X POST http://localhost:8000/api/content/refresh
```

## Integración con flujo de trabajo

DirectOS se integra con:
- **Claude Desktop:** Comando `/vault` para actualizar knowledge base
- **Obsidian:** Carpeta `data/content/` sincronizada
- **Git:** Branch `main` es fuente de verdad
- **CI/CD:** GitHub Actions para validar markdown

## Enlaces útiles

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [HTMX](https://htmx.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [python-frontmatter](https://python-frontmatter.readthedocs.io/)
