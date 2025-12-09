# DirectOS - Roadmap

> Mejoras pendientes y próximas versiones

## Estado actual: v10.10

Ver [CHANGELOG.md](./CHANGELOG.md) para el historial completo de cambios.

---

## Completado

### v10.10 - Canvas Pro & Sistema Educativo ✅
- [x] **Insertar nodo en conexión**: Arrastra sobre línea → se inserta automáticamente
- [x] **Conectar en puertos**: Suelta cerca de puerto → se conecta
- [x] **Minimap funcional**: Vista miniatura con colores por categoría
- [x] **Animación de flujo**: Pulso animado en conexiones durante ejecución
- [x] **Estados visuales**: executing (amarillo), success (✓), error (✗)
- [x] **Atajos de teclado**: Ctrl+C/V, Ctrl+L, Supr, Escape, +/-/0
- [x] **Tooltips en conexiones**: Hover → explica datos y por qué
- [x] **Panel de nodo mejorado**: Qué hace, Input/Output, Cuándo usarlo
- [x] **Learning Path export**: Genera guía con prompts para Claude Code
- [x] **7 nuevos nodos**: Telegram (in/out), REST API, Text Splitter, Notion, Airtable, Spreadsheet
- [x] **Refactor**: `_parse_command_frontmatter()` extraído en backend

### v10.9 - MINEROS BRAIN & MEMORY ✅
- [x] **MINEROS_SYSTEM_PROMPT**: Prompt maestro con identidad DirectOS
- [x] **buildClaudeContext()**: Constructor de contexto dinámico
- [x] **parseClaudeResponse()**: Parser JSON robusto con auto-reparación
- [x] **askClaudeUnified()**: API unificada para todas las llamadas Claude
- [x] **MinerosMemory**: Objeto de persistencia evolutiva
- [x] **trackNodeUsed()**: Registra nodos usados
- [x] **trackPipelineCreated()**: Detecta flujos favoritos
- [x] **trackSuggestion()**: Trackea aceptación de sugerencias
- [x] **getSummaryForClaude()**: Genera contexto de memoria para LLM
- [x] Refactorización de 5 funciones Claude a sistema unificado

### v10.8 - Claude Intelligence Suite ✅
- [x] Nodo Claude Transform (prompt personalizable)
- [x] Debug Inteligente (Claude sugiere soluciones en errores)
- [x] Validación Semántica (análisis del pipeline con IA)
- [x] Auto-documentación (genera README Markdown)
- [x] Sugerencias Proactivas (toast al añadir nodos)
- [x] Chat Contextual (FAB flotante con historial)
- [x] Pipeline Assistant (crear pipeline con lenguaje natural)

### v10.7 - Persistencia & Logs Inline ✅
- [x] Panel "Mis Pipelines" en sidebar
- [x] Guardar pipeline en localStorage
- [x] Cargar pipeline guardado
- [x] Eliminar pipeline con confirmación
- [x] Logs inline por nodo (click/doble-click)
- [x] Modal de logs con formato mono
- [x] Copy output al portapapeles
- [x] Indicador visual en nodos ejecutados

### v10.5 - Dry Run & Pausas por Nodo ✅
- [x] Botón "Simular" con modal de preview
- [x] Tiempo estimado por nodo y total
- [x] Checkboxes HITL por nodo (pausar antes/después)
- [x] Indicador visual de nodos con HITL (borde cyan)
- [x] Edición de datos durante pausas

### v10.4 - Inspector (HITL) ✅
- [x] Nodo Inspector con panel didáctico
- [x] Vista origen → proceso → datos → destino
- [x] 20+ tips didácticos por herramienta
- [x] Edición inline de datos

### v10.3 - Claude CLI Integration ✅
- [x] Endpoint `/api/claude/ask`
- [x] Nodo Claude (CLI) sin coste API
- [x] Tutorial interactivo (TUTORIAL.md + tutorial.html)

### v10.2 - Output & Flow Nodes ✅
- [x] Output: File, Notify, Email, Slack
- [x] Flow: If, Loop, Delay
- [x] Snap to Grid (20px)
- [x] Validación de conexiones (ciclos, tipos)

### v10.1 - Pipeline Execution ✅
- [x] Ejecución secuencial real de pipelines
- [x] Estado visual por nodo (idle/running/success/error)

### v10.0 - Trigger Nodes ✅
- [x] Trigger Manual, File Watch, Cron, Webhook

### v9.x ✅
- [x] Prompt Builder Pro (8 plantillas)
- [x] Undo/Redo, Export JSON, Atajos teclado
- [x] App Store de Flujos (12 recetas)
- [x] Knowledge Base (RAG)

---

## v10.8 - Ejecución Avanzada

**Prioridad: Alta | Esfuerzo: Medio**

### Triggers Automáticos
- [ ] **File Watch activo**: Trigger ejecuta pipeline automáticamente
- [ ] **Cron real**: Scheduler que ejecuta en background
- [ ] **Webhook listener**: Endpoint activo que dispara pipeline

### Logs Globales
- [ ] **Panel de logs global**: Stream de toda la ejecución
- [ ] **Filtros por nivel**: INFO, SUCCESS, ERROR

### Persistencia Avanzada
- [ ] **Auto-save**: Guardar automáticamente cada 30s
- [ ] **Export JSON mejorado**: Incluir metadata (nombre, descripción, versión)
- [ ] **Import JSON**: Cargar pipeline desde archivo
- [ ] **Compartir**: URL con pipeline encoded (base64)

---

## v11.0 - Panel de Ejecuciones

**Prioridad: Media | Esfuerzo: Alto**

### Historial
- [ ] **Lista de runs**: Status, duración, timestamp, errores
- [ ] **Detalle de run**: Ver paso a paso qué se ejecutó
- [ ] **Filtros**: Por pipeline, estado, fecha

### Control
- [ ] **Retry por nodo**: Re-ejecutar solo el paso que falló
- [ ] **Cancel**: Detener ejecución en curso
- [ ] **Métricas**: Archivos procesados, tiempo promedio, tasa éxito

---

## v12.0 - Multi-proyecto & CLI

**Prioridad: Baja | Esfuerzo: Alto**

### Workspaces
- [ ] Gestionar varios proyectos
- [ ] Dashboard global con métricas

### Integración
- [ ] **MCP Server**: DirectOS como servidor MCP
- [ ] **CLI**: `directos run pipeline.json`

---

## Backlog

### UX/UI
- [ ] Dark/Light mode toggle
- [ ] Tour guiado para nuevos usuarios
- [ ] Modo compacto sidebar
- [ ] Más atajos: `Cmd+K` buscar global, `Cmd+N` nuevo pipeline

### Arquitectura
- [ ] Modularizar index.html (canvas.js, validation.js, etc.)
- [ ] Estado centralizado (store pattern)
- [ ] Event bus para comunicación

### Contenido
- [ ] Más patrones (objetivo: 50)
- [ ] Tutoriales por herramienta
- [ ] Nuevas herramientas: Redis, PostgreSQL, LangChain

---

## Quick Wins Pendientes

| Mejora | Impacto | Esfuerzo |
|--------|---------|----------|
| Auto-save pipeline | Alto | Bajo |
| Panel de logs global | Medio | Medio |
| Export JSON con metadata | Medio | Bajo |
| Import JSON | Medio | Bajo |

---

## Cómo priorizar

```
            IMPACTO
        Alto    Bajo
     ┌───────┬───────┐
Bajo │ HACER │Backlog│  ESFUERZO
     ├───────┼───────┤
Alto │ v11+  │ Skip  │
     └───────┴───────┘
```

**Próximo a implementar**: v11.0 (Panel de Ejecuciones, Triggers automáticos)

---

*Última actualización: 9 Dic 2025 - v10.10*
