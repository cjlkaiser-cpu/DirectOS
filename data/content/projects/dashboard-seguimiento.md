---
id: dashboard-seguimiento
name: Dashboard Seguimiento
version: v1.2
status: active
stack:
  - python
  - sqlite
  - markdown
  - html
  - chart.js
repo: ~/Desktop/dashboard-seguimiento
description: Dashboard personal para trackear aprendizaje técnico. Visualiza progreso en herramientas, proyectos y objetivos desde markdown.
---

# Dashboard Seguimiento v1.2

Dashboard personal para trackear aprendizaje técnico. Lee archivos markdown con frontmatter y genera visualizaciones interactivas.

## Flujo de trabajo

1. **Fuente de datos**
   - Lee `knowledge-base.md` con herramientas y nivel
   - Lee `MAPA-APRENDIZAJE.md` con objetivos y progreso
   - Lee `data/content/projects/*.md` para métricas de proyectos
   - Parse de YAML frontmatter + contenido markdown

2. **Procesamiento**
   - Extrae niveles de herramientas (learning/solid/expert)
   - Calcula tiempo invertido en proyectos
   - Agrupa por categorías (Frontend, Backend, IA, DevOps)
   - Genera estadísticas de progreso

3. **Visualización**
   - Gráfico radar: nivel por categoría técnica
   - Timeline: evolución temporal de proyectos
   - Heatmap: intensidad de uso por herramienta
   - Cards KPI: métricas clave (horas, proyectos, herramientas)

4. **Exportación**
   - PNG de gráficos para portfolio
   - JSON con datos para integración
   - Markdown report mensual

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Generar dashboard
python main.py --generate

# Modo servidor live
python main.py --serve --port 8080

# Exportar PNG
python main.py --export dashboard.png

# Generar reporte mensual
python main.py --report --month 2024-11
```

## Arquitectura

```
dashboard-seguimiento/
├── main.py                  # Entry point
├── modules/
│   ├── parser.py            # Markdown + frontmatter parser
│   ├── analyzer.py          # Cálculo de métricas
│   ├── visualizer.py        # Chart.js wrapper
│   └── exporter.py          # PNG/JSON export
├── templates/
│   └── dashboard.html       # Template HTML
├── output/
│   ├── dashboard.html       # Dashboard generado
│   ├── report.md            # Reporte markdown
│   └── exports/             # PNGs exportados
└── data/
    ├── knowledge-base.md    # Herramientas y niveles
    ├── MAPA-APRENDIZAJE.md  # Objetivos y progreso
    └── content/
        └── projects/        # Proyectos documentados
```

### Stack técnico

- **Parser:** python-frontmatter + mistune
- **Visualización:** Chart.js + Alpine.js
- **Backend:** Python 3.11 + Jinja2
- **Data:** SQLite para histórico (opcional)
- **Export:** Playwright para screenshots PNG

## Aprendizajes clave

### Lo que funcionó bien

1. **Markdown como base de datos:** No requiere input manual adicional
2. **Frontmatter estructurado:** Fácil parsear con python-frontmatter
3. **Chart.js theming:** Dark mode profesional con paleta custom
4. **Histórico automático:** Git commits = timeline de evolución

### Problemas resueltos

- **Datos inconsistentes:** Validación de frontmatter con Pydantic
- **Gráficos vacíos:** Valores default para herramientas sin nivel
- **Export PNG borroso:** Aumentar DPR a 2x para Retina
- **Fechas mixtas:** Normalizar a ISO 8601

### Métricas calculadas

```python
# Ejemplos de métricas derivadas
total_tools = len(knowledge_base.tools)
solid_tools = len([t for t in tools if t.level == 'solid'])
progress_pct = (solid_tools / total_tools) * 100

# Tiempo invertido por proyecto
project_hours = sum([p.hours for p in projects])

# Distribución por categoría
category_counts = Counter([t.category for t in tools])
```

### Siguientes pasos

- [ ] Integración con GitHub (commits, stars)
- [ ] Scraping de Kaggle/HackerRank para badges
- [ ] Notificaciones semanales de progreso
- [ ] Comparativa con objetivos predefinidos

## Métricas actuales

- **Herramientas trackeadas:** 28 tools
- **Proyectos documentados:** 6 proyectos
- **Horas invertidas:** ~240 horas (estimado)
- **Nivel promedio:** Solid (65% del stack)
- **Categorías dominadas:** Backend (90%), Frontend (75%)

## Uso típico

### Generar dashboard después de actualizar conocimiento
```bash
# 1. Editar knowledge-base.md (cambiar niveles)
vim knowledge-base.md

# 2. Regenerar dashboard
python main.py --generate

# 3. Abrir en navegador
open output/dashboard.html
```

### Exportar para portfolio
```bash
# Generar PNG de alta calidad
python main.py --export portfolio-tech.png --dpr 2

# Subir a GitHub README
cp output/portfolio-tech.png ~/github/profile/
```

### Reporte mensual automático
```bash
# Cron job mensual
0 0 1 * * cd ~/dashboard-seguimiento && python main.py --report --month $(date +%Y-%m) --email
```

## Visualizaciones disponibles

### 1. Radar Chart - Nivel por Categoría
```javascript
{
  labels: ['Frontend', 'Backend', 'IA', 'DevOps', 'Data'],
  datasets: [{
    label: 'Nivel actual',
    data: [75, 90, 70, 60, 65]
  }]
}
```

### 2. Timeline - Proyectos por fecha
```javascript
{
  type: 'line',
  data: {
    labels: ['Ene', 'Feb', 'Mar', 'Abr'],
    datasets: [{
      label: 'Proyectos completados',
      data: [1, 1, 2, 2]
    }]
  }
}
```

### 3. Heatmap - Uso de herramientas
```html
<div class="heatmap">
  <div class="cell" data-value="10">Python</div>
  <div class="cell" data-value="8">FastAPI</div>
  <div class="cell" data-value="5">HTMX</div>
</div>
```

## Integración con DirectOS

```yaml
# En DirectOS, endpoint para stats
GET /api/stats/learning
→ Returns:
  - tools_count: 28
  - solid_count: 18
  - learning_count: 10
  - projects_count: 6
  - total_hours: 240
```

## Deploy

```bash
# GitHub Pages (estático)
python main.py --generate --output docs/
git add docs/ && git commit -m "Update dashboard"
git push

# Observable (notebooks)
python main.py --export observable.json
# Importar en observablehq.com
```

## Enlaces útiles

- [Chart.js Docs](https://www.chartjs.org/)
- [python-frontmatter](https://python-frontmatter.readthedocs.io/)
- [Playwright](https://playwright.dev/python/)
