# DirectOS v5.3

> Arquitecto visual de pipelines para el ecosistema minerOS

## Qué es

DirectOS es una herramienta web de archivo único que permite diseñar arquitecturas de software visualmente, validar dependencias entre herramientas, y generar prompts estructurados para Claude Code.

## El problema que resuelve

```
ANTES                          DESPUÉS
──────                         ───────
Planificas en tu cabeza   →    Planificas visualmente
Escribes prompt desde 0   →    Generas desde diagrama
Olvidas dependencias      →    Sistema valida (Whisper→FFmpeg)
Claude Code sin contexto  →    Recibe arquitectura completa
```

## Posición en el Workflow minerOS

```
1. ENTENDER    → Claude navegador
2. PLANIFICAR  → Claude navegador
3. DISEÑAR     → DirectOS ← AQUÍ
4. CONSTRUIR   → Claude Code
5. PROBAR      → Terminal
6. EVALUAR     → ¿Aporta valor?
7. DOCUMENTAR  → Knowledge base
```

## Funcionalidades

### Arquitecto Pro
- Drag & drop de herramientas al canvas
- Validación de dependencias (ej: "Whisper necesita FFmpeg")
- Estimación de complejidad
- Compilar a prompt estructurado
- Guardar/cargar arquitecturas (localStorage)
- Exportar diagrama a PNG

### Flujos Tácticos
- Diagrama interactivo del pipeline multimedia
- Click en nodos para ver detalles y código
- Saltar directamente al Generador con contexto

### Generador de Prompts
- Seleccionar rol (Arquitecto, Ingeniero IA, etc.)
- Definir objetivo
- Seleccionar stack
- Generar prompt formateado para LLMs

### Glosario
- Catálogo de herramientas con tips
- Categorizado: Frontend, Backend, IA, Storage, Process

## Stack técnico

- HTML5 único archivo (~475 líneas)
- Tailwind CSS (CDN)
- JavaScript vanilla
- html2canvas (exportación PNG)
- Font Awesome (iconos)
- localStorage (persistencia)

## Uso

```bash
# Opción 1: Abrir directamente
open index.html

# Opción 2: Servidor local (para desarrollo)
python3 -m http.server 8080
# Abrir http://localhost:8080
```

## Estructura

```
DirectOS/
├── index.html      ← aplicación principal
├── README.md       ← este archivo
└── versions/       ← histórico de versiones
    ├── v1-directoOs.html
    ├── v2-director.html
    ├── v4.2-director.html
    ├── v4.4-DirecOS.html
    ├── v5.3-DirectOS.html
    └── proto-*.html (prototipos)
```

## Herramientas incluidas

| Herramienta | Categoría | Tag |
|-------------|-----------|-----|
| HTML5 | Frontend | Estructura |
| Tailwind | Frontend | Estilos |
| HTMX | Frontend | Interactividad |
| FastAPI | Backend | API Server |
| Python | Backend | Lenguaje Core |
| Loguru | Backend | Logging |
| OpenCV | Process | Visión Artificial |
| FFmpeg | Process | Motor Multimedia |
| CLIP | IA Model | Embeddings |
| Whisper | IA Model | Speech-to-Text |
| ChromaDB | Storage | Vector DB |
| SQLite | Storage | Relacional |

## Filosofía

- **KISS**: Un archivo, sin dependencias de build
- **Local-first**: Todo en el navegador
- **Modular**: Fácil de extender
- **minerOS style**: Herramienta que aporta valor real

---

Parte del ecosistema **minerOS** | Creado por Carlos | Nov 2025
