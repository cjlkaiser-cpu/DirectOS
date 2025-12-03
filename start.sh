#!/bin/bash
# =============================================================================
# DirectOS v9.0 - Agent Mode - Script de Arranque
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════╗"
echo "║     DirectOS v9.0 - Agent Mode            ║"
echo "╚═══════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Python3 no encontrado. Instálalo primero.${NC}"
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo -e "${BLUE}Creando entorno virtual...${NC}"
    python3 -m venv venv
fi

# Activar entorno virtual
echo -e "${BLUE}Activando entorno virtual...${NC}"
source venv/bin/activate

# Instalar dependencias si es necesario
if [ ! -f "venv/.deps_installed" ]; then
    echo -e "${BLUE}Instalando dependencias...${NC}"
    pip install --upgrade pip
    pip install -r backend/requirements.txt
    touch venv/.deps_installed
    echo -e "${GREEN}Dependencias instaladas.${NC}"
fi

# Verificar .env
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Archivo .env no encontrado.${NC}"
    echo -e "${YELLOW}Scout (análisis de errores) no funcionará sin ANTHROPIC_API_KEY${NC}"
    echo -e "${YELLOW}Copia .env.example a .env y añade tu API key${NC}"
    echo ""
fi

# Obtener IP local para minerOS móvil
LOCAL_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "localhost")

# Iniciar minerOS Mobile en background (puerto 8080)
MINEROS_DIR="$HOME/Desktop/dashboard-mobile-mineros"
if [ -d "$MINEROS_DIR" ]; then
    echo -e "${GREEN}Iniciando minerOS Mobile...${NC}"
    (cd "$MINEROS_DIR" && python3 -m http.server 8080 > /dev/null 2>&1) &
    MINEROS_PID=$!
    echo -e "${BLUE}→ minerOS Mobile: http://${LOCAL_IP}:8080${NC}"
fi

# Iniciar DirectOS
echo -e "${GREEN}Iniciando DirectOS...${NC}"
echo -e "${BLUE}→ Frontend: http://localhost:8000${NC}"
echo -e "${BLUE}→ API Docs: http://localhost:8000/docs${NC}"
echo ""

# Abrir navegador después de 2 segundos (en background)
(sleep 2 && open "http://localhost:8000") &

cd backend
# --host 0.0.0.0 permite acceso desde móvil en la misma red WiFi
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
