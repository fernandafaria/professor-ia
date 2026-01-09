"""
Script para popular a base de conhecimento RAG com conteúdo educacional.

Este script coleta conteúdo das fontes prioritárias e adiciona ao sistema RAG.
"""

import os
import sys
import logging
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.scraping.pipeline import ScrapingPipeline
from backend.app.core.rag.retriever_supabase import RAGRetriever
from backend.app.config import settings
from backend.app.services.database import get_db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RAGPopulator:
    """Classe para popular a base de conhecimento RAG."""
    
    def __init__(self):
        """Inicializa o populador RAG."""
        self.pipeline = ScrapingPipeline()
        self.retriever = RAGRetriever()
        
    def populate_phase1_mvp(self, use_firecrawl: bool = True) -> Dict[str, Any]:
        """
        Popula RAG com fontes da Fase 1 (MVP).
        
        Fontes prioritárias:
        1. API BNCC Cientificar (estrutura curricular)
        2. Projeto Ágatha Edu (questões ENEM/vestibulares)
        3. Nova Escola (planos de aula)
        
        Args:
            use_firecrawl: Se deve usar Firecrawl para scraping
            
        Returns:
            Estatísticas da população
        """
        logger.info("=" * 60)
        logger.info("FASE 1 - MVP: Populando RAG com fontes prioritárias")
        logger.info("=" * 60)
        
        stats = {
            "phase": "MVP",
            "started_at": datetime.now().isoformat(),
            "sources": {},
            "total_documents": 0,
            "total_chunks": 0,
            "errors": [],
        }
        
        # 1. API BNCC Cientificar
        logger.info("\n[1/3] Coletando dados da API BNCC Cientificar...")
        try:
            bncc_docs = self.pipeline.scrape_source("API BNCC Cientificar")
            stats["sources"]["BNCC"] = {
                "documents": len(bncc_docs),
                "status": "success"
            }
            stats["total_chunks"] += len(bncc_docs)
            logger.info(f"✓ BNCC: {len(bncc_docs)} chunks coletados")
        except Exception as e:
            error_msg = f"Erro ao coletar BNCC: {e}"
            logger.error(error_msg, exc_info=True)
            stats["sources"]["BNCC"] = {"status": "error", "error": str(e)}
            stats["errors"].append(error_msg)
        
        # 2. Projeto Ágatha Edu (questões)
        logger.info("\n[2/3] Coletando questões do Projeto Ágatha Edu...")
        try:
            agatha_docs = self.pipeline.scrape_source(
                "Projeto Ágatha Edu",
                use_firecrawl=use_firecrawl,
                crawl=True,
                max_pages=50  # Começar com 50 páginas
            )
            stats["sources"]["Projeto Ágatha"] = {
                "documents": len(agatha_docs),
                "status": "success"
            }
            stats["total_chunks"] += len(agatha_docs)
            logger.info(f"✓ Projeto Ágatha: {len(agatha_docs)} chunks coletados")
        except Exception as e:
            error_msg = f"Erro ao coletar Projeto Ágatha: {e}"
            logger.error(error_msg, exc_info=True)
            stats["sources"]["Projeto Ágatha"] = {"status": "error", "error": str(e)}
            stats["errors"].append(error_msg)
        
        # 3. Nova Escola (planos de aula)
        logger.info("\n[3/3] Coletando planos de aula da Nova Escola...")
        try:
            nova_escola_docs = self.pipeline.scrape_source(
                "Nova Escola",
                use_firecrawl=use_firecrawl,
                crawl=True,
                max_pages=100  # Começar com 100 páginas
            )
            stats["sources"]["Nova Escola"] = {
                "documents": len(nova_escola_docs),
                "status": "success"
            }
            stats["total_chunks"] += len(nova_escola_docs)
            logger.info(f"✓ Nova Escola: {len(nova_escola_docs)} chunks coletados")
        except Exception as e:
            error_msg = f"Erro ao coletar Nova Escola: {e}"
            logger.error(error_msg, exc_info=True)
            stats["sources"]["Nova Escola"] = {"status": "error", "error": str(e)}
            stats["errors"].append(error_msg)
        
        # Consolidar todos os documentos
        all_documents = []
        for source_name, source_stats in stats["sources"].items():
            if source_stats.get("status") == "success":
                # Recuperar documentos da fonte
                docs = self.pipeline.scrape_source(source_name)
                all_documents.extend(docs)
        
        stats["total_documents"] = len(all_documents)
        
        # Adicionar ao RAG
        if all_documents:
            logger.info(f"\n📚 Adicionando {len(all_documents)} chunks ao RAG...")
            try:
                # Obter sessão do banco de dados
                db_gen = get_db()
                db = next(db_gen)
                try:
                    self.pipeline.add_to_rag(all_documents, batch_size=50, db=db)
                    stats["added_to_rag"] = True
                    logger.info("✓ Documentos adicionados ao RAG com sucesso!")
                finally:
                    db.close()
            except Exception as e:
                error_msg = f"Erro ao adicionar ao RAG: {e}"
                logger.error(error_msg, exc_info=True)
                stats["added_to_rag"] = False
                stats["errors"].append(error_msg)
        else:
            logger.warning("⚠ Nenhum documento para adicionar ao RAG")
            stats["added_to_rag"] = False
        
        stats["completed_at"] = datetime.now().isoformat()
        
        return stats
    
    def populate_cultural_content(
        self,
        max_pages_per_source: int = 20
    ) -> Dict[str, Any]:
        """
        Popula RAG com conteúdo cultural (games, futebol, música).
        
        Args:
            max_pages_per_source: Número máximo de páginas por fonte
            
        Returns:
            Estatísticas da população
        """
        logger.info("=" * 60)
        logger.info("FASE 2: Populando RAG com conteúdo cultural")
        logger.info("=" * 60)
        
        stats = {
            "phase": "Cultural",
            "started_at": datetime.now().isoformat(),
            "sources": {},
            "total_documents": 0,
            "total_chunks": 0,
            "errors": [],
        }
        
        cultural_sources = [
            "Fandom Wikis",
            "Globo Esporte",
            "Letras.mus.br",
        ]
        
        all_documents = []
        
        for source_name in cultural_sources:
            logger.info(f"\nColetando: {source_name}...")
            try:
                docs = self.pipeline.scrape_source(
                    source_name,
                    use_firecrawl=True,
                    crawl=True,
                    max_pages=max_pages_per_source
                )
                stats["sources"][source_name] = {
                    "documents": len(docs),
                    "status": "success"
                }
                all_documents.extend(docs)
                logger.info(f"✓ {source_name}: {len(docs)} chunks coletados")
            except Exception as e:
                error_msg = f"Erro ao coletar {source_name}: {e}"
                logger.error(error_msg, exc_info=True)
                stats["sources"][source_name] = {"status": "error", "error": str(e)}
                stats["errors"].append(error_msg)
        
        stats["total_chunks"] = len(all_documents)
        
        # Adicionar ao RAG
        if all_documents:
            logger.info(f"\n📚 Adicionando {len(all_documents)} chunks ao RAG...")
            try:
                # Obter sessão do banco de dados
                db_gen = get_db()
                db = next(db_gen)
                try:
                    self.pipeline.add_to_rag(all_documents, batch_size=50, db=db)
                    stats["added_to_rag"] = True
                    logger.info("✓ Documentos adicionados ao RAG com sucesso!")
                finally:
                    db.close()
            except Exception as e:
                error_msg = f"Erro ao adicionar ao RAG: {e}"
                logger.error(error_msg, exc_info=True)
                stats["added_to_rag"] = False
                stats["errors"].append(error_msg)
        
        stats["completed_at"] = datetime.now().isoformat()
        
        return stats
    
    def verify_rag_content(self) -> Dict[str, Any]:
        """
        Verifica o conteúdo atual no RAG no Supabase.
        
        Returns:
            Estatísticas do RAG
        """
        try:
            # Obter sessão do banco de dados
            db_gen = get_db()
            db = next(db_gen)
            try:
                from sqlalchemy import text
                
                # Contar documentos na tabela
                result = db.execute(text("SELECT COUNT(*) FROM rag_documents"))
                total_count = result.scalar()
                
                stats = {
                    "table_name": "rag_documents",
                    "total_documents": total_count,
                    "status": "success"
                }
                
                logger.info(f"✓ RAG Table: {stats['table_name']}")
                logger.info(f"✓ Total de documentos: {stats['total_documents']}")
                
                return stats
            finally:
                db.close()
            
        except Exception as e:
            logger.error(f"Erro ao verificar RAG: {e}", exc_info=True)
            return {
                "status": "error",
                "error": str(e)
            }
    
    def test_retrieval(self, query: str = "matemática básica") -> List[Dict]:
        """
        Testa a recuperação de documentos do RAG.
        
        Args:
            query: Query de teste
            
        Returns:
            Documentos recuperados
        """
        logger.info(f"\n🔍 Testando recuperação com query: '{query}'")
        
        try:
            # Obter sessão do banco de dados
            db_gen = get_db()
            db = next(db_gen)
            try:
                results = self.retriever.retrieve(query, db=db, n_results=3)
                
                logger.info(f"✓ {len(results)} documentos recuperados")
                for i, doc in enumerate(results, 1):
                    logger.info(f"\n  {i}. {doc.get('metadata', {}).get('title', 'Sem título')}")
                    logger.info(f"     Conteúdo: {doc.get('content', '')[:100]}...")
                
                return results
            finally:
                db.close()
            
        except Exception as e:
            logger.error(f"Erro ao testar recuperação: {e}", exc_info=True)
            return []


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Popular base de conhecimento RAG com conteúdo educacional"
    )
    
    parser.add_argument(
        "--phase",
        type=str,
        choices=["mvp", "cultural", "all", "verify", "test"],
        default="mvp",
        help="Fase a executar (mvp, cultural, all, verify, test)"
    )
    
    parser.add_argument(
        "--no-firecrawl",
        action="store_true",
        help="Não usar Firecrawl (usar scrapers tradicionais)"
    )
    
    parser.add_argument(
        "--max-pages",
        type=int,
        default=50,
        help="Número máximo de páginas por fonte (padrão: 50)"
    )
    
    parser.add_argument(
        "--test-query",
        type=str,
        default="matemática básica",
        help="Query para teste de recuperação"
    )
    
    args = parser.parse_args()
    
    # Verificar configurações
    if not os.getenv("FIRECRAWL_API_KEY") and not args.no_firecrawl:
        logger.warning(
            "⚠ FIRECRAWL_API_KEY não configurada. "
            "Usando scrapers tradicionais. Configure com: export FIRECRAWL_API_KEY='...'"
        )
        use_firecrawl = False
    else:
        use_firecrawl = not args.no_firecrawl
    
    populator = RAGPopulator()
    
    try:
        if args.phase == "mvp":
            stats = populator.populate_phase1_mvp(use_firecrawl=use_firecrawl)
            print("\n" + "=" * 60)
            print("RESUMO - FASE 1 (MVP)")
            print("=" * 60)
            print(f"Total de chunks: {stats['total_chunks']}")
            print(f"Adicionado ao RAG: {stats.get('added_to_rag', False)}")
            if stats.get('errors'):
                print(f"Erros: {len(stats['errors'])}")
            
        elif args.phase == "cultural":
            stats = populator.populate_cultural_content(max_pages_per_source=args.max_pages)
            print("\n" + "=" * 60)
            print("RESUMO - CONTEÚDO CULTURAL")
            print("=" * 60)
            print(f"Total de chunks: {stats['total_chunks']}")
            print(f"Adicionado ao RAG: {stats.get('added_to_rag', False)}")
            
        elif args.phase == "all":
            # Executar todas as fases
            mvp_stats = populator.populate_phase1_mvp(use_firecrawl=use_firecrawl)
            cultural_stats = populator.populate_cultural_content(max_pages_per_source=args.max_pages)
            
            print("\n" + "=" * 60)
            print("RESUMO COMPLETO")
            print("=" * 60)
            print(f"MVP - Chunks: {mvp_stats['total_chunks']}")
            print(f"Cultural - Chunks: {cultural_stats['total_chunks']}")
            print(f"Total: {mvp_stats['total_chunks'] + cultural_stats['total_chunks']}")
            
        elif args.phase == "verify":
            stats = populator.verify_rag_content()
            print("\n" + "=" * 60)
            print("VERIFICAÇÃO DO RAG")
            print("=" * 60)
            print(f"Collection: {stats.get('collection_name')}")
            print(f"Total documentos: {stats.get('total_documents')}")
            
        elif args.phase == "test":
            results = populator.test_retrieval(query=args.test_query)
            print("\n" + "=" * 60)
            print("TESTE DE RECUPERAÇÃO")
            print("=" * 60)
            print(f"Query: '{args.test_query}'")
            print(f"Resultados: {len(results)}")
            
    except KeyboardInterrupt:
        logger.info("\n⚠ Processo interrompido pelo usuário")
        return 1
    except Exception as e:
        logger.error(f"Erro durante execução: {e}", exc_info=True)
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
