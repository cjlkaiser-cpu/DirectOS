---
id: typer
name: Typer
category: Backend
icon: fa-terminal
color: text-emerald-400
tag: CLI
status: new
level: exploring
next: Typer rich integration
---

# Typer

Crea CLIs profesionales con Python usando type hints.

## Por qué en minerOS

Convierte tus scripts en herramientas de línea de comandos con ayuda automática y autocompletado.

## Casos de uso

- CLI para minerOS
- Scripts con argumentos
- Herramientas internas

## Código ejemplo

```python
import typer

app = typer.Typer()

@app.command()
def process(path: str, verbose: bool = False):
    '''Procesa archivos en PATH'''
    typer.echo(f'Procesando {path}')
```

## Proyectos que lo usan

- PhotoMine v2.0 (planeado - CLI completa)
- DirectOS CLI (futuro - gestión desde terminal)
