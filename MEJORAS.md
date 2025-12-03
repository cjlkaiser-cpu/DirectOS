# DirectOS - Plan de Mejoras

> Roadmap de evolución para las próximas versiones

## Estado actual: v9.0 - Agent Mode

### Lo que tenemos
- [x] Pipeline Builder con canvas visual y conexiones SVG
- [x] 6 Presets de arquitectura
- [x] **34 Patrones de prompts** organizados en packs
- [x] **38 Herramientas** con fichas técnicas
- [x] **13 Proyectos** documentados con stacks
- [x] Estado de maestría (used/learning/new)
- [x] Knowledge Base (RAG) con embeddings
- [x] Scout (análisis de errores con Claude)
- [x] Monitor de sistema
- [x] **App Store de Flujos** (12 recetas)
- [x] **Sistema de toasts** para feedback visual
- [x] **Exportar a PNG** con html2canvas
- [x] **Guardar/Cargar arquitecturas** con modal visual
- [x] **Sync con minerOS Mobile**: Endpoints para push/pull de ideas
- [x] **Importar desde código**: Detectar imports y generar arquitectura

### Agent Mode v9.0 (NUEVO)
- [x] **Pipeline Executor**: Ejecutar pipelines diseñados como código real
- [x] **Watchdog Service**: Detectar archivos nuevos y procesarlos automáticamente
- [x] **Scheduler**: Programar tareas con cron expressions o intervalos
- [x] **Notificaciones macOS**: Alertas desktop cuando terminan procesos
- [x] **API REST completa**: 25+ endpoints para Agent Mode

---

## v8.2 - Quick Wins (UX)

**Prioridad: Alta | Esfuerzo: Bajo**

### Mejoras de UX
- [ ] **Filtros en Glosario**: Por estado (Dominada/Learning/New) y categoría
- [ ] **Búsqueda en Glosario**: Input de búsqueda para encontrar herramientas
- [ ] **Búsqueda en Patrones**: Encontrar patrón por palabra clave
- [x] **Contador de progreso**: Círculo SVG animado en Glosario
- [ ] **Dark/Light mode toggle**: Para preferencias de usuario

### Mejoras de datos
- [x] **Cambiar estado desde modal**: Botones en modal de herramienta
- [x] **Persistir estado en localStorage**: OfflineStore + sync
- [x] **Más herramientas**: Docker, pytest, httpx, jq, flask, huggingface, tkinter, pymupdf, rich, uvicorn...

---


---

## v8.0 - Pipeline Builder ✅ COMPLETADO

**Prioridad: Media | Esfuerzo: Alto**

### Arquitecto Pro++
- [x] **Conexiones visuales**: Líneas SVG bezier entre nodos
- [x] **Validación en tiempo real**: Panel de validación con checks/warnings/errors
- [x] **Generación de código**: Botón "Generar Código" → Python completo
- [x] **Importar arquitectura desde código**: Detectar imports y generar diagrama ✅

### Templates de proyecto
- [x] **"Crear proyecto desde preset"**: Modal con estructura de carpetas
- [x] **Git init automático**: Opción en modal de scaffold
- ~~**Integración con cookiecutter**~~: Descartada - no aporta valor suficiente

---

## v9.0 - Agent Mode ✅ COMPLETADO

**Backend implementado - UI pendiente**

### DirectOS como Agente
- [x] **Ejecutar pipelines**: Motor de ejecución con soporte async
- [x] **Watchdog integrado**: Detectar archivos nuevos (*.pdf, *.mp3, etc.)
- [x] **Scheduling**: Cron expressions y intervalos ("cada 15m", "9am diario")
- [x] **Notificaciones**: Alertas macOS nativas con sonido

### Endpoints API Agent Mode
```
POST /api/agent/execute         - Ejecutar pipeline
GET  /api/agent/runs            - Listar ejecuciones
POST /api/agent/watches         - Crear watch de archivos
POST /api/agent/schedules       - Programar tarea
POST /api/agent/start-all       - Iniciar servicios
GET  /api/agent/status          - Estado general
```

---

## v10.0 - Multi-proyecto (Próxima)

### Multi-proyecto
- [ ] **Workspaces**: Gestionar varios proyectos minerOS
- [ ] **Dashboard global**: Ver estado de todos los proyectos
- [ ] **Métricas**: Cuántos archivos procesados, errores, etc.

### Agent Mode UI
- [ ] **Panel de control**: Iniciar/parar servicios desde frontend
- [ ] **Configurador de watches**: UI para crear watchers
- [ ] **Programador visual**: Crear schedules sin escribir cron

---

## Ideas en el Backlog

### UX/UI
- [ ] Modo compacto para sidebar
- [ ] Atajos de teclado (Cmd+K para buscar)
- [ ] Tour guiado para nuevos usuarios
- [ ] Exportar configuración completa

### Integraciones
- [ ] **MCP Server**: DirectOS como servidor MCP para Claude Code
- [ ] **CLI**: `directos search "RAG"` desde terminal
- [ ] **API pública**: Otros proyectos consultan DirectOS

### Contenido
- [x] Más patrones de prompts (objetivo: 30) → **34 patrones**
- [x] Más herramientas (objetivo: 40) → **38 herramientas**
- [ ] Tutoriales interactivos por herramienta
- [ ] Links a documentación oficial

---

## Cómo priorizar

```
                IMPACTO
            Alto    Bajo
         ┌───────┬───────┐
    Bajo │ v7.1  │ Backlog│  ESFUERZO
         ├───────┼───────┤
    Alto │ v8-9  │  Skip  │
         └───────┴───────┘
```

**Criterios**:
1. ¿Aporta valor real al workflow diario?
2. ¿Se puede hacer en una sesión de Claude Code?
3. ¿Sigue la filosofía KISS de minerOS?

---

## Contribuciones

Ideas, bugs o mejoras → Abrir issue o PR en el repo.

---

*Última actualización: 3 Dic 2025*
