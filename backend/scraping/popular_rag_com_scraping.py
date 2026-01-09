#!/usr/bin/env python3
"""
Script para popular a base RAG com todos os arquivos de scraping existentes.
Carrega arquivos JSON de scraping e adiciona ao RAG no Supabase.
"""

import json
import sys
import logging
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# Adicionar diretório raiz ao path
backend_path = Path(__file__).parent.parent
sys.path.insert(0, str(backend_path))

from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_json_file(filepath: str) -> Any:
    """Carrega arquivo JSON."""
    file_path = Path(filepath)
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    logger.info(f"📂 Carregando: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    logger.info(f"✅ {len(data)} itens carregados")
    return data


def process_papers_to_documents(papers: List[Dict], chunks_file: str = None) -> List[Dict]:
    """
    Processa papers em documentos para RAG.
    
    Se chunks_file for fornecido, usa os chunks já processados.
    Caso contrário, processa os papers em chunks.
    """
    documents = []
    
    if chunks_file and Path(chunks_file).exists():
        # Usar chunks já processados
        logger.info(f"📚 Usando chunks processados de: {chunks_file}")
        chunks = load_json_file(chunks_file)
        
        for chunk in chunks:
            doc = {
                "content": chunk.get("content", ""),
                "metadata": chunk.get("metadata", {}),
                "source": chunk.get("metadata", {}).get("source", "neurodivergence_papers"),
                "subject": chunk.get("metadata", {}).get("subject"),
                "grade": chunk.get("metadata", {}).get("grade"),
            }
            documents.append(doc)
    else:
        # Processar papers em chunks
        logger.info("📝 Processando papers em chunks...")
        from scraping.processors.content_processor import ContentProcessor
        
        processor = ContentProcessor(chunk_size=2000, chunk_overlap=200)
        
        for paper in papers:
            # Criar conteúdo combinado
            content_parts = []
            if paper.get("title"):
                content_parts.append(f"Título: {paper['title']}")
            if paper.get("abstract"):
                content_parts.append(f"Resumo: {paper['abstract']}")
            
            content = "\n\n".join(content_parts)
            
            if not content:
                continue
            
            # Processar em chunks
            chunks = processor.process_text(
                content,
                metadata={
                    "title": paper.get("title", ""),
                    "authors": ", ".join(paper.get("authors", [])),
                    "publication_date": paper.get("publication_date", ""),
                    "doi": paper.get("doi", ""),
                    "source_url": paper.get("source_url", ""),
                    "source_database": paper.get("source_database", ""),
                    "neurodivergence_type": paper.get("neurodivergence_type", ""),
                    "source": "neurodivergence_papers",
                }
            )
            
            for chunk in chunks:
                doc = {
                    "content": chunk["content"],
                    "metadata": chunk.get("metadata", {}),
                    "source": "neurodivergence_papers",
                    "subject": None,  # Papers não têm matéria específica
                    "grade": None,  # Papers não têm série específica
                }
                documents.append(doc)
    
    logger.info(f"✅ {len(documents)} documentos processados para RAG")
    return documents


def add_documents_to_rag(documents: List[Dict], db) -> Dict[str, Any]:
    """Adiciona documentos ao RAG no Supabase."""
    retriever = RAGRetriever(db=db)
    
    logger.info(f"\n📚 Adicionando {len(documents)} documentos ao RAG...")
    
    stats = {
        "total": len(documents),
        "success": 0,
        "errors": 0,
        "error_messages": []
    }
    
    # Processar em batches
    batch_size = 50
    batch_documents = []
    batch_metadatas = []
    
    for i, doc in enumerate(documents):
        batch_documents.append(doc["content"])
        batch_metadatas.append(doc.get("metadata", {}))
        
        # Adicionar campos específicos ao metadata
        batch_metadatas[-1].update({
            "source": doc.get("source", "neurodivergence_papers"),
            "subject": doc.get("subject"),
            "grade": doc.get("grade"),
        })
        
        # Adicionar batch quando atingir o tamanho
        if len(batch_documents) >= batch_size or i == len(documents) - 1:
            try:
                retriever.add_documents(
                    documents=batch_documents,
                    metadatas=batch_metadatas,
                    db=db
                )
                stats["success"] += len(batch_documents)
                logger.info(f"  ✓ Batch {i // batch_size + 1}: {len(batch_documents)} documentos adicionados")
            except Exception as e:
                stats["errors"] += len(batch_documents)
                error_msg = f"Erro no batch {i // batch_size + 1}: {str(e)}"
                stats["error_messages"].append(error_msg)
                logger.error(f"  ✗ {error_msg}")
            
            # Limpar batch
            batch_documents = []
            batch_metadatas = []
    
    return stats


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Popular RAG com arquivos de scraping existentes"
    )
    parser.add_argument(
        "--papers-file",
        type=str,
        default="data/raw/papers_neurodivergence_20260108_224656.json",
        help="Arquivo JSON com papers"
    )
    parser.add_argument(
        "--chunks-file",
        type=str,
        default="data/raw/papers_neurodivergence_20260108_224656_chunks.json",
        help="Arquivo JSON com chunks processados (opcional)"
    )
    parser.add_argument(
        "--use-chunks",
        action="store_true",
        help="Usar arquivo de chunks se disponível"
    )
    
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("🚀 Popular RAG com Dados de Scraping")
    logger.info("=" * 60)
    logger.info("")
    
    # Carregar dados
    try:
        papers = load_json_file(args.papers_file)
    except FileNotFoundError as e:
        logger.error(f"❌ {e}")
        logger.info("\n💡 Arquivos disponíveis:")
        data_dir = Path(__file__).parent.parent / "data" / "raw"
        if data_dir.exists():
            for f in data_dir.glob("*.json"):
                logger.info(f"   - {f}")
        return 1
    
    # Processar documentos
    try:
        chunks_file = args.chunks_file if args.use_chunks else None
        documents = process_papers_to_documents(papers, chunks_file)
    except Exception as e:
        logger.error(f"❌ Erro ao processar documentos: {e}", exc_info=True)
        return 1
    
    if not documents:
        logger.warning("⚠️  Nenhum documento para adicionar")
        return 1
    
    # Adicionar ao RAG
    try:
        db = next(get_db())
        try:
            stats = add_documents_to_rag(documents, db)
            db.commit()  # Commit explícito
        except Exception as e:
            db.rollback()
            raise
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("📊 Estatísticas")
        logger.info("=" * 60)
        logger.info(f"Total de documentos: {stats['total']}")
        logger.info(f"✅ Adicionados com sucesso: {stats['success']}")
        logger.info(f"❌ Erros: {stats['errors']}")
        
        if stats['error_messages']:
            logger.info("\n⚠️  Erros encontrados:")
            for msg in stats['error_messages'][:5]:  # Mostrar apenas primeiros 5
                logger.info(f"   - {msg}")
        
        if stats['success'] > 0:
            logger.info("")
            logger.info("🎉 RAG populado com sucesso!")
            logger.info("")
            logger.info("🧪 Testar busca:")
            logger.info("   python3 -c \"")
            logger.info("   from app.services.database import get_db")
            logger.info("   from app.core.rag.retriever_supabase import RAGRetriever")
            logger.info("   db = next(get_db())")
            logger.info("   retriever = RAGRetriever(db=db)")
            logger.info("   results = retriever.retrieve('neurodivergência', db=db, n_results=3)")
            logger.info("   print(f'Encontrados {len(results)} documentos')")
            logger.info("   \"")
        
        return 0 if stats['errors'] == 0 else 1
        
    except Exception as e:
        logger.error(f"❌ Erro ao adicionar ao RAG: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
