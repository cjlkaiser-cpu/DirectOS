---
id: farmaia
name: farmaIA
version: v5.0
status: production
stack:
  - nodejs
  - express
  - sqlite
  - claude
  - html
  - css
repo: ~/Desktop/farmaia
description: Mi Botiquín Inteligente - Sistema completo con backend Node.js/Express seguro + SQLite + CIMA API (25K+ medicamentos).
---

# farmaIA v5.0 - "Mi Botiquín Inteligente"

De frontend simple a **sistema completo con backend seguro**.

## Flujo de trabajo

1. **Backend Node.js/Express**
   - API keys protegidas en variables de entorno
   - Rate Limiting para prevenir abuso
   - Helmet.js para seguridad headers
   - Endpoints REST para consultas y botiquín

2. **Base de datos híbrida**
   - SQLite local: 99 medicamentos + 79 interacciones
   - CIMA API: 25,300+ medicamentos oficiales AEMPS
   - Sincronización automática

3. **Mi Botiquín Inteligente (Killer Feature)**
   - Perfil de seguridad: alergias, condiciones crónicas, embarazo/lactancia
   - **Inyección automática del perfil en cada consulta**
   - Gestión de caducidad con semáforo visual (verde/amarillo/rojo)
   - Consultas contextualizadas con tu perfil

4. **Streaming SSE**
   - Respuestas en tiempo real token por token
   - Detección automática de emergencias (alerta 112)
   - UI responsiva con streaming

## Comandos principales

```bash
# Instalación
cd farmaia
npm install

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu API key de Anthropic

# Iniciar servidor backend
node backend/server.js
# Backend en http://localhost:3000

# Abrir frontend
open frontend/index.html
# O con Live Server en VS Code
```

## Arquitectura

```
farmaia/
├── backend/
│   ├── server.js           # Express server principal
│   ├── routes/
│   │   ├── api.js          # Endpoints de consultas
│   │   └── botiquin.js     # Gestión Mi Botiquín
│   ├── database/
│   │   └── farmaia.db      # SQLite local
│   └── services/
│       ├── claude.js       # Cliente Anthropic API
│       └── cima.js         # Cliente CIMA API
├── frontend/
│   ├── index.html          # UI principal
│   ├── styles/
│   │   └── main.css        # Glassmorphism + Dark mode
│   └── js/
│       ├── app.js          # Lógica principal
│       └── botiquin.js     # Gestión botiquín
└── .env                    # API keys (no subir a git)
```

### Stack técnico

- **Backend:** Node.js + Express.js
- **Base de datos:** SQLite (local) + CIMA API (remota)
- **IA:** Claude 3.5 Sonnet (Anthropic API)
- **Frontend:** HTML5 + CSS3 (Glassmorphism) + JavaScript vanilla
- **Seguridad:** Helmet.js + Rate Limiting + CORS
- **Streaming:** Server-Sent Events (SSE)

## Aprendizajes clave

### Lo que funcionó bien

1. **Node.js/Express backend:** Primera vez con backend JavaScript, muy intuitivo
2. **SQLite + API híbrido:** Combinar datos locales + oficiales
3. **Inyección automática perfil:** Cada consulta incluye contexto personal
4. **Glassmorphism:** UI profesional sin frameworks CSS
5. **Streaming SSE:** Respuestas token por token mejoran UX

### Problemas resueltos

- **API keys expuestas:** Movidas a backend con variables de entorno
- **CORS errors:** Configurado correctamente en Express
- **Rate limiting:** Evitar abuso de API de Claude
- **Caducidades medicamentos:** Semáforo visual automático
- **Consultas sin contexto:** Inyección automática de perfil

### Features clave

**Mi Botiquín Inteligente:**
```javascript
// El perfil se inyecta automáticamente en cada consulta
const perfil = {
  alergias: ["penicilina"],
  condiciones: ["hipertensión"],
  embarazo: false,
  lactancia: false
};

// Cada consulta incluye: "IMPORTANTE: Paciente con..."
```

**Detección emergencias:**
- Si Claude detecta síntomas graves → Alerta 112
- Mensajes: "mareos intensos", "dolor pecho", "dificultad respirar"

**Base de datos híbrida:**
- SQLite: Medicamentos personales rápido
- CIMA API: Catálogo oficial completo
- Fallback automático si CIMA falla

### Siguientes pasos

- [ ] Añadir historial de consultas (localStorage)
- [ ] Exportar informe de botiquín a PDF
- [ ] Notificaciones caducidad próxima
- [ ] PWA para uso offline
- [ ] Sistema de recordatorios de tomas

## Métricas

- **Medicamentos locales:** 99 en SQLite
- **Interacciones conocidas:** 79 pares
- **Medicamentos CIMA:** 25,300+ oficiales
- **Consultas IA realizadas:** 50+ con éxito
- **Líneas de código:** ~2,500 líneas
- **Tiempo respuesta:** ~2-4s por consulta

## Casos de uso reales

### Consulta con perfil
```
Usuario: "¿Puedo tomar ibuprofeno?"

farmaIA (con perfil):
"Dado que tienes hipertensión, debes tener precaución
con ibuprofeno ya que puede aumentar la presión arterial.
Consulta con tu médico antes de tomarlo."
```

### Gestión caducidades
```
Mi Botiquín:
🟢 Paracetamol - Caduca: 2026-05-12 (18 meses)
🟡 Omeprazol - Caduca: 2025-02-20 (3 meses)
🔴 Aspirina - Caduca: 2025-01-05 (¡CADUCADO!)
```

### Detección emergencia
```
Usuario: "Tengo dolor intenso en el pecho"

farmaIA:
⚠️ EMERGENCIA DETECTADA ⚠️
Llama al 112 INMEDIATAMENTE
Los síntomas descritos pueden indicar...
```

## Deploy

```bash
# Producción local
node backend/server.js

# Con PM2 (proceso continuo)
npm install -g pm2
pm2 start backend/server.js --name farmaia
pm2 save

# Ver logs
pm2 logs farmaia
```

## Aprendizajes Node.js/Express

```javascript
// Express básico
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(helmet());
app.use(cors());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 min
  max: 100 // 100 requests
});
app.use('/api/', limiter);

// Routing
app.post('/api/consulta', async (req, res) => {
  // SSE streaming
  res.setHeader('Content-Type', 'text/event-stream');
  // ...
});

app.listen(3000);
```

## Enlaces útiles

- [Express.js Docs](https://expressjs.com/)
- [Node.js Docs](https://nodejs.org/)
- [CIMA AEMPS](https://cima.aemps.es/)
- [Anthropic API](https://docs.anthropic.com/)
- [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
