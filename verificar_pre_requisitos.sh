#!/bin/zsh

echo "=== Verificação de Pré-requisitos ==="
echo ""

echo "🐍 Python:"
python3 --version 2>&1 || echo "❌ Não instalado"
python3.10 --version 2>&1 || echo "⚠️  Python 3.10 não encontrado (use python3.10)"
echo ""

echo "📦 Node.js:"
node --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "📦 npm:"
npm --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "📦 pnpm:"
pnpm --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "🔧 Git:"
git --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "🐘 PostgreSQL:"
psql --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "🐳 Docker:"
docker --version 2>&1 || echo "⚠️  Não instalado (opcional)"
if command -v docker >/dev/null 2>&1; then
    if docker info >/dev/null 2>&1; then
        echo "   Status: ✅ Rodando"
    else
        echo "   Status: ⚠️  Instalado mas não rodando"
    fi
fi
echo ""

echo "🍺 Homebrew:"
brew --version 2>&1 || echo "❌ Não instalado"
echo ""

echo "=== Fim da Verificação ==="
