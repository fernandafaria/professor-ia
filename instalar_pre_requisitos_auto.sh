#!/bin/zsh

# Script de Instalação Automática de Pré-requisitos (Não-Interativo)
# macOS - Usando Homebrew
# Use este script se quiser instalar tudo automaticamente sem perguntas

echo "🚀 Instalando Pré-requisitos (Modo Automático)"
echo "=================================================="
echo ""

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 1. Homebrew
if ! command_exists brew; then
    echo "${YELLOW}Instalando Homebrew...${NC}"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || {
        echo "${RED}Erro ao instalar Homebrew. Execute manualmente.${NC}"
        exit 1
    }
    
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
        eval "$(/usr/local/bin/brew shellenv)"
    fi
fi

# 2. Python 3.10+
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]); then
    echo "${YELLOW}Instalando Python 3.10+...${NC}"
    brew install python@3.10
fi

# 3. pnpm
if ! command_exists pnpm; then
    echo "${YELLOW}Instalando pnpm...${NC}"
    npm install -g pnpm
fi

# 4. PostgreSQL
if ! command_exists psql; then
    echo "${YELLOW}Instalando PostgreSQL 15...${NC}"
    brew install postgresql@15
    
    if [[ -d "/opt/homebrew/opt/postgresql@15/bin" ]]; then
        echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
        export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"
    elif [[ -d "/usr/local/opt/postgresql@15/bin" ]]; then
        echo 'export PATH="/usr/local/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
        export PATH="/usr/local/opt/postgresql@15/bin:$PATH"
    fi
    
    brew services start postgresql@15
    createdb p1a_db 2>/dev/null || true
fi

# Resumo
echo ""
echo "${GREEN}✅ Instalação concluída!${NC}"
echo ""
echo "Execute: source ~/.zshrc"
echo "Depois: ./verificar_pre_requisitos.sh"
