"""
Scout Module - Análisis de Errores con Claude
==============================================
Analiza logs de error y sugiere soluciones usando Claude API.

Requiere:
- ANTHROPIC_API_KEY en variables de entorno o .env
"""

import os
from pathlib import Path
from typing import Optional
from loguru import logger

try:
    from anthropic import Anthropic
    from dotenv import load_dotenv
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False
    logger.warning("Dependencias de Scout no instaladas")

# Cargar variables de entorno
if DEPS_AVAILABLE:
    load_dotenv()


class Scout:
    """
    Agente Scout para análisis de errores.

    Uso:
        scout = Scout()
        result = await scout.analyze("TypeError: cannot read property...")
    """

    # Prompt de sistema para el análisis
    SYSTEM_PROMPT = """Eres Scout, un asistente experto en debugging para el ecosistema minerOS.

Tu stack de referencia:
- Python 3.11, FastAPI, Flask
- SQLite, ChromaDB
- CLIP, Whisper, sentence-transformers
- HTML/CSS/JS, Tailwind, HTMX

Cuando analices un error:
1. Identifica el tipo de error y su causa probable
2. Explica de forma clara y concisa qué está pasando
3. Sugiere la solución más directa (código si aplica)
4. Si hay alternativas, menciónalas brevemente

Formato de respuesta:
- Sé directo y práctico (estilo minerOS: KISS)
- No uses jerga innecesaria
- Si el error es común, indica la solución inmediata
- Si necesitas más contexto, indica qué información falta"""

    def __init__(self):
        self.client = None
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if DEPS_AVAILABLE and self.api_key:
            self._initialize()
        elif not self.api_key:
            logger.warning("ANTHROPIC_API_KEY no configurada")

    def _initialize(self):
        """Inicializar cliente de Anthropic"""
        try:
            self.client = Anthropic(api_key=self.api_key)
            logger.info("Scout inicializado con Claude API")
        except Exception as e:
            logger.error(f"Error inicializando Scout: {e}")
            self.client = None

    def is_ready(self) -> bool:
        """Verificar si el módulo está listo"""
        return self.client is not None

    async def analyze(self, error_text: str, context: str = "") -> dict:
        """
        Analizar un error y sugerir solución.

        Args:
            error_text: El texto del error/traceback
            context: Contexto adicional (archivo, qué estabas haciendo)

        Returns:
            dict con analysis, suggestion, confidence
        """
        if not self.is_ready():
            return {
                "analysis": "Scout no está configurado",
                "suggestion": "Configura ANTHROPIC_API_KEY en .env",
                "confidence": "N/A"
            }

        # Construir el mensaje
        user_message = f"""Analiza este error:

```
{error_text}
```"""

        if context:
            user_message += f"""

Contexto adicional:
{context}"""

        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system=self.SYSTEM_PROMPT,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            # Extraer el texto de la respuesta
            full_response = response.content[0].text

            # Parsear la respuesta (simple por ahora)
            # En el futuro podríamos pedir JSON estructurado
            return {
                "analysis": full_response,
                "suggestion": self._extract_suggestion(full_response),
                "confidence": self._estimate_confidence(error_text, full_response)
            }

        except Exception as e:
            logger.error(f"Error en análisis Scout: {e}")
            return {
                "analysis": f"Error al analizar: {str(e)}",
                "suggestion": "Verifica tu conexión y API key",
                "confidence": "error"
            }

    def _extract_suggestion(self, response: str) -> str:
        """Extraer la sugerencia principal de la respuesta"""
        # Buscar bloques de código como sugerencia principal
        import re
        code_blocks = re.findall(r'```[\w]*\n(.*?)```', response, re.DOTALL)
        if code_blocks:
            return code_blocks[0].strip()

        # Si no hay código, tomar las primeras líneas
        lines = response.strip().split('\n')
        return '\n'.join(lines[:3]) if len(lines) > 3 else response

    def _estimate_confidence(self, error: str, response: str) -> str:
        """Estimar confianza de la respuesta"""
        # Heurísticas simples
        common_errors = [
            "ImportError", "ModuleNotFoundError",
            "TypeError", "AttributeError",
            "KeyError", "IndexError",
            "SyntaxError", "IndentationError"
        ]

        for err in common_errors:
            if err in error:
                return "alta"

        if "no estoy seguro" in response.lower() or "podría ser" in response.lower():
            return "media"

        if len(response) > 500:  # Respuesta detallada
            return "alta"

        return "media"

    def analyze_sync(self, error_text: str, context: str = "") -> dict:
        """Versión síncrona de analyze para uso directo"""
        import asyncio
        return asyncio.run(self.analyze(error_text, context))


# =============================================================================
# PRUEBA RÁPIDA
# =============================================================================

if __name__ == "__main__":
    scout = Scout()
    if scout.is_ready():
        result = scout.analyze_sync(
            "TypeError: 'NoneType' object is not subscriptable",
            "Intentando acceder a results['data'] después de una query"
        )
        print(result)
    else:
        print("Scout no configurado. Añade ANTHROPIC_API_KEY a .env")
