"""
Scraper simplificado usando Firecrawl MCP via subprocess direto.

Esta versão usa o MCP do Firecrawl de forma mais direta, chamando o servidor
MCP através de subprocess e comunicação via stdin/stdout.
"""

import os
import json
import subprocess
import logging
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)


class FirecrawlMCPSimpleScraper(BaseScraper):
    """
    Scraper simplificado usando Firecrawl MCP.
    
    Usa o servidor MCP do Firecrawl diretamente através de subprocess.
    """
    
    def __init__(self, source_config: Dict[str, Any]):
        """Inicializa scraper Firecrawl MCP."""
        super().__init__(source_config, respect_robots=False)
        
        self.api_key = os.getenv("FIRECRAWL_API_KEY", "")
        if not self.api_key:
            raise ValueError("FIRECRAWL_API_KEY não configurada")
    
    def _run_mcp_command(
        self,
        command: str,
        args: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Executa comando MCP do Firecrawl.
        
        Args:
            command: Comando MCP (scrape, crawl)
            args: Argumentos do comando
            
        Returns:
            Resultado ou None
        """
        try:
            # Usar a biblioteca firecrawl-py diretamente é mais simples
            # Mas se quiser usar MCP, podemos fazer via HTTP ou subprocess
            
            # Alternativa: usar firecrawl-py que já está instalado
            # e funciona de forma similar ao MCP
            from firecrawl import FirecrawlApp
            
            client = FirecrawlApp(api_key=self.api_key)
            
            if command == "scrape":
                result = client.scrape_url(args["url"], params={
                    "formats": ["markdown"],
                    "onlyMainContent": True,
                    **{k: v for k, v in args.items() if k != "url"}
                })
                return result.get("data", {}) if result else None
            
            elif command == "crawl":
                result = client.crawl(
                    url=args["url"],
                    limit=args.get("limit", 10),
                    formats=["markdown"],
                    only_main_content=True,
                )
                # O resultado pode ser uma lista de documentos ou um objeto com data
                if result:
                    if isinstance(result, list):
                        return result
                    elif hasattr(result, 'data'):
                        return result.data
                    elif hasattr(result, 'documents'):
                        return result.documents
                return None
            
            return None
            
        except ImportError:
            logger.error("firecrawl-py não instalado. Instale com: pip install firecrawl-py")
            return None
        except Exception as e:
            logger.error(f"Erro ao executar comando MCP {command}: {e}", exc_info=True)
            return None
    
    def scrape(
        self,
        urls: Optional[List[str]] = None,
        crawl: bool = False,
        max_pages: Optional[int] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping usando Firecrawl (via API, compatível com MCP).
        
        Args:
            urls: Lista de URLs específicas
            crawl: Se True, faz crawling
            max_pages: Número máximo de páginas
            **kwargs: Parâmetros adicionais
            
        Returns:
            Lista de documentos normalizados
        """
        documents = []
        
        if crawl:
            # Crawling
            result = self._run_mcp_command("crawl", {
                "url": self.url,
                "limit": max_pages or 10
            })
            
            if result:
                # Processar lista de documentos
                pages_list = result if isinstance(result, list) else [result]
                
                for page in pages_list:
                    # Pode ser um objeto Document ou dict
                    if hasattr(page, 'markdown'):
                        # É um objeto Document
                        page_url = page.metadata.url if hasattr(page, 'metadata') and hasattr(page.metadata, 'url') else self.url
                        content = page.markdown
                        title = page.metadata.title if hasattr(page, 'metadata') and hasattr(page.metadata, 'title') else ""
                    else:
                        # É um dict
                        page_url = page.get("url", self.url)
                        content = page.get("markdown", page.get("content", ""))
                        title = page.get("metadata", {}).get("title", "")
                    
                    if content:
                        doc = {
                            "title": title or "Conteúdo Firecrawl",
                            "content": content,
                            "metadata": {
                                "type": self.config.get("type", "web_content"),
                                "source_url": self.url,
                                "scraped_via": "firecrawl_mcp",
                            },
                            "tags": [],
                            "url": page_url,
                        }
                        
                        if self.validate_data(doc):
                            documents.append(self.normalize_data(doc))
        
        elif urls:
            # URLs específicas
            for url in urls:
                result = self._run_mcp_command("scrape", {"url": url, **kwargs})
                
                if result:
                    # Pode ser um dict ou objeto Document
                    if isinstance(result, dict):
                        content = result.get("markdown", result.get("content", ""))
                        title = result.get("metadata", {}).get("title", "")
                    else:
                        # Objeto Document
                        content = result.markdown if hasattr(result, 'markdown') else str(result)
                        title = result.metadata.title if hasattr(result, 'metadata') and hasattr(result.metadata, 'title') else ""
                    
                    if content:
                        doc = {
                            "title": title or "Conteúdo Firecrawl",
                            "content": content,
                            "metadata": {
                                "type": self.config.get("type", "web_content"),
                                "source_url": url,
                                "scraped_via": "firecrawl_mcp",
                            },
                            "tags": [],
                            "url": url,
                        }
                        
                        if self.validate_data(doc):
                            documents.append(self.normalize_data(doc))
        
        else:
            # URL base
            result = self._run_mcp_command("scrape", {"url": self.url, **kwargs})
            
            if result:
                # Pode ser um dict ou objeto Document
                if isinstance(result, dict):
                    content = result.get("markdown", result.get("content", ""))
                    title = result.get("metadata", {}).get("title", "")
                else:
                    # Objeto Document
                    content = result.markdown if hasattr(result, 'markdown') else str(result)
                    title = result.metadata.title if hasattr(result, 'metadata') and hasattr(result.metadata, 'title') else ""
                
                if content:
                    doc = {
                        "title": title or "Conteúdo Firecrawl",
                        "content": content,
                        "metadata": {
                            "type": self.config.get("type", "web_content"),
                            "source_url": self.url,
                            "scraped_via": "firecrawl_mcp",
                        },
                        "tags": [],
                        "url": self.url,
                    }
                    
                    if self.validate_data(doc):
                        documents.append(self.normalize_data(doc))
        
        logger.info(f"Scraping Firecrawl MCP concluído: {len(documents)} documentos coletados")
        return documents
