#!/bin/zsh

# Script para iniciar ChromaDB

echo "🗄️  Iniciando ChromaDB..."
echo ""

# Verificar se chroma está instalado
if ! command -v chroma &> /dev/null; then
    echo "⚠️  Comando 'chroma' não encontrado"
    echo "💡 Tentando usar Python diretamente..."
    
    # Tentar usar Python
    python3 -c "import chromadb; print('✅ ChromaDB instalado')" 2>/dev/null || {
        echo "❌ ChromaDB não está instalado"
        echo "📦 Instale com: pip3 install chromadb"
        exit 1
    }
    
    # Iniciar via Python
    echo "🚀 Iniciando ChromaDB via Python..."
    python3 -c "
import chromadb
from chromadb.config import Settings
import uvicorn
from chromadb.app import create_app

app = create_app(Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='./chroma_db',
    anonymized_telemetry=False
))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
" &
    
    CHROMA_PID=$!
    echo "✅ ChromaDB iniciado (PID: $CHROMA_PID)"
    echo "📝 Para parar: kill $CHROMA_PID"
    
else
    # Usar comando chroma diretamente
    echo "🚀 Iniciando ChromaDB..."
    chroma run --path ./chroma_db --port 8000 &
    
    CHROMA_PID=$!
    echo "✅ ChromaDB iniciado (PID: $CHROMA_PID)"
    echo "📝 Para parar: kill $CHROMA_PID"
fi

echo ""
echo "⏳ Aguardando ChromaDB iniciar..."
sleep 3

# Verificar se está rodando
if curl -s http://localhost:8000/api/v1/heartbeat > /dev/null 2>&1; then
    echo "✅ ChromaDB está rodando em http://localhost:8000"
else
    echo "⚠️  ChromaDB pode não estar rodando ainda. Aguarde alguns segundos."
fi
