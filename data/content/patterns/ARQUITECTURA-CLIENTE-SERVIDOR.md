---
id: arquitectura-cliente-servidor
name: Arquitectura Cliente-Servidor Local
category: Arquitectura
icon: fa-network-wired
color: text-blue-400
tag: Sistema
status: dominado
---

# Arquitectura Cliente-Servidor Local

Patrón para crear sistemas donde múltiples dispositivos consumen una API central en tu red local.

## Problema que resuelve

Apps aisladas con datos duplicados en cada dispositivo vs. una fuente de verdad accesible desde cualquier lugar.

## La Arquitectura en 3 Capas

```
┌─────────────────────────────────────────────────────────┐
│                    CAPA 1: CLIENTES                     │
│         (Cualquier dispositivo con navegador)           │
├─────────────────────────────────────────────────────────┤
│   📱 iPhone           💻 Mac            🖥️ iPad        │
│   192.168.x.x:8081    localhost:8081    misma red      │
│                                                         │
│   Solo HTML/CSS/JS - Sin lógica de negocio             │
│   LocalStorage local - Fetch para pedir datos          │
└────────────────────────┬────────────────────────────────┘
                         │  HTTP (JSON)
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    CAPA 2: API                          │
│              FastAPI Python (el servidor)               │
├─────────────────────────────────────────────────────────┤
│   UN SOLO SERVIDOR = UNA FUENTE DE VERDAD              │
│                                                         │
│   GET  /api/items     → Dame la lista                  │
│   GET  /api/items/42  → Dame el item 42                │
│   POST /api/items     → Guarda este nuevo              │
│                                                         │
│   Escucha en: 0.0.0.0:8000 (todas las IPs)            │
└────────────────────────┬────────────────────────────────┘
                         │  Lee/Escribe
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    CAPA 3: DATOS                        │
│           Archivos Markdown / SQLite / JSON             │
└─────────────────────────────────────────────────────────┘
```

## Las 3 Ideas Clave

### 1. Separación Cliente ↔ Servidor

```
ANTES (monolítico):           AHORA (separado):
┌──────────────┐              ┌────────┐      ┌────────┐
│ Todo junto   │              │Cliente │ HTTP │Servidor│
│ HTML+JS+Data │              │(tonto) │◀────▶│(listo) │
└──────────────┘              └────────┘      └────────┘
Solo ESE navegador            CUALQUIER dispositivo
```

### 2. `0.0.0.0` = "Escucho a todos"

```bash
# Solo tu Mac puede conectar
uvicorn main:app --host 127.0.0.1 --port 8000

# Cualquier dispositivo en tu red puede conectar
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. REST = Contrato Universal

| Acción | Método | URL | Significado |
|--------|--------|-----|-------------|
| Leer todos | GET | `/api/items` | Dame la lista |
| Leer uno | GET | `/api/items/42` | Dame el 42 |
| Crear | POST | `/api/items` | Guarda este |
| Actualizar | PUT | `/api/items/42` | Actualiza el 42 |
| Borrar | DELETE | `/api/items/42` | Elimina el 42 |

## Flujo Completo (ejemplo)

```
1. 📱 iPhone abre → 192.168.0.15:8081
   └── Carga index.html (estático)

2. 📱 JavaScript ejecuta:
   └── fetch('http://192.168.0.15:8000/api/projects')

3. 🌐 Petición viaja: iPhone → Router → Mac

4. 🖥️ FastAPI recibe:
   └── Lee datos → Devuelve JSON

5. 📱 JavaScript recibe JSON:
   └── Pinta en pantalla
```

## Código Ejemplo

### Servidor (FastAPI)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir conexiones desde otros orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/items")
async def get_items():
    return [{"id": 1, "name": "Item 1"}]

# Arrancar: uvicorn main:app --host 0.0.0.0 --port 8000
```

### Cliente (JavaScript)

```javascript
// Auto-detectar IP del servidor
const API_HOST = window.location.hostname === 'localhost'
  ? 'localhost'
  : window.location.hostname;

const API_URL = `http://${API_HOST}:8000`;

// Pedir datos
async function fetchItems() {
  const response = await fetch(`${API_URL}/api/items`);
  const items = await response.json();
  renderItems(items);
}
```

## Aplicaciones del Patrón

```
PhotoMine API:
GET  /api/photos       → Lista de fotos
POST /api/photos/search → Búsqueda semántica

DocMine API:
GET  /api/documents    → Lista de documentos
POST /api/documents/analyze → Analizar PDF

Dashboard Mobile:
GET  /api/projects     → Proyectos
GET  /api/tools        → Herramientas
```

## Seguridad

| Contexto | Host | Riesgo |
|----------|------|--------|
| Casa | `0.0.0.0` | Bajo (red privada) |
| WiFi público | `localhost` | Usa solo localhost |
| Internet | ngrok/tunnel | Expone temporalmente |

## Stack Técnico

- **Servidor**: FastAPI + Uvicorn (Python)
- **Cliente**: HTML + Vanilla JS + Fetch API
- **Datos**: SQLite / JSON / Markdown
- **Red**: HTTP sobre WiFi local

## Ventajas vs Apps Aisladas

| Antes | Ahora |
|-------|-------|
| Apps aisladas | Sistema conectado |
| Datos duplicados | Una fuente de verdad |
| Solo donde lo abres | Desde cualquier sitio |
| Código mezclado | Responsabilidades separadas |

---

*Patrón aprendido con Dashboard Mobile minerOS v1.2 - Nov 2025*
