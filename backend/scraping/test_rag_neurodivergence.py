"""
Script para testar recuperação de papers do RAG.
"""

import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_rag_retrieval():
    """Testa recuperação de papers do RAG"""
    try:
        import chromadb
        from sentence_transformers import SentenceTransformer
        
        logger.info("Conectando ao ChromaDB...")
        client = chromadb.PersistentClient(path="./chroma_db")
        
        collection = client.get_collection("neurodivergence_papers")
        count = collection.count()
        logger.info(f"✅ Collection 'neurodivergence_papers' encontrada")
        logger.info(f"📊 Total de documentos: {count}")
        
        if count == 0:
            logger.warning("⚠️  Collection está vazia. Adicione papers primeiro.")
            return
        
        # Carregar modelo de embedding
        logger.info("Carregando modelo de embedding...")
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        
        # Testar buscas
        test_queries = [
            "estratégias educacionais para TDAH",
            "intervenções para dislexia",
            "autismo educação",
            "ADHD learning strategies"
        ]
        
        logger.info("\n" + "=" * 60)
        logger.info("TESTANDO RECUPERAÇÃO DE PAPERS")
        logger.info("=" * 60)
        
        for query in test_queries:
            logger.info(f"\n🔍 Query: '{query}'")
            
            # Gerar embedding da query
            query_embedding = model.encode(query, convert_to_numpy=True).tolist()
            
            # Buscar no ChromaDB
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=3
            )
            
            if results["ids"] and len(results["ids"][0]) > 0:
                logger.info(f"  ✅ Encontrados {len(results['ids'][0])} resultados:")
                
                for i, doc_id in enumerate(results["ids"][0], 1):
                    idx = results["ids"][0].index(doc_id)
                    metadata = results["metadatas"][0][idx]
                    content = results["documents"][0][idx]
                    distance = results["distances"][0][idx] if results["distances"] else None
                    
                    logger.info(f"\n  {i}. {metadata.get('title', 'Sem título')[:80]}...")
                    logger.info(f"     Fonte: {metadata.get('source', 'N/A')}")
                    logger.info(f"     Tipo: {metadata.get('neurodivergence_type', 'N/A')}")
                    if distance is not None:
                        logger.info(f"     Similaridade: {1-distance:.3f}")
                    logger.info(f"     Conteúdo: {content[:150]}...")
            else:
                logger.info("  ⚠️  Nenhum resultado encontrado")
        
        logger.info("\n" + "=" * 60)
        logger.info("✅ Teste concluído!")
        
    except ImportError as e:
        logger.error(f"❌ Bibliotecas não instaladas: {e}")
        logger.info("Instale: pip3 install chromadb sentence-transformers")
        return 1
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(test_rag_retrieval())
