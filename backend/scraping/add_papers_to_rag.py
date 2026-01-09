"""
Script para adicionar papers processados ao RAG (ChromaDB).
"""

import json
import sys
import logging
from pathlib import Path
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_chunks_file(filepath: str) -> List[Dict]:
    """Carrega chunks de arquivo JSON"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def add_to_chromadb(chunks: List[Dict], collection_name: str = "neurodivergence_papers"):
    """
    Adiciona chunks ao ChromaDB.
    
    Requer ChromaDB rodando e bibliotecas instaladas.
    """
    try:
        import chromadb
        from chromadb.config import Settings
        from sentence_transformers import SentenceTransformer
        
        logger.info("Conectando ao ChromaDB...")
        
        # Conectar ao ChromaDB
        client = chromadb.Client(Settings(
            chroma_api_impl="rest",
            chroma_server_host="localhost",
            chroma_server_http_port=8000,
        ))
        
        # Obter ou criar collection
        try:
            collection = client.get_collection(name=collection_name)
            logger.info(f"Collection '{collection_name}' encontrada")
        except:
            collection = client.create_collection(
                name=collection_name,
                metadata={"description": "Papers sobre neurodivergências"}
            )
            logger.info(f"Collection '{collection_name}' criada")
        
        # Carregar modelo de embedding
        logger.info("Carregando modelo de embedding...")
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        
        # Processar em batches
        batch_size = 50
        total_added = 0
        
        logger.info(f"Adicionando {len(chunks)} chunks ao ChromaDB...")
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
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
        
        logger.info(f"\n✅ Total de {total_added} chunks adicionados ao RAG!")
        
        # Verificar
        count = collection.count()
        logger.info(f"📊 Total na collection: {count} documentos")
        
        return True
        
    except ImportError as e:
        logger.error(f"❌ Bibliotecas não instaladas: {e}")
        logger.info("\nInstale as dependências:")
        logger.info("  pip install chromadb sentence-transformers")
        return False
    except Exception as e:
        logger.error(f"❌ Erro ao adicionar ao ChromaDB: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Adicionar papers ao RAG")
    parser.add_argument("--file", type=str, required=True,
                       help="Arquivo JSON com chunks processados")
    parser.add_argument("--collection", type=str, default="neurodivergence_papers",
                       help="Nome da collection no ChromaDB")
    
    args = parser.parse_args()
    
    # Carregar chunks
    logger.info(f"Carregando chunks de: {args.file}")
    chunks = load_chunks_file(args.file)
    logger.info(f"✅ {len(chunks)} chunks carregados")
    
    # Adicionar ao RAG
    success = add_to_chromadb(chunks, args.collection)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
