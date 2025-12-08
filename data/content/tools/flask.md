---
id: flask
name: Flask
category: Backend
icon: fa-flask
color: text-gray-300
tag: Web Framework
status: used
level: solid
next: Flask Blueprints, Flask-Login
---

# Flask

Microframework web para Python. Simple y extensible.

## Por qué en minerOS

Ideal para prototipos rápidos y APIs simples. Menos estructura que FastAPI pero más flexible. Con Jinja2 permite crear dashboards completos.

## Casos de uso

- APIs REST simples
- Dashboards web con Jinja2
- Sistemas de gestion
- Prototipos rápidos
- Aplicaciones de validación

## Código ejemplo

```python
from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('data.db')
    stats = conn.execute('SELECT COUNT(*) FROM items').fetchone()[0]
    return render_template('dashboard.html', total=stats)

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    return jsonify({'result': data.get('text', '').upper()})

if __name__ == '__main__':
    # host='127.0.0.1' evita error 403 en algunos navegadores
    app.run(host='127.0.0.1', debug=True, port=5000)
```

## Tips aprendidos

- Usar `host='127.0.0.1'` en lugar de `localhost` para evitar HTTP 403
- `use_reloader=False` previene doble ejecucion en debug
- Jinja2 con `{{ variable|default('N/A') }}` para valores nulos

## Proyectos que lo usan

- BioMistral Validation (chat validador)
- Factoria Demo (sistema gestion escuela con 8 templates Jinja2)
