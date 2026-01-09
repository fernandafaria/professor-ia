"""
Scraper para API BNCC Cientificar.
"""

import logging
from typing import Dict, List, Any, Optional
import requests
from .base import BaseScraper

logger = logging.getLogger(__name__)


class BNCCAPIScraper(BaseScraper):
    """Scraper para API BNCC Cientificar."""
    
    def __init__(self, source_config: Dict[str, Any]):
        """Inicializa scraper da API BNCC."""
        super().__init__(source_config, respect_robots=False)  # API não precisa robots.txt
        self.api_base = source_config.get("api_endpoints", {}).get("base", 
            "https://cientificar1992.pythonanywhere.com/api")
    
    def _fetch_disciplines(self) -> List[Dict[str, Any]]:
        """Busca lista de disciplinas disponíveis."""
        url = f"{self.api_base}/disciplinas"
        response = self._fetch(url)
        
        if not response:
            logger.error("Falha ao buscar disciplinas da API BNCC")
            return []
        
        try:
            data = response.json()
            return data if isinstance(data, list) else []
        except Exception as e:
            logger.error(f"Erro ao parsear resposta de disciplinas: {e}")
            return []
    
    def _fetch_skills(
        self,
        discipline: Optional[str] = None,
        grade: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Busca habilidades da BNCC.
        
        Args:
            discipline: Filtro por disciplina (opcional)
            grade: Filtro por série/ano (opcional)
        """
        url = f"{self.api_base}/habilidades"
        params = {}
        
        if discipline:
            params["disciplina"] = discipline
        if grade:
            params["serie"] = grade
        
        response = self._fetch(url, params=params)
        
        if not response:
            logger.error("Falha ao buscar habilidades da API BNCC")
            return []
        
        try:
            data = response.json()
            return data if isinstance(data, list) else []
        except Exception as e:
            logger.error(f"Erro ao parsear resposta de habilidades: {e}")
            return []
    
    def _fetch_knowledge_objects(
        self,
        discipline: Optional[str] = None,
        grade: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Busca objetos de conhecimento da BNCC.
        
        Args:
            discipline: Filtro por disciplina (opcional)
            grade: Filtro por série/ano (opcional)
        """
        url = f"{self.api_base}/objetos-conhecimento"
        params = {}
        
        if discipline:
            params["disciplina"] = discipline
        if grade:
            params["serie"] = grade
        
        response = self._fetch(url, params=params)
        
        if not response:
            logger.error("Falha ao buscar objetos de conhecimento da API BNCC")
            return []
        
        try:
            data = response.json()
            return data if isinstance(data, list) else []
        except Exception as e:
            logger.error(f"Erro ao parsear resposta de objetos de conhecimento: {e}")
            return []
    
    def scrape(
        self,
        disciplines: Optional[List[str]] = None,
        grades: Optional[List[str]] = None,
        include_knowledge_objects: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping completo da API BNCC.
        
        Args:
            disciplines: Lista de disciplinas para filtrar (None = todas)
            grades: Lista de séries para filtrar (None = todas)
            include_knowledge_objects: Se deve incluir objetos de conhecimento
            
        Returns:
            Lista de documentos normalizados
        """
        documents = []
        
        # Buscar disciplinas se não especificadas
        if not disciplines:
            disciplines_data = self._fetch_disciplines()
            disciplines = [d.get("nome") for d in disciplines_data if d.get("nome")]
        
        logger.info(f"Iniciando scraping BNCC para {len(disciplines)} disciplinas")
        
        # Processar cada disciplina
        for discipline in disciplines:
            logger.info(f"Processando disciplina: {discipline}")
            
            # Buscar habilidades
            skills = self._fetch_skills(discipline=discipline)
            
            for skill in skills:
                doc = {
                    "title": f"{skill.get('codigo', '')} - {skill.get('nome', '')}",
                    "content": skill.get("descricao", ""),
                    "metadata": {
                        "type": "bncc_skill",
                        "codigo": skill.get("codigo"),
                        "disciplina": discipline,
                        "serie": skill.get("serie"),
                        "unidade_tematica": skill.get("unidade_tematica"),
                        "objeto_conhecimento": skill.get("objeto_conhecimento"),
                    },
                    "tags": [discipline, skill.get("unidade_tematica", "")],
                    "url": f"{self.url}/habilidade/{skill.get('codigo', '')}",
                }
                
                if self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
            
            # Buscar objetos de conhecimento se solicitado
            if include_knowledge_objects:
                knowledge_objects = self._fetch_knowledge_objects(discipline=discipline)
                
                for obj in knowledge_objects:
                    doc = {
                        "title": obj.get("nome", ""),
                        "content": obj.get("descricao", ""),
                        "metadata": {
                            "type": "bncc_knowledge_object",
                            "disciplina": discipline,
                            "serie": obj.get("serie"),
                            "unidade_tematica": obj.get("unidade_tematica"),
                        },
                        "tags": [discipline, obj.get("unidade_tematica", "")],
                        "url": f"{self.url}/objeto/{obj.get('id', '')}",
                    }
                    
                    if self.validate_data(doc):
                        documents.append(self.normalize_data(doc))
        
        logger.info(f"Scraping BNCC concluído: {len(documents)} documentos coletados")
        return documents
