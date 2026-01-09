#!/bin/bash

# Script para organizar assets exportados do Figma
# Uso: ./organize-assets.sh

echo "📦 Organizando assets do Figma..."
echo ""

# Criar estrutura de pastas
mkdir -p public/assets/images
mkdir -p public/assets/icons
mkdir -p public/assets/fonts

echo "✅ Estrutura de pastas criada:"
echo "   - public/assets/images/  (para imagens e ilustrações)"
echo "   - public/assets/icons/   (para ícones e logos)"
echo "   - public/assets/fonts/   (para fontes, se houver)"
echo ""

echo "📋 Próximos passos:"
echo ""
echo "1. Exporte os assets do Figma:"
echo "   - Acesse o arquivo original no Figma"
echo "   - Selecione os assets (ícones, imagens)"
echo "   - Painel direito → Export"
echo "   - Escolha formato: SVG (ícones) ou PNG/JPG (imagens)"
echo ""
echo "2. Salve os arquivos exportados:"
echo "   - Salve em Downloads ou outra pasta temporária"
echo ""
echo "3. Mova para a estrutura correta:"
echo ""
echo "   # Ícones/Logos (SVG recomendado)"
echo "   mv ~/Downloads/logo.svg public/assets/icons/"
echo "   mv ~/Downloads/star-icon.svg public/assets/icons/"
echo ""
echo "   # Imagens (PNG/JPG)"
echo "   mv ~/Downloads/hero-bg.png public/assets/images/"
echo ""
echo "4. Atualize os componentes:"
echo "   - Os componentes já estão preparados com TODOs"
echo "   - Basta descomentar e ajustar paths"
echo ""
echo "5. Teste no navegador:"
echo "   npm run dev"
echo "   Verifique se os assets aparecem em http://localhost:3000"
echo ""

echo "📚 Veja o guia completo: ../EXPORTAR-ASSETS-FIGMA-MAKE.md"
echo ""
