"""
Script para fazer scraping usando Firecrawl MCP.

Este script demonstra como usar o Firecrawl através do MCP para fazer
scraping das fontes educacionais mapeadas.
"""

import os
import sys
import logging
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.scraping.pipeline import ScrapingPipeline

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def scrape_with_mcp(source_name: str, crawl: bool = True, max_pages: int = 10):
    """
    Faz scraping usando Firecrawl MCP.
    
    Args:
        source_name: Nome da fonte
        crawl: Se deve fazer crawling
        max_pages: Número máximo de páginas
    """
    # Verificar API key
    if not os.getenv("FIRECRAWL_API_KEY"):
        logger.error("FIRECRAWL_API_KEY não configurada!")
        logger.info("Configure com: export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'")
        return
    
    logger.info("=" * 60)
    logger.info(f"SCRAPING COM FIRECRAWL MCP: {source_name}")
    logger.info("=" * 60)
    
    pipeline = ScrapingPipeline()
    
    try:
        # Fazer scraping usando MCP
        documents = pipeline.scrape_source(
            source_name,
            use_firecrawl=True,
            use_mcp=True,  # Usar MCP do Firecrawl
            crawl=crawl,
            max_pages=max_pages
        )
        
        logger.info(f"\n✓ Coletados {len(documents)} documentos")
        
        # Mostrar alguns exemplos
        for i, doc in enumerate(documents[:3], 1):
            logger.info(f"\n{i}. {doc.get('title', 'Sem título')}")
            logger.info(f"   URL: {doc.get('url', 'N/A')}")
            logger.info(f"   Conteúdo: {doc.get('content', '')[:100]}...")
        
        # Adicionar ao RAG
        if documents:
            logger.info(f"\n📚 Adicionando {len(documents)} documentos ao RAG...")
            pipeline.add_to_rag(documents, batch_size=50)
            logger.info("✓ Documentos adicionados ao RAG!")
        
        return documents
        
    except Exception as e:
        logger.error(f"Erro durante scraping: {e}", exc_info=True)
        return []


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Fazer scraping usando Firecrawl MCP"
    )
    
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Nome da fonte para fazer scraping"
    )
    
    parser.add_argument(
        "--crawl",
        action="store_true",
        help="Fazer crawling do site inteiro"
    )
    
    parser.add_argument(
        "--max-pages",
        type=int,
        default=10,
        help="Número máximo de páginas (padrão: 10)"
    )
    
    parser.add_argument(
        "--no-rag",
        action="store_true",
        help="Não adicionar ao RAG"
    )
    
    args = parser.parse_args()
    
    documents = scrape_with_mcp(
        source_name=args.source,
        crawl=args.crawl,
        max_pages=args.max_pages
    )
    
    if not args.no_rag and documents:
        pipeline = ScrapingPipeline()
        pipeline.add_to_rag(documents)
        logger.info("✓ Documentos adicionados ao RAG")


if __name__ == "__main__":
    main()
