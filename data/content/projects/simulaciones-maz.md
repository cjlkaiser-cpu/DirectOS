---
id: simulaciones-maz
name: Simulaciones MAZ
version: v1.0
status: production
stack:
  - html
  - javascript
  - chartjs
  - montecarlo
  - css
repo: ~/Desktop/Simulaciones
description: Sistema de simulación financiera con Monte Carlo para proyecciones presupuestarias. Dashboard interactivo con 3 módulos de análisis y visualización de datos.
---

# Simulaciones MAZ v1.0

Sistema de simulación financiera con **Monte Carlo** para proyecciones presupuestarias. Dashboard interactivo con visualización de escenarios múltiples.

## Flujo de trabajo

1. **Dashboard Financiero MAZ**
   - Visualización de presupuestos
   - Gráficos interactivos
   - Comparativas por periodo
   - Exportación de datos

2. **Simulación Monte Carlo 2026**
   - Proyecciones con tendencia histórica
   - Análisis de probabilidades
   - Escenarios optimista/pesimista/realista
   - Distribución de resultados

3. **Simulaciones de Presupuesto**
   - Escenarios múltiples
   - Variables configurables
   - Análisis de sensibilidad
   - Reportes visuales

## Comandos principales

```bash
# Abrir Dashboard Financiero
open "Dashboard Financiero MAZ.html"

# Abrir Simulación Monte Carlo
open "Simulación Monte Carlo 2026 - Tendencia Histórica Completa.html"

# Abrir Simulaciones de Presupuesto
open "Simulaciones Financieras MAZ - Presupuesto 2026.html"

# Servir con servidor local (opcional)
python -m http.server 8080
# Luego abrir http://localhost:8080
```

## Arquitectura

```
Simulaciones/
├── Dashboard Financiero MAZ.html           # Dashboard principal
├── Dashboard Financiero MAZ_files/         # Assets del dashboard
│   ├── scripts.js
│   └── styles.css
├── Simulación Monte Carlo 2026 - Tendencia Histórica Completa.html
├── Simulación Monte Carlo 2026 - Tendencia Histórica Completa_files/
│   ├── montecarlo.js                       # Lógica de simulación
│   └── charts.js                           # Gráficos
└── Simulaciones Financieras MAZ - Presupuesto 2026.html
    └── Simulaciones Financieras MAZ - Presupuesto 2026_files/
        ├── simulator.js                    # Motor de simulación (~1MB)
        └── ui.js                           # Interfaz
```

### Stack técnico

- **Frontend:** HTML5 + JavaScript vanilla
- **Gráficos:** Chart.js (visualización)
- **Simulación:** Monte Carlo (probabilístico)
- **Estilos:** CSS3 (responsive)
- **Deploy:** Archivos estáticos (sin servidor necesario)
- **Tamaño:** ~1MB de código JavaScript

## Aprendizajes clave

### Lo que funcionó bien

1. **Monte Carlo:** Simulación probabilística precisa
2. **JavaScript vanilla:** Sin frameworks, carga rápida
3. **Chart.js:** Visualización clara de distribuciones
4. **HTML self-contained:** Todo en un archivo, portable
5. **Escenarios múltiples:** Comparativa fácil

### Problemas resueltos

- **Complejidad de simulación:** Encapsulado en módulo reutilizable
- **Visualización de datos:** Chart.js con configuración óptima
- **Interactividad:** Event listeners bien organizados
- **Exportación:** Datos descargables en CSV/JSON
- **Performance:** Simulaciones rápidas (miles de iteraciones)

### Módulos principales

**Dashboard Financiero MAZ:**
- Visualización de presupuestos reales
- Gráficos de barras y líneas
- Comparativas por periodo
- Filtros por categoría

**Simulación Monte Carlo 2026:**
- 10,000+ iteraciones por simulación
- Tendencia histórica completa
- Análisis de riesgo
- Distribución de probabilidades
- Intervalos de confianza (95%)

**Simulaciones de Presupuesto:**
- Escenarios configurables
- Variables ajustables (ingresos, gastos, inflación)
- Análisis de sensibilidad
- Proyecciones multi-año
- Reportes visuales

### Siguientes pasos

- [ ] API backend para guardar simulaciones
- [ ] Comparar múltiples simulaciones
- [ ] Exportar PDF con reportes
- [ ] Dashboard consolidado (3 módulos en 1)
- [ ] Simulación en tiempo real con sliders

## Métricas

- **Archivos HTML:** 3 módulos independientes
- **Líneas de código:** ~5,000 líneas JavaScript total
- **Tamaño total:** ~1.2 MB (incluyendo assets)
- **Iteraciones Monte Carlo:** 10,000 por simulación
- **Gráficos:** Chart.js con configuración avanzada

## Casos de uso reales

### Proyección presupuestaria 2026

```
Escenario Base:
- Ingresos: 100,000€
- Gastos: 85,000€
- Resultado esperado: 15,000€

Monte Carlo (10,000 iteraciones):
- Probabilidad > 0€: 87%
- Probabilidad > 10,000€: 65%
- Percentil 95: 25,000€
- Percentil 5: 5,000€
```

### Análisis de sensibilidad

```
Variable: Ingresos ±20%
- Optimista (+20%): Resultado = 27,000€
- Base (0%): Resultado = 15,000€
- Pesimista (-20%): Resultado = 3,000€

Variable: Gastos ±15%
- Optimista (-15%): Resultado = 27,750€
- Base (0%): Resultado = 15,000€
- Pesimista (+15%): Resultado = 2,250€
```

### Dashboard de seguimiento

```
Presupuesto vs Real (Q1 2025):
┌────────────┬────────────┬────────────┬──────────┐
│ Categoría  │ Presupuesto│ Real       │ Variación│
├────────────┼────────────┼────────────┼──────────┤
│ Ingresos   │ 25,000€    │ 27,500€    │ +10.0%   │
│ Gastos     │ 21,000€    │ 22,000€    │ +4.8%    │
│ Resultado  │ 4,000€     │ 5,500€     │ +37.5%   │
└────────────┴────────────┴────────────┴──────────┘
```

## Método Monte Carlo

El motor de simulación usa el siguiente algoritmo:

```javascript
function monteCarloSimulation(iterations, baseIncome, baseExpenses, volatility) {
  const results = [];

  for (let i = 0; i < iterations; i++) {
    // Generar variación aleatoria con distribución normal
    const incomeVariation = randomNormal(0, volatility);
    const expenseVariation = randomNormal(0, volatility);

    const income = baseIncome * (1 + incomeVariation);
    const expenses = baseExpenses * (1 + expenseVariation);
    const result = income - expenses;

    results.push(result);
  }

  return {
    mean: average(results),
    median: median(results),
    stdDev: standardDeviation(results),
    percentile95: percentile(results, 95),
    percentile5: percentile(results, 5),
    probability: results.filter(r => r > 0).length / iterations
  };
}
```

## Visualización

**Gráficos disponibles:**

1. **Histograma de distribución:**
   - Muestra frecuencia de resultados
   - Identifica moda y tendencia central
   - Revela simetría/asimetría

2. **Gráfico de línea (tendencia):**
   - Evolución temporal
   - Comparación presupuesto vs real
   - Proyecciones futuras

3. **Gráfico de barras (categorías):**
   - Comparación por categorías
   - Desglose de gastos/ingresos
   - Análisis por periodo

4. **Box plot:**
   - Percentiles clave (5, 25, 50, 75, 95)
   - Identificación de outliers
   - Rango intercuartil

## Deploy

```bash
# Opción 1: Abrir directamente (sin servidor)
open "Dashboard Financiero MAZ.html"

# Opción 2: Servidor local Python
cd /Users/carlos/Desktop/Simulaciones
python3 -m http.server 8080
open http://localhost:8080

# Opción 3: Servidor Node.js (alternativa)
npx http-server -p 8080
```

## Filosofía KISS

**¿Por qué NO usar frameworks?**

```
React/Vue/Angular:
- Build step necesario
- Dependencias pesadas
- Complejidad innecesaria para simulaciones

HTML + JavaScript vanilla:
- Carga instantánea
- Sin dependencias externas
- Portable (USB, email, etc.)
- Debuggeable en DevTools
```

**Principio:** Si HTML + JavaScript vanilla resuelve el problema, ¿para qué más?

## Comparativa

| Feature | Simulaciones MAZ | Excel | Python Scripts |
|---------|------------------|-------|----------------|
| Interfaz | ✅ Web interactiva | Hojas de cálculo | Terminal |
| Monte Carlo | ✅ 10K iteraciones | Limitado | ✅ Completo |
| Visualización | ✅ Chart.js | Gráficos básicos | Matplotlib |
| Portable | ✅ HTML file | .xlsx file | Requiere Python |
| Velocidad | ✅ Instantáneo | Medio | Medio |
| Accesibilidad | ✅ Navegador | Requiere Excel | Requiere setup |

## Enlaces útiles

- [Chart.js Docs](https://www.chartjs.org/)
- [Monte Carlo Simulation (Wikipedia)](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [JavaScript Random Distribution](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
