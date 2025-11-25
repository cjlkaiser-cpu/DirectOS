# FASE 6: Comando /vault inteligente

## Ubicación

```
~/.claude/commands/vault.md
```

## Cambios implementados

El comando `/vault` ahora es **inteligente** y actualiza automáticamente tanto:
- ✅ `knowledge-base.md` (como siempre)
- ✅ Archivos individuales en `data/content/` (NUEVO)

## Lógica de decisión

```
SI (herramienta mencionada):
    SI (existe tools/{herramienta}.md):
        ACTUALIZAR level/next
    SINO:
        CREAR archivo nuevo
    ACTUALIZAR knowledge-base.md

SI (proyecto mencionado):
    SI (existe projects/{proyecto}.md):
        ACTUALIZAR Aprendizajes/Métricas
    SINO:
        CREAR archivo nuevo
    ACTUALIZAR knowledge-base.md

SI (patrón/workflow mencionado):
    SI (existe patterns/{patron}.md):
        ACTUALIZAR prompt/flujo
    SINO:
        CREAR archivo nuevo
    ACTUALIZAR knowledge-base.md

SIEMPRE:
    ACTUALIZAR knowledge-base.md changelog
```

## Flujo de uso

1. Usuario ejecuta `/vault` en Claude Desktop
2. Claude pregunta qué se hizo en la sesión
3. Claude detecta tipo de cambio (tool/project/pattern)
4. Claude actualiza archivos correspondientes
5. Claude refresca cache: `curl -X POST http://localhost:8000/api/content/refresh`
6. Claude pregunta si hacer commit

## Plantillas incluidas

### Herramienta nueva
```yaml
---
id: nombre-tool
name: Nombre Tool
category: Backend|Frontend|IA|DevOps|Data
icon: fa-solid fa-icon
color: text-blue-500
tag: Tag descriptivo
status: used|explored
level: learning|solid|expert
next: Siguiente paso
---
```

### Proyecto nuevo
```yaml
---
id: nombre-proyecto
name: Nombre Proyecto
version: v1.0
status: prototype|active|production|archived
stack: [tool1, tool2]
repo: ruta/o/url
description: Breve descripción
---
```

### Patrón nuevo
```yaml
---
id: nombre-patron
name: Nombre del Patrón
emoji: 🔧
problem: El problema en una frase
flow: [tool1, tool2]
flowDesc: Flujo → Paso 1 → Paso 2
---
```

## Validaciones automáticas

El comando verifica:
- [ ] YAML frontmatter válido
- [ ] Campos requeridos presentes
- [ ] Formato markdown correcto
- [ ] Referencias consistentes

## Comandos útiles embebidos

```bash
# Listar herramientas actuales
ls ~/Desktop/DirectOS/data/content/tools/

# Listar proyectos actuales
ls ~/Desktop/DirectOS/data/content/projects/

# Verificar frontmatter
python3 -c "import frontmatter; print(frontmatter.load('file.md').metadata)"

# Refrescar cache
curl -X POST http://localhost:8000/api/content/refresh
```

## Beneficios

1. **DRY:** No duplicar información entre knowledge-base.md y content/
2. **Automático:** Crea archivos si no existen
3. **Inteligente:** Detecta tipo de cambio automáticamente
4. **Git-friendly:** Cambios pequeños y claros
5. **Validado:** Verifica formato antes de guardar

## Ejemplo de salida

```
✅ knowledge-base.md actualizado
✅ tools/python.md → level: solid → expert
✅ projects/farmaia.md → Métricas actualizadas
🆕 patterns/nuevo-patron.md creado

Cache refrescado ✓

¿Crear commit con estos cambios? (sí/no)
```

## Arquitectura

```
/vault comando
    ↓
Pregunta al usuario
    ↓
Detecta tipo cambio ← Lógica inteligente
    ↓
├─ Herramienta → tools/
├─ Proyecto    → projects/
├─ Patrón      → patterns/
└─ Siempre     → knowledge-base.md
    ↓
Valida frontmatter
    ↓
Guarda archivos
    ↓
Refresca cache API
    ↓
Pregunta commit
```

## Principios de diseño

- **KISS:** Solo cambios necesarios
- **Piano piano:** No sobre-documentar
- **Incremental:** Updates pequeños y frecuentes
- **DRY:** Una fuente de verdad por dato
- **Git-friendly:** Diffs claros y reviewables

## Testing

```bash
# Test 1: Herramienta nueva
/vault
> "Aprendí Docker"
→ Debe crear tools/docker.md + actualizar knowledge-base.md

# Test 2: Proyecto actualizado
/vault
> "farmaIA ahora tiene 15,000 medicamentos"
→ Debe actualizar projects/farmaia.md métricas

# Test 3: Patrón nuevo
/vault
> "Descubrí workflow para validar prompts"
→ Debe crear patterns/prompt-validator.md
```

## Troubleshooting

### Error: "Frontmatter inválido"
```bash
# Verificar manualmente
python3 -c "import frontmatter; print(frontmatter.load('file.md'))"
```

### Cache no se refresca
```bash
# Refrescar manualmente
curl -X POST http://localhost:8000/api/content/refresh
```

### Archivos no aparecen en API
```bash
# Verificar que existen
ls ~/Desktop/DirectOS/data/content/tools/

# Verificar permisos
ls -la ~/Desktop/DirectOS/data/content/
```

## Roadmap futuro

- [ ] Auto-detect desde git diff
- [ ] Sugerir nivel de herramienta basado en uso
- [ ] Generar changelog automático mensual
- [ ] Integración con GitHub para stats
- [ ] Notificaciones de aprendizajes semanales
