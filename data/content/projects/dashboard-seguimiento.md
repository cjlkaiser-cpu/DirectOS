---
id: dashboard-seguimiento
name: Dashboard Seguimiento
version: v1.2
status: active
stack:
  - html
  - css
  - javascript
repo: ~/Desktop/dashboard-seguimiento
description: Dashboard interactivo para tracking de aprendizaje estilo minerOS. HTML puro + localStorage (KISS, sin frameworks).
---

# Dashboard Seguimiento v1.2

Dashboard interactivo para tracking personal de aprendizaje estilo minerOS.

## Flujo de trabajo

1. **7 Secciones principales**
   - **Periodo:** Selección de semana/sprint
   - **Resumen:** Visión general del progreso
   - **Panel RAG:** Estado visual Rojo/Ámbar/Verde
   - **Objetivos:** Metas de la semana
   - **Kit Herramientas:** Inventario de stack
   - **Kanban:** To Do → Doing → Done
   - **Cierre:** Reflexión y siguiente paso

2. **Persistencia localStorage**
   - Auto-guarda cada cambio
   - Historial de 10 semanas
   - Exportación/importación JSON
   - Sin backend necesario

3. **Kit de Herramientas**
   - Inventario visual del stack
   - Niveles: Explorando → Sólido → Dominado
   - Tracking de progreso por tecnología
   - Barra de progreso global

4. **Panel RAG**
   - Estado visual por área (Rojo/Ámbar/Verde)
   - Frontend, Backend, IA, DevOps
   - Indicadores de fortaleza

## Comandos principales

```bash
# Clonar/crear proyecto
mkdir dashboard-seguimiento
cd dashboard-seguimiento

# Inicializar git
git init
git add .
git commit -m "Dashboard Seguimiento v1.2"

# Abrir localmente
open index.html

# O usar Live Server en VS Code
# Click derecho → Open with Live Server

# Deploy a GitHub Pages
git remote add origin <repo-url>
git push -u origin main
# Activar GitHub Pages en Settings → Pages
```

## Arquitectura

```
dashboard-seguimiento/
├── index.html              # Estructura HTML5
├── styles/
│   ├── main.css            # Estilos base
│   ├── components.css      # Componentes reutilizables
│   └── dashboard.css       # Grid del dashboard
├── js/
│   ├── app.js              # Lógica principal
│   ├── storage.js          # localStorage manager
│   ├── kanban.js           # Sistema Kanban
│   └── kit.js              # Kit de Herramientas
└── assets/
    └── icons/              # SVG icons
```

### Stack técnico

- **Frontend:** HTML5 + CSS3 + JavaScript vanilla
- **Persistencia:** localStorage (navegador)
- **Estilos:** CSS Grid + Flexbox + Custom Properties
- **Deploy:** GitHub Pages (estático, gratis)
- **Filosofía:** KISS - Sin frameworks ni dependencias

## Aprendizajes clave

### Lo que funcionó bien

1. **localStorage:** Persistencia sin backend, súper simple
2. **JavaScript vanilla:** Sin frameworks = carga instantánea
3. **CSS Grid:** Layout responsive perfecto
4. **Historial 10 semanas:** Tracking a largo plazo
5. **Exportar/Importar JSON:** Backup manual fácil

### Problemas resueltos

- **Pérdida de datos:** Auto-guarda cada cambio en localStorage
- **Sincronización:** No necesaria, todo es local
- **Versionado:** Git + GitHub para backup
- **Responsive:** CSS Grid adapta a móvil automáticamente
- **Performance:** HTML estático = carga instantánea

### Features clave

**Kit de Herramientas:**
```javascript
const herramientas = {
  "Python": { nivel: "Dominado", progreso: 90 },
  "FastAPI": { nivel: "Sólido", progreso: 75 },
  "HTMX": { nivel: "Explorando", progreso: 40 }
};

// Niveles: Explorando (🌱) → Sólido (🔨) → Dominado (⭐)
```

**Panel RAG (Rojo/Ámbar/Verde):**
```javascript
const estadoAreas = {
  frontend: "verde",    // ✅ Dominado
  backend: "verde",     // ✅ Dominado
  ia: "ambar",          // ⚠️ En progreso
  devops: "ambar"       // ⚠️ En progreso
};
```

**Kanban dinámico:**
```javascript
// Drag & drop entre columnas
const tareas = {
  todo: ["Aprender Docker"],
  doing: ["Proyecto PhotoMine"],
  done: ["farmaIA v5.0"]
};
```

**Persistencia localStorage:**
```javascript
// Auto-guarda cada cambio
function guardarEstado() {
  const estado = {
    semana: semanActual,
    herramientas: herramientas,
    tareas: tareas,
    timestamp: Date.now()
  };
  localStorage.setItem('dashboard', JSON.stringify(estado));
}

// Historial de 10 semanas
function guardarHistorial() {
  let historial = JSON.parse(localStorage.getItem('historial')) || [];
  historial.push(estadoActual);
  if (historial.length > 10) historial.shift(); // Solo 10
  localStorage.setItem('historial', JSON.stringify(historial));
}
```

### Siguientes pasos

- [ ] Gráficos de evolución (Chart.js opcional)
- [ ] Comparativa semanal automática
- [ ] Exportar PDF con resumen
- [ ] PWA para uso offline
- [ ] Dark/Light mode toggle

## Métricas

- **Secciones:** 7 módulos interactivos
- **Historial:** 10 semanas tracked
- **Herramientas:** 22+ tecnologías
- **Tamaño:** ~1 MB (HTML+CSS+JS)
- **Líneas de código:** ~1,200 líneas
- **Deploy:** Gratis en GitHub Pages

## Casos de uso reales

### Tracking semanal
```
Semana 47 (Nov 18-24):
✅ Frontend: Verde (Portfolio publicado)
⚠️ Backend: Ámbar (farmaIA v5.0 en progreso)
🔴 DevOps: Rojo (Docker pendiente)

To Do:
- [ ] Aprender Docker basics

Doing:
- [⏳] farmaIA backend Node.js

Done:
- [✓] Portfolio Dibujo publicado
- [✓] Git FASE 1 completada
```

### Kit de Herramientas
```
🟢 DOMINADO (90-100%):
- Python, Flask, HTML/CSS, Git

🟡 SÓLIDO (60-89%):
- FastAPI, SQLite, Node.js, Express

🔵 EXPLORANDO (0-59%):
- Docker, HTMX, ChromaDB
```

### Exportar backup
```javascript
// En consola del navegador
const backup = localStorage.getItem('dashboard');
console.log(backup); // Copiar y pegar a archivo .json
```

## Deploy a GitHub Pages

```bash
# 1. Crear repo en GitHub
gh repo create dashboard-seguimiento --public

# 2. Push código
git add .
git commit -m "Dashboard Seguimiento v1.2"
git push -u origin main

# 3. Activar GitHub Pages
# Ir a: Settings → Pages
# Source: main branch → / (root)
# Save

# 4. URL pública:
# https://tu-usuario.github.io/dashboard-seguimiento
```

## Filosofía KISS

**¿Por qué NO usar frameworks?**

```
React/Vue/Angular:
- Build step necesario
- Dependencias pesadas (MB)
- Complejidad innecesaria para dashboard simple

HTML+CSS+JS vanilla:
- Carga instantánea
- Sin dependencias
- Debuggeable en DevTools
- Publicable directamente
```

**Principio:** Si HTML puro + localStorage resuelve el problema, ¿para qué más?

## Comparativa

| Feature | Dashboard (vanilla) | Notion | Trello |
|---------|---------------------|--------|--------|
| Gratis | ✅ | Límites | Límites |
| Offline | ✅ | ❌ | ❌ |
| Privado | ✅ 100% local | Cloud | Cloud |
| Custom | ✅ Total | Limitado | Limitado |
| Rápido | ✅ Instantáneo | Medio | Medio |

## Estructura HTML

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard Seguimiento</title>
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>
  <div class="dashboard">
    <!-- Periodo -->
    <section class="periodo">...</section>

    <!-- Resumen -->
    <section class="resumen">...</section>

    <!-- Panel RAG -->
    <section class="rag-panel">
      <div class="area verde">Frontend ✅</div>
      <div class="area ambar">IA ⚠️</div>
    </section>

    <!-- Objetivos -->
    <section class="objetivos">...</section>

    <!-- Kit Herramientas -->
    <section class="kit">
      <div class="herramienta dominado">
        <h4>Python ⭐</h4>
        <div class="progress-bar" style="width: 90%"></div>
      </div>
    </section>

    <!-- Kanban -->
    <section class="kanban">
      <div class="columna todo">...</div>
      <div class="columna doing">...</div>
      <div class="columna done">...</div>
    </section>

    <!-- Cierre -->
    <section class="cierre">...</section>
  </div>

  <script src="js/app.js"></script>
</body>
</html>
```

## Enlaces útiles

- [localStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [GitHub Pages Docs](https://pages.github.com/)
