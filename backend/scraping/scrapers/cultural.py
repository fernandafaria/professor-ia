"""
Scrapers para fontes culturais (games, futebol, música, etc.).
"""

import logging
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)


class CulturalScraper(BaseScraper):
    """Scraper genérico para fontes culturais."""
    
    def __init__(self, source_config: Dict[str, Any]):
        """Inicializa scraper cultural."""
        super().__init__(source_config)
        self.selectors = source_config.get("selectors", {})
        self.cultural_type = source_config.get("type", "news")  # news, wiki, data, lyrics
    
    def _extract_article(self, html: str, article_url: str) -> Optional[Dict[str, Any]]:
        """Extrai dados de um artigo cultural."""
        soup = self._parse_html(html)
        
        # Título
        title = ""
        title_selector = self.selectors.get("title", "h1")
        title_elem = soup.select_one(title_selector)
        if title_elem:
            title = title_elem.get_text(strip=True)
        else:
            h1 = soup.find("h1")
            if h1:
                title = h1.get_text(strip=True)
        
        # Conteúdo
        content = ""
        content_selector = self.selectors.get("content", "article, div.content, main")
        content_elem = soup.select_one(content_selector)
        if content_elem:
            for script in content_elem(["script", "style", "nav", "footer", "header"]):
                script.decompose()
            content = content_elem.get_text(separator="\n", strip=True)
        
        # Tags
        tags = []
        tags_selector = self.selectors.get("tags", "div.tags a, a.tag")
        tags_elems = soup.select(tags_selector)
        for tag_elem in tags_elems:
            tag_text = tag_elem.get_text(strip=True)
            if tag_text:
                tags.append(tag_text)
        
        if not title and not content:
            return None
        
        return {
            "title": title or "Artigo",
            "content": content,
            "metadata": {
                "type": "cultural_content",
                "cultural_type": self.cultural_type,
            },
            "tags": tags,
            "url": article_url,
        }
    
    def _extract_article_list(self, html: str) -> List[str]:
        """Extrai lista de URLs de artigos."""
        soup = self._parse_html(html)
        article_urls = []
        
        # Buscar links de artigos
        article_links = soup.select("article a[href], div.article a[href], a[href*='/noticia/'], a[href*='/artigo/']")
        
        for link in article_links:
            href = link.get("href", "")
            if href:
                if href.startswith("/"):
                    href = f"{self.url}{href}"
                elif not href.startswith("http"):
                    href = f"{self.url}/{href}"
                
                if href not in article_urls and self.url in href:
                    article_urls.append(href)
        
        return article_urls
    
    def scrape(
        self,
        max_articles: Optional[int] = None,
        start_page: int = 1,
        max_pages: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de conteúdo cultural.
        
        Args:
            max_articles: Número máximo de artigos a coletar
            start_page: Página inicial
            max_pages: Número máximo de páginas a processar
            
        Returns:
            Lista de artigos normalizados
        """
        documents = []
        page = start_page
        articles_collected = 0
        
        logger.info(f"Iniciando scraping cultural: {self.name} (max={max_articles})")
        
        while True:
            list_url = f"{self.url}"
            if page > 1:
                list_url = f"{self.url}/page/{page}"
            
            response = self._fetch(list_url)
            if not response:
                logger.warning(f"Falha ao buscar página {page}")
                break
            
            article_urls = self._extract_article_list(response.text)
            
            if not article_urls:
                logger.info(f"Nenhum artigo encontrado na página {page}")
                break
            
            for article_url in article_urls:
                if max_articles and articles_collected >= max_articles:
                    break
                
                article_response = self._fetch(article_url)
                if not article_response:
                    continue
                
                article_data = self._extract_article(article_response.text, article_url)
                
                if article_data and self.validate_data(article_data):
                    documents.append(self.normalize_data(article_data))
                    articles_collected += 1
                    logger.debug(f"Artigo coletado: {articles_collected}")
            
            if max_articles and articles_collected >= max_articles:
                break
            
            if max_pages and page >= start_page + max_pages - 1:
                break
            
            page += 1
        
        logger.info(f"Scraping cultural concluído: {len(documents)} artigos coletados")
        return documents


class WikiScraper(CulturalScraper):
    """Scraper especializado para wikis (Fandom, Liquipedia, etc.)."""
    
    def _extract_article(self, html: str, article_url: str) -> Optional[Dict[str, Any]]:
        """Extrai dados de um artigo de wiki."""
        soup = self._parse_html(html)
        
        # Título
        title = ""
        title_elem = soup.select_one(self.selectors.get("title", "h1.page-header__title, h1"))
        if title_elem:
            title = title_elem.get_text(strip=True)
        
        # Conteúdo principal
        content = ""
        content_elem = soup.select_one(self.selectors.get("article", "article.mw-content-text, div.mw-parser-output"))
        if content_elem:
            # Remover elementos não relevantes
            for elem in content_elem(["script", "style", "nav", "aside", "table.navbox"]):
                elem.decompose()
            content = content_elem.get_text(separator="\n", strip=True)
        
        # Infobox (dados estruturados)
        infobox_data = {}
        infobox_elem = soup.select_one(self.selectors.get("infobox", "aside.portable-infobox, table.infobox"))
        if infobox_elem:
            rows = infobox_elem.select("tr")
            for row in rows:
                cells = row.select("td, th")
                if len(cells) >= 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    if key and value:
                        infobox_data[key] = value
        
        if not title and not content:
            return None
        
        return {
            "title": title or "Artigo Wiki",
            "content": content,
            "metadata": {
                "type": "wiki_article",
                "cultural_type": self.cultural_type,
                "infobox": infobox_data,
            },
            "tags": list(infobox_data.keys()) if infobox_data else [],
            "url": article_url,
        }
