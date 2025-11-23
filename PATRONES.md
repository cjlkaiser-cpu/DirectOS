# Biblioteca de Patrones de Prompts - DirectOS v7.1

> 33 patrones listos para copiar y usar con Claude Code / Claude API

---

## Resumen por Packs

| Pack | Categoría | Patrones | Enfoque |
|------|-----------|----------|---------|
| 1 | Refactoring | 3 | Código limpio |
| 2 | Contenido | 1 | Markdown → Multi-formato |
| 3 | Seguridad | 1 | Privacidad datos |
| 4 | Knowledge | 1 | RAG y síntesis |
| 5 | Aprendizaje | 3 | Estudiar y traducir |
| 6 | DevOps | 3 | Calidad código |
| 7 | Debug & Performance | 2 | Errores y velocidad |
| 8 | Data & API | 2 | Esquemas y endpoints |
| 9 | Meta & Automation | 2 | Prompts y watchdog |
| 10 | Creatividad & UI | 3 | Frontend bonito |
| 11 | Ingeniería & Robustez | 3 | Sistema sólido |
| 12 | Data Engineering | 3 | Limpieza datos |
| 13 | Documentación Visual | 3 | Diagramas y docs |

**Total: 33 patrones**

---

## Pack 1: Refactoring

### 1. Refactorizador Modular

**Problema**: Tienes un script `prueba.py` de 300 líneas que funciona, pero es un caos.

**Prompt**:
```
Actúa como Arquitecto de Software. Toma este código monolítico y refactorízalo
siguiendo la arquitectura limpia de minerOS. Sepáralo en: routers/ (endpoints),
services/ (lógica pura), y core/ (configuración). Usa inyección de dependencias
y Pydantic para validación. Entrégame la estructura de archivos final.
```

**Flujo Táctico**: `Script → Analiza → Separa módulos → Estructura limpia`

**Herramientas**: Python, FastAPI, Loguru

---

### 2. Guardián de Calidad

**Problema**: Tienes miedo de tocar el código porque se puede romper.

**Prompt**:
```
Actúa como Ingeniero de QA experto en Pytest. Genera una suite de tests completa
para este módulo. Incluye conftest.py con fixtures para mockear la base de datos
y las llamadas a APIs externas (como OpenAI). Cubre casos de éxito, casos de error
y casos borde.
```

**Flujo Táctico**: `Código → Analiza → Genera tests → conftest.py + tests/`

**Herramientas**: Python, SQLite, Loguru

---

### 3. Constructor de Interfaz

**Problema**: Tienes la API hecha pero te da pereza hacer el HTML.

**Prompt**:
```
Actúa como Desarrollador Frontend Minimalista. Teniendo en cuenta este esquema
de datos Pydantic del backend, genera un componente HTML5 + TailwindCSS autónomo.
Usa HTMX para conectar con el endpoint sin escribir JavaScript. El diseño debe
ser limpio, oscuro (Slate-900) y mobile-first.
```

**Flujo Táctico**: `Pydantic Schema → HTML5 + Tailwind → HTMX bindings`

**Herramientas**: HTML5, Tailwind, HTMX, FastAPI

---

## Pack 2: Contenido

### 4. Alquimista de Contenido

**Problema**: Tienes un archivo Markdown técnico y quieres convertirlo en contenido publicable.

**Prompt**:
```
Actúa como Content Strategist técnico. Toma este archivo Markdown y genera:
1) Un hilo de Twitter de 5 tweets con hooks y emojis
2) Un post de LinkedIn profesional con bullet points
3) Una Newsletter HTML maquetada
Mantén el tono técnico pero accesible.
```

**Flujo Táctico**: `Markdown → IA extrae ideas → Genera formatos → HTML Newsletter`

**Herramientas**: Python, Claude API, CLIP, HTML5, SQLite

---

## Pack 3: Seguridad

### 5. Escudo de Privacidad

**Problema**: Necesitas compartir logs o documentos pero contienen datos sensibles.

**Prompt**:
```
Actúa como Ingeniero de Seguridad. Crea un script Python que escanee archivos
recursivamente, detecte datos sensibles (DNI, Email, Teléfono, API Keys, IBANs)
usando regex y opcionalmente Spacy NER, y genere una copia censurada con [REDACTED].
Usa Loguru para alertar cada hallazgo. Sin APIs externas - todo local.
```

**Flujo Táctico**: `Archivos → OCR si es imagen → Regex/Spacy detecta → Copia censurada`

**Herramientas**: Python, Tesseract OCR, Loguru

---

## Pack 4: Knowledge

### 6. Sintetizador de Conocimiento

**Problema**: Tienes 50 PDFs sobre un tema y necesitas un resumen coherente.

**Prompt**:
```
Actúa como Investigador Senior. Genera un "Estado del Arte" sobre el tema
especificado basándote únicamente en los fragmentos recuperados de mi Knowledge
Base local. Estructura el ensayo con: Introducción, Conceptos clave, Evolución
histórica, Estado actual, y Conclusiones. Cita las fuentes originales.
```

**Flujo Táctico**: `Tema → ChromaDB busca → Reranking → LLM sintetiza → Informe HTML`

**Herramientas**: FastAPI, ChromaDB, Python, Claude API, HTML5

---

## Pack 5: Aprendizaje

### 7. Mentor Socrático

**Problema**: Quieres comprobar si realmente entendiste un documento técnico.

**Prompt**:
```
Actúa como profesor universitario experto en evaluación. Lee este documento
técnico y genera un test de 10 preguntas tipo test (4 opciones, solo 1 correcta).
Incluye preguntas de comprensión, aplicación y análisis. Devuelve un JSON con:
pregunta, opciones[], respuesta_correcta, explicacion.
```

**Flujo Táctico**: `PDF/MD → LLM genera quiz → JSON → Interfaz Flashcards`

**Herramientas**: Python, Claude API, HTMX, Markdown

---

### 8. Resumen Ejecutivo

**Problema**: Al final del día no recuerdas qué guardaste en tus carpetas.

**Prompt**:
```
Actúa como Asistente Personal. Escanea los archivos creados/modificados en las
últimas 24 horas en la carpeta especificada. Para cada archivo, extrae su "esencia"
(título, tipo, tema principal). Genera un resumen narrativo de 1 párrafo:
"Hoy guardaste 3 facturas, 2 notas de voz sobre X, y 1 snippet de código para Y".
```

**Flujo Táctico**: `Watchdog → Clasifica archivos → IA resume → DIARIO.md`

**Herramientas**: Python, Watchdog, Tesseract OCR, CLIP, Claude API, Markdown

---

### 9. Torre de Babel

**Problema**: Necesitas leer documentación técnica en otro idioma.

**Prompt**:
```
Actúa como Traductor Técnico especializado. Traduce este documento manteniendo:
1) Bloques de código intactos
2) Nombres de variables/funciones sin traducir
3) Terminología técnica estándar (API, endpoint, etc)
Genera una versión bilingüe lado a lado si es posible.
```

**Flujo Táctico**: `Markdown → Separa código/texto → Traduce texto → Re-ensambla`

**Herramientas**: Python, Claude API, HTML5, Markdown

---

## Pack 6: DevOps

### 10. Code Reviewer

**Problema**: Quieres un segundo par de ojos antes de hacer commit.

**Prompt**:
```
Actúa como Senior Python Developer con 10 años de experiencia. Revisa este código
buscando:
1) Vulnerabilidades de seguridad (inyección, exposición de secrets)
2) Problemas de rendimiento (N+1, memory leaks)
3) Falta de type hints
4) Code smells (funciones largas, acoplamiento)
Prioriza los hallazgos por severidad.
```

**Flujo Táctico**: `Código → Análisis estático → IA review → Reporte priorizado`

**Herramientas**: Python, Loguru

---

### 11. Semilla de Datos

**Problema**: Necesitas datos de prueba realistas sin usar datos reales de producción.

**Prompt**:
```
Actúa como Ingeniero de Datos. Genera un dataset de prueba con el esquema especificado.
Los datos deben ser:
1) Coherentes entre sí (edades realistas, nombres plausibles)
2) Diversos (cubrir casos borde)
3) En formato JSON/CSV
Incluye al menos 100 registros.
```

**Flujo Táctico**: `Esquema → LLM genera JSON → Valida Pydantic → Inserta SQLite`

**Herramientas**: FastAPI, Claude API, Python, SQLite

---

### 12. Documentador Fantasma

**Problema**: Tu código funciona pero no tiene documentación.

**Prompt**:
```
Actúa como Technical Writer. Lee este módulo Python usando AST y genera:
1) Docstrings en formato Google Style para cada función
2) Un README.md con: descripción, instalación, uso básico, y ejemplos
3) Un diagrama ASCII del flujo principal
No inventes funcionalidad - documenta solo lo que existe.
```

**Flujo Táctico**: `Código → AST extrae estructura → LLM documenta → docs/`

**Herramientas**: Python, Claude API, Markdown

---

## Pack 7: Debug & Performance

### 13. Debugger Sherlock

**Problema**: Tienes un error críptico y no sabes por dónde empezar.

**Prompt**:
```
Actúa como Detective de Bugs Senior. Analiza este traceback como si fueras Sherlock Holmes.
Identifica:
1) La línea exacta del fallo y el tipo de excepción
2) El contexto (qué datos entraron que causaron esto)
3) 3 hipótesis ordenadas por probabilidad
4) Plan de debugging paso a paso con prints/breakpoints estratégicos
No asumas - deduce desde la evidencia.
```

**Flujo Táctico**: `Traceback → Analiza contexto → Hipótesis → Plan de acción`

**Herramientas**: Python, Loguru, Claude API

---

### 14. Performance Hunter

**Problema**: Tu script funciona pero tarda demasiado.

**Prompt**:
```
Actúa como Performance Engineer. Analiza este código Python buscando:
1) Loops O(n²) convertibles a O(n) con sets/dicts
2) Operaciones I/O bloqueantes que podrían ser async
3) Memory allocations innecesarias en loops
4) Candidatos para caching (@lru_cache, memoization)
Prioriza por impacto/esfuerzo. Dame el código optimizado.
```

**Flujo Táctico**: `Código lento → Profiling mental → Identificar hotspots → Optimizar`

**Herramientas**: Python, Loguru

---

## Pack 8: Data & API

### 15. Schema Detective

**Problema**: Recibes un JSON/CSV gigante y necesitas entender su estructura.

**Prompt**:
```
Actúa como Data Analyst. Analiza este dataset (JSON/CSV) y genera:
1) Modelo Pydantic con tipos inferidos automáticamente
2) Campos opcionales (Optional[]) vs requeridos detectados
3) Valores únicos que deberían ser Enums (ej: status, categoría)
4) Relaciones entre entidades si existen (foreign keys implícitas)
Formato listo para copiar a models.py.
```

**Flujo Táctico**: `JSON/CSV → Inferir tipos → Generar Pydantic → models.py`

**Herramientas**: Python, Pydantic, FastAPI

---

### 16. API Architect

**Problema**: Sabes qué necesitas pero no cómo diseñar los endpoints.

**Prompt**:
```
Actúa como API Designer experto en REST. Dado este dominio de negocio, diseña una
API RESTful completa:
1) Recursos y rutas (GET/POST/PUT/DELETE) con nomenclatura correcta
2) Esquemas Pydantic de request/response para cada endpoint
3) Códigos HTTP específicos (201 crear, 204 borrar, 404, 422)
4) Ejemplo curl de cada endpoint
Estilo FastAPI, listo para implementar.
```

**Flujo Táctico**: `Dominio → Identificar recursos → Diseñar rutas → Schemas`

**Herramientas**: FastAPI, Pydantic, Python

---

## Pack 9: Meta & Automation

### 17. Prompt Optimizer

**Problema**: Tu prompt funciona a medias, a veces da respuestas inconsistentes.

**Prompt**:
```
Actúa como Prompt Engineer Senior. Analiza este prompt y mejóralo aplicando:
1) Rol específico con años de experiencia y expertise
2) Formato de salida estructurado (JSON, Markdown, etc)
3) Ejemplos few-shot si el patrón es complejo
4) Restricciones explícitas (qué NO hacer)
5) Pensamiento paso a paso si requiere razonamiento
Devuelve: versión original vs mejorada con explicación de cambios.
```

**Flujo Táctico**: `Prompt débil → Análisis → Aplicar técnicas → Prompt robusto`

**Herramientas**: Claude API, Markdown

---

### 18. Workflow Automator

**Problema**: Haces lo mismo manualmente cada día (renombrar, mover, procesar).

**Prompt**:
```
Actúa como Automation Engineer. Dado este flujo manual que describo, genera un
script Python con Watchdog que:
1) Detecte archivos nuevos por patrón (*.pdf, *.jpg)
2) Ejecute la acción automáticamente (renombrar, mover, procesar)
3) Loguee cada operación con Loguru (timestamp, archivo, acción)
4) Tenga modo --dry-run para probar sin ejecutar
Sin dependencias externas innecesarias. Local-first.
```

**Flujo Táctico**: `Describir flujo → Watchdog detecta → Acción → Log`

**Herramientas**: Python, Watchdog, Loguru

---

## Pack 10: Creatividad & UI

### 19. Pincel Digital (UI Polisher)

**Problema**: Tienes un HTML funcional pero feo. Quieres que parezca una app SaaS profesional.

**Prompt**:
```
Actúa como Diseñador UI/UX Senior experto en Tailwind CSS. Toma este HTML crudo
y rediséñalo completamente para que sea moderno, oscuro (dark mode) y minimalista.
Requisitos:
- Usa gradientes sutiles para los fondos (slate-900 → slate-950)
- Mejora la tipografía (Inter o system-ui)
- Añade micro-interacciones (hover states, transiciones 200ms)
- Sombras sutiles para profundidad
- Mantén la estructura funcional intacta, solo mejora la estética
```

**Flujo Táctico**: `HTML feo → Análisis UX → Tailwind magic → HTML profesional`

**Herramientas**: HTML5, Tailwind CSS, Alpine.js

---

### 20. Narrador de Datos (Chart Maker)

**Problema**: Tienes datos en SQLite/Python pero verlos en tablas es aburrido.

**Prompt**:
```
Actúa como Experto en Visualización de Datos. Tengo este dataset JSON (o consulta SQL).
Genera el código HTML + JavaScript para visualizarlo usando Chart.js.
Objetivo: Dashboard interactivo con:
- Gráfico de línea temporal para evolución
- Gráfico donut para distribución por categorías
- Tarjetas KPI con los totales
Paleta: colores neón (cyan, magenta, amarillo) sobre fondo slate-900.
```

**Flujo Táctico**: `Datos → Elegir visualización → Chart.js → Dashboard`

**Herramientas**: HTML5, JavaScript, SQLite, Python

---

### 21. Arquitecto de Componentes (Web Component)

**Problema**: Repites mucho código HTML (tarjetas, botones, menús).

**Prompt**:
```
Actúa como Frontend Developer experto en DRY. Extrae este bloque de HTML repetitivo
y conviértelo en:
Opción A) Macro de Jinja2 reutilizable
Opción B) Template HTML con slots
Opción C) Componente Alpine.js con x-data

Que acepte parámetros: título, imagen, estado, onClick.
Incluye ejemplo de uso instanciándolo 3 veces con datos diferentes.
```

**Flujo Táctico**: `HTML repetido → Identificar variaciones → Parametrizar → Componente`

**Herramientas**: HTML5, Jinja2, Alpine.js, HTMX

---

## Pack 11: Ingeniería & Robustez

### 22. Comandante de Terminal (CLI Builder)

**Problema**: Ejecutar scripts editando variables en el código es cutre. Quieres `minerOS scan --path ./docs`.

**Prompt**:
```
Actúa como Python Tooling Expert. Convierte este script suelto en una CLI profesional
usando Typer (o Click). Requisitos:
- Comandos claros: scan, process, clean, status
- Opciones con valores por defecto sensatos
- Barras de progreso con rich/tqdm para tareas largas
- Ayuda automática bonita (--help)
- Colores en terminal para éxito/error
- Manejo de Ctrl+C graceful
```

**Flujo Táctico**: `Script → Identificar inputs → Typer CLI → Instalable con pip`

**Herramientas**: Python, Typer/Click, Rich, Loguru

---

### 23. Cirujano de Datos (SQL Optimizer)

**Problema**: Tus consultas a SQLite empiezan a ir lentas o el esquema es un caos.

**Prompt**:
```
Actúa como DBA (Database Administrator) experto en SQLite. Analiza este esquema
de tablas y esta consulta SQL lenta.
Tareas:
1) Identifica cuellos de botella (table scans, joins sin índice)
2) Sugiere índices específicos (CREATE INDEX ...)
3) Normaliza si hay redundancia (3NF)
4) Reescribe la query optimizada
5) Explica el plan de ejecución (EXPLAIN QUERY PLAN)
```

**Flujo Táctico**: `Schema + Query → EXPLAIN → Índices → Query optimizada`

**Herramientas**: SQLite, Python

---

### 24. Centinela de Errores (Error Handler)

**Problema**: Tu script se rompe si falta internet o un archivo, y no sabes por qué.

**Prompt**:
```
Actúa como Ingeniero de Fiabilidad (SRE). Envuelve este bloque de código crítico
en una estructura robusta de manejo de errores.
Requisitos:
- Excepciones específicas (NetworkError, FileNotFoundError, TimeoutError)
- Retry con backoff exponencial (3 intentos, 1s→2s→4s)
- Fallback graceful si todo falla
- Loguru para registrar: timestamp, intento, error, contexto
- Return value que indique éxito/fallo sin explotar
```

**Flujo Táctico**: `Código frágil → Identificar fallos → try/except → Retry → Log`

**Herramientas**: Python, Loguru, tenacity

---

## Pack 12: Data Engineering

### 25. Conserje de Datos (Data Janitor)

**Problema**: Tienes un CSV/JSON sucio con fechas mixtas, nulos y duplicados.

**Prompt**:
```
Actúa como Data Engineer. Tengo este dataset sucio. Genera un script de limpieza
con Pandas que:
1) Estandarice fechas a ISO 8601 (detectando formatos mixtos)
2) Maneje nulos: media para numéricos, "UNKNOWN" para strings, o flag _is_null
3) Elimine duplicados (por subset de columnas clave)
4) Detecte outliers (valores > 3 std)
5) Exporte reporte de calidad: % completitud por columna, duplicados encontrados
Output: CSV limpio + quality_report.json
```

**Flujo Táctico**: `CSV sucio → Pandas → Limpieza → CSV limpio + reporte`

**Herramientas**: Python, Pandas, Loguru

---

### 26. Susurrador de Regex (Pattern Extractor)

**Problema**: Necesitas extraer información específica de texto no estructurado (logs, emails, PDFs OCR).

**Prompt**:
```
Actúa como experto en Expresiones Regulares de Python. Necesito extraer [PATRÓN]
de este texto sucio.
Ejemplos de patrones complejos:
- Referencias catastrales españolas
- IBANs europeos
- Números de expediente
- Fechas en cualquier formato

Para cada patrón:
1) Regex comentada paso a paso
2) Código Python con re.findall()
3) Tests con casos borde (qué debería matchear y qué no)
```

**Flujo Táctico**: `Texto → Identificar patrón → Regex → Extraer → Lista limpia`

**Herramientas**: Python, re (regex)

---

### 27. Traductor de Formatos (Universal Adapter)

**Problema**: Necesitas mover datos entre sistemas incompatibles (XML→SQLite, Excel→JSON).

**Prompt**:
```
Actúa como Integration Engineer. Tengo datos en [FORMATO_ORIGEN] y necesito
migrarlos a [FORMATO_DESTINO].
Genera el script de migración en Python que:
1) Parsee el origen (lxml para XML, openpyxl para Excel, etc)
2) Transforme al esquema destino (mapeo de campos)
3) Valide con Pydantic antes de insertar
4) Maneje errores por registro (no fallar todo por uno malo)
5) Genere log de migración: exitosos, fallidos, warnings
```

**Flujo Táctico**: `Origen → Parse → Transform → Validate → Load → Log`

**Herramientas**: Python, lxml/openpyxl, Pydantic, SQLite

---

## Pack 13: Documentación Visual

### 28. Diagramador Automático (Mermaid Maker)

**Problema**: Necesitas explicar un flujo visualmente pero dibujar es tedioso.

**Prompt**:
```
Actúa como Technical Illustrator. Analiza este código/flujo y genera código Mermaid.js
para visualizarlo.
Tipos de diagrama según necesidad:
- Secuencia: llamadas entre Frontend → API → DB
- Flowchart: lógica de decisión (if/else)
- ER: relaciones entre tablas
- State: estados de un proceso

Output: código Mermaid listo para pegar en GitHub/Notion + preview ASCII.
```

**Flujo Táctico**: `Código/descripción → Elegir tipo → Mermaid.js → Diagrama`

**Herramientas**: Mermaid.js, Markdown, Python

---

### 29. Bibliotecario de API (Swagger Writer)

**Problema**: Tu API funciona pero no tiene documentación para otros devs.

**Prompt**:
```
Actúa como API Documentation Specialist. Tengo estas funciones Python que actúan
como endpoints. Genera documentación OpenAPI 3.0 (Swagger) en YAML:
- Paths con métodos HTTP
- Request body con schemas JSON
- Responses: 200 (éxito), 400 (validación), 404 (no encontrado), 500 (server)
- Ejemplos realistas para cada endpoint
- Tags para agrupar por recurso

Bonus: genera también el docstring para que FastAPI auto-genere /docs.
```

**Flujo Táctico**: `Código → Extraer endpoints → OpenAPI YAML → /docs automático`

**Herramientas**: FastAPI, Pydantic, OpenAPI/Swagger

---

### 30. Gestor de Entorno (Config Master)

**Problema**: Tienes API keys y rutas hardcodeadas en el código. Peligroso y feo.

**Prompt**:
```
Actúa como DevOps Engineer. Analiza este script y:
1) Identifica TODAS las variables que deberían ser configuración:
   - API Keys / Secrets
   - Rutas de archivos
   - URLs de servicios
   - Puertos
   - Feature flags
2) Refactoriza usando python-dotenv + Pydantic Settings
3) Genera .env.example con valores placeholder
4) Añade validación (la app no arranca si falta ANTHROPIC_API_KEY)
```

**Flujo Táctico**: `Código → Identificar config → .env + Settings → Validación`

**Herramientas**: Python, python-dotenv, Pydantic

---

## Bonus: 3 Patrones Comodín

### 31. El Meta-Patrón (Pattern Generator)

**Problema**: Necesitas un patrón que no existe en esta lista.

**Prompt**:
```
Actúa como Prompt Architect de minerOS. Necesito un nuevo patrón de prompt para
[DESCRIBIR PROBLEMA].
Genera siguiendo esta estructura:
- Nombre creativo + emoji
- El Problema (1 frase)
- El Prompt (completo, listo para usar)
- Flujo Táctico (herramientas involucradas)
- Ejemplo de uso real
```

---

### 32. El Auditor de Proyecto (Project Scanner)

**Problema**: Heredas un proyecto y no sabes por dónde empezar.

**Prompt**:
```
Actúa como Tech Lead haciendo due diligence. Escanea este proyecto y genera un
informe ejecutivo:
1) Stack detectado (lenguajes, frameworks, DBs)
2) Estructura de carpetas y convenciones
3) Puntos de entrada (main.py, index.html)
4) Dependencias críticas (requirements.txt, package.json)
5) Red flags: código muerto, secrets expuestos, deuda técnica obvia
6) Siguiente paso recomendado
```

---

### 33. El Simplificador (KISS Enforcer)

**Problema**: Sospechas que tu código está sobre-engineered.

**Prompt**:
```
Actúa como Senior Developer minimalista. Revisa este código con filosofía KISS
(Keep It Simple, Stupid). Identifica:
1) Abstracciones prematuras (clases que solo se usan una vez)
2) Patrones de diseño innecesarios
3) Configuración excesiva para el caso de uso real
4) Código que "por si acaso" nunca se ejecuta

Para cada hallazgo: muestra el código actual vs la versión simplificada.
La pregunta clave: "¿Esto resuelve un problema real o uno imaginario?"
```

---

## Cómo usar esta biblioteca

### En Claude Code:
```bash
# Copiar el prompt y pegarlo directamente
claude "Actúa como Debugger Sherlock... [pegar traceback]"
```

### En DirectOS:
1. Ir a **Generador** → **Biblioteca de Patrones**
2. Seleccionar el pack y patrón
3. Click en "Cargar en Generador"
4. Personalizar y copiar

### Tips:
- Combina patrones: primero **Schema Detective**, luego **API Architect**
- Encadena: **Code Reviewer** → **Guardián de Calidad** → **Documentador Fantasma**
- Itera: usa **Prompt Optimizer** para mejorar tus propios prompts

---

*DirectOS v7.1 - 33 Patrones | minerOS Ecosystem | Nov 2025*
