#!/bin/zsh

# Script de Instalação de Pré-requisitos para Plataforma EdTech
# macOS - Usando Homebrew

# Não usar set -e para permitir continuar mesmo com erros
# set -e

echo "🚀 Instalando Pré-requisitos para Plataforma EdTech"
echo "=================================================="
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Função para verificar se comando existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 1. Instalar Homebrew
echo "📦 1. Verificando Homebrew..."
if ! command_exists brew; then
    echo "${YELLOW}Homebrew não encontrado.${NC}"
    echo "${YELLOW}Para instalar, execute manualmente:${NC}"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo ""
    if [ -t 0 ]; then
        # Terminal interativo - pode fazer perguntas
        read -p "Deseja instalar Homebrew agora? (s/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        # Adicionar Homebrew ao PATH (se necessário)
        if [[ -f "/opt/homebrew/bin/brew" ]]; then
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/opt/homebrew/bin/brew shellenv)"
        elif [[ -f "/usr/local/bin/brew" ]]; then
            echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
            eval "$(/usr/local/bin/brew shellenv)"
        fi
            echo "${GREEN}✅ Homebrew instalado${NC}"
        else
            echo "${RED}⚠️  Homebrew não instalado. Algumas instalações podem falhar.${NC}"
        fi
    else
        # Terminal não-interativo - apenas informa
        echo "${YELLOW}⚠️  Modo não-interativo detectado.${NC}"
        echo "${YELLOW}   Para instalar Homebrew, execute:${NC}"
        echo "${YELLOW}   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"${NC}"
    fi
else
    echo "${GREEN}✅ Homebrew já instalado${NC}"
    brew --version
fi
echo ""

# 2. Atualizar Python para 3.10+
echo "🐍 2. Verificando Python..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]); then
    echo "${YELLOW}Python $PYTHON_VERSION encontrado. Precisa Python 3.10+${NC}"
    if command_exists brew; then
        echo "${YELLOW}Instalando Python 3.10+...${NC}"
        brew install python@3.10 || echo "${RED}⚠️  Erro ao instalar Python 3.10. Tente manualmente: brew install python@3.10${NC}"
        echo "${GREEN}✅ Python 3.10+ instalado${NC}"
        echo "${YELLOW}⚠️  Nota: Use 'python3.10' ou configure alias${NC}"
    else
        echo "${RED}⚠️  Homebrew não está instalado. Instale Homebrew primeiro.${NC}"
    fi
else
    echo "${GREEN}✅ Python $PYTHON_VERSION já atende aos requisitos (3.10+)${NC}"
fi
echo ""

# 3. Verificar Node.js e npm
echo "📦 3. Verificando Node.js e npm..."
if command_exists node && command_exists npm; then
    NODE_VERSION=$(node --version)
    NPM_VERSION=$(npm --version)
    echo "${GREEN}✅ Node.js $NODE_VERSION instalado${NC}"
    echo "${GREEN}✅ npm $NPM_VERSION instalado${NC}"
else
    echo "${YELLOW}Instalando Node.js...${NC}"
    brew install node
fi
echo ""

# 4. Instalar pnpm
echo "📦 4. Instalando pnpm..."
if command_exists pnpm; then
    echo "${GREEN}✅ pnpm já instalado${NC}"
    pnpm --version
else
    echo "${YELLOW}Instalando pnpm...${NC}"
    npm install -g pnpm
    echo "${GREEN}✅ pnpm instalado${NC}"
fi
echo ""

# 5. Verificar Git
echo "🔧 5. Verificando Git..."
if command_exists git; then
    GIT_VERSION=$(git --version)
    echo "${GREEN}✅ $GIT_VERSION instalado${NC}"
    
    # Verificar se está configurado
    if [ -z "$(git config --global user.name)" ]; then
        echo "${YELLOW}⚠️  Git não está configurado. Configure com:${NC}"
        echo "   git config --global user.name 'Seu Nome'"
        echo "   git config --global user.email 'seu@email.com'"
    fi
else
    echo "${YELLOW}Instalando Git...${NC}"
    brew install git
fi
echo ""

# 6. Instalar PostgreSQL
echo "🐘 6. Verificando PostgreSQL..."
if command_exists psql; then
    PSQL_VERSION=$(psql --version)
    echo "${GREEN}✅ $PSQL_VERSION instalado${NC}"
else
    if command_exists brew; then
        echo "${YELLOW}Instalando PostgreSQL 15...${NC}"
        brew install postgresql@15 || {
            echo "${RED}⚠️  Erro ao instalar PostgreSQL. Tente manualmente: brew install postgresql@15${NC}"
            echo ""
            return 0
        }
        
        # Adicionar ao PATH
        if [[ -d "/opt/homebrew/opt/postgresql@15/bin" ]]; then
            echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
            export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"
        elif [[ -d "/usr/local/opt/postgresql@15/bin" ]]; then
            echo 'export PATH="/usr/local/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
            export PATH="/usr/local/opt/postgresql@15/bin:$PATH"
        fi
        
        # Iniciar serviço
        brew services start postgresql@15 || echo "${YELLOW}⚠️  Não foi possível iniciar PostgreSQL automaticamente${NC}"
        
        # Criar banco de dados
        if command_exists createdb; then
            createdb p1a_db 2>/dev/null && echo "${GREEN}✅ Banco p1a_db criado${NC}" || echo "${YELLOW}⚠️  Banco p1a_db já existe ou erro ao criar${NC}"
        fi
        
        echo "${GREEN}✅ PostgreSQL instalado${NC}"
        echo "${YELLOW}⚠️  Para iniciar: brew services start postgresql@15${NC}"
        echo "${YELLOW}⚠️  Para criar banco: createdb p1a_db${NC}"
    else
        echo "${RED}⚠️  Homebrew não está instalado. Instale Homebrew primeiro.${NC}"
    fi
fi
echo ""

# 7. Verificar Docker
echo "🐳 7. Verificando Docker..."
if command_exists docker; then
    DOCKER_VERSION=$(docker --version)
    echo "${GREEN}✅ $DOCKER_VERSION instalado${NC}"
    
    # Verificar se está rodando
    if docker info >/dev/null 2>&1; then
        echo "${GREEN}✅ Docker está rodando${NC}"
    else
        echo "${YELLOW}⚠️  Docker instalado mas não está rodando${NC}"
        echo "${YELLOW}   Inicie o Docker Desktop${NC}"
    fi
else
    echo "${YELLOW}Docker não encontrado.${NC}"
    echo "${YELLOW}Instale Docker Desktop de: https://www.docker.com/products/docker-desktop/${NC}"
    echo "${YELLOW}Ou execute: brew install --cask docker${NC}"
    if [ -t 0 ]; then
        # Terminal interativo
        read -p "Deseja instalar Docker Desktop agora? (s/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
        brew install --cask docker
            echo "${GREEN}✅ Docker Desktop instalado${NC}"
            echo "${YELLOW}⚠️  Inicie o Docker Desktop manualmente${NC}"
        fi
    else
        echo "${YELLOW}⚠️  Modo não-interativo. Instale Docker Desktop manualmente.${NC}"
    fi
fi
echo ""

# Resumo final
echo "=================================================="
echo "📋 Resumo da Instalação:"
echo "=================================================="
echo ""

# Verificar tudo novamente
echo "Versões instaladas:"
echo "-------------------"

if command_exists python3; then
    echo "✅ Python: $(python3 --version 2>&1)"
else
    echo "❌ Python: Não instalado"
fi

if command_exists python3.10; then
    echo "✅ Python 3.10: $(python3.10 --version 2>&1)"
fi

if command_exists node; then
    echo "✅ Node.js: $(node --version)"
else
    echo "❌ Node.js: Não instalado"
fi

if command_exists npm; then
    echo "✅ npm: $(npm --version)"
else
    echo "❌ npm: Não instalado"
fi

if command_exists pnpm; then
    echo "✅ pnpm: $(pnpm --version)"
else
    echo "❌ pnpm: Não instalado"
fi

if command_exists git; then
    echo "✅ Git: $(git --version)"
else
    echo "❌ Git: Não instalado"
fi

if command_exists psql; then
    echo "✅ PostgreSQL: $(psql --version)"
else
    echo "❌ PostgreSQL: Não instalado"
fi

if command_exists docker; then
    echo "✅ Docker: $(docker --version)"
    if docker info >/dev/null 2>&1; then
        echo "   Status: Rodando"
    else
        echo "   Status: Instalado mas não rodando"
    fi
else
    echo "⚠️  Docker: Não instalado (opcional)"
fi

echo ""
echo "=================================================="
echo "✅ Instalação concluída!"
echo ""
echo "📝 Próximos passos:"
echo "   1. Reinicie o terminal ou execute: source ~/.zshrc"
echo "   2. Configure Git (se necessário):"
echo "      git config --global user.name 'Seu Nome'"
echo "      git config --global user.email 'seu@email.com'"
echo "   3. Inicie PostgreSQL: brew services start postgresql@15"
echo "   4. Crie o banco: createdb p1a_db"
echo "   5. Inicie Docker Desktop (se instalado)"
echo "=================================================="
