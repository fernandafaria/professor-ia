"""
CLI para execução de scraping.
"""

import argparse
import logging
from pathlib import Path
from .pipeline import ScrapingPipeline
from .utils import setup_logging, format_scraping_stats, save_documents_to_file

logger = logging.getLogger(__name__)


def main():
    """Função principal do CLI."""
    parser = argparse.ArgumentParser(
        description="Pipeline de scraping para plataforma educacional P1A"
    )
    
    parser.add_argument(
        "--source",
        type=str,
        help="Nome da fonte específica para fazer scraping",
    )
    
    parser.add_argument(
        "--priority",
        type=str,
        choices=["critical", "very_high", "high", "medium", "low"],
        help="Prioridade das fontes a processar",
    )
    
    parser.add_argument(
        "--priorities",
        nargs="+",
        default=["critical", "very_high", "high"],
        help="Lista de prioridades a processar (padrão: critical very_high high)",
    )
    
    parser.add_argument(
        "--max-sources",
        type=int,
        help="Número máximo de fontes a processar",
    )
    
    parser.add_argument(
        "--no-rag",
        action="store_true",
        help="Não adicionar documentos ao RAG",
    )
    
    parser.add_argument(
        "--save",
        type=str,
        help="Salvar documentos coletados em arquivo (caminho)",
    )
    
    parser.add_argument(
        "--format",
        type=str,
        choices=["json", "jsonl"],
        default="json",
        help="Formato do arquivo de saída (padrão: json)",
    )
    
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nível de logging (padrão: INFO)",
    )
    
    parser.add_argument(
        "--config",
        type=str,
        help="Caminho para arquivo sources.yaml (padrão: config/sources.yaml)",
    )
    
    parser.add_argument(
        "--use-firecrawl",
        action="store_true",
        help="Usar Firecrawl para scraping (recomendado para sites com JavaScript)",
    )
    
    parser.add_argument(
        "--crawl",
        action="store_true",
        help="Fazer crawling do site inteiro (apenas com --use-firecrawl)",
    )
    
    parser.add_argument(
        "--max-pages",
        type=int,
        help="Número máximo de páginas a coletar (apenas com --crawl)",
    )
    
    args = parser.parse_args()
    
    # Configurar logging
    setup_logging(args.log_level)
    
    # Inicializar pipeline
    try:
        pipeline = ScrapingPipeline(sources_config_path=args.config)
    except Exception as e:
        logger.error(f"Erro ao inicializar pipeline: {e}", exc_info=True)
        return 1
    
    # Executar scraping
    try:
        if args.source:
            # Scraping de fonte específica
            logger.info(f"Fazendo scraping de fonte específica: {args.source}")
            
            # Preparar kwargs para Firecrawl se necessário
            scraper_kwargs = {}
            if args.use_firecrawl:
                scraper_kwargs["use_firecrawl"] = True
                if args.crawl:
                    scraper_kwargs["crawl"] = True
                    if args.max_pages:
                        scraper_kwargs["max_pages"] = args.max_pages
            
            documents = pipeline.scrape_source(
                args.source,
                **scraper_kwargs
            )
            
            if args.save:
                save_documents_to_file(documents, args.save, args.format)
            
            if not args.no_rag and documents:
                pipeline.add_to_rag(documents)
            
            print(f"\n✓ Scraping concluído: {len(documents)} documentos coletados")
            
        elif args.priority:
            # Scraping por prioridade
            logger.info(f"Fazendo scraping de fontes com prioridade: {args.priority}")
            documents = pipeline.scrape_by_priority(
                priority=args.priority,
                max_sources=args.max_sources
            )
            
            if args.save:
                save_documents_to_file(documents, args.save, args.format)
            
            if not args.no_rag and documents:
                pipeline.add_to_rag(documents)
            
            print(f"\n✓ Scraping concluído: {len(documents)} documentos coletados")
            
        else:
            # Pipeline completo
            logger.info("Executando pipeline completo de scraping")
            stats = pipeline.run_full_pipeline(
                priorities=args.priorities,
                add_to_rag=not args.no_rag
            )
            
            if args.save:
                # Salvar todos os documentos (precisa coletar novamente ou salvar do stats)
                logger.warning("Opção --save não disponível para pipeline completo")
            
            print("\n" + format_scraping_stats(stats))
    
    except KeyboardInterrupt:
        logger.info("Scraping interrompido pelo usuário")
        return 130
    except Exception as e:
        logger.error(f"Erro durante scraping: {e}", exc_info=True)
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
