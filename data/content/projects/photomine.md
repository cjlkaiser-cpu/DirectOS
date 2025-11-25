---
id: photomine
name: PhotoMine
version: v1.4
status: production
stack:
  - python
  - clip
  - sqlite
  - opencv
  - watchdog
repo: https://github.com/yourusername/photomine
description: Sistema de organización de fotos para localizadores de cine/TV con IA (CLIP) + Dashboard Web + Sistema de Validación Interactiva.
---

# PhotoMine v1.4

Sistema completo de análisis y organización de fotos para localizadores de cine/TV con IA (CLIP) + Dashboard Web + Sistema de Validación Interactiva.

## Flujo de trabajo

1. **Ingesta y análisis**
   - Watchdog monitorea carpetas de fotos
   - Extracción de metadatos EXIF (GPS, fecha, cámara)
   - CLIP genera embeddings visuales + tags automáticos
   - Hash perceptual para detectar duplicados

2. **Base de datos**
   - SQLite con 12 tablas relacionadas
   - FTS5 para búsqueda full-text en tags
   - Sistema de validación con estados (pending/validated/rejected)
   - Notas de producción con categorías

3. **Dashboard Web**
   - Galería con filtros avanzados
   - Mapa interactivo de localizaciones GPS
   - Sistema de validación interactiva
   - Renombrado inteligente batch

4. **Búsqueda semántica**
   - Query en lenguaje natural ("atardecer en la playa")
   - CLIP busca por similitud visual
   - Ranking por relevancia

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Procesar carpeta de fotos (primera vez)
python main.py --input ~/Desktop/Fotos --recursive

# Modo incremental (solo nuevas)
python main.py --input ~/Desktop/Fotos --incremental

# Dashboard web
python web_app.py
open http://localhost:5000

# Búsqueda desde CLI
python main.py --search "playa atardecer" --limit 10
```

## Arquitectura

```
photomine/
├── main.py                  # CLI procesador
├── web_app.py              # Dashboard Flask
├── modules/
│   ├── database.py         # SQLite + 12 tablas
│   ├── ai_analyzer.py      # CLIP embeddings
│   ├── metadata_extractor.py  # EXIF parser
│   ├── search.py           # Semantic search
│   └── renaming_engine.py  # Smart rename
├── templates/
│   ├── base.html           # Layout base
│   ├── index.html          # Dashboard
│   ├── search.html         # Búsqueda
│   ├── validate.html       # Validación interactiva
│   ├── gallery.html        # Galería filtrable
│   ├── map.html            # Mapa GPS
│   └── photo_details.html  # Detalle foto
└── data/
    └── photomine.db        # Base de datos
```

### Stack técnico

- **IA:** OpenAI CLIP (ViT-B/32) optimizado para Apple Silicon (MPS)
- **Base de datos:** SQLite con FTS5 y extensiones JSON
- **Backend:** Python 3.11 + Flask
- **Frontend:** HTML5 + TailwindCSS + Alpine.js
- **Metadatos:** Pillow + piexif
- **Monitoreo:** watchdog para detección automática

## Aprendizajes clave

### Lo que funcionó bien

1. **CLIP local en MPS:** Análisis de 1,000 fotos en 3 minutos (Apple Silicon)
2. **Hash perceptual:** Detectó 247 duplicados en biblioteca de 10,000 fotos
3. **Validación interactiva:** Reducir falsos positivos del 40% al 8%
4. **Renombrado batch:** Exportar 500 fotos organizadas en 30 segundos

### Problemas resueltos

- **EXIF corrupto:** Try/except robusto + valores default
- **GPS en múltiples formatos:** Normalización a decimal degrees
- **Fotos sin fecha:** Usar mtime del archivo como fallback
- **Memoria con 10k fotos:** Procesamiento en batches de 100

### Mejoras IA implementadas

- **Análisis en dos pasadas:** Primera pasada rápida + segunda con contexto
- **Sistema de coherencia:** Detecta si tags son consistentes entre fotos similares
- **Confidencia mínima:** Filtrar tags con score < 0.3
- **Tags contextuales:** Añadir "hora_del_dia", "clima", "ambiente"

### Siguientes pasos

- [ ] OCR para detectar texto en fotos (letreros, señales)
- [ ] Clustering automático por similaridad visual
- [ ] Exportación a formato Notion/Airtable
- [ ] Mobile app para validación on-the-go

## Métricas

- **Fotos procesadas:** 12,456 imágenes
- **Tags únicos:** 892 conceptos detectados
- **Localizaciones:** 438 coordenadas GPS únicas
- **Duplicados encontrados:** 247 pares
- **Líneas de código:** 3,214 líneas Python

## Casos de uso reales

### Localizador de cine
```python
# Buscar exteriores de día con arquitectura moderna
python main.py --search "modern building exterior daylight" --limit 20

# Filtrar por GPS (radio 5km desde punto)
python main.py --geo 41.3851,2.1734 --radius 5 --category "exterior"
```

### Organización familiar
```python
# Encontrar fotos de vacaciones en playa
python main.py --search "beach sunset family" --year 2024

# Agrupar por fecha y renombrar
python main.py --batch-rename --pattern "{date}_{location}_{index}"
```

## Deploy

```bash
# Systemd service para procesamiento automático
sudo cp scripts/photomine.service /etc/systemd/system/
sudo systemctl enable photomine
sudo systemctl start photomine

# Nginx reverse proxy para dashboard
sudo cp scripts/nginx.conf /etc/nginx/sites-available/photomine
```

## Enlaces útiles

- [CLIP Paper](https://arxiv.org/abs/2103.00020)
- [Apple Silicon ML](https://developer.apple.com/metal/pytorch/)
- [EXIF Spec](https://www.exif.org/)
