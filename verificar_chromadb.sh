#!/bin/bash
# Script para verificar status do ChromaDB

CHROMA_HOST="${CHROMA_HOST:-localhost}"
CHROMA_PORT="${CHROMA_PORT:-8000}"

echo "🔍 Verificando status do ChromaDB..."
echo ""

# Verificar se está rodando
if lsof -Pi :$CHROMA_PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "✅ ChromaDB está rodando na porta $CHROMA_PORT"
    
    # Tentar fazer heartbeat
    if curl -s "http://$CHROMA_HOST:$CHROMA_PORT/api/v1/heartbeat" > /dev/null 2>&1; then
        echo "✅ Servidor responde corretamente"
        echo ""
        echo "   URL: http://$CHROMA_HOST:$CHROMA_PORT"
        echo "   Status: ✅ Ativo"
        
        # Tentar listar collections
        echo ""
        echo "📚 Collections disponíveis:"
        curl -s "http://$CHROMA_HOST:$CHROMA_PORT/api/v1/collections" 2>/dev/null | python3 -m json.tool 2>/dev/null || echo "   (Não foi possível listar collections)"
    else
        echo "⚠️  Porta $CHROMA_PORT está em uso, mas não responde como ChromaDB"
    fi
else
    echo "❌ ChromaDB não está rodando na porta $CHROMA_PORT"
    echo ""
    echo "💡 Para iniciar:"
    echo "   ./iniciar_chromadb.sh"
    exit 1
fi
