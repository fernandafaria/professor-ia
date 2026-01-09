"""
Scraper para Nova Escola (planos de aula e conteúdos educacionais).
"""

import logging
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)


class NovaEscolaScraper(BaseScraper):
    """Scraper para Nova Escola."""
    
    def __init__(self, source_config: Dict[str, Any]):
        """Inicializa scraper da Nova Escola."""
        super().__init__(source_config)
        self.selectors = source_config.get("selectors", {})
    
    def _extract_article(self, html: str, article_url: str) -> Optional[Dict[str, Any]]:
        """
        Extrai dados de um artigo/plano de aula.
        
        Args:
            html: HTML da página do artigo
            article_url: URL do artigo
            
        Returns:
            Dicionário com dados do artigo ou None
        """
        soup = self._parse_html(html)
        
        # Extrair título
        title = ""
        title_elem = soup.select_one(self.selectors.get("title", "h1.article-title"))
        if title_elem:
            title = title_elem.get_text(strip=True)
        else:
            # Fallback para h1 genérico
            h1 = soup.find("h1")
            if h1:
                title = h1.get_text(strip=True)
        
        # Extrair conteúdo
        content = ""
        content_elem = soup.select_one(self.selectors.get("content", "div.article-body"))
        if content_elem:
            # Remover scripts e styles
            for script in content_elem(["script", "style"]):
                script.decompose()
            content = content_elem.get_text(separator="\n", strip=True)
        else:
            # Fallback: buscar article ou main
            article = soup.find("article") or soup.find("main")
            if article:
                for script in article(["script", "style"]):
                    script.decompose()
                content = article.get_text(separator="\n", strip=True)
        
        # Extrair tags
        tags = []
        tags_elems = soup.select(self.selectors.get("tags", "div.tags a"))
        for tag_elem in tags_elems:
            tag_text = tag_elem.get_text(strip=True)
            if tag_text:
                tags.append(tag_text)
        
        # Extrair habilidades BNCC
        bncc_skills = []
        bncc_elems = soup.select(self.selectors.get("bncc_skills", "div.bncc-habilidades"))
        for bncc_elem in bncc_elems:
            skill_text = bncc_elem.get_text(strip=True)
            if skill_text:
                bncc_skills.append(skill_text)
        
        # Extrair série/ano
        grade = ""
        grade_elem = soup.select_one(self.selectors.get("grade", "span.serie"))
        if grade_elem:
            grade = grade_elem.get_text(strip=True)
        
        # Extrair disciplina
        subject = ""
        subject_elem = soup.select_one(self.selectors.get("subject", "span.disciplina"))
        if subject_elem:
            subject = subject_elem.get_text(strip=True)
        
        if not title and not content:
            return None
        
        return {
            "title": title or "Artigo Nova Escola",
            "content": content,
            "metadata": {
                "type": "lesson_plan" if "plano" in title.lower() or "plano" in content.lower()[:200] else "article",
                "subject": subject,
                "grade": grade,
                "bncc_skills": bncc_skills,
            },
            "tags": tags + [subject, grade] if subject and grade else tags + ([subject] if subject else []),
            "url": article_url,
        }
    
    def _extract_article_list(self, html: str) -> List[str]:
        """
        Extrai lista de URLs de artigos de uma página de listagem.
        
        Args:
            html: HTML da página de listagem
            
        Returns:
            Lista de URLs de artigos
        """
        soup = self._parse_html(html)
        article_urls = []
        
        # Buscar links de artigos (múltiplos seletores possíveis)
        article_links = soup.select("article a[href], div.article a[href], a[href*='/artigo/'], a[href*='/plano/']")
        
        for link in article_links:
            href = link.get("href", "")
            if href:
                # Converter para URL absoluta se necessário
                if href.startswith("/"):
                    href = f"{self.url}{href}"
                elif not href.startswith("http"):
                    href = f"{self.url}/{href}"
                
                # Evitar duplicatas
                if href not in article_urls and self.url in href:
                    article_urls.append(href)
        
        return article_urls
    
    def scrape(
        self,
        subject: Optional[str] = None,
        grade: Optional[str] = None,
        content_type: Optional[str] = None,  # "lesson_plan", "article", etc.
        max_articles: Optional[int] = None,
        start_page: int = 1,
        max_pages: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de artigos/planos de aula da Nova Escola.
        
        Args:
            subject: Disciplina para filtrar (opcional)
            grade: Série/ano para filtrar (opcional)
            content_type: Tipo de conteúdo (opcional)
            max_articles: Número máximo de artigos a coletar
            start_page: Página inicial
            max_pages: Número máximo de páginas a processar
            
        Returns:
            Lista de artigos normalizados
        """
        documents = []
        page = start_page
        articles_collected = 0
        
        logger.info(f"Iniciando scraping Nova Escola (subject={subject}, grade={grade}, max={max_articles})")
        
        while True:
            # Construir URL da página de listagem
            list_url = f"{self.url}/conteudo"
            params = {"page": page}
            
            if subject:
                params["disciplina"] = subject
            if grade:
                params["serie"] = grade
            if content_type:
                params["tipo"] = content_type
            
            response = self._fetch(list_url, params=params)
            if not response:
                # Tentar URL alternativa sem parâmetros
                list_url = f"{self.url}"
                response = self._fetch(list_url)
                if not response:
                    logger.warning(f"Falha ao buscar página {page}")
                    break
            
            # Extrair URLs de artigos
            article_urls = self._extract_article_list(response.text)
            
            if not article_urls:
                logger.info(f"Nenhum artigo encontrado na página {page}")
                break
            
            # Processar cada artigo
            for article_url in article_urls:
                if max_articles and articles_collected >= max_articles:
                    logger.info(f"Limite de {max_articles} artigos atingido")
                    break
                
                article_response = self._fetch(article_url)
                if not article_response:
                    continue
                
                article_data = self._extract_article(
                    article_response.text,
                    article_url
                )
                
                if article_data and self.validate_data(article_data):
                    documents.append(self.normalize_data(article_data))
                    articles_collected += 1
                    logger.debug(f"Artigo coletado: {articles_collected}")
            
            # Verificar se deve continuar
            if max_articles and articles_collected >= max_articles:
                break
            
            if max_pages and page >= start_page + max_pages - 1:
                break
            
            page += 1
        
        logger.info(f"Scraping Nova Escola concluído: {len(documents)} artigos coletados")
        return documents
