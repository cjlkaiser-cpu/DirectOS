---
id: ruff
name: Ruff / Black
category: DevOps
icon: fa-check-double
color: text-yellow-200
tag: Calidad
status: new
level: exploring
next: Pre-commit hooks
---

# Ruff / Black

Herramientas de limpieza y formateo de código.

## Por qué en minerOS

Hacen que tu código se vea profesional automáticamente. Black formatea y Ruff busca errores.

## Casos de uso

- Formatear al guardar
- Detectar imports no usados
- Estilo consistente

## Código ejemplo

```bash
# En terminal
ruff check .
black .
```

## Proyectos que lo usan

- Experimentos (código más limpio)
- DirectOS v8.0 (planeado - CI/CD)
