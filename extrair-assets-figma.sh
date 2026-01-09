#!/bin/bash

# Script para ajudar na extração de assets do Figma
# Este script cria a estrutura de pastas e documenta o processo

echo "🎨 Preparando estrutura para assets do Figma..."
echo ""

# Criar estrutura de pastas
mkdir -p frontend/public/assets/images
mkdir -p frontend/public/assets/icons
mkdir -p frontend/public/assets/fonts

echo "✅ Pastas criadas:"
echo "   - frontend/public/assets/images/"
echo "   - frontend/public/assets/icons/"
echo "   - frontend/public/assets/fonts/"
echo ""

echo "📋 Próximos passos:"
echo ""
echo "1. Obtenha o link direto do design no Figma (não o protótipo compartilhado)"
echo "   Formato: https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]"
echo ""
echo "2. No chat do Cursor, digite:"
echo ""
echo "   Extraia todos os assets deste design do Figma:"
echo "   fileKey: [SEU_FILE_KEY]"
echo "   nodeId: [SEU_NODE_ID]"
echo ""
echo "   Salve em:"
echo "   - Imagens: public/assets/images/"
echo "   - Ícones: public/assets/icons/"
echo ""
echo "3. Ou exporte manualmente do Figma:"
echo "   - Selecione os assets"
echo "   - Clique direito → Export"
echo "   - Salve em frontend/public/assets/[images|icons]/"
echo ""
echo "📚 Veja o guia completo: COMO-EXTRAIR-ASSETS-FIGMA.md"
echo ""
