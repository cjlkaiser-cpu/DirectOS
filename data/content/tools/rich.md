---
id: rich
name: Rich
category: Process
icon: fa-palette
color: text-purple-400
tag: Terminal UI
status: learning
level: working
next: Rich Live displays
---

# Rich

Librería Python para output enriquecido en terminal. Colores, tablas, progress bars.

## Por qué en minerOS

Hace que los scripts de CLI sean visualmente atractivos y fáciles de seguir.

## Casos de uso

- Progress bars bonitas
- Tablas formateadas
- Syntax highlighting
- Logs con colores

## Código ejemplo

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

# Tabla
table = Table(title="Resultados")
table.add_column("Archivo", style="cyan")
table.add_column("Estado", style="green")
table.add_row("doc1.pdf", "Procesado")
console.print(table)

# Progress bar
for item in track(range(100), description="Procesando..."):
    pass
```

## Proyectos que lo usan

- Web Scraper IA (output formateado)
