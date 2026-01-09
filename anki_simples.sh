#!/bin/zsh
# Script super simples para Anki

echo "🎯 Configurando Anki..."
echo ""

# Abrir Anki
open -a Anki 2>/dev/null

# Desabilitar App Nap
defaults write net.ichi2.anki NSAppSleepDisabled -bool true

echo "✅ Feito!"
echo ""
echo "📋 Agora no Anki:"
echo "   1. Tools > Add-ons"
echo "   2. Get Add-ons..."
echo "   3. Digite: 2055492159"
echo "   4. Reinicie o Anki"
echo ""
echo "✅ Teste: curl http://localhost:8765"
