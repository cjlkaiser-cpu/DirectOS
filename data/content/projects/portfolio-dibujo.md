---
id: portfolio-dibujo
name: Portfolio Dibujo
version: v1.0
status: prototype
stack:
  - html
  - css
  - alpine
  - markdown
  - python
repo: ~/Desktop/portfolio-dibujo
description: Portfolio web estático para artista digital. Galería responsive, categorías por técnica, sin JavaScript pesado.
---

# Portfolio Dibujo v1.0

Portfolio web minimalista para artista digital. Galería responsive generada desde archivos markdown.

## Flujo de trabajo

1. **Gestión de contenido**
   - Una carpeta por proyecto: `projects/retrato-ana/`
   - Cada proyecto tiene `info.md` con metadata
   - Imágenes en la misma carpeta (auto-detectadas)
   - Thumbnails generados automáticamente

2. **Generación estática**
   - Script Python lee carpetas de proyectos
   - Parse de markdown con frontmatter
   - Genera HTML estático con Jinja2
   - Optimiza imágenes (WebP + lazy loading)

3. **Interfaz**
   - Grid masonry con Alpine.js
   - Filtros por categoría (ilustración, retrato, paisaje)
   - Modal de detalle con swipe gestures
   - Dark/Light mode automático

4. **Deploy**
   - GitHub Pages (gratis)
   - Cloudflare Pages (gratis + CDN)
   - Netlify (gratis + formulario contacto)

## Comandos principales

```bash
# Instalación
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Crear nuevo proyecto
python main.py new "Retrato de Ana" --category retrato

# Generar sitio estático
python main.py build

# Preview local
python main.py serve --port 8080
open http://localhost:8080

# Deploy a GitHub Pages
python main.py deploy --github
```

## Arquitectura

```
portfolio-dibujo/
├── main.py                  # CLI generator
├── modules/
│   ├── parser.py            # Markdown parser
│   ├── image_optimizer.py   # WebP + thumbnails
│   └── generator.py         # Static site gen
├── templates/
│   ├── base.html            # Layout base
│   ├── index.html           # Home + galería
│   ├── project.html         # Detalle proyecto
│   └── about.html           # Sobre mí
├── projects/
│   ├── retrato-ana/
│   │   ├── info.md          # Metadata
│   │   ├── imagen-1.jpg
│   │   └── imagen-2.jpg
│   └── paisaje-bosque/
│       ├── info.md
│       └── imagen-1.jpg
└── output/
    └── site/                # HTML generado
```

### Formato info.md

```yaml
---
title: Retrato de Ana
date: 2024-11-15
category: retrato
medium: digital
tools: [Procreate, iPad Pro]
duration: 8 horas
featured: true
---

# Retrato de Ana

Comisión para cliente. Estilo semi-realista con énfasis en expresión facial.

## Proceso

1. Boceto inicial en grafito digital
2. Lineart con pincel personalizado
3. Color base + sombras
4. Detalles y luces

## Aprendizajes

- Mejoré el rendering de piel
- Nueva técnica para ojos brillantes
- Workflow más rápido (de 12h a 8h)
```

### Stack técnico

- **Generator:** Python 3.11 + Jinja2
- **Frontend:** HTML5 + TailwindCSS + Alpine.js
- **Imágenes:** Pillow para resize + WebP
- **Deploy:** GitHub Actions para build automático

## Aprendizajes clave

### Lo que funcionó bien

1. **Markdown para proyectos:** No requiere CMS ni base de datos
2. **Generación estática:** Carga instantánea, SEO perfecto
3. **WebP + lazy loading:** Sitio liviano (5MB → 1.2MB)
4. **Alpine.js minimal:** Interactividad sin webpack

### Problemas resueltos

- **Imágenes pesadas:** Compresión WebP + fallback JPG
- **Grid inconsistente:** Masonry layout con CSS Grid
- **Modal scroll:** Lock body scroll al abrir modal
- **SEO para galerías:** Meta tags dinámicos por proyecto

### Optimizaciones

```python
# Generación de thumbnails
def create_thumbnail(image_path, size=(400, 400)):
    img = Image.open(image_path)
    img.thumbnail(size, Image.LANCZOS)

    # Exportar WebP con calidad 85
    webp_path = image_path.replace('.jpg', '.webp')
    img.save(webp_path, 'WEBP', quality=85)

    return webp_path

# Lazy loading automático
<img src="thumbnail.webp"
     data-src="full.webp"
     loading="lazy"
     class="lazy-image">
```

### Siguientes pasos

- [ ] Blog integrado (markdown posts)
- [ ] Sistema de comisiones (formulario + pricing)
- [ ] Analytics con Plausible (privacy-friendly)
- [ ] Multi-idioma (ES/EN)

## Métricas

- **Proyectos publicados:** 24 trabajos
- **Categorías:** 4 (retrato, paisaje, ilustración, concept art)
- **Tamaño del sitio:** 1.2 MB (optimizado)
- **Lighthouse Score:** 98/100
- **Tiempo de build:** ~5 segundos

## Casos de uso

### Añadir proyecto nuevo
```bash
# 1. Crear carpeta
mkdir projects/retrato-nuevo

# 2. Copiar imágenes
cp ~/Desktop/retrato/*.jpg projects/retrato-nuevo/

# 3. Crear info.md
cat > projects/retrato-nuevo/info.md << EOF
---
title: Retrato Nuevo
date: 2024-11-25
category: retrato
---

Descripción del proyecto...
EOF

# 4. Regenerar sitio
python main.py build
```

### Actualizar estilos globales
```bash
# Editar templates/base.html
vim templates/base.html

# Rebuild
python main.py build

# Preview
python main.py serve
```

### Deploy a producción
```bash
# Build optimizado
python main.py build --optimize

# Deploy a GitHub Pages
python main.py deploy --github

# O deploy a Netlify
netlify deploy --prod --dir output/site
```

## Comparativa generadores

| Feature | Custom Python | Hugo | Jekyll | Next.js |
|---------|--------------|------|--------|---------|
| Setup | ✅ Simple | Medium | Medium | Complex |
| Speed | ✅ 5s | 1s | 30s | 10s |
| Control | ✅ Total | Limitado | Limitado | Medio |
| Markdown | ✅ | ✅ | ✅ | Plugin |
| Images | ✅ Custom | Plugin | Plugin | ✅ |

## Estructura HTML generada

```html
<!-- output/site/index.html -->
<!DOCTYPE html>
<html>
<head>
  <meta name="description" content="Portfolio de [Artista]">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav>...</nav>

  <main x-data="gallery()">
    <div class="filters">
      <button @click="filter='all'">Todos</button>
      <button @click="filter='retrato'">Retratos</button>
    </div>

    <div class="grid masonry">
      <template x-for="project in filteredProjects">
        <div class="project-card">
          <img :src="project.thumbnail" loading="lazy">
          <h3 x-text="project.title"></h3>
        </div>
      </template>
    </div>
  </main>
</body>
</html>
```

## GitHub Actions para auto-deploy

```yaml
# .github/workflows/deploy.yml
name: Deploy Portfolio

on:
  push:
    branches: [main]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Build site
        run: python main.py build --optimize

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output/site
```

## SEO y Analytics

```html
<!-- Meta tags por proyecto -->
<meta name="description" content="{{ project.description }}">
<meta property="og:title" content="{{ project.title }}">
<meta property="og:image" content="{{ project.featured_image }}">
<meta property="og:type" content="article">

<!-- Schema.org para Google -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VisualArtwork",
  "name": "{{ project.title }}",
  "image": "{{ project.featured_image }}",
  "creator": {
    "@type": "Person",
    "name": "{{ artist.name }}"
  }
}
</script>
```

## Enlaces útiles

- [Alpine.js](https://alpinejs.dev/)
- [TailwindCSS](https://tailwindcss.com/)
- [WebP Docs](https://developers.google.com/speed/webp)
- [GitHub Pages](https://pages.github.com/)
