---
id: agentic-prompts-library
name: Biblioteca de Prompts Agénticos
problem: Crear prompts efectivos para agentes de IA que sean reutilizables, mantenibles y produzcan resultados consistentes
flow: [claude-code, slash-commands, skills, subagents]
created: 2024-12-06
version: 1.0.0
---

# Biblioteca de Prompts Agénticos

> "Los prompts son la nueva unidad de ingeniería. Un prompt bien diseñado es un multiplicador de fuerza que genera cientos de horas de trabajo productivo."

## Filosofía: Stakeholder Trifecta

Todo prompt agéntico se diseña para **3 audiencias**:

| Audiencia | Pregunta clave | Criterio |
|-----------|----------------|----------|
| **Tú** | ¿Lo entenderé en 6 meses? | Claridad personal |
| **Tu Equipo** | ¿Un colega nuevo lo entendería? | Colaboración |
| **Tus Agentes** | ¿El workflow es ejecutable? | Ejecución precisa |

---

## Anatomía: Las 6 Secciones Composables

```
┌─────────────────────────────────────────────────────────┐
│  1. METADATA (frontmatter YAML)                         │
│     description, allowed-tools, argument-hint, model    │
├─────────────────────────────────────────────────────────┤
│  2. TITLE + PURPOSE                                     │
│     # Nombre descriptivo del agente                     │
├─────────────────────────────────────────────────────────┤
│  3. VARIABLES                                           │
│     Tabla de variables dinámicas y estáticas            │
├─────────────────────────────────────────────────────────┤
│  4. WORKFLOW  ★ S-TIER                                  │
│     Secuencia numerada de pasos (QUÉ hacer)             │
├─────────────────────────────────────────────────────────┤
│  5. INSTRUCTIONS                                        │
│     Reglas y guías (CÓMO ejecutar)                      │
├─────────────────────────────────────────────────────────┤
│  6. REPORT                                              │
│     Formato exacto de salida esperado                   │
└─────────────────────────────────────────────────────────┘
```

### Detalle de cada sección

#### 1. Metadata (Frontmatter YAML)

```yaml
---
description: Qué hace + cuándo usarlo (max 100 chars)
allowed-tools: Read, Write, Bash(npm:*)
argument-hint: [archivo o directorio]
model: sonnet  # opcional: haiku, sonnet, opus
---
```

**Reglas:**
- `description`: Incluir QUÉ y CUÁNDO
- `allowed-tools`: Mínimo necesario (principio de menor privilegio)
- `argument-hint`: Formato esperado de $ARGUMENTS

#### 2. Title + Purpose

```markdown
# Nombre del Agent

Descripción extendida si es necesaria (1-2 líneas).
```

#### 3. Variables

```markdown
## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Input del usuario |
| `$1`, `$2` | dinámico | Argumentos posicionales |
| TARGET | estático | Valor derivado o default |
| MODE | estático | Opción calculada |
```

**Tipos:**
- **Dinámico**: Cambia con cada ejecución (`$ARGUMENTS`, `$1`)
- **Estático**: Definido en el prompt o calculado

#### 4. Workflow ★

```markdown
## Workflow

1. **Verbo en infinitivo** descripción
   - Sub-paso si necesario
   - Otro sub-paso

2. **Siguiente paso**
   - Detalles

3. **Paso final**
```

**Reglas:**
- Pasos **secuenciales** (no categorías)
- Verbos de acción: Leer, Analizar, Detectar, Generar, Reportar
- 4-7 pasos típicamente
- Cada paso = una acción clara

#### 5. Instructions

```markdown
## Instructions

- **Regla importante** en negrita
- Qué ignorar o saltar
- Edge cases
- Límites (máximo X por archivo)

### Subsección si necesario
Detalles adicionales...
```

**Diferencia con Workflow:**
- Workflow = QUÉ hacer (secuencia)
- Instructions = CÓMO hacerlo (reglas)

#### 6. Report

```markdown
## Report

```
FORMATO DE SALIDA
═════════════════

📍 ubicación
🏷️ [ETIQUETA] Categoría
❌ Problema
✅ Solución

────────────────
📊 RESUMEN
────────────────
Métrica: valor
```
```

---

## Biblioteca de Comandos

### /doc - Documentation Generator

```markdown
---
description: Genera documentación técnica desde código. Usa cuando necesites README, docs de API, o documentar archivos/directorios.
allowed-tools: Read, Write, Glob, Grep
argument-hint: [archivo, directorio o "readme"]
---

# Documentation Generator

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Target: archivo, directorio, o "readme" |
| MODE | estático | Detectado: `readme` \| `file` \| `directory` |
| OUTPUT | estático | Mismo nombre + `.md` o `README.md` |

## Workflow

1. **Detectar modo** según `$ARGUMENTS`
2. **Recopilar contexto** (imports, exports, estructura)
3. **Analizar patrones** (framework, convenciones)
4. **Generar documentación** (aplicar template)
5. **Presentar resultado** (preview + confirmar)

## Instructions

- NO inventar funcionalidad que no existe
- Ejemplos de código deben ser reales del proyecto
- Mantener estilo de docs existentes

## Report

### MODE=readme
# {Proyecto} → Instalación → Uso → Estructura → API → Desarrollo

### MODE=file
# {archivo} → Descripción → Exports → Dependencias

### MODE=directory
# {dir}/ → Archivos (tabla) → Arquitectura
```

---

### /code-review - Code Reviewer

```markdown
---
description: Code review de calidad, seguridad y mantenibilidad. Usa después de escribir código o antes de commit/PR.
allowed-tools: Read, Grep, Glob
argument-hint: [archivo o directorio]
---

# Code Reviewer

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Target a revisar |
| TARGET | estático | Si vacío → git diff |
| DEPTH | estático | `quick` \| `thorough` |
| MAX_ISSUES | estático | 10 por archivo |

## Workflow

1. **Determinar scope** (archivo, directorio, o git diff)
2. **Leer código** (identificar lenguaje/framework)
3. **Analizar** (calidad, seguridad, mantenibilidad)
4. **Clasificar** (CRÍTICO → INFO)
5. **Generar reporte** (agrupado, ordenado)

## Instructions

- Máximo 10 issues por archivo
- Siempre incluir línea exacta
- Sugerencia concreta de fix
- Si no hay issues → "código limpio"

## Report

📋 CODE REVIEW: {target}
📍 archivo:línea
🏷️ [SEVERIDAD] Categoría
❌ Problema
✅ Sugerencia
📊 RESUMEN + Top 3 prioridades
```

---

### /refactor - Refactoring Advisor

```markdown
---
description: Analiza código y sugiere refactorizaciones. Usa cuando el código funciona pero quieres mejorarlo.
allowed-tools: Read, Grep, Glob
argument-hint: [archivo o directorio]
---

# Refactoring Advisor

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Target a analizar |
| PRIORITY | estático | impacto × (1/esfuerzo) |

## Workflow

1. **Leer código** target
2. **Detectar code smells** (largo, duplicado, complejo)
3. **Identificar dead code** (no usado)
4. **Evaluar naming** (descriptivo, consistente)
5. **Priorizar** (quick wins primero)
6. **Generar reporte** (ANTES/DESPUÉS)

## Instructions

- NO romper funcionalidad
- Código ANTES y DESPUÉS obligatorio
- Explicar POR QUÉ es mejor
- Respetar estilo existente

## Report

🔧 REFACTORING ANALYSIS
💡 QUICK WINS (alto impacto, fácil)
📋 REFACTORS MAYORES (planear)
📊 Deuda técnica: BAJA|MEDIA|ALTA
```

---

### /security - Security Auditor

```markdown
---
description: Auditoría de seguridad OWASP Top 10 + secrets
allowed-tools: Read, Grep, Glob
argument-hint: [directorio o vacío para todo]
---

# Security Auditor

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Scope del escaneo |
| SEVERITY | estático | 🔴 CRÍTICO → 🔵 BAJO |

## Workflow

1. **Escanear secrets** (API keys, passwords, tokens)
2. **Buscar SQL injection** (concatenación en queries)
3. **Detectar XSS** (innerHTML, dangerouslySetInnerHTML)
4. **Validar inputs** (endpoints sin sanitización)
5. **Auditar dependencias** (npm audit, pip-audit)
6. **Clasificar y reportar**

## Instructions

- Ignorar: .env.example, *.test.*, README*
- Incluir referencia OWASP para cada hallazgo
- Priorizar por explotabilidad

## Report

🛡️ AUDITORÍA DE SEGURIDAD
🔴 [CRÍTICO] Tipo - ubicación
❌ Código vulnerable
✅ Código seguro
🔗 Referencia OWASP
📊 RESUMEN por severidad
```

---

### /test - Test Runner

```markdown
---
description: Ejecuta tests, analiza fallos y sugiere correcciones
allowed-tools: Read, Bash(npm:*), Bash(pytest:*), Grep, Glob
argument-hint: [archivo, patrón o vacío]
---

# Test Runner

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | Archivo/patrón específico |
| FRAMEWORK | estático | Detectado: jest, pytest, go test |

## Workflow

1. **Detectar framework** (package.json, pytest.ini, go.mod)
2. **Ejecutar tests** ($ARGUMENTS o todos)
3. **Analizar fallos** (mensaje, ubicación, causa)
4. **Sugerir corrección** (código corregido)
5. **Reportar cobertura** (si disponible)

## Instructions

- Ejecutar con verbose (-v)
- Para cada fallo: leer test + código testeado
- Comparar expected vs actual

## Report

✅ TODOS PASAN | ❌ X FALLOS
Para fallos:
- Test: nombre
- Causa probable
- Sugerencia de fix
⚠️ Código sin tests detectado
```

---

### /update-context - Context Updater

```markdown
---
description: Actualiza CLAUDE.md del proyecto con cambios recientes
allowed-tools: Read, Write, Edit, Bash(git:*)
---

# Context Updater

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| PROJECT_ROOT | estático | Directorio actual |
| CLAUDE_FILE | estático | {PROJECT_ROOT}/CLAUDE.md |
| LOOKBACK | estático | Últimos 5 commits |

## Workflow

1. **Analizar cambios** (git log, git diff)
2. **Leer CLAUDE.md** actual
3. **Identificar actualizaciones** necesarias
4. **Preguntar al usuario** (decisiones, bugs, TODOs)
5. **Generar diff** de cambios propuestos
6. **Confirmar y guardar**

## Instructions

- NO borrar información útil
- Mantener formato existente
- Fechas: DD mmm YYYY
- Si no hay cambios → decirlo

## Report

📝 ACTUALIZACIÓN DE CLAUDE.md
📊 Cambios detectados
📋 Actualizaciones propuestas
¿Guardar? [S/n]
```

---

### /vault - Personal Vault

```markdown
---
description: Actualiza el Vault personal con aprendizajes de la sesión
allowed-tools: Read, Write, Edit, Bash(curl:*), Bash(ls:*)
---

# Vault Updater

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| VAULT_PATH | estático | ~/learning-journey/ |
| DIRECTOS_PATH | estático | ~/Desktop/DirectOS/data/content/ |

## Workflow

1. **Preguntar al usuario** (proyecto, aprendizajes, logros)
2. **Actualizar knowledge-base.md** (stats, changelog)
3. **Sincronizar dashboard.html**
4. **Crear/actualizar** tools/, projects/, patterns/
5. **Refrescar cache** DirectOS
6. **Mostrar resumen** y ofrecer commit

## Instructions

- KISS: Solo cambios necesarios
- Incremental: Pequeñas actualizaciones
- DRY: No duplicar datos
- Git-friendly: Cambios revisables

## Report

✅ knowledge-base.md actualizado
✅ dashboard.html sincronizado
✅ tools/X.md → level: expert
🆕 projects/Y.md creado
¿Crear commit?
```

---

### /scan-projects - Project Scanner

```markdown
---
description: Escanea Desktop buscando proyectos no documentados
allowed-tools: Read, Bash(ls:*), Bash(find:*), Glob, Grep
---

# Project Scanner

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| SCAN_PATH | estático | ~/Desktop/ |
| VAULT_PATH | estático | ~/learning-journey/knowledge-base.md |

## Workflow

1. **Leer Vault** actual (proyectos documentados)
2. **Escanear Desktop** (buscar .git, package.json, etc.)
3. **Detectar stack** por archivos encontrados
4. **Comparar** documentados vs encontrados
5. **Reportar** nuevos proyectos

## Instructions

- Ignorar: venv, node_modules, .git, backups
- Detectar stack por archivo característico

## Report

📊 ESCANEO COMPLETO
✅ Documentados (X): lista
🆕 Sin documentar (Y): tabla con stack y fecha
→ Usar /vault para añadir
```

---

## Plantilla para Nuevos Prompts

```markdown
---
description: [QUÉ hace] + [CUÁNDO usarlo]. Max 100 chars.
allowed-tools: [lista mínima necesaria]
argument-hint: [formato de argumentos]
---

# [Nombre Descriptivo]

## Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `$ARGUMENTS` | dinámico | [Qué espera recibir] |
| [VAR] | estático | [Valor calculado o default] |

## Workflow

1. **[Verbo]** [descripción del paso]
   - Sub-paso si necesario

2. **[Verbo]** [siguiente paso]

3. **[Verbo]** [paso final]

## Instructions

- **[Regla importante]** en negrita
- [Qué ignorar]
- [Edge cases]
- [Límites]

## Report

```
[FORMATO DE SALIDA]
═══════════════════

📍 ubicación
🏷️ [ETIQUETA] Categoría

────────────────
📊 RESUMEN
────────────────
```
```

---

## Checklist de Validación

Antes de publicar un prompt agéntico:

- [ ] **Metadata**: description incluye QUÉ + CUÁNDO
- [ ] **Metadata**: allowed-tools es el mínimo necesario
- [ ] **Variables**: Tabla con tipo (dinámico/estático)
- [ ] **Workflow**: Pasos secuenciales (no categorías)
- [ ] **Workflow**: 4-7 pasos típicamente
- [ ] **Instructions**: Separadas del workflow
- [ ] **Instructions**: Incluye límites y edge cases
- [ ] **Report**: Formato exacto de salida
- [ ] **General**: < 150 líneas total
- [ ] **General**: Sin rutas hardcodeadas
- [ ] **General**: Una sola responsabilidad

---

## Changelog

- **06 dic 2024**: Creación inicial con 8 comandos refactorizados
