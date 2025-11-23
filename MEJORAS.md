# DirectOS - Plan de Mejoras

> Roadmap de evolución para las próximas versiones

## Estado actual: v7.1 - Patterns Expansion

### Lo que tenemos
- [x] Arquitecto Pro con drag & drop
- [x] 6 Presets de arquitectura
- [x] **33 Patrones de prompts** (antes 15)
- [x] 22 Herramientas con fichas técnicas
- [x] Estado de maestría (used/learning/new)
- [x] Knowledge Base (RAG) con embeddings
- [x] Scout (análisis de errores con Claude)
- [x] Monitor de sistema
- [x] **Documento PATRONES.md** con referencia completa
- [x] **8 nuevos packs**: Debug, Data, UI, Robustez, Automation, Data Eng, Docs Visual, Comodín

---

## v7.2 - Quick Wins (UX)

**Prioridad: Alta | Esfuerzo: Bajo**

### Mejoras de UX
- [ ] **Filtros en Glosario**: Por estado (Dominada/Learning/New) y categoría
- [ ] **Búsqueda en Glosario**: Input de búsqueda para encontrar herramientas
- [ ] **Búsqueda en Patrones**: Encontrar patrón por palabra clave
- [ ] **Contador de progreso**: "Has dominado 8/22 herramientas (36%)"
- [ ] **Dark/Light mode toggle**: Para preferencias de usuario

### Mejoras de datos
- [ ] **Cambiar estado desde modal**: Botón para marcar herramienta como "dominada"
- [ ] **Persistir estado en localStorage**: Que se guarde tu progreso
- [ ] **Más herramientas**: Docker, pytest, httpx, jq...

---

## v8.0 - Learning Path

**Prioridad: Alta | Esfuerzo: Medio**

### Sistema de Progreso
- [ ] **Rutas de aprendizaje**: "Ruta RAG", "Ruta Scraping", "Ruta DevOps"
- [ ] **Dependencias entre herramientas**: "Para usar CLIP, primero domina Pillow"
- [ ] **Sugerencias inteligentes**: "Ya dominas X, prueba Y"
- [ ] **Badges/Logros**: "RAG Master", "Pipeline Architect"

### Quiz Mode
- [ ] **Test por herramienta**: Preguntas generadas con el patrón "Mentor Socrático"
- [ ] **Flashcards**: Revisar conceptos clave
- [ ] **Spaced repetition**: Recordatorios para repasar

### Integración
- [ ] **Sincronizar con Obsidian**: Exportar progreso como nota
- [ ] **Importar notas**: Indexar tu vault de Obsidian completo

---

## v9.0 - Pipeline Builder

**Prioridad: Media | Esfuerzo: Alto**

### Arquitecto Pro++
- [ ] **Conexiones visuales**: Líneas arrastrables entre nodos
- [ ] **Validación en tiempo real**: Errores mostrados al conectar
- [ ] **Generación de código**: Del diagrama al scaffold de Python
- [ ] **Importar arquitectura desde código**: Detectar imports y generar diagrama

### Templates de proyecto
- [ ] **"Crear proyecto desde preset"**: Genera estructura de carpetas
- [ ] **Integración con cookiecutter**: Templates de minerOS
- [ ] **Git init automático**: Inicializar repo al crear proyecto

---

## v10.0 - Agent Mode

**Prioridad: Baja | Esfuerzo: Muy Alto**

### DirectOS como Agente
- [ ] **Ejecutar pipelines**: No solo diseñar, sino correr
- [ ] **Watchdog integrado**: Detectar archivos nuevos y procesarlos
- [ ] **Scheduling**: "Ejecutar cada día a las 9am"
- [ ] **Notificaciones**: Alertas cuando termina un proceso

### Multi-proyecto
- [ ] **Workspaces**: Gestionar varios proyectos minerOS
- [ ] **Dashboard global**: Ver estado de todos los proyectos
- [ ] **Métricas**: Cuántos archivos procesados, errores, etc.

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
- [ ] Más patrones de prompts (objetivo: 30)
- [ ] Más herramientas (objetivo: 40)
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

*Última actualización: Nov 2025*
