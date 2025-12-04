---
id: chacona-estudio
name: Chacona Estudio
version: v1.0
status: production
stack:
  - javascript
  - html
  - css
  - indexeddb
repo: github.com/cjlkaiser-cpu/chacona-estudio
description: Web app para estudiar la Chacona BWV 1004 de Bach con tracking de progreso, grabación de audio y fotos de partitura.
---

# Chacona Estudio v1.0

Web app interactiva para el estudio sistemático de la Chacona BWV 1004 de Bach. Permite trackear el progreso por variación, grabar notas de voz, subir fotos de partituras anotadas, y exportar/importar backups.

## Origen

Extracción de datos de https://www.deviolines.com/ (64 variaciones con imágenes del manuscrito y descripciones).

## Features

- **64 variaciones** con imagen del manuscrito + descripción
- **Tracking de progreso** por variación (checkbox + fecha)
- **Notas personales** con autosave
- **Grabación de audio directa** (MediaRecorder API)
- **Subida de fotos** de partitura anotada
- **Export/Import** de backups (JSON con base64)
- **Navegación por teclado** (← →)
- **100% offline** (IndexedDB para almacenamiento)

## Arquitectura

```
chacona-estudio/
├── index.html
├── css/
│   └── styles.css
└── js/
    ├── data.js      # 64 variaciones (número, título, imagen, texto, sección)
    └── app.js       # IndexedDB + MediaRecorder + UI
```

### IndexedDB Schema (v2)

```javascript
studyData: { id, completed, completedDate, notes }
audioFiles: { id, audio (Blob) }
photoFiles: { id, photo (Blob) }
```

## Stack técnico

- **Frontend:** HTML5 + CSS3 + JavaScript vanilla
- **Storage:** IndexedDB (3 stores: studyData, audioFiles, photoFiles)
- **Audio:** MediaRecorder API (webm/mp4)
- **Backup:** JSON con base64 encoding para blobs
- **Deploy:** GitHub Pages

## Aprendizajes clave

### Lo que funcionó bien

1. **IndexedDB** para archivos grandes (supera límite 5MB de localStorage)
2. **MediaRecorder API** funciona en todos los navegadores modernos
3. **Export/Import con base64** permite portabilidad completa

### Problemas resueltos

- **Brave no cargaba**: Código del overlay ejecutándose antes de DOMContentLoaded → moverlo dentro del evento
- **Cache agresiva**: Añadir `?v=X` a los scripts para forzar recarga
- **Error handling**: Añadir null checks para cuando IndexedDB falle (modo sin persistencia)

### Siguientes pasos

- [ ] Añadir metrónomo integrado
- [ ] Comparar grabaciones entre sesiones
- [ ] Estadísticas de tiempo de estudio

## Métricas

- **Variaciones:** 64
- **Secciones:** 3 (Re menor I, Re Mayor, Re menor II)
- **Stores IndexedDB:** 3
- **Compatibilidad:** Safari, Chrome, Firefox, Brave, móvil
