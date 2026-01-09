"""
Scraper para Projeto Ágatha Edu (banco de questões).
"""

import logging
import re
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)


class ProjetoAgathaScraper(BaseScraper):
    """Scraper para Projeto Ágatha Edu."""
    
    def __init__(self, source_config: Dict[str, Any]):
        """Inicializa scraper do Projeto Ágatha."""
        super().__init__(source_config)
        self.selectors = source_config.get("selectors", {})
    
    def _extract_question_from_page(self, html: str, question_url: str) -> Optional[Dict[str, Any]]:
        """
        Extrai dados de uma questão individual.
        
        Args:
            html: HTML da página da questão
            question_url: URL da questão
            
        Returns:
            Dicionário com dados da questão ou None
        """
        soup = self._parse_html(html)
        
        # Extrair enunciado
        question_text = ""
        question_elem = soup.select_one(self.selectors.get("question_text", "div.enunciado"))
        if question_elem:
            question_text = question_elem.get_text(strip=True)
        
        # Extrair alternativas
        alternatives = []
        alternatives_elems = soup.select(self.selectors.get("alternatives", "div.alternativas"))
        for alt_elem in alternatives_elems:
            alt_text = alt_elem.get_text(strip=True)
            if alt_text:
                alternatives.append(alt_text)
        
        # Extrair gabarito
        answer = ""
        answer_elem = soup.select_one(self.selectors.get("answer", "div.gabarito"))
        if answer_elem:
            answer = answer_elem.get_text(strip=True)
        
        # Extrair resolução se disponível
        resolution = ""
        resolution_elem = soup.select_one(self.selectors.get("resolution", "div.resolucao"))
        if resolution_elem:
            resolution = resolution_elem.get_text(strip=True)
        
        # Extrair disciplina
        subject = ""
        subject_elem = soup.select_one(self.selectors.get("subject", "span.disciplina"))
        if subject_elem:
            subject = subject_elem.get_text(strip=True)
        
        # Extrair dificuldade
        difficulty = ""
        difficulty_elem = soup.select_one(self.selectors.get("difficulty", "span.dificuldade"))
        if difficulty_elem:
            difficulty = difficulty_elem.get_text(strip=True)
        
        if not question_text:
            return None
        
        return {
            "title": f"Questão {subject} - {difficulty}" if subject else "Questão",
            "content": f"{question_text}\n\nAlternativas:\n" + "\n".join(
                f"{chr(65+i)}. {alt}" for i, alt in enumerate(alternatives)
            ) + f"\n\nGabarito: {answer}" + (f"\n\nResolução:\n{resolution}" if resolution else ""),
            "metadata": {
                "type": "question",
                "subject": subject,
                "difficulty": difficulty,
                "has_resolution": bool(resolution),
                "num_alternatives": len(alternatives),
            },
            "tags": [subject, difficulty] if subject and difficulty else [subject] if subject else [],
            "url": question_url,
        }
    
    def _extract_question_list(self, html: str) -> List[str]:
        """
        Extrai lista de URLs de questões de uma página de listagem.
        
        Args:
            html: HTML da página de listagem
            
        Returns:
            Lista de URLs de questões
        """
        soup = self._parse_html(html)
        question_urls = []
        
        question_elems = soup.select(self.selectors.get("question_list", "div.questao"))
        for elem in question_elems:
            link = elem.find("a", href=True)
            if link:
                href = link["href"]
                # Converter para URL absoluta se necessário
                if href.startswith("/"):
                    href = f"{self.url}{href}"
                elif not href.startswith("http"):
                    href = f"{self.url}/{href}"
                question_urls.append(href)
        
        return question_urls
    
    def scrape(
        self,
        subject: Optional[str] = None,
        max_questions: Optional[int] = None,
        start_page: int = 1,
        max_pages: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de questões do Projeto Ágatha.
        
        Args:
            subject: Disciplina para filtrar (opcional)
            max_questions: Número máximo de questões a coletar
            start_page: Página inicial
            max_pages: Número máximo de páginas a processar
            
        Returns:
            Lista de questões normalizadas
        """
        documents = []
        page = start_page
        questions_collected = 0
        
        logger.info(f"Iniciando scraping Projeto Ágatha (subject={subject}, max={max_questions})")
        
        while True:
            # Construir URL da página de listagem
            list_url = f"{self.url}/questoes"
            params = {"page": page}
            if subject:
                params["disciplina"] = subject
            
            response = self._fetch(list_url, params=params)
            if not response:
                logger.warning(f"Falha ao buscar página {page}")
                break
            
            # Extrair URLs de questões
            question_urls = self._extract_question_list(response.text)
            
            if not question_urls:
                logger.info(f"Nenhuma questão encontrada na página {page}")
                break
            
            # Processar cada questão
            for question_url in question_urls:
                if max_questions and questions_collected >= max_questions:
                    logger.info(f"Limite de {max_questions} questões atingido")
                    break
                
                question_response = self._fetch(question_url)
                if not question_response:
                    continue
                
                question_data = self._extract_question_from_page(
                    question_response.text,
                    question_url
                )
                
                if question_data and self.validate_data(question_data):
                    documents.append(self.normalize_data(question_data))
                    questions_collected += 1
                    logger.debug(f"Questão coletada: {questions_collected}")
            
            # Verificar se deve continuar
            if max_questions and questions_collected >= max_questions:
                break
            
            if max_pages and page >= start_page + max_pages - 1:
                break
            
            page += 1
        
        logger.info(f"Scraping Projeto Ágatha concluído: {len(documents)} questões coletadas")
        return documents
