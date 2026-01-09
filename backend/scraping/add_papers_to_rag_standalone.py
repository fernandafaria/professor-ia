"""
Script standalone para adicionar papers ao RAG.
Versão que verifica dependências e fornece instruções claras.
"""

import json
import sys
import logging
from pathlib import Path
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    missing = []
    
    try:
        import chromadb
    except ImportError:
        missing.append("chromadb")
    
    try:
        import sentence_transformers
    except ImportError:
        missing.append("sentence-transformers")
    
    return missing


def check_chromadb_running():
    """Verifica se ChromaDB está rodando"""
    try:
        import requests
        response = requests.get("http://localhost:8000/api/v1/heartbeat", timeout=2)
        return response.status_code == 200
    except:
        return False


def load_chunks_file(filepath: str) -> List[Dict]:
    """Carrega chunks de arquivo JSON"""
    file_path = Path(filepath)
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def add_to_chromadb(chunks: List[Dict], collection_name: str = "neurodivergence_papers"):
    """
    Adiciona chunks ao ChromaDB.
    """
    import chromadb
    from chromadb.config import Settings
    from sentence_transformers import SentenceTransformer
    
    logger.info("Conectando ao ChromaDB...")
    
    # Conectar ao ChromaDB
    try:
        client = chromadb.Client(Settings(
            chroma_api_impl="rest",
            chroma_server_host="localhost",
            chroma_server_http_port=8000,
        ))
    except Exception as e:
        logger.error(f"❌ Erro ao conectar ao ChromaDB: {e}")
        logger.info("\n💡 Certifique-se de que o ChromaDB está rodando:")
        logger.info("   chroma run --path ./chroma_db --port 8000")
        return False
    
    # Obter ou criar collection
    try:
        collection = client.get_collection(name=collection_name)
        logger.info(f"✅ Collection '{collection_name}' encontrada")
    except:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "Papers sobre neurodivergências"}
        )
        logger.info(f"✅ Collection '{collection_name}' criada")
    
    # Carregar modelo de embedding
    logger.info("Carregando modelo de embedding...")
    try:
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        logger.info("✅ Modelo carregado")
    except Exception as e:
        logger.error(f"❌ Erro ao carregar modelo: {e}")
        return False
    
    # Processar em batches
    batch_size = 50
    total_added = 0
    
    logger.info(f"📚 Adicionando {len(chunks)} chunks ao ChromaDB...")
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        
        try:
            # Extrair dados
            texts = [chunk["content"] for chunk in batch]
            metadatas = [chunk["metadata"] for chunk in batch]
            ids = [chunk["id"] for chunk in batch]
            
            # Gerar embeddings
            embeddings = model.encode(texts, convert_to_numpy=True).tolist()
            
            # Adicionar ao ChromaDB
            collection.add(
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas,
                ids=ids
            )
            
            total_added += len(batch)
            logger.info(f"  ✓ Batch {i//batch_size + 1}: {len(batch)} chunks adicionados")
            
        except Exception as e:
            logger.error(f"  ✗ Erro no batch {i//batch_size + 1}: {e}")
            continue
    
    logger.info(f"\n✅ Total de {total_added} chunks adicionados ao RAG!")
    
    # Verificar
    try:
        count = collection.count()
        logger.info(f"📊 Total na collection: {count} documentos")
    except:
        pass
    
    return True


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Adicionar papers ao RAG")
    parser.add_argument("--file", type=str, 
                       default="data/raw/papers_neurodivergence_20260108_224656_chunks.json",
                       help="Arquivo JSON com chunks processados")
    parser.add_argument("--collection", type=str, default="neurodivergence_papers",
                       help="Nome da collection no ChromaDB")
    parser.add_argument("--check-only", action="store_true",
                       help="Apenas verificar dependências e ChromaDB")
    
    args = parser.parse_args()
    
    # Verificar dependências
    logger.info("🔍 Verificando dependências...")
    missing = check_dependencies()
    
    if missing:
        logger.error(f"❌ Bibliotecas faltando: {', '.join(missing)}")
        logger.info("\n📦 Instale as dependências:")
        logger.info("   pip install chromadb sentence-transformers")
        logger.info("\nOu se estiver usando ambiente virtual:")
        logger.info("   source venv/bin/activate")
        logger.info("   pip install chromadb sentence-transformers")
        return 1
    
    logger.info("✅ Todas as dependências estão instaladas")
    
    # Verificar ChromaDB
    logger.info("\n🔍 Verificando ChromaDB...")
    if not check_chromadb_running():
        logger.error("❌ ChromaDB não está rodando")
        logger.info("\n💡 Inicie o ChromaDB:")
        logger.info("   chroma run --path ./chroma_db --port 8000")
        logger.info("\nOu em outro terminal:")
        logger.info("   cd backend")
        logger.info("   chroma run --path ./chroma_db --port 8000")
        return 1
    
    logger.info("✅ ChromaDB está rodando")
    
    if args.check_only:
        logger.info("\n✅ Tudo pronto para adicionar papers ao RAG!")
        return 0
    
    # Carregar chunks
    logger.info(f"\n📂 Carregando chunks de: {args.file}")
    try:
        chunks = load_chunks_file(args.file)
        logger.info(f"✅ {len(chunks)} chunks carregados")
    except FileNotFoundError as e:
        logger.error(f"❌ {e}")
        logger.info("\n💡 Encontre o arquivo mais recente:")
        logger.info("   ls -t backend/data/raw/*_chunks.json | head -1")
        return 1
    except Exception as e:
        logger.error(f"❌ Erro ao carregar arquivo: {e}")
        return 1
    
    # Adicionar ao RAG
    success = add_to_chromadb(chunks, args.collection)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
