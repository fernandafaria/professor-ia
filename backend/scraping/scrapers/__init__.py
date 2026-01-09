"""Scrapers especializados para diferentes fontes."""

from .base import BaseScraper
from .bncc_api import BNCCAPIScraper
from .projeto_agatha import ProjetoAgathaScraper
from .nova_escola import NovaEscolaScraper
from .cultural import CulturalScraper, WikiScraper
from .firecrawl import FirecrawlScraper
from .firecrawl_mcp_simple import FirecrawlMCPSimpleScraper

__all__ = [
    "BaseScraper",
    "BNCCAPIScraper",
    "ProjetoAgathaScraper",
    "NovaEscolaScraper",
    "CulturalScraper",
    "WikiScraper",
    "FirecrawlScraper",
    "FirecrawlMCPSimpleScraper",
]