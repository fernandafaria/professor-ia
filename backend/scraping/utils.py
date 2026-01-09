"""
Utilitários para scraping.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO"):
    """Configura logging para scraping."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def validate_source_config(source_config: Dict[str, Any]) -> bool:
    """
    Valida configuração de fonte.
    
    Args:
        source_config: Configuração da fonte
        
    Returns:
        True se válida, False caso contrário
    """
    required_fields = ["name", "url", "type", "priority"]
    
    for field in required_fields:
        if field not in source_config:
            logger.error(f"Campo obrigatório ausente: {field}")
            return False
    
    # Validar valores
    valid_priorities = ["critical", "very_high", "high", "medium", "low"]
    if source_config["priority"] not in valid_priorities:
        logger.warning(f"Prioridade inválida: {source_config['priority']}")
    
    return True


def format_scraping_stats(stats: Dict[str, Any]) -> str:
    """
    Formata estatísticas de scraping para exibição.
    
    Args:
        stats: Estatísticas do scraping
        
    Returns:
        String formatada
    """
    lines = [
        "=" * 50,
        "Estatísticas de Scraping",
        "=" * 50,
        f"Fontes processadas: {stats.get('sources_processed', 0)}",
        f"Documentos coletados: {stats.get('documents_collected', 0)}",
        f"Chunks criados: {stats.get('chunks_created', 0)}",
    ]
    
    if stats.get("added_to_rag"):
        lines.append(f"Adicionado ao RAG: Sim")
    else:
        lines.append(f"Adicionado ao RAG: Não")
    
    if stats.get("errors"):
        lines.append(f"\nErros ({len(stats['errors'])}):")
        for error in stats["errors"]:
            lines.append(f"  - {error}")
    
    lines.append("=" * 50)
    
    return "\n".join(lines)


def save_documents_to_file(
    documents: list,
    filepath: str,
    format: str = "json"
):
    """
    Salva documentos coletados em arquivo.
    
    Args:
        documents: Lista de documentos
        filepath: Caminho do arquivo
        format: Formato (json, jsonl)
    """
    if format == "json":
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(documents, f, ensure_ascii=False, indent=2)
    elif format == "jsonl":
        with open(filepath, "w", encoding="utf-8") as f:
            for doc in documents:
                f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    else:
        raise ValueError(f"Formato não suportado: {format}")
    
    logger.info(f"Documentos salvos em {filepath} ({len(documents)} documentos)")
