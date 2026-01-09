#!/bin/bash

# Script para verificar se tudo está pronto para deploy no Railway

echo "🔍 Verificando configuração para deploy no Railway..."
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0

# Verificar se está no diretório backend
if [ ! -f "app/main.py" ]; then
    echo -e "${RED}❌ ERRO: Execute este script dentro do diretório backend/${NC}"
    echo "   cd backend && bash verificar-deploy.sh"
    exit 1
fi

echo "📁 Verificando arquivos necessários..."
echo ""

# 1. Verificar Procfile
if [ -f "Procfile" ]; then
    echo -e "${GREEN}✅ Procfile existe${NC}"
    if grep -q "uvicorn app.main:app" Procfile && grep -q "\$PORT" Procfile; then
        echo -e "${GREEN}   ✓ Conteúdo correto${NC}"
    else
        echo -e "${RED}   ❌ Conteúdo incorreto!${NC}"
        echo "   Deve conter: web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo -e "${RED}❌ Procfile NÃO existe!${NC}"
    echo "   Criar: echo 'web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT' > Procfile"
    ERRORS=$((ERRORS + 1))
fi

# 2. Verificar runtime.txt
if [ -f "runtime.txt" ]; then
    echo -e "${GREEN}✅ runtime.txt existe${NC}"
    if grep -q "python-3" runtime.txt; then
        echo -e "${GREEN}   ✓ Versão Python especificada${NC}"
    else
        echo -e "${YELLOW}   ⚠️  Versão Python não encontrada${NC}"
    fi
else
    echo -e "${RED}❌ runtime.txt NÃO existe!${NC}"
    echo "   Criar: echo 'python-3.11' > runtime.txt"
    ERRORS=$((ERRORS + 1))
fi

# 3. Verificar requirements.txt
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✅ requirements.txt existe${NC}"
    if grep -q "fastapi" requirements.txt && grep -q "uvicorn" requirements.txt; then
        echo -e "${GREEN}   ✓ Dependências básicas presentes${NC}"
    else
        echo -e "${YELLOW}   ⚠️  Dependências básicas podem estar faltando${NC}"
    fi
else
    echo -e "${RED}❌ requirements.txt NÃO existe!${NC}"
    ERRORS=$((ERRORS + 1))
fi

# 4. Verificar app/main.py
if [ -f "app/main.py" ]; then
    echo -e "${GREEN}✅ app/main.py existe${NC}"
else
    echo -e "${RED}❌ app/main.py NÃO existe!${NC}"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "🔐 Verificando variáveis de ambiente necessárias..."
echo ""
echo -e "${YELLOW}⚠️  Verifique manualmente no Railway:${NC}"
echo "   - DATABASE_URL (obrigatória)"
echo "   - SECRET_KEY (obrigatória)"
echo "   - CORS_ORIGINS (obrigatória)"
echo "   - ANTHROPIC_API_KEY (recomendada)"
echo ""

echo "📋 Verificando estrutura do projeto..."
echo ""

# Verificar estrutura básica
if [ -d "app" ]; then
    echo -e "${GREEN}✅ Diretório app/ existe${NC}"
    if [ -f "app/config.py" ]; then
        echo -e "${GREEN}   ✓ app/config.py existe${NC}"
    else
        echo -e "${YELLOW}   ⚠️  app/config.py não encontrado${NC}"
    fi
else
    echo -e "${RED}❌ Diretório app/ NÃO existe!${NC}"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✅ Tudo parece estar configurado corretamente!${NC}"
    echo ""
    echo "📝 Próximos passos:"
    echo "   1. Verifique Root Directory = 'backend' no Railway"
    echo "   2. Adicione variáveis de ambiente no Railway"
    echo "   3. Faça commit e push das mudanças"
    echo "   4. Deploy no Railway"
    exit 0
else
    echo -e "${RED}❌ Encontrados $ERRORS erro(s)!${NC}"
    echo ""
    echo "🔧 Corrija os erros acima antes de fazer deploy."
    exit 1
fi
