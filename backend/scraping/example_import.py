"""
Exemplo de importação de dados BNCC já coletados.
"""

import logging
from pathlib import Path
from scraping.importers import BNCCJSONImporter
from scraping.utils import setup_logging, format_scraping_stats

# Configurar logging
setup_logging("INFO")
logger = logging.getLogger(__name__)


def example_import_all():
    """Exemplo: importar todos os dados BNCC."""
    print("\n" + "="*60)
    print("Exemplo: Importação completa de dados BNCC")
    print("="*60)
    
    # Caminho para o arquivo JSON
    json_file = Path(__file__).parent.parent.parent / "scraping" / "extract-data-2026-01-08 (1).json"
    
    if not json_file.exists():
        print(f"✗ Arquivo não encontrado: {json_file}")
        print("  Por favor, ajuste o caminho do arquivo no código")
        return
    
    # Inicializar importador
    importer = BNCCJSONImporter(str(json_file))
    
    # Importar todos os dados
    stats = importer.import_data(
        categories=None,  # Todas as categorias
        chunk=True,  # Dividir em chunks
        add_to_rag=True,  # Adicionar ao RAG
        batch_size=100,  # Processar em lotes de 100
    )
    
    # Exibir estatísticas
    print("\n" + format_scraping_stats(stats))


def example_import_fundamental_only():
    """Exemplo: importar apenas Ensino Fundamental."""
    print("\n" + "="*60)
    print("Exemplo: Importação apenas Ensino Fundamental")
    print("="*60)
    
    json_file = Path(__file__).parent.parent.parent / "scraping" / "extract-data-2026-01-08 (1).json"
    
    if not json_file.exists():
        print(f"✗ Arquivo não encontrado: {json_file}")
        return
    
    importer = BNCCJSONImporter(str(json_file))
    
    # Importar apenas Ensino Fundamental
    stats = importer.import_data(
        categories=["fundamental_education"],
        chunk=True,
        add_to_rag=True,
    )
    
    print("\n" + format_scraping_stats(stats))


def example_import_without_rag():
    """Exemplo: importar sem adicionar ao RAG (apenas processar)."""
    print("\n" + "="*60)
    print("Exemplo: Processamento sem adicionar ao RAG")
    print("="*60)
    
    json_file = Path(__file__).parent.parent.parent / "scraping" / "extract-data-2026-01-08 (1).json"
    
    if not json_file.exists():
        print(f"✗ Arquivo não encontrado: {json_file}")
        return
    
    importer = BNCCJSONImporter(str(json_file))
    
    # Processar sem adicionar ao RAG
    stats = importer.import_data(
        categories=None,
        chunk=True,
        add_to_rag=False,  # Não adicionar ao RAG
    )
    
    print("\n" + format_scraping_stats(stats))
    print("\nNota: Documentos processados mas não adicionados ao RAG")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Exemplos de Importação - Dados BNCC")
    print("="*60)
    
    # Descomentar o exemplo que deseja executar:
    
    # example_import_all()
    # example_import_fundamental_only()
    # example_import_without_rag()
    
    print("\n" + "="*60)
    print("Descomente um dos exemplos acima para executar")
    print("="*60)
    print("\nOu use o CLI:")
    print("  python -m backend.scraping.import_bncc_data 'scraping/extract-data-2026-01-08 (1).json'")
