# DirectOS v9.0 - Agent Mode Tutorial

> Guía práctica para automatizar tareas con Agent Mode

## ¿Qué es Agent Mode?

Agent Mode convierte DirectOS de una herramienta de **diseño** de pipelines en un **agente autónomo** que ejecuta tareas automáticamente.

---

## Componentes

| Componente | Función |
|------------|---------|
| **Executor** | Ejecuta pipelines diseñados en el canvas |
| **Watchdog** | Detecta archivos nuevos en carpetas |
| **Scheduler** | Programa tareas (cron o intervalos) |
| **Notifier** | Envía alertas de macOS cuando terminan procesos |

---

## Casos de Uso

### 1. Procesar PDFs automáticamente

**Escenario**: Cada vez que descargas un PDF, extraer texto y guardarlo.

**Configuración**:
1. Ir a **Agent Mode**
2. Crear Watch:
   - Nombre: `PDFs Descargas`
   - Directorio: `~/Downloads`
   - Patrones: `*.pdf`
3. Iniciar Watchdog
4. Descargar un PDF → Se procesa automáticamente

---

### 2. Transcribir audio con Whisper

**Escenario**: Detectar archivos de audio y transcribirlos.

**Configuración**:
1. Crear Watch:
   - Nombre: `Audio Transcripción`
   - Directorio: `~/Downloads`
   - Patrones: `*.mp3, *.wav, *.m4a`
2. En Pipeline Builder, diseñar:
   ```
   [Whisper] → [SQLite]
   ```
3. Iniciar Watchdog
4. Descargar audio → Transcripción automática

---

### 3. Backup diario automático

**Escenario**: Ejecutar un script de backup cada día a las 9am.

**Configuración**:
1. Ir a **Agent Mode**
2. Crear Tarea Programada:
   - Nombre: `Backup Diario`
   - Tipo: `Cron`
   - Horario: `0 9 * * *`
3. Iniciar Scheduler

**Horarios comunes**:
| Cron | Significado |
|------|-------------|
| `0 9 * * *` | Cada día a las 9:00 AM |
| `0 23 * * *` | Cada día a las 11:00 PM |
| `0 * * * *` | Cada hora |
| `*/15 * * * *` | Cada 15 minutos |
| `0 0 * * 0` | Cada domingo a medianoche |

---

### 4. Monitorear capturas de pantalla

**Escenario**: Detectar screenshots y procesarlas con OCR.

**Configuración**:
1. Crear Watch:
   - Nombre: `Screenshots`
   - Directorio: `~/Desktop`
   - Patrones: `Screenshot*.png, Captura*.png`
2. Iniciar Watchdog

---

### 5. Ejecutar pipeline desde el canvas

**Escenario**: Diseñas un pipeline y quieres ejecutarlo.

**Pasos**:
1. En **Pipeline Builder**, arrastra herramientas al canvas
2. Conecta los nodos
3. Ve a **Agent Mode**
4. Clic en **"Ejecutar Pipeline Actual"**
5. Ver progreso en "Ejecuciones Recientes"

---

## Acciones Rápidas

| Botón | Función |
|-------|---------|
| **Iniciar Todo** | Activa Watchdog + Scheduler |
| **Detener** | Para todos los servicios |
| **Ejecutar Pipeline Actual** | Ejecuta lo que está en el canvas |
| **Test Notificación** | Envía notificación de prueba |
| **Iniciar Watchdog** | Activa detección de archivos |
| **Iniciar Scheduler** | Activa tareas programadas |

---

## Tips

1. **El punto verde** junto a Watchdog/Scheduler indica que está activo
2. **Las notificaciones de macOS** requieren permisos en Preferencias del Sistema
3. **Los watches persisten** - se guardan aunque cierres DirectOS
4. **Usa intervalos simples** como `15m`, `1h`, `1d` en lugar de cron si es más fácil

---

## Troubleshooting

**El watchdog no detecta archivos**:
- Verifica que el directorio existe
- Asegúrate de que el patrón es correcto (`*.pdf`, no `pdf`)
- El punto debe estar verde

**No recibo notificaciones de macOS**:
- Ve a Preferencias del Sistema → Notificaciones
- Busca "Script Editor" o "Terminal"
- Activa las notificaciones

**El pipeline no se ejecuta**:
- Verifica que hay nodos en el canvas
- Abre la consola del navegador (Cmd+Option+J) para ver errores

---

*DirectOS v9.0 - Agent Mode*
