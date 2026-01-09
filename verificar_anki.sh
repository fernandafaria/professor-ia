#!/bin/bash
# Script para verificar se o Anki está instalado e configurado corretamente

echo "🔍 Verificando instalação do Anki..."
echo ""

# Verificar se Anki está instalado
if [ -d "/Applications/Anki.app" ]; then
    echo "✅ Anki instalado em /Applications/Anki.app"
else
    echo "❌ Anki não encontrado em /Applications"
    echo "   Baixe em: https://apps.ankiweb.net/"
fi

# Verificar se Anki está rodando
if ps aux | grep -i "Anki.app" | grep -v grep > /dev/null; then
    echo "✅ Anki está rodando"
else
    echo "⚠️  Anki não está rodando"
    echo "   Abra o Anki antes de continuar"
fi

# Verificar AnkiConnect
echo ""
echo "🔌 Verificando AnkiConnect..."
response=$(curl -s -w "\n%{http_code}" http://localhost:8765 2>&1 | tail -1)
if [ "$response" = "200" ] || curl -s http://localhost:8765 > /dev/null 2>&1; then
    echo "✅ AnkiConnect está respondendo"
    echo ""
    echo "Versão do AnkiConnect:"
    curl -s -X POST http://localhost:8765 -H 'Content-Type: application/json' -d '{"action":"version","version":6}' 2>&1 | head -3
else
    echo "❌ AnkiConnect não está respondendo"
    echo ""
    echo "Possíveis causas:"
    echo "  - Anki não está rodando"
    echo "  - Plugin AnkiConnect não está instalado"
    echo "  - Porta 8765 está ocupada"
    echo ""
    echo "Soluções:"
    echo "  1. Abra o Anki"
    echo "  2. Instale o plugin AnkiConnect (código: 2055492159)"
    echo "  3. Reinicie o Anki"
    echo "  4. Desabilite App Nap: ./desabilitar_app_nap_anki.sh"
fi

# Verificar porta
echo ""
echo "🔌 Verificando porta 8765..."
if lsof -i :8765 > /dev/null 2>&1; then
    echo "✅ Porta 8765 está aberta"
    lsof -i :8765 | head -2
else
    echo "⚠️  Porta 8765 não está em uso"
fi

echo ""
echo "✅ Verificação concluída!"
