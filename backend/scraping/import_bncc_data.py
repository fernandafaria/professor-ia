"""
Script para importar dados BNCC já coletados.
"""

import argparse
import logging
from pathlib import Path
from .importers import BNCCJSONImporter
from .utils import setup_logging, format_scraping_stats

logger = logging.getLogger(__name__)


def main():
    """Função principal do importador."""
    parser = argparse.ArgumentParser(
        description="Importa dados BNCC de arquivo JSON para o sistema RAG"
    )
    
    parser.add_argument(
        "json_file",
        type=str,
        help="Caminho para arquivo JSON com dados BNCC",
    )
    
    parser.add_argument(
        "--categories",
        nargs="+",
        choices=["fundamental_education", "high_school"],
        help="Categorias a importar (padrão: todas)",
    )
    
    parser.add_argument(
        "--no-chunk",
        action="store_true",
        help="Não dividir documentos em chunks",
    )
    
    parser.add_argument(
        "--no-rag",
        action="store_true",
        help="Não adicionar documentos ao RAG",
    )
    
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Tamanho do lote para adicionar ao RAG (padrão: 100)",
    )
    
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nível de logging (padrão: INFO)",
    )
    
    args = parser.parse_args()
    
    # Configurar logging
    setup_logging(args.log_level)
    
    # Verificar se arquivo existe
    json_path = Path(args.json_file)
    if not json_path.exists():
        logger.error(f"Arquivo não encontrado: {json_path}")
        return 1
    
    # Inicializar importador
    try:
        importer = BNCCJSONImporter(str(json_path))
    except Exception as e:
        logger.error(f"Erro ao inicializar importador: {e}", exc_info=True)
        return 1
    
    # Importar dados
    try:
        logger.info("Iniciando importação de dados BNCC")
        stats = importer.import_data(
            categories=args.categories,
            chunk=not args.no_chunk,
            add_to_rag=not args.no_rag,
            batch_size=args.batch_size,
        )
        
        # Exibir estatísticas
        print("\n" + format_scraping_stats(stats))
        
        return 0
    
    except KeyboardInterrupt:
        logger.info("Importação interrompida pelo usuário")
        return 130
    except Exception as e:
        logger.error(f"Erro durante importação: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    exit(main())
