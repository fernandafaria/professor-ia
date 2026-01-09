#!/bin/zsh

# Script para verificar versões do Python instaladas

echo "🐍 Verificando Versões do Python"
echo "=================================================="
echo ""

echo "Python padrão (python3):"
python3 --version 2>&1
which python3
echo ""

echo "Python 3.10:"
python3.10 --version 2>&1 || echo "❌ Python 3.10 não encontrado"
which python3.10 2>&1 || echo ""
echo ""

echo "Python 3.11:"
python3.11 --version 2>&1 || echo "❌ Python 3.11 não encontrado"
which python3.11 2>&1 || echo ""
echo ""

echo "Python 3.12:"
python3.12 --version 2>&1 || echo "❌ Python 3.12 não encontrado"
which python3.12 2>&1 || echo ""
echo ""

echo "=================================================="
echo "📋 Resumo:"
echo ""

CURRENT=$(python3 --version 2>&1 | awk '{print $2}')
MAJOR=$(echo $CURRENT | cut -d. -f1)
MINOR=$(echo $CURRENT | cut -d. -f2)

if [ "$MAJOR" -eq 3 ] && [ "$MINOR" -ge 10 ]; then
    echo "✅ Python $CURRENT atende aos requisitos (3.10+)"
else
    echo "⚠️  Python $CURRENT precisa ser atualizado para 3.10+"
    echo ""
    echo "💡 Para instalar Python 3.10+:"
    echo "   1. Acesse: https://www.python.org/downloads/"
    echo "   2. Baixe e instale Python 3.10+"
    echo "   3. Ou instale Homebrew e execute: brew install python@3.10"
fi
