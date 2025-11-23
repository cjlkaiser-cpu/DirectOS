#!/bin/bash
# =============================================================================
# DirectOS v6.0 - Script de Arranque
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
echo "║        DirectOS v6.0 - minerOS            ║"
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

# Iniciar servidor
echo -e "${GREEN}Iniciando DirectOS...${NC}"
echo -e "${BLUE}→ Frontend: http://localhost:8000${NC}"
echo -e "${BLUE}→ API Docs: http://localhost:8000/docs${NC}"
echo ""

cd backend
python -m uvicorn main:app --reload --port 8000
