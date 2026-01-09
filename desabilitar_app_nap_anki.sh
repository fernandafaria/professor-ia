#!/bin/bash
# Script para desabilitar App Nap para o Anki

echo "🛠️ Desabilitando App Nap para o Anki..."
echo ""

# Desabilita App Nap
defaults write net.ichi2.anki NSAppSleepDisabled -bool true

echo "✅ App Nap desabilitado para o Anki!"
echo ""
echo "📋 Próximos passos:"
echo "1. Reinicie o Anki completamente (Cmd+Q)"
echo "2. Abra novamente o Anki"
echo "3. As mudanças estarão aplicadas"
echo ""
echo "Para verificar se funcionou, teste a conexão:"
echo "  curl http://localhost:8765"
