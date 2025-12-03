---
id: dashboard-mobile-mineros
name: minerOS Dashboard Mobile
version: v1.0
status: production
stack:
  - html
  - css
  - javascript
repo: https://github.com/cjlkaiser-cpu/dashboard-mobile-mineros
description: Dashboard PWA móvil para consulta rápida de proyectos y capturas de ideas. Mobile-first, offline-capable, un solo archivo HTML.
---

# minerOS Dashboard Mobile v1.0

Dashboard PWA móvil para consulta rápida de proyectos y capturas de ideas. Diseñado mobile-first siguiendo filosofía KISS.

## Flujo de trabajo

1. **Consulta de proyectos**: Vista filtrable por estado (production/prototype/archived)
2. **Capturas rápidas**: Ideas, dudas, bugs, TODOs con prioridad y markdown
3. **Timer de sesiones**: Check-in de trabajo con racha de actividad
4. **Sync con DirectOS**: Conexión opcional con API localhost:8000

## Comandos principales

```bash
# Abrir directamente
open index.html

# Servidor local (para PWA)
cd ~/Desktop/dashboard-mobile-mineros
python3 -m http.server 8080

# Acceder desde móvil
# http://TU_IP:8080
```

## Arquitectura

```
dashboard-mobile-mineros/
├── index.html          # App completa (HTML+CSS+JS)
├── manifest.json       # Config PWA
├── sw.js              # Service Worker (offline)
├── MEJORAS.md         # Historial desarrollo
├── README.md          # Documentación
└── icons/
    ├── icon.svg       # Icono base
    └── generate-icons.html
```

### Stack técnico

- **Frontend:** HTML5 + CSS3 + JavaScript ES6+ (vanilla)
- **Persistencia:** LocalStorage
- **PWA:** Service Worker + Web Manifest
- **API:** Fetch a DirectOS (opcional)

## Aprendizajes clave

### Lo que funcionó bien

1. **Un solo archivo HTML**: KISS máximo, fácil de mantener y debuggear
2. **Mobile-first CSS**: Variables CSS + flexbox/grid responsive
3. **Service Worker cache-first**: Offline funcional después de primera visita
4. **Touch events nativos**: Swipe to delete sin librerías
5. **visualViewport API**: Detectar teclado virtual para "zen mode"
6. **LocalStorage como fuente de verdad**: Sin backend, sin complicaciones

### Problemas resueltos

- **XSS en innerHTML**: Función `escapeHTML()` antes de renderizar
- **Teclado virtual oculta inputs**: visualViewport API + scroll automático
- **PWA en iOS**: Meta tags específicos apple-mobile-web-app-*
- **Iconos PWA**: Generador HTML con canvas para todos los tamaños

### Técnicas implementadas

- **Swipe to delete**: touchstart/touchmove/touchend con transform
- **Markdown básico**: Regex seguro (post-sanitización)
- **Haptic feedback**: navigator.vibrate() en acciones clave
- **Stale-while-revalidate**: Cache primero, actualiza en background

## Fases de desarrollo

| Fase | Contenido |
|------|-----------|
| 1 | Seguridad XSS + Backup JSON + Filtros |
| 2 | Timer sesiones + Actividad real + Racha |
| 3 | Swipe + Zen mode + Haptic feedback |
| 4 | Markdown + Selector proyecto + Prioridades |
| 5 | PWA instalable + Service Worker + Offline |
| 6 | Conexión API DirectOS |

## Próximas mejoras (v1.1)

- Heatmap actividad estilo GitHub
- Smart Pasting (detectar URLs)
- Búsqueda rápida

## Métricas

- **Líneas de código:** ~2500 (un solo archivo)
- **Dependencias externas:** 0
- **Tamaño total:** <100KB
- **Tiempo de desarrollo:** 1 sesión
- **Fases completadas:** 6/6
