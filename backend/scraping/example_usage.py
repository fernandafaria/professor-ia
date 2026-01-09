"""
Exemplo de uso do sistema de scraping.
"""

import logging
from scraping import ScrapingPipeline
from scraping.utils import setup_logging, format_scraping_stats

# Configurar logging
setup_logging("INFO")
logger = logging.getLogger(__name__)


def example_single_source():
    """Exemplo: scraping de uma fonte específica."""
    print("\n" + "="*60)
    print("Exemplo 1: Scraping de fonte específica (API BNCC)")
    print("="*60)
    
    pipeline = ScrapingPipeline()
    
    # Fazer scraping da API BNCC
    documents = pipeline.scrape_source(
        "API BNCC Cientificar",
        disciplines=["Matemática", "Língua Portuguesa"],  # Filtrar disciplinas
        grades=["6º/7º ano", "8º/9º ano"],  # Filtrar séries
    )
    
    print(f"\n✓ Documentos coletados: {len(documents)}")
    
    # Adicionar ao RAG
    if documents:
        pipeline.add_to_rag(documents)
        print("✓ Documentos adicionados ao RAG")


def example_priority_scraping():
    """Exemplo: scraping por prioridade."""
    print("\n" + "="*60)
    print("Exemplo 2: Scraping por prioridade (critical)")
    print("="*60)
    
    pipeline = ScrapingPipeline()
    
    # Fazer scraping de todas as fontes críticas
    documents = pipeline.scrape_by_priority(
        priority="critical",
        max_sources=3,  # Limitar número de fontes
    )
    
    print(f"\n✓ Documentos coletados: {len(documents)}")
    
    # Adicionar ao RAG
    if documents:
        pipeline.add_to_rag(documents, batch_size=50)
        print("✓ Documentos adicionados ao RAG")


def example_full_pipeline():
    """Exemplo: pipeline completo."""
    print("\n" + "="*60)
    print("Exemplo 3: Pipeline completo")
    print("="*60)
    
    pipeline = ScrapingPipeline()
    
    # Executar pipeline completo
    stats = pipeline.run_full_pipeline(
        priorities=["critical", "very_high", "high"],
        add_to_rag=True,
    )
    
    # Exibir estatísticas
    print("\n" + format_scraping_stats(stats))


def example_cultural_scraping():
    """Exemplo: scraping de fontes culturais."""
    print("\n" + "="*60)
    print("Exemplo 4: Scraping de fontes culturais")
    print("="*60)
    
    pipeline = ScrapingPipeline()
    
    # Fazer scraping de fontes culturais (games, futebol, música)
    cultural_sources = [
        "Fandom Wikis",
        "Globo Esporte",
        "Letras.mus.br",
    ]
    
    all_documents = []
    for source_name in cultural_sources:
        try:
            documents = pipeline.scrape_source(
                source_name,
                max_articles=10,  # Limitar para exemplo
            )
            all_documents.extend(documents)
            print(f"✓ {source_name}: {len(documents)} documentos")
        except Exception as e:
            print(f"✗ {source_name}: Erro - {e}")
    
    print(f"\n✓ Total: {len(all_documents)} documentos culturais coletados")
    
    # Adicionar ao RAG
    if all_documents:
        pipeline.add_to_rag(all_documents)
        print("✓ Documentos adicionados ao RAG")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Exemplos de Uso - Sistema de Scraping P1A")
    print("="*60)
    
    # Descomentar o exemplo que deseja executar:
    
    # example_single_source()
    # example_priority_scraping()
    # example_full_pipeline()
    # example_cultural_scraping()
    
    print("\n" + "="*60)
    print("Descomente um dos exemplos acima para executar")
    print("="*60)
