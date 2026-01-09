#!/bin/bash
# Script para parar o servidor ChromaDB

CHROMA_PORT="${CHROMA_PORT:-8000}"

echo "🛑 Parando ChromaDB..."

# Verificar se existe PID file
if [ -f chroma.pid ]; then
    PID=$(cat chroma.pid)
    if ps -p $PID > /dev/null 2>&1; then
        kill $PID
        echo "✅ ChromaDB parado (PID: $PID)"
        rm chroma.pid
    else
        echo "⚠️  Processo não encontrado, removendo PID file"
        rm chroma.pid
    fi
fi

# Tentar parar qualquer processo na porta
if lsof -Pi :$CHROMA_PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    PID=$(lsof -Pi :$CHROMA_PORT -sTCP:LISTEN -t)
    kill $PID
    echo "✅ Processo na porta $CHROMA_PORT parado (PID: $PID)"
else
    echo "ℹ️  Nenhum processo rodando na porta $CHROMA_PORT"
fi

echo "✅ Pronto!"
