---
id: flask
name: Flask
category: Backend
icon: fa-flask
color: text-gray-300
tag: Web Framework
status: learning
level: working
next: Flask Blueprints
---

# Flask

Microframework web para Python. Simple y extensible.

## Por qué en minerOS

Ideal para prototipos rápidos y APIs simples. Menos estructura que FastAPI pero más flexible.

## Casos de uso

- APIs REST simples
- Dashboards web
- Prototipos rápidos
- Aplicaciones de validación

## Código ejemplo

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    return jsonify({'result': data.get('text', '').upper()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Proyectos que lo usan

- BioMistral Validation (chat validador)
