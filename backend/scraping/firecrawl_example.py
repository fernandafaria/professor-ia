"""
Exemplo de uso do Firecrawl para web scraping das fontes prioritárias.

Este script demonstra como usar o Firecrawl para fazer scraping das fontes
mapeadas no documento mapeamento_webscraping_edtech.md.
"""

import os
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.scraping.scrapers.firecrawl import FirecrawlScraper
from backend.scraping.pipeline import ScrapingPipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def example_single_url():
    """Exemplo: fazer scraping de uma URL específica."""
    print("\n=== Exemplo 1: Scraping de URL única ===\n")
    
    source_config = {
        "name": "Nova Escola - Exemplo",
        "url": "https://novaescola.org.br/conteudo/12345/plano-de-aula",
        "type": "educational",
        "priority": "high",
    }
    
    scraper = FirecrawlScraper(source_config)
    documents = scraper.scrape()
    
    print(f"Documentos coletados: {len(documents)}")
    if documents:
        doc = documents[0]
        print(f"\nTítulo: {doc['title']}")
        print(f"Conteúdo (primeiros 200 chars): {doc['content'][:200]}...")
        print(f"URL: {doc['url']}")


def example_crawl_site():
    """Exemplo: fazer crawling de um site inteiro."""
    print("\n=== Exemplo 2: Crawling de site ===\n")
    
    source_config = {
        "name": "Nova Escola",
        "url": "https://novaescola.org.br",
        "type": "educational",
        "priority": "high",
    }
    
    scraper = FirecrawlScraper(source_config)
    
    # Fazer crawling limitado (10 páginas)
    documents = scraper.scrape(crawl=True, max_pages=10)
    
    print(f"Páginas coletadas: {len(documents)}")
    for i, doc in enumerate(documents[:3], 1):
        print(f"\n{i}. {doc['title']}")
        print(f"   URL: {doc['url']}")


def example_article_list():
    """Exemplo: coletar lista de artigos e depois cada artigo."""
    print("\n=== Exemplo 3: Lista de artigos ===\n")
    
    source_config = {
        "name": "Nova Escola",
        "url": "https://novaescola.org.br",
        "type": "educational",
        "priority": "high",
    }
    
    scraper = FirecrawlScraper(source_config)
    
    # Coletar artigos de uma página de listagem
    list_url = "https://novaescola.org.br/conteudo"
    documents = scraper.scrape_article_list(
        list_url=list_url,
        article_selector="a[href*='/conteudo/']",
        max_articles=5
    )
    
    print(f"Artigos coletados: {len(documents)}")
    for i, doc in enumerate(documents, 1):
        print(f"\n{i}. {doc['title']}")
        print(f"   URL: {doc['url']}")


def example_pipeline_integration():
    """Exemplo: usar Firecrawl através do pipeline."""
    print("\n=== Exemplo 4: Integração com Pipeline ===\n")
    
    pipeline = ScrapingPipeline()
    
    # Fazer scraping usando Firecrawl
    documents = pipeline.scrape_source(
        "Nova Escola",
        use_firecrawl=True,
        crawl=False,  # Apenas URL base
        max_pages=5
    )
    
    print(f"Documentos coletados: {len(documents)}")
    
    # Adicionar ao RAG (opcional)
    # pipeline.add_to_rag(documents)


def example_priority_sources():
    """Exemplo: fazer scraping das fontes prioritárias usando Firecrawl."""
    print("\n=== Exemplo 5: Fontes Prioritárias com Firecrawl ===\n")
    
    # Fontes prioritárias do mapeamento
    priority_sources = [
        {
            "name": "Nova Escola",
            "url": "https://novaescola.org.br",
            "type": "educational",
            "priority": "high",
        },
        {
            "name": "Projeto Ágatha Edu",
            "url": "https://www.projetoagathaedu.com.br",
            "type": "questions",
            "priority": "very_high",
        },
    ]
    
    all_documents = []
    
    for source_config in priority_sources:
        print(f"\nProcessando: {source_config['name']}")
        
        try:
            scraper = FirecrawlScraper(source_config)
            
            # Fazer scraping limitado para exemplo
            docs = scraper.scrape(crawl=True, max_pages=3)
            all_documents.extend(docs)
            
            print(f"  ✓ {len(docs)} documentos coletados")
            
        except Exception as e:
            print(f"  ✗ Erro: {e}")
    
    print(f"\nTotal: {len(all_documents)} documentos coletados")


def main():
    """Executa todos os exemplos."""
    # Verificar se API key está configurada
    if not os.getenv("FIRECRAWL_API_KEY"):
        print("ERRO: FIRECRAWL_API_KEY não configurada!")
        print("Configure a variável de ambiente:")
        print("  export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'")
        return
    
    print("=" * 60)
    print("Exemplos de uso do Firecrawl para Web Scraping")
    print("=" * 60)
    
    try:
        # Executar exemplos
        example_single_url()
        example_crawl_site()
        example_article_list()
        example_pipeline_integration()
        example_priority_sources()
        
        print("\n" + "=" * 60)
        print("Todos os exemplos concluídos!")
        print("=" * 60)
        
    except Exception as e:
        logger.error(f"Erro ao executar exemplos: {e}", exc_info=True)


if __name__ == "__main__":
    main()
