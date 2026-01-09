#!/bin/zsh

# Script para instalar Python 3.10+ via Homebrew

echo "🐍 Instalando Python 3.10+"
echo "=================================================="
echo ""

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# 1. Verificar/Instalar Homebrew
echo "📦 1. Verificando Homebrew..."
if ! command -v brew &> /dev/null; then
    echo "${YELLOW}Homebrew não encontrado. Instalando...${NC}"
    echo ""
    echo "⚠️  Este processo pode levar alguns minutos e solicitará sua senha de administrador."
    echo ""
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Adicionar Homebrew ao PATH
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
        eval "$(/opt/homebrew/bin/brew shellenv)"
        echo "${GREEN}✅ Homebrew instalado (Apple Silicon)${NC}"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
        eval "$(/usr/local/bin/brew shellenv)"
        echo "${GREEN}✅ Homebrew instalado (Intel)${NC}"
    fi
else
    echo "${GREEN}✅ Homebrew já instalado${NC}"
    brew --version
fi
echo ""

# 2. Instalar Python 3.10
echo "🐍 2. Instalando Python 3.10+..."
if command -v brew &> /dev/null; then
    brew install python@3.10
    
    # Verificar instalação
    if command -v python3.10 &> /dev/null; then
        PYTHON_VERSION=$(python3.10 --version)
        echo "${GREEN}✅ $PYTHON_VERSION instalado${NC}"
    else
        # Tentar encontrar no PATH do Homebrew
        if [[ -f "/opt/homebrew/bin/python3.10" ]]; then
            export PATH="/opt/homebrew/bin:$PATH"
            PYTHON_VERSION=$(python3.10 --version)
            echo "${GREEN}✅ $PYTHON_VERSION instalado${NC}"
            echo "${YELLOW}⚠️  Adicione ao PATH: export PATH=\"/opt/homebrew/bin:\$PATH\"${NC}"
        elif [[ -f "/usr/local/bin/python3.10" ]]; then
            export PATH="/usr/local/bin:$PATH"
            PYTHON_VERSION=$(python3.10 --version)
            echo "${GREEN}✅ $PYTHON_VERSION instalado${NC}"
            echo "${YELLOW}⚠️  Adicione ao PATH: export PATH=\"/usr/local/bin:\$PATH\"${NC}"
        else
            echo "${RED}❌ Python 3.10 instalado mas não encontrado no PATH${NC}"
        fi
    fi
else
    echo "${RED}❌ Homebrew não está disponível${NC}"
    exit 1
fi
echo ""

# 3. Configurar aliases (opcional)
echo "🔧 3. Configurando aliases..."
read -p "Deseja criar aliases para python3 e pip3 apontarem para 3.10? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    if [[ -f "/opt/homebrew/bin/python3.10" ]]; then
        echo 'alias python3=/opt/homebrew/bin/python3.10' >> ~/.zshrc
        echo 'alias pip3=/opt/homebrew/bin/pip3.10' >> ~/.zshrc
        echo "${GREEN}✅ Aliases configurados${NC}"
    elif [[ -f "/usr/local/bin/python3.10" ]]; then
        echo 'alias python3=/usr/local/bin/python3.10' >> ~/.zshrc
        echo 'alias pip3=/usr/local/bin/pip3.10' >> ~/.zshrc
        echo "${GREEN}✅ Aliases configurados${NC}"
    fi
fi
echo ""

# 4. Verificação final
echo "=================================================="
echo "📋 Verificação Final:"
echo "=================================================="
echo ""

if command -v python3.10 &> /dev/null; then
    echo "${GREEN}✅ Python 3.10: $(python3.10 --version)${NC}"
    echo "   Localização: $(which python3.10)"
else
    echo "${YELLOW}⚠️  Python 3.10 não encontrado no PATH${NC}"
    echo "   Tente: source ~/.zshrc"
    echo "   Ou use: /opt/homebrew/bin/python3.10 (Apple Silicon)"
    echo "   Ou use: /usr/local/bin/python3.10 (Intel)"
fi

echo ""
echo "Python sistema: $(python3 --version)"
echo ""

echo "=================================================="
echo "✅ Instalação concluída!"
echo ""
echo "📝 Próximos passos:"
echo "   1. Reinicie o terminal ou execute: source ~/.zshrc"
echo "   2. Verifique: python3.10 --version"
echo "   3. Crie ambiente virtual: python3.10 -m venv venv"
echo "=================================================="
