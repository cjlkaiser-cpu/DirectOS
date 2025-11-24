---
id: pytest
name: Pytest
category: DevOps
icon: fa-vial
color: text-green-400
tag: Testing
status: new
level: exploring
next: TDD con pytest
---

# Pytest

Framework de testing para Python. Simple pero potente.

## Por qué en minerOS

Escribe tests una vez, ejecútalos mil veces. Detecta bugs antes de que lleguen a producción.

## Casos de uso

- Tests unitarios
- Tests de integración
- Mocks y fixtures

## Código ejemplo

```python
def test_suma():
    assert suma(2, 2) == 4

def test_api(client):
    response = client.get('/health')
    assert response.status_code == 200
```

## Proyectos que lo usan

- DirectOS v8.0 (planeado - cobertura 80%+)
- farmaIA v6.0 (futuro - tests de interacciones)
