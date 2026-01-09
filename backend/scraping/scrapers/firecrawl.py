"""
Scraper usando Firecrawl para web scraping avançado.
Suporta tanto API direta quanto integração via MCP.
"""

import logging
import os
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)

try:
    from firecrawl import FirecrawlApp
    FIRECRAWL_AVAILABLE = True
except ImportError:
    FIRECRAWL_AVAILABLE = False
    logger.warning("Biblioteca firecrawl não instalada. Instale com: pip install firecrawl-py")


class FirecrawlScraper(BaseScraper):
    """
    Scraper usando Firecrawl para fazer scraping de páginas web.
    
    Firecrawl é especialmente útil para:
    - Páginas com JavaScript (SPA)
    - Sites com proteção anti-bot
    - Extração de conteúdo limpo e estruturado
    - Scraping em larga escala
    """
    
    def __init__(self, source_config: Dict[str, Any]):
        """
        Inicializa scraper Firecrawl.
        
        Args:
            source_config: Configuração da fonte do sources.yaml
        """
        super().__init__(source_config, respect_robots=False)  # Firecrawl gerencia isso
        
        # API Key do Firecrawl
        self.api_key = os.getenv("FIRECRAWL_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "FIRECRAWL_API_KEY não configurada. "
                "Configure a variável de ambiente ou no .env"
            )
        
        # Inicializar cliente Firecrawl
        if FIRECRAWL_AVAILABLE:
            self.client = FirecrawlApp(api_key=self.api_key)
        else:
            self.client = None
            logger.error("Biblioteca firecrawl não disponível")
    
    def _scrape_url(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Faz scraping de uma URL usando Firecrawl.
        
        Args:
            url: URL para fazer scraping
            params: Parâmetros adicionais para Firecrawl
            
        Returns:
            Dados extraídos ou None em caso de erro
        """
        if not self.client:
            logger.error("Cliente Firecrawl não disponível")
            return None
        
        try:
            # Parâmetros padrão
            scrape_params = {
                "formats": ["markdown", "html"],  # Formato markdown é mais limpo
                "onlyMainContent": True,  # Apenas conteúdo principal
                "includeTags": ["article", "main", "section"],  # Tags HTML relevantes
            }
            
            if params:
                scrape_params.update(params)
            
            logger.debug(f"Fazendo scraping com Firecrawl: {url}")
            result = self.client.scrape_url(url, params=scrape_params)
            
            if not result or not result.get("success"):
                logger.warning(f"Falha ao fazer scraping de {url}: {result.get('error', 'Unknown error')}")
                return None
            
            return result.get("data", {})
            
        except Exception as e:
            logger.error(f"Erro ao fazer scraping de {url} com Firecrawl: {e}", exc_info=True)
            return None
    
    def _crawl_site(
        self,
        url: str,
        max_pages: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Faz crawling de um site inteiro usando Firecrawl.
        
        Args:
            url: URL base do site
            max_pages: Número máximo de páginas a coletar
            params: Parâmetros adicionais para Firecrawl
            
        Returns:
            Lista de páginas coletadas
        """
        if not self.client:
            logger.error("Cliente Firecrawl não disponível")
            return []
        
        try:
            crawl_params = {
                "limit": max_pages or 10,
                "formats": ["markdown", "html"],
                "onlyMainContent": True,
            }
            
            if params:
                crawl_params.update(params)
            
            logger.info(f"Iniciando crawling de {url} (max_pages={max_pages})")
            result = self.client.crawl_url(url, params=crawl_params)
            
            if not result or not result.get("success"):
                logger.warning(f"Falha ao fazer crawling de {url}: {result.get('error', 'Unknown error')}")
                return []
            
            pages = result.get("data", [])
            logger.info(f"Crawling concluído: {len(pages)} páginas coletadas")
            
            return pages
            
        except Exception as e:
            logger.error(f"Erro ao fazer crawling de {url} com Firecrawl: {e}", exc_info=True)
            return []
    
    def _extract_from_firecrawl_data(
        self,
        firecrawl_data: Dict[str, Any],
        url: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extrai e normaliza dados do resultado do Firecrawl.
        
        Args:
            firecrawl_data: Dados retornados pelo Firecrawl
            url: URL original
            
        Returns:
            Dados normalizados ou None
        """
        # Firecrawl retorna dados em diferentes formatos
        content = ""
        title = ""
        
        # Tentar extrair markdown (preferido)
        if "markdown" in firecrawl_data:
            content = firecrawl_data["markdown"]
        
        # Fallback para HTML limpo
        elif "html" in firecrawl_data:
            content = firecrawl_data["html"]
        
        # Fallback para texto
        elif "text" in firecrawl_data:
            content = firecrawl_data["text"]
        
        # Extrair título
        if "metadata" in firecrawl_data:
            metadata = firecrawl_data["metadata"]
            title = metadata.get("title", "")
            if not title and "og:title" in metadata:
                title = metadata["og:title"]
        
        # Se não encontrou título, tentar extrair do conteúdo markdown
        if not title and content:
            lines = content.split("\n")
            for line in lines[:5]:  # Verificar primeiras 5 linhas
                line = line.strip()
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
        
        if not content:
            return None
        
        # Extrair metadados adicionais
        metadata = firecrawl_data.get("metadata", {})
        
        return {
            "title": title or "Conteúdo Firecrawl",
            "content": content,
            "metadata": {
                "type": self.config.get("type", "web_content"),
                "source_url": url,
                "description": metadata.get("description", ""),
                "author": metadata.get("author", ""),
                "published_date": metadata.get("publishedTime", ""),
                "language": metadata.get("language", "pt-BR"),
                **metadata,
            },
            "tags": metadata.get("keywords", []),
            "url": url,
        }
    
    def scrape(
        self,
        urls: Optional[List[str]] = None,
        crawl: bool = False,
        max_pages: Optional[int] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping usando Firecrawl.
        
        Args:
            urls: Lista de URLs específicas para fazer scraping (opcional)
            crawl: Se True, faz crawling do site inteiro a partir da URL base
            max_pages: Número máximo de páginas (para crawl)
            **kwargs: Parâmetros adicionais para Firecrawl
            
        Returns:
            Lista de documentos normalizados
        """
        documents = []
        
        if crawl:
            # Modo crawling: coletar múltiplas páginas do site
            pages = self._crawl_site(
                url=self.url,
                max_pages=max_pages,
                params=kwargs
            )
            
            for page in pages:
                page_url = page.get("url", "")
                if not page_url:
                    continue
                
                doc = self._extract_from_firecrawl_data(page, page_url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        elif urls:
            # Modo URL específica: fazer scraping de URLs fornecidas
            for url in urls:
                firecrawl_data = self._scrape_url(url, params=kwargs)
                if not firecrawl_data:
                    continue
                
                doc = self._extract_from_firecrawl_data(firecrawl_data, url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        else:
            # Modo padrão: fazer scraping da URL base
            firecrawl_data = self._scrape_url(self.url, params=kwargs)
            if firecrawl_data:
                doc = self._extract_from_firecrawl_data(firecrawl_data, self.url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        logger.info(f"Scraping Firecrawl concluído: {len(documents)} documentos coletados")
        return documents
    
    def scrape_article_list(
        self,
        list_url: str,
        article_selector: str = "a[href]",
        max_articles: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de uma lista de artigos e depois coleta cada artigo.
        
        Args:
            list_url: URL da página de listagem
            article_selector: Seletor CSS para links de artigos
            max_articles: Número máximo de artigos a coletar
            
        Returns:
            Lista de artigos coletados
        """
        # Primeiro, fazer scraping da página de listagem
        list_data = self._scrape_url(list_url)
        if not list_data:
            return []
        
        # Extrair URLs de artigos do markdown ou HTML
        content = list_data.get("markdown", "") or list_data.get("html", "")
        if not content:
            return []
        
        # Parse básico para extrair links
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")
        
        article_urls = []
        links = soup.select(article_selector)
        for link in links:
            href = link.get("href", "")
            if href:
                # Converter para URL absoluta
                if href.startswith("/"):
                    href = f"{self.url}{href}"
                elif not href.startswith("http"):
                    href = f"{self.url}/{href}"
                
                if href not in article_urls:
                    article_urls.append(href)
        
        # Limitar número de artigos
        if max_articles:
            article_urls = article_urls[:max_articles]
        
        logger.info(f"Encontrados {len(article_urls)} artigos. Coletando...")
        
        # Coletar cada artigo
        return self.scrape(urls=article_urls)
