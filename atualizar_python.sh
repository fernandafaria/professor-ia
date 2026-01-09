#!/bin/zsh

# Script para atualizar Python para 3.10+
# macOS

echo "🐍 Atualizando Python para 3.10+"
echo "=================================================="
echo ""

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar versão atual
CURRENT_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Versão atual: Python $CURRENT_VERSION"
echo ""

# Verificar se já tem 3.10+
MAJOR=$(echo $CURRENT_VERSION | cut -d. -f1)
MINOR=$(echo $CURRENT_VERSION | cut -d. -f2)

if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 10 ]; then
    echo "${GREEN}✅ Python $CURRENT_VERSION já atende aos requisitos (3.10+)${NC}"
    python3 --version
    exit 0
fi

# Verificar Homebrew
if ! command -v brew &> /dev/null; then
    echo "${YELLOW}⚠️  Homebrew não está instalado${NC}"
    echo ""
    echo "Para instalar Python 3.10+, você precisa do Homebrew."
    echo ""
    echo "Opção 1: Instalar Homebrew primeiro"
    echo "  /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo ""
    echo "Opção 2: Baixar Python diretamente"
    echo "  https://www.python.org/downloads/"
    echo ""
    read -p "Deseja instalar Homebrew agora? (s/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        # Configurar PATH
        if [[ -f "/opt/homebrew/bin/brew" ]]; then
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/opt/homebrew/bin/brew shellenv)"
        elif [[ -f "/usr/local/bin/brew" ]]; then
            echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/usr/local/bin/brew shellenv)"
        fi
    else
        echo "${YELLOW}Instale Python 3.10+ manualmente de: https://www.python.org/downloads/${NC}"
        exit 1
    fi
fi

# Instalar Python 3.10+
echo "${YELLOW}Instalando Python 3.10+ via Homebrew...${NC}"
brew install python@3.10

# Verificar instalação
if command -v python3.10 &> /dev/null; then
    PYTHON_310_PATH=$(which python3.10)
    PYTHON_310_VERSION=$(python3.10 --version)
    
    echo ""
    echo "${GREEN}✅ Python 3.10+ instalado com sucesso!${NC}"
    echo "   Versão: $PYTHON_310_VERSION"
    echo "   Caminho: $PYTHON_310_PATH"
    echo ""
    
    # Perguntar se quer criar alias
    read -p "Deseja criar alias 'python3' -> 'python3.10'? (s/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        if [[ "$PYTHON_310_PATH" == *"/opt/homebrew"* ]]; then
            echo 'alias python3=/opt/homebrew/bin/python3.10' >> ~/.zshrc
        else
            echo 'alias python3=/usr/local/bin/python3.10' >> ~/.zshrc
        fi
        echo "${GREEN}✅ Alias criado. Execute: source ~/.zshrc${NC}"
    fi
    
    # Perguntar se quer criar novo venv
    echo ""
    read -p "Deseja criar novo ambiente virtual com Python 3.10? (s/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        cd /Users/fernandafaria/Downloads/P1A/backend 2>/dev/null || cd .
        
        if [ -d "venv" ]; then
            echo "${YELLOW}⚠️  Ambiente virtual existente encontrado${NC}"
            read -p "Deseja remover e criar novo? (s/n) " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Ss]$ ]]; then
                rm -rf venv
                python3.10 -m venv venv
                echo "${GREEN}✅ Novo ambiente virtual criado${NC}"
                echo "   Ative com: source venv/bin/activate"
            fi
        else
            python3.10 -m venv venv
            echo "${GREEN}✅ Ambiente virtual criado${NC}"
            echo "   Ative com: source venv/bin/activate"
        fi
    fi
    
else
    echo "${RED}❌ Erro ao instalar Python 3.10+${NC}"
    echo "   Tente manualmente: brew install python@3.10"
    exit 1
fi

echo ""
echo "=================================================="
echo "${GREEN}✅ Atualização concluída!${NC}"
echo ""
echo "📝 Próximos passos:"
echo "   1. Reinicie o terminal ou execute: source ~/.zshrc"
echo "   2. Verifique: python3.10 --version"
echo "   3. Crie ambiente virtual: python3.10 -m venv venv"
echo "   4. Ative: source venv/bin/activate"
echo "   5. Instale dependências: pip install -r requirements.txt"
echo "=================================================="
