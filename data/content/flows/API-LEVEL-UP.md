---
id: api-level-up
name: API Level Up - Hoja de Ruta
category: Backend
icon: fa-rocket
color: text-green-400
tag: Flujo
status: referencia
stack:
  - fastapi
  - python
  - pydantic
  - sqlite
  - sqlalchemy
---

# API Level Up - Hoja de Ruta

Evolución natural de una API FastAPI desde MVP hasta producción.

## Niveles de Madurez

| Nivel | Básico (MVP) | Intermedio | Avanzado |
|-------|--------------|------------|----------|
| **Datos** | JSON/Memoria | SQLite + SQLAlchemy | PostgreSQL |
| **Validación** | Manual/ninguna | Pydantic models | Validación custom |
| **Seguridad** | Abierto | API keys | JWT + OAuth |
| **Docs** | Manual | `/docs` automático | OpenAPI exportado |
| **Errores** | print() | HTTPException | Middleware global |
| **Testing** | Manual | pytest básico | CI/CD completo |

---

## Orden Recomendado de Implementación

```
1. Pydantic models    ← Casi gratis, FastAPI ya lo soporta
       ↓
2. /docs automático   ← Viene GRATIS con Pydantic
       ↓
3. SQLite             ← Cuando JSON se quede corto
       ↓
4. Auth               ← Cuando compartas con otros
```

---

## Nivel 1: Pydantic Models

### Antes (sin validación)
```python
@app.post("/api/projects")
async def create_project(data: dict):
    # ¿Qué campos tiene data? No sabemos
    # ¿Tipos correctos? No sabemos
    return {"id": 1, **data}
```

### Después (con Pydantic)
```python
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    stack: list[str] = []
    status: str = "prototype"

class ProjectResponse(BaseModel):
    id: str
    name: str
    description: str | None
    stack: list[str]
    status: str

@app.post("/api/projects", response_model=ProjectResponse)
async def create_project(project: ProjectCreate):
    # FastAPI valida automáticamente
    # Si falta 'name' → Error 422 claro
    return {"id": "new-id", **project.model_dump()}
```

### Beneficios
- Validación automática de tipos
- Errores claros para el cliente
- Autocompletado en el IDE
- Documentación auto-generada

---

## Nivel 2: Documentación Automática

FastAPI genera docs **GRATIS** si usas Pydantic:

```
http://localhost:8000/docs     → Swagger UI (interactivo)
http://localhost:8000/redoc    → ReDoc (documentación)
```

### Mejorar la documentación
```python
from fastapi import FastAPI

app = FastAPI(
    title="DirectOS API",
    description="Knowledge Base y gestión de proyectos",
    version="6.1.0"
)

@app.get("/api/projects",
         summary="Lista todos los proyectos",
         description="Retorna proyectos ordenados por estado")
async def get_projects():
    ...
```

---

## Nivel 3: SQLite + SQLAlchemy

### Cuándo migrar de JSON a SQLite
- Más de ~100 registros
- Necesitas búsquedas complejas
- Relaciones entre entidades
- Múltiples escrituras concurrentes

### Setup básico
```python
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data/directos.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(String, default="prototype")
    stack = Column(String)  # JSON string

Base.metadata.create_all(bind=engine)
```

### Dependency Injection
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/projects")
async def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
```

---

## Nivel 4: Autenticación

### Opción A: API Keys (simple)
```python
from fastapi import Header, HTTPException

API_KEYS = {"carlos-key-123", "guest-key-456"}

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app.get("/api/projects")
async def get_projects(api_key: str = Depends(verify_api_key)):
    ...
```

Cliente:
```javascript
fetch('/api/projects', {
    headers: { 'X-API-Key': 'carlos-key-123' }
})
```

### Opción B: JWT (más robusto)
```python
from fastapi.security import HTTPBearer
from jose import jwt

security = HTTPBearer()

@app.get("/api/projects")
async def get_projects(token = Depends(security)):
    payload = jwt.decode(token.credentials, SECRET_KEY)
    user_id = payload.get("sub")
    ...
```

---

## Checklist de Progreso

### MVP (Ya tienes)
- [x] GET endpoints funcionando
- [x] Datos en JSON/archivos
- [x] CORS configurado
- [x] Multi-dispositivo (0.0.0.0)

### Nivel Intermedio
- [ ] Pydantic models en todos los endpoints
- [ ] /docs funcionando
- [ ] Manejo de errores con HTTPException
- [ ] SQLite para datos principales

### Nivel Avanzado
- [ ] API keys para acceso externo
- [ ] Rate limiting
- [ ] Logging estructurado
- [ ] Tests automatizados

---

## Stack Recomendado por Nivel

| Nivel | Stack |
|-------|-------|
| MVP | FastAPI + JSON + uvicorn |
| Intermedio | + Pydantic + SQLite + SQLAlchemy |
| Avanzado | + JWT + pytest + loguru + PostgreSQL |

---

## Recursos

- [FastAPI docs](https://fastapi.tiangolo.com/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

---

*Flow creado después de Dashboard Mobile v1.2 - Nov 2025*
*"De endpoints básicos a API profesional, paso a paso"*
