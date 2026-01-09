"""
Scraper para bases de dados acadêmicas sobre neurodivergências
Suporta ERIC, PubMed, SciELO e outras fontes
"""

import requests
import time
import logging
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import json
from datetime import datetime

logger = logging.getLogger(__name__)

# Importação condicional do BaseScraper
try:
    from .base import BaseScraper
except ImportError:
    # Fallback se BaseScraper não estiver disponível
    class BaseScraper:
        def __init__(self, delay: float = 2.0, timeout: int = 60):
            self.delay = delay
            self.timeout = timeout
            self.logger = logger


class AcademicScraper(BaseScraper):
    """Scraper base para bases de dados acadêmicas"""
    
    def __init__(self, delay: float = 2.0, timeout: int = 60):
        try:
            super().__init__(delay=delay, timeout=timeout)
        except:
            # Fallback se BaseScraper não funcionar
            self.delay = delay
            self.timeout = timeout
            self.logger = logger
        self.user_agent = "Mozilla/5.0 (Educational Platform Research Bot)"
    
    def search_papers(
        self,
        query: str,
        max_results: int = 50,
        neurodivergence_type: Optional[str] = None
    ) -> List[Dict]:
        """
        Busca papers com base em query
        
        Args:
            query: Termo de busca
            max_results: Número máximo de resultados
            neurodivergence_type: Tipo de neurodivergência (TDAH, dislexia, TEA)
        
        Returns:
            Lista de papers encontrados
        """
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def extract_paper_data(self, paper_element) -> Dict:
        """Extrai dados de um paper"""
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def normalize_paper(self, paper_data: Dict) -> Dict:
        """Normaliza dados do paper para formato padrão"""
        return {
            "title": paper_data.get("title", ""),
            "abstract": paper_data.get("abstract", ""),
            "authors": paper_data.get("authors", []),
            "publication_date": paper_data.get("publication_date", ""),
            "doi": paper_data.get("doi", ""),
            "source_url": paper_data.get("source_url", ""),
            "pdf_url": paper_data.get("pdf_url", ""),
            "keywords": paper_data.get("keywords", []),
            "neurodivergence_type": paper_data.get("neurodivergence_type", ""),
            "educational_level": paper_data.get("educational_level", ""),
            "subject_area": paper_data.get("subject_area", ""),
            "intervention_type": paper_data.get("intervention_type", ""),
            "language": paper_data.get("language", "en"),
            "full_text": paper_data.get("full_text", ""),
            "citations": paper_data.get("citations", 0),
            "references": paper_data.get("references", []),
            "scraped_at": datetime.now().isoformat()
        }


class ERICScraper(AcademicScraper):
    """Scraper para ERIC (Education Resources Information Center)"""
    
    def __init__(self, api_key: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.base_url = "https://api.ies.ed.gov/eric/"
        self.web_url = "https://eric.ed.gov"
    
    def search_papers(
        self,
        query: str,
        max_results: int = 50,
        neurodivergence_type: Optional[str] = None
    ) -> List[Dict]:
        """Busca papers no ERIC"""
        if self.api_key:
            return self._search_via_api(query, max_results)
        else:
            return self._search_via_web(query, max_results)
    
    def _search_via_api(self, query: str, max_results: int) -> List[Dict]:
        """Busca via API (requer chave)"""
        params = {
            "search": query,
            "format": "json",
            "key": self.api_key,
            "rows": max_results
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            papers = []
            for item in data.get("response", {}).get("docs", []):
                paper = self._extract_from_api_result(item)
                papers.append(paper)
            
            return papers
        except Exception as e:
            self.logger.error(f"Erro ao buscar no ERIC via API: {e}")
            return []
    
    def _search_via_web(self, query: str, max_results: int) -> List[Dict]:
        """Busca via web scraping"""
        search_url = f"{self.web_url}/"
        params = {
            "q": query,
            "ff1": "dtySince2000"  # Desde 2000
        }
        
        try:
            response = self._make_request(search_url, params=params)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            papers = []
            results = soup.select("div.result-item")[:max_results]
            
            for result in results:
                paper = self._extract_from_web_result(result)
                if paper:
                    papers.append(paper)
            
            return papers
        except Exception as e:
            self.logger.error(f"Erro ao buscar no ERIC via web: {e}")
            return []
    
    def _extract_from_api_result(self, item: Dict) -> Dict:
        """Extrai dados de resultado da API"""
        return {
            "title": item.get("title", [""])[0] if item.get("title") else "",
            "abstract": item.get("description", [""])[0] if item.get("description") else "",
            "authors": item.get("author", []),
            "publication_date": item.get("publicationdate", ""),
            "source_url": item.get("url", ""),
            "keywords": item.get("descriptor", []),
            "language": "en"
        }
    
    def _extract_from_web_result(self, result_element) -> Optional[Dict]:
        """Extrai dados de resultado do web scraping"""
        try:
            title_elem = result_element.select_one("h3.result-title a")
            if not title_elem:
                return None
            
            title = title_elem.get_text(strip=True)
            url = title_elem.get("href", "")
            if url and not url.startswith("http"):
                url = f"{self.web_url}{url}"
            
            abstract_elem = result_element.select_one("div.result-abstract")
            abstract = abstract_elem.get_text(strip=True) if abstract_elem else ""
            
            authors_elem = result_element.select_one("div.result-authors")
            authors = [a.get_text(strip=True) for a in authors_elem.select("a")] if authors_elem else []
            
            date_elem = result_element.select_one("span.result-date")
            date = date_elem.get_text(strip=True) if date_elem else ""
            
            return {
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "publication_date": date,
                "source_url": url,
                "language": "en"
            }
        except Exception as e:
            self.logger.error(f"Erro ao extrair dados do resultado: {e}")
            return None


class PubMedScraper(AcademicScraper):
    """Scraper para PubMed"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.web_url = "https://pubmed.ncbi.nlm.nih.gov"
    
    def search_papers(
        self,
        query: str,
        max_results: int = 50,
        neurodivergence_type: Optional[str] = None
    ) -> List[Dict]:
        """Busca papers no PubMed"""
        # Adicionar termos específicos se fornecido
        if neurodivergence_type:
            query = f"{query} AND ({neurodivergence_type} OR {neurodivergence_type.lower()})"
        
        # Buscar IDs
        search_url = f"{self.base_url}esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json"
        }
        
        try:
            response = requests.get(search_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            ids = data.get("esearchresult", {}).get("idlist", [])
            if not ids:
                return []
            
            # Buscar detalhes
            papers = self._fetch_paper_details(ids)
            return papers
        except Exception as e:
            self.logger.error(f"Erro ao buscar no PubMed: {e}")
            return []
    
    def _fetch_paper_details(self, ids: List[str]) -> List[Dict]:
        """Busca detalhes dos papers pelos IDs"""
        fetch_url = f"{self.base_url}efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "xml"
        }
        
        try:
            response = requests.get(fetch_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            papers = []
            
            for article in root.findall(".//PubmedArticle"):
                paper = self._extract_from_xml(article)
                if paper:
                    papers.append(paper)
            
            return papers
        except Exception as e:
            self.logger.error(f"Erro ao buscar detalhes no PubMed: {e}")
            return []
    
    def _extract_from_xml(self, article_element) -> Optional[Dict]:
        """Extrai dados do XML do PubMed"""
        try:
            # Título
            title_elem = article_element.find(".//ArticleTitle")
            title = title_elem.text if title_elem is not None else ""
            
            # Abstract
            abstract_elems = article_element.findall(".//AbstractText")
            abstract = " ".join([elem.text for elem in abstract_elems if elem.text])
            
            # Autores
            authors = []
            for author in article_element.findall(".//Author"):
                last_name = author.find("LastName")
                first_name = author.find("ForeName")
                if last_name is not None and first_name is not None:
                    authors.append(f"{first_name.text} {last_name.text}")
            
            # Data de publicação
            pub_date = article_element.find(".//PubDate")
            date_str = ""
            if pub_date is not None:
                year = pub_date.find("Year")
                month = pub_date.find("Month")
                if year is not None:
                    date_str = year.text
                    if month is not None:
                        date_str = f"{month.text} {date_str}"
            
            # DOI
            doi_elem = article_element.find(".//ArticleId[@IdType='doi']")
            doi = doi_elem.text if doi_elem is not None else ""
            
            # PubMed ID
            pmid_elem = article_element.find(".//PMID")
            pmid = pmid_elem.text if pmid_elem is not None else ""
            
            # URL
            url = f"{self.web_url}/{pmid}" if pmid else ""
            
            return {
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "publication_date": date_str,
                "doi": doi,
                "source_url": url,
                "language": "en"
            }
        except Exception as e:
            self.logger.error(f"Erro ao extrair dados do XML: {e}")
            return None


class SciELOScraper(AcademicScraper):
    """Scraper para SciELO Brasil"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_url = "https://api.scielo.org/v1/"
        self.web_url = "https://www.scielo.org"
    
    def search_papers(
        self,
        query: str,
        max_results: int = 50,
        neurodivergence_type: Optional[str] = None
    ) -> List[Dict]:
        """Busca papers no SciELO"""
        params = {
            "q": query,
            "lang": "pt",
            "format": "json",
            "limit": max_results
        }
        
        try:
            response = requests.get(self.api_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            papers = []
            for item in data.get("objects", [])[:max_results]:
                paper = self._extract_from_api_result(item)
                if paper:
                    papers.append(paper)
            
            return papers
        except Exception as e:
            self.logger.error(f"Erro ao buscar no SciELO: {e}")
            return []
    
    def _extract_from_api_result(self, item: Dict) -> Optional[Dict]:
        """Extrai dados de resultado da API"""
        try:
            return {
                "title": item.get("title", [""])[0] if item.get("title") else "",
                "abstract": item.get("abstract", [""])[0] if item.get("abstract") else "",
                "authors": item.get("author", []),
                "publication_date": item.get("publication_date", ""),
                "doi": item.get("doi", ""),
                "source_url": item.get("url", ""),
                "keywords": item.get("keywords", []),
                "language": "pt-BR"
            }
        except Exception as e:
            self.logger.error(f"Erro ao extrair dados do SciELO: {e}")
            return None
