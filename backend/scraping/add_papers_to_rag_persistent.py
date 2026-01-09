"""
Script para adicionar papers ao RAG usando ChromaDB persistente (sem servidor).
Não requer ChromaDB rodando como servidor.
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
    file_path = Path(filepath)
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def add_to_chromadb_persistent(chunks: List[Dict], collection_name: str = "neurodivergence_papers", db_path: str = "./chroma_db"):
    """
    Adiciona chunks ao ChromaDB usando modo persistente (sem servidor).
    """
    try:
        import chromadb
        from sentence_transformers import SentenceTransformer
        
        logger.info("Conectando ao ChromaDB (modo persistente)...")
        
        # Criar cliente persistente
        client = chromadb.PersistentClient(path=db_path)
        logger.info(f"✅ ChromaDB conectado (path: {db_path})")
        
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
            logger.info("💡 Baixando modelo pela primeira vez (pode levar alguns minutos)...")
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
                ids = [chunk["id"] for chunk in batch]
                
                # Converter metadados (ChromaDB não aceita listas)
                metadatas = []
                for chunk in batch:
                    metadata = chunk["metadata"].copy()
                    # Converter listas em strings
                    if "authors" in metadata and isinstance(metadata["authors"], list):
                        metadata["authors"] = ", ".join(metadata["authors"][:10])  # Limitar a 10 autores
                    if "keywords" in metadata and isinstance(metadata["keywords"], list):
                        metadata["keywords"] = ", ".join(metadata["keywords"][:10])  # Limitar a 10 keywords
                    if "references" in metadata and isinstance(metadata["references"], list):
                        metadata["references"] = ", ".join(metadata["references"][:5])  # Limitar a 5 referências
                    metadatas.append(metadata)
                
                # Gerar embeddings
                logger.info(f"  Gerando embeddings para batch {i//batch_size + 1}...")
                embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=False).tolist()
                
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
                import traceback
                traceback.print_exc()
                continue
        
        logger.info(f"\n✅ Total de {total_added} chunks adicionados ao RAG!")
        
        # Verificar
        try:
            count = collection.count()
            logger.info(f"📊 Total na collection: {count} documentos")
        except:
            pass
        
        return True
        
    except ImportError as e:
        logger.error(f"❌ Bibliotecas não instaladas: {e}")
        logger.info("\n📦 Instale as dependências:")
        logger.info("   pip3 install chromadb sentence-transformers")
        return False
    except Exception as e:
        logger.error(f"❌ Erro ao adicionar ao ChromaDB: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Adicionar papers ao RAG (modo persistente)")
    parser.add_argument("--file", type=str, 
                       default="data/raw/papers_neurodivergence_20260108_224656_chunks.json",
                       help="Arquivo JSON com chunks processados")
    parser.add_argument("--collection", type=str, default="neurodivergence_papers",
                       help="Nome da collection no ChromaDB")
    parser.add_argument("--db-path", type=str, default="./chroma_db",
                       help="Caminho do banco ChromaDB")
    
    args = parser.parse_args()
    
    # Carregar chunks
    logger.info(f"📂 Carregando chunks de: {args.file}")
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
    success = add_to_chromadb_persistent(chunks, args.collection, args.db_path)
    
    if success:
        logger.info("\n🎉 Papers adicionados ao RAG com sucesso!")
        logger.info(f"📁 Banco de dados: {args.db_path}")
        logger.info(f"📚 Collection: {args.collection}")
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
