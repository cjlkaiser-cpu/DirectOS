# DirectOS - Roadmap

> Mejoras pendientes y próximas versiones

## Estado actual: v9.0

Ver [CHANGELOG.md](./CHANGELOG.md) para el historial completo de cambios.

---

## v9.1 - Agent Mode UI (Próxima)

**Prioridad: Alta | Esfuerzo: Medio**

### Panel de Control Agent Mode
- [ ] **Vista Agent Mode** en sidebar
- [ ] **Iniciar/parar servicios** desde frontend
- [ ] **Configurador de watches**: UI para crear watchers de archivos
- [ ] **Programador visual**: Crear schedules sin escribir cron
- [ ] **Monitor de ejecuciones**: Ver pipelines en progreso

### Mejoras Prompt Builder
- [ ] **Autocompletado de tools**: Sugerencias al escribir allowed-tools
- [ ] **Snippets de report**: Plantillas de formato de salida
- [ ] **Historial de comandos**: Ver cambios anteriores

---

## v10.0 - Multi-proyecto

**Prioridad: Media | Esfuerzo: Alto**

### Workspaces
- [ ] Gestionar varios proyectos minerOS
- [ ] Dashboard global con estado de todos los proyectos
- [ ] Métricas: archivos procesados, errores, etc.

### Integración Claude Code
- [ ] **MCP Server**: DirectOS como servidor MCP
- [ ] **CLI**: `directos search "RAG"` desde terminal

---

## Backlog

### UX/UI
- [ ] Modo compacto para sidebar
- [ ] Atajos de teclado (Cmd+K para buscar)
- [ ] Tour guiado para nuevos usuarios
- [ ] Dark/Light mode toggle

### Contenido
- [ ] Tutoriales interactivos por herramienta
- [ ] Links a documentación oficial
- [ ] Más patrones (objetivo: 50)

---

## Cómo priorizar

```
            IMPACTO
        Alto    Bajo
     ┌───────┬───────┐
Bajo │ HACER │Backlog│  ESFUERZO
     ├───────┼───────┤
Alto │ v9-10 │ Skip  │
     └───────┴───────┘
```

**Criterios**:
1. ¿Aporta valor real al workflow diario?
2. ¿Se puede hacer en una sesión de Claude Code?
3. ¿Sigue la filosofía KISS de minerOS?

---

*Última actualización: 6 Dic 2025*
