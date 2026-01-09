#!/usr/bin/env python3
"""
Script para popular RAG com conteúdo educacional (BNCC, planos de aula, etc).
Usa o pipeline de scraping para coletar e adicionar conteúdo educacional.
"""

import sys
import logging
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importar usando caminho relativo
from populate_rag import RAGPopulator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Popular RAG com conteúdo educacional"
    )
    parser.add_argument(
        "--phase",
        type=str,
        choices=["mvp", "cultural", "all"],
        default="mvp",
        help="Fase a executar: mvp (BNCC, Ágatha, Nova Escola), cultural, ou all"
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
    
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("🚀 Popular RAG com Conteúdo Educacional")
    logger.info("=" * 60)
    logger.info("")
    
    # Verificar configurações
    import os
    use_firecrawl = not args.no_firecrawl and os.getenv("FIRECRAWL_API_KEY")
    
    if not use_firecrawl:
        logger.warning("⚠️  FIRECRAWL_API_KEY não configurada - usando scrapers tradicionais")
    
    populator = RAGPopulator()
    
    try:
        if args.phase == "mvp":
            logger.info("📚 FASE MVP: Coletando conteúdo educacional prioritário")
            logger.info("   - API BNCC Cientificar (estrutura curricular)")
            logger.info("   - Projeto Ágatha Edu (questões ENEM/vestibulares)")
            logger.info("   - Nova Escola (planos de aula)")
            logger.info("")
            
            stats = populator.populate_phase1_mvp(use_firecrawl=use_firecrawl)
            
            logger.info("")
            logger.info("=" * 60)
            logger.info("📊 RESUMO - FASE MVP")
            logger.info("=" * 60)
            logger.info(f"Total de chunks coletados: {stats.get('total_chunks', 0)}")
            logger.info(f"Adicionado ao RAG: {'✅ Sim' if stats.get('added_to_rag') else '❌ Não'}")
            
            if stats.get('sources'):
                logger.info("\n📚 Por fonte:")
                for source, source_stats in stats['sources'].items():
                    status = source_stats.get('status', 'unknown')
                    count = source_stats.get('documents', 0)
                    if status == 'success':
                        logger.info(f"   ✅ {source}: {count} documentos")
                    else:
                        logger.info(f"   ❌ {source}: Erro - {source_stats.get('error', 'Desconhecido')}")
            
            if stats.get('errors'):
                logger.warning(f"\n⚠️  {len(stats['errors'])} erros encontrados")
                for error in stats['errors'][:3]:  # Mostrar apenas primeiros 3
                    logger.warning(f"   - {error}")
        
        elif args.phase == "cultural":
            logger.info("🎨 FASE CULTURAL: Coletando conteúdo cultural")
            stats = populator.populate_cultural_content(max_pages_per_source=args.max_pages)
            
            logger.info("")
            logger.info("=" * 60)
            logger.info("📊 RESUMO - CONTEÚDO CULTURAL")
            logger.info("=" * 60)
            logger.info(f"Total de chunks: {stats.get('total_chunks', 0)}")
            logger.info(f"Adicionado ao RAG: {'✅ Sim' if stats.get('added_to_rag') else '❌ Não'}")
        
        elif args.phase == "all":
            logger.info("🌐 FASE COMPLETA: Coletando todo o conteúdo")
            mvp_stats = populator.populate_phase1_mvp(use_firecrawl=use_firecrawl)
            cultural_stats = populator.populate_cultural_content(max_pages_per_source=args.max_pages)
            
            logger.info("")
            logger.info("=" * 60)
            logger.info("📊 RESUMO COMPLETO")
            logger.info("=" * 60)
            logger.info(f"MVP - Chunks: {mvp_stats.get('total_chunks', 0)}")
            logger.info(f"Cultural - Chunks: {cultural_stats.get('total_chunks', 0)}")
            total = mvp_stats.get('total_chunks', 0) + cultural_stats.get('total_chunks', 0)
            logger.info(f"Total: {total}")
        
        logger.info("")
        logger.info("✅ Processo concluído!")
        logger.info("")
        logger.info("🧪 Verificar documentos no RAG:")
        logger.info("   python3 -c \"")
        logger.info("   from app.services.database import get_db")
        logger.info("   from sqlalchemy import text")
        logger.info("   db = next(get_db())")
        logger.info("   result = db.execute(text('SELECT source, COUNT(*) FROM rag_documents GROUP BY source'))")
        logger.info("   for row in result: print(f'{row[0]}: {row[1]} documentos')")
        logger.info("   \"")
        
        return 0
        
    except KeyboardInterrupt:
        logger.info("\n⚠️  Processo interrompido pelo usuário")
        return 1
    except Exception as e:
        logger.error(f"❌ Erro durante execução: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
