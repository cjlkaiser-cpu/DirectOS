---
id: giga-estudio
name: Giga Estudio
version: v1.0
status: production
stack:
  - javascript
  - indexeddb
  - mediarecorder
repo: https://github.com/cjlkaiser-cpu/giga-estudio
description: Web app para estudiar la Giga BWV 1004 de Bach con secciones progresivas.
---

# Giga Estudio v1.0

Web app para el estudio sistematico de la Giga de la Partita No. 2 en Re menor (BWV 1004) de J.S. Bach.

## Flujo de trabajo

1. Navegar por secciones progresivas del movimiento
2. Ver partitura/manuscrito de cada seccion
3. Grabar interpretacion personal con MediaRecorder
4. Guardar grabaciones en IndexedDB local
5. Trackear progreso (X/10 secciones completadas)
6. Export/Import datos para backup

## Comandos principales

```bash
# Abrir en navegador
open https://cjlkaiser-cpu.github.io/giga-estudio/

# Clonar repo
git clone https://github.com/cjlkaiser-cpu/giga-estudio
```

## Arquitectura

```
giga-estudio/
├── index.html            # App principal
├── styles.css            # Estilos
├── app.js                # Logica + IndexedDB
└── assets/
    └── secciones/        # Imagenes partitura
```

### Stack tecnico

- **Frontend:** HTML5 + CSS3 + JavaScript vanilla
- **Audio:** MediaRecorder API (grabacion)
- **Persistencia:** IndexedDB v2 (local, sin servidor)
- **Export:** Base64 JSON (backup completo)

## Aprendizajes clave

### Lo que funciono bien

1. Patron reutilizado de Chacona Estudio (copy-paste + adaptar)
2. IndexedDB v2 para upgrades sin perder datos
3. Secciones progresivas mantienen motivacion

### Problemas resueltos

- Upgrade IndexedDB sin romper datos existentes
- Export base64 para grabaciones grandes

## Metricas

- **Secciones:** 10 divisiones del movimiento
- **Progreso visual:** Barra + contador
- **Offline:** 100% funcional sin internet
