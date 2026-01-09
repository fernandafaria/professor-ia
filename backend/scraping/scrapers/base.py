"""
Classe base para scrapers.
"""

import time
import random
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from urllib.robotparser import RobotFileParser
import requests
from bs4 import BeautifulSoup
from app.config import settings

logger = logging.getLogger(__name__)


class BaseScraper(ABC):
    """Classe base abstrata para todos os scrapers."""
    
    def __init__(
        self,
        source_config: Dict[str, Any],
        respect_robots: bool = True,
    ):
        """
        Inicializa o scraper base.
        
        Args:
            source_config: Configuração da fonte do sources.yaml
            respect_robots: Se deve respeitar robots.txt
        """
        self.config = source_config
        self.name = source_config.get("name", "Unknown")
        self.url = source_config.get("url", "")
        self.priority = source_config.get("priority", "medium")
        self.frequency = source_config.get("frequency", "daily")
        self.respect_robots = respect_robots
        self.robots_parser = None
        
        # Configurações de scraping
        self.delay_min = settings.SCRAPING_DELAY_MIN
        self.delay_max = settings.SCRAPING_DELAY_MAX
        self.timeout = 30
        self.max_retries = 3
        self.user_agent = settings.SCRAPING_USER_AGENT
        
        # Headers padrão
        self.headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        
        # Verificar robots.txt se necessário
        if self.respect_robots:
            self._check_robots_txt()
    
    def _check_robots_txt(self):
        """Verifica e carrega robots.txt."""
        try:
            robots_url = f"{self.url}/robots.txt"
            self.robots_parser = RobotFileParser()
            self.robots_parser.set_url(robots_url)
            self.robots_parser.read()
            logger.info(f"Robots.txt carregado para {self.name}")
        except Exception as e:
            logger.warning(f"Erro ao carregar robots.txt para {self.name}: {e}")
            self.robots_parser = None
    
    def _can_fetch(self, path: str) -> bool:
        """Verifica se pode fazer scraping do path."""
        if not self.respect_robots or not self.robots_parser:
            return True
        return self.robots_parser.can_fetch(self.user_agent, f"{self.url}{path}")
    
    def _delay(self):
        """Aplica delay aleatório entre requisições."""
        delay = random.uniform(self.delay_min, self.delay_max)
        time.sleep(delay)
    
    def _fetch(
        self,
        url: str,
        method: str = "GET",
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> Optional[requests.Response]:
        """
        Faz requisição HTTP com retry e tratamento de erros.
        
        Args:
            url: URL para fazer requisição
            method: Método HTTP (GET, POST, etc.)
            params: Parâmetros da query string
            headers: Headers customizados
            **kwargs: Outros argumentos para requests
            
        Returns:
            Response object ou None em caso de erro
        """
        # Verificar robots.txt
        path = url.replace(self.url, "")
        if not self._can_fetch(path):
            logger.warning(f"Robots.txt bloqueia acesso a {url}")
            return None
        
        # Combinar headers
        request_headers = {**self.headers}
        if headers:
            request_headers.update(headers)
        
        # Retry logic
        for attempt in range(self.max_retries):
            try:
                self._delay()
                
                response = requests.request(
                    method=method,
                    url=url,
                    params=params,
                    headers=request_headers,
                    timeout=self.timeout,
                    **kwargs
                )
                
                response.raise_for_status()
                logger.debug(f"Requisição bem-sucedida: {url}")
                return response
                
            except requests.exceptions.RequestException as e:
                logger.warning(
                    f"Tentativa {attempt + 1}/{self.max_retries} falhou para {url}: {e}"
                )
                if attempt == self.max_retries - 1:
                    logger.error(f"Falha ao fazer requisição para {url} após {self.max_retries} tentativas")
                    return None
                time.sleep(2 ** attempt)  # Backoff exponencial
        
        return None
    
    def _parse_html(self, html: str) -> BeautifulSoup:
        """Parse HTML usando BeautifulSoup."""
        return BeautifulSoup(html, "lxml")
    
    @abstractmethod
    def scrape(self, **kwargs) -> List[Dict[str, Any]]:
        """
        Método abstrato para fazer scraping.
        
        Returns:
            Lista de documentos coletados
        """
        pass
    
    def validate_data(self, data: Dict[str, Any]) -> bool:
        """
        Valida dados coletados.
        
        Args:
            data: Dados a validar
            
        Returns:
            True se válido, False caso contrário
        """
        # Validação básica: deve ter pelo menos título ou conteúdo
        return bool(data.get("title") or data.get("content"))
    
    def normalize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normaliza dados coletados para formato padrão.
        
        Args:
            data: Dados brutos
            
        Returns:
            Dados normalizados
        """
        normalized = {
            "source": self.name,
            "source_url": self.url,
            "title": data.get("title", "").strip(),
            "content": data.get("content", "").strip(),
            "metadata": {
                "type": self.config.get("type", "unknown"),
                "priority": self.priority,
                "collected_at": time.time(),
                **data.get("metadata", {}),
            },
            "tags": data.get("tags", []),
            "url": data.get("url", ""),
        }
        
        return normalized
