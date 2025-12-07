---
id: claude-node
name: Claude (CLI)
category: IA Model
icon: fa-brain
color: text-amber-400
tag: LLM Pro/Max
status: used
level: master
next: Ollama para modelos locales
---

# Claude (CLI)

Ejecuta Claude usando tu suscripción Pro/Max via Claude Code CLI.

## Por qué en minerOS

Acceso a Claude sin pagar API. Usa tu suscripción existente para análisis, generación de código, y razonamiento avanzado.

## Casos de uso

- Análisis de código
- Generación de documentación
- Debugging inteligente
- Resúmenes y síntesis
- Refactoring asistido

## Código ejemplo

```python
import subprocess
import json

def ask_claude(prompt, system_prompt=""):
    """Ejecuta Claude CLI con tu suscripción"""
    full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt

    result = subprocess.run(
        ["claude", "-p", full_prompt, "--output-format", "json"],
        capture_output=True,
        text=True,
        timeout=180
    )

    if result.returncode == 0:
        data = json.loads(result.stdout)
        return data.get("result", result.stdout)
    return None

# Uso
response = ask_claude(
    "Analiza este código y sugiere mejoras",
    system_prompt="Eres un experto en Python"
)
```

## Tips aprendidos

- Timeout de 3 minutos para prompts largos
- Usar --output-format json para parsear fácil
- Funciona con suscripción Pro/Max (no API)

## Proyectos que lo usan

- DirectOS v10.2 (Pipeline Builder)
- Scout (análisis de errores)
