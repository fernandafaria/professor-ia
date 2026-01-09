#!/bin/bash
# Script simplificado para configurar Anki em 3 passos

echo "🎯 Configuração Simples do Anki"
echo "================================"
echo ""

echo "✅ Passo 1: Abrindo o Anki..."
open -a Anki 2>/dev/null || echo "   Abra o Anki manualmente: Applications > Anki"
echo ""

echo "📋 Passo 2: Instale o plugin AnkiConnect"
echo "   No Anki: Tools > Add-ons > Get Add-ons..."
echo "   Código: 2055492159"
echo "   Depois reinicie o Anki (Cmd+Q)"
echo ""

echo "⚙️  Passo 3: Desabilitando App Nap..."
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
echo "   ✅ App Nap desabilitado!"
echo "   Reinicie o Anki novamente"
echo ""

echo "✅ Teste se funcionou:"
echo "   curl http://localhost:8765"
echo ""
echo "🎉 Pronto! Consulte ANKI-SIMPLES.md para mais detalhes"
