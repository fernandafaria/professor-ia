"""Sistema de web scraping para coleta de conteúdo."""

from .pipeline import ScrapingPipeline
from .processors import ContentProcessor
from .scrapers import (
    BaseScraper,
    BNCCAPIScraper,
    ProjetoAgathaScraper,
    NovaEscolaScraper,
    CulturalScraper,
    WikiScraper,
)
from .importers import BNCCJSONImporter

__all__ = [
    "ScrapingPipeline",
    "ContentProcessor",
    "BaseScraper",
    "BNCCAPIScraper",
    "ProjetoAgathaScraper",
    "NovaEscolaScraper",
    "CulturalScraper",
    "WikiScraper",
    "BNCCJSONImporter",
]