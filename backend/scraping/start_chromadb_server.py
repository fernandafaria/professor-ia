#!/usr/bin/env python3
"""
Script para iniciar servidor ChromaDB.
Alternativa quando o comando 'chroma' não está disponível.
"""

import os
import sys
from pathlib import Path

def start_chromadb_server():
    """Inicia servidor ChromaDB."""
    
    # Configurações
    chroma_host = os.getenv('CHROMA_HOST', 'localhost')
    chroma_port = int(os.getenv('CHROMA_PORT', '8000'))
    chroma_path = os.getenv('CHROMA_PATH', './chroma_db')
    
    # Criar diretório se não existir
    Path(chroma_path).mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("🚀 Iniciando ChromaDB Server")
    print("=" * 60)
    print(f"Host: {chroma_host}")
    print(f"Porta: {chroma_port}")
    print(f"Diretório de dados: {chroma_path}")
    print("")
    print("💡 Para parar: Ctrl+C")
    print("=" * 60)
    print("")
    
    try:
        import chromadb
        
        # Na versão mais recente do ChromaDB, use o método correto
        # Tentar usar HttpClientServer se disponível
        try:
            from chromadb.server.fastapi import FastAPI as ChromaFastAPI
            from chromadb.config import Settings
            import uvicorn
            
            settings = Settings(
                chroma_server_host=chroma_host,
                chroma_server_http_port=chroma_port,
                chroma_db_impl='duckdb+parquet',
                persist_directory=chroma_path,
                allow_reset=True
            )
            
            app = ChromaFastAPI(settings)
            
            print(f"✅ Servidor iniciando em http://{chroma_host}:{chroma_port}")
            print("")
            
            uvicorn.run(app, host=chroma_host, port=chroma_port, log_level="info")
            
        except ImportError:
            # Fallback: tentar iniciar servidor simples
            print("⚠️  Usando modo alternativo...")
            
            # Usar modo persistente (não requer servidor)
            print("💡 Nota: Seu código pode usar ChromaDB em modo persistente")
            print("   sem precisar de servidor standalone")
            print("")
            print("   Exemplo:")
            print("   from chromadb import PersistentClient")
            print(f"   client = PersistentClient(path='{chroma_path}')")
            print("")
            
            sys.exit(0)
            
    except ImportError as e:
        print(f"❌ Erro: ChromaDB não está instalado")
        print(f"   Instale com: pip install chromadb uvicorn")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro ao iniciar ChromaDB: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    start_chromadb_server()
