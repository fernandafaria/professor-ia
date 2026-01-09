#!/bin/bash
# Script para iniciar o servidor ChromaDB automaticamente
# Plataforma Educacional P1A

set -e

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

CHROMA_HOST="${CHROMA_HOST:-localhost}"
CHROMA_PORT="${CHROMA_PORT:-8000}"
CHROMA_PATH="${CHROMA_PATH:-./chroma_db}"

echo "============================================================"
echo "🚀 Iniciando ChromaDB para Plataforma Educacional P1A"
echo "============================================================"
echo ""

# Verificar se chromadb está instalado
echo "🔍 Verificando se ChromaDB está instalado..."
if ! python3 -c "import chromadb" 2>/dev/null; then
    echo -e "${YELLOW}⚠️  ChromaDB não encontrado${NC}"
    echo "   Tentando instalar via pip..."
    
    if pip3 install chromadb --quiet; then
        echo -e "${GREEN}✅ ChromaDB instalado com sucesso!${NC}"
    else
        echo -e "${RED}❌ Erro ao instalar ChromaDB${NC}"
        echo "   Instale manualmente com: pip3 install chromadb"
        exit 1
    fi
else
    CHROMA_VERSION=$(python3 -c "import chromadb; print(getattr(chromadb, '__version__', 'desconhecida'))" 2>/dev/null || echo "instalado")
    echo -e "${GREEN}✅ ChromaDB encontrado (versão: $CHROMA_VERSION)${NC}"
fi

# Tentar encontrar comando chroma
CHROMA_CMD=""
if command -v chroma &> /dev/null; then
    CHROMA_CMD="chroma"
elif python3 -c "import chromadb.cli" 2>/dev/null; then
    CHROMA_CMD="python3 -m chromadb.cli"
else
    # Usar modo persistente se não houver servidor standalone
    echo -e "${YELLOW}⚠️  Comando 'chroma' não encontrado${NC}"
    echo "   Usando modo persistente (não requer servidor standalone)"
    USE_PERSISTENT_MODE=true
fi

# Verificar se já está rodando
echo ""
echo "🔍 Verificando se ChromaDB já está rodando na porta $CHROMA_PORT..."
if lsof -Pi :$CHROMA_PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${YELLOW}⚠️  Já existe um processo rodando na porta $CHROMA_PORT${NC}"
    echo "   Verificando se é ChromaDB..."
    
    # Tentar fazer uma requisição ao ChromaDB
    if curl -s "http://$CHROMA_HOST:$CHROMA_PORT/api/v1/heartbeat" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ ChromaDB já está rodando!${NC}"
        echo ""
        echo "   URL: http://$CHROMA_HOST:$CHROMA_PORT"
        echo "   Status: ✅ Ativo"
        exit 0
    else
        echo -e "${RED}❌ Porta $CHROMA_PORT está em uso por outro processo${NC}"
        echo "   Finalize o processo ou configure outra porta em .env"
        exit 1
    fi
fi

# Criar diretório para dados do ChromaDB se não existir
echo ""
echo "📁 Preparando diretório de dados..."
mkdir -p "$CHROMA_PATH"
echo -e "${GREEN}✅ Diretório: $CHROMA_PATH${NC}"

# Iniciar ChromaDB usando uvicorn diretamente (método mais confiável)
echo ""
echo "🚀 Iniciando servidor ChromaDB..."
echo "   Host: $CHROMA_HOST"
echo "   Porta: $CHROMA_PORT"
echo "   Diretório: $CHROMA_PATH"
echo ""

# Usar script Python dedicado
CHROMA_SERVER_SCRIPT="backend/scraping/start_chromadb_server.py"

if [ ! -f "$CHROMA_SERVER_SCRIPT" ]; then
    echo -e "${RED}❌ Script Python não encontrado: $CHROMA_SERVER_SCRIPT${NC}"
    exit 1
fi

# Iniciar ChromaDB em background ou foreground
if [ "$1" == "--background" ] || [ "$1" == "-b" ]; then
    echo "🔄 Iniciando em background..."
    echo ""
    
    CHROMA_PATH="$CHROMA_PATH" CHROMA_HOST="$CHROMA_HOST" CHROMA_PORT="$CHROMA_PORT" \
        nohup python3 "$CHROMA_SERVER_SCRIPT" > chroma.log 2>&1 &
    
    CHROMA_PID=$!
    echo $CHROMA_PID > chroma.pid
    
    echo -e "${GREEN}✅ ChromaDB iniciado em background (PID: $CHROMA_PID)${NC}"
    echo "   Logs: tail -f chroma.log"
    echo "   Parar: kill $CHROMA_PID ou ./parar_chromadb.sh"
    
    # Aguardar um pouco e verificar se iniciou corretamente
    sleep 3
    if ps -p $CHROMA_PID > /dev/null 2>&1; then
        # Tentar fazer heartbeat
        sleep 2
        if curl -s "http://$CHROMA_HOST:$CHROMA_PORT/api/v1/heartbeat" > /dev/null 2>&1; then
            echo -e "${GREEN}✅ ChromaDB está rodando e respondendo!${NC}"
            echo "   URL: http://$CHROMA_HOST:$CHROMA_PORT"
        else
            echo -e "${YELLOW}⚠️  ChromaDB iniciado, mas ainda inicializando...${NC}"
            echo "   Aguarde alguns segundos e verifique: ./verificar_chromadb.sh"
        fi
    else
        echo -e "${RED}❌ ChromaDB não iniciou corretamente${NC}"
        echo "   Verifique os logs: cat chroma.log"
        rm -f chroma.pid
        exit 1
    fi
else
    # Iniciar em foreground
    echo -e "${YELLOW}💡 Dica: Mantenha este terminal aberto enquanto usar o RAG${NC}"
    echo -e "${YELLOW}   Para parar o servidor, pressione Ctrl+C${NC}"
    echo ""
    echo "============================================================"
    echo ""
    
    CHROMA_PATH="$CHROMA_PATH" CHROMA_HOST="$CHROMA_HOST" CHROMA_PORT="$CHROMA_PORT" \
        python3 "$CHROMA_SERVER_SCRIPT"
fi
