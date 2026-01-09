"""
Scraper usando Firecrawl através do MCP (Model Context Protocol).

Este scraper se comunica com o servidor MCP do Firecrawl para fazer scraping.
"""

import os
import json
import subprocess
import logging
import tempfile
from typing import Dict, List, Any, Optional
from .base import BaseScraper

logger = logging.getLogger(__name__)


class FirecrawlMCPScraper(BaseScraper):
    """
    Scraper usando Firecrawl através do MCP.
    
    O MCP (Model Context Protocol) permite usar o Firecrawl como um servidor
    que expõe ferramentas para scraping.
    """
    
    def __init__(self, source_config: Dict[str, Any]):
        """
        Inicializa scraper Firecrawl MCP.
        
        Args:
            source_config: Configuração da fonte do sources.yaml
        """
        super().__init__(source_config, respect_robots=False)
        
        # API Key do Firecrawl
        self.api_key = os.getenv("FIRECRAWL_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "FIRECRAWL_API_KEY não configurada. "
                "Configure a variável de ambiente ou no .env"
            )
        
        # Verificar se npx está disponível
        try:
            subprocess.run(["npx", "--version"], capture_output=True, check=True)
            self.npx_available = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.warning("npx não disponível. Tentando usar firecrawl-mcp diretamente")
            self.npx_available = True  # Ainda tentar
    
    def _call_mcp_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Chama uma ferramenta do MCP do Firecrawl.
        
        Args:
            tool_name: Nome da ferramenta (ex: "firecrawl_scrape", "firecrawl_crawl")
            arguments: Argumentos para a ferramenta
            
        Returns:
            Resultado da ferramenta ou None em caso de erro
        """
        try:
            # Criar payload MCP
            mcp_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": arguments
                }
            }
            
            # Criar script Node.js temporário para chamar MCP
            script_content = f"""
const {{ spawn }} = require('child_process');
const readline = require('readline');

// Iniciar servidor MCP do Firecrawl
const mcpProcess = spawn('npx', ['-y', 'firecrawl-mcp'], {{
    env: {{ ...process.env, FIRECRAWL_API_KEY: '{self.api_key}' }},
    stdio: ['pipe', 'pipe', 'pipe']
}});

const payload = {json.dumps(mcp_payload)};

// Enviar requisição
mcpProcess.stdin.write(JSON.stringify(payload) + '\\n');

// Ler resposta
let responseData = '';
mcpProcess.stdout.on('data', (data) => {{
    responseData += data.toString();
    try {{
        const response = JSON.parse(responseData);
        if (response.result) {{
            console.log(JSON.stringify(response.result));
            mcpProcess.kill();
            process.exit(0);
        }}
    }} catch (e) {{
        // Ainda não tem JSON completo
    }}
}});

mcpProcess.stderr.on('data', (data) => {{
    console.error(data.toString());
}});

setTimeout(() => {{
    mcpProcess.kill();
    process.exit(1);
}}, 30000);
"""
            
            # Escrever script temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                f.write(script_content)
                script_path = f.name
            
            try:
                # Executar script Node.js
                result = subprocess.run(
                    ["node", script_path],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0 and result.stdout:
                    try:
                        return json.loads(result.stdout)
                    except json.JSONDecodeError:
                        logger.error(f"Resposta inválida do MCP: {result.stdout}")
                        return None
                else:
                    logger.error(f"Erro ao executar MCP: {result.stderr}")
                    return None
                    
            finally:
                # Limpar script temporário
                os.unlink(script_path)
                
        except Exception as e:
            logger.error(f"Erro ao chamar ferramenta MCP {tool_name}: {e}", exc_info=True)
            return None
    
    def _scrape_url_mcp(self, url: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """
        Faz scraping de uma URL usando MCP do Firecrawl.
        
        Args:
            url: URL para fazer scraping
            params: Parâmetros adicionais
            
        Returns:
            Dados extraídos ou None
        """
        arguments = {
            "url": url,
            "formats": ["markdown"],
            "onlyMainContent": True,
        }
        
        if params:
            arguments.update(params)
        
        logger.debug(f"Fazendo scraping via MCP: {url}")
        result = self._call_mcp_tool("firecrawl_scrape", arguments)
        
        if not result:
            return None
        
        # O resultado do MCP vem em formato específico
        # Ajustar conforme a estrutura real da resposta
        return result
    
    def _crawl_site_mcp(
        self,
        url: str,
        max_pages: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Faz crawling de um site usando MCP do Firecrawl.
        
        Args:
            url: URL base do site
            max_pages: Número máximo de páginas
            
        Returns:
            Lista de páginas coletadas
        """
        arguments = {
            "url": url,
            "limit": max_pages or 10,
            "formats": ["markdown"],
            "onlyMainContent": True,
        }
        
        logger.info(f"Iniciando crawling via MCP: {url} (max_pages={max_pages})")
        result = self._call_mcp_tool("firecrawl_crawl", arguments)
        
        if not result:
            return []
        
        # Processar resultado
        pages = result.get("data", []) if isinstance(result, dict) else []
        logger.info(f"Crawling via MCP concluído: {len(pages)} páginas coletadas")
        
        return pages
    
    def _extract_from_mcp_result(
        self,
        mcp_result: Dict[str, Any],
        url: str
    ) -> Optional[Dict[str, Any]]:
        """
        Extrai e normaliza dados do resultado do MCP.
        
        Args:
            mcp_result: Resultado do MCP
            url: URL original
            
        Returns:
            Dados normalizados ou None
        """
        # Estrutura pode variar dependendo da resposta do MCP
        content = ""
        title = ""
        
        # Tentar diferentes estruturas de resposta
        if isinstance(mcp_result, dict):
            if "markdown" in mcp_result:
                content = mcp_result["markdown"]
            elif "content" in mcp_result:
                content = mcp_result["content"]
            elif "data" in mcp_result:
                data = mcp_result["data"]
                if isinstance(data, dict):
                    content = data.get("markdown", data.get("content", ""))
                    title = data.get("title", data.get("metadata", {}).get("title", ""))
            
            if "metadata" in mcp_result:
                metadata = mcp_result["metadata"]
                title = metadata.get("title", title)
        
        if not content:
            return None
        
        return {
            "title": title or "Conteúdo Firecrawl MCP",
            "content": content,
            "metadata": {
                "type": self.config.get("type", "web_content"),
                "source_url": url,
                "scraped_via": "firecrawl_mcp",
                **mcp_result.get("metadata", {}),
            },
            "tags": [],
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
        Faz scraping usando Firecrawl via MCP.
        
        Args:
            urls: Lista de URLs específicas para fazer scraping
            crawl: Se True, faz crawling do site inteiro
            max_pages: Número máximo de páginas (para crawl)
            **kwargs: Parâmetros adicionais
            
        Returns:
            Lista de documentos normalizados
        """
        documents = []
        
        if crawl:
            # Modo crawling via MCP
            pages = self._crawl_site_mcp(
                url=self.url,
                max_pages=max_pages
            )
            
            for page in pages:
                page_url = page.get("url", self.url)
                doc = self._extract_from_mcp_result(page, page_url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        elif urls:
            # Modo URL específica via MCP
            for url in urls:
                mcp_result = self._scrape_url_mcp(url, params=kwargs)
                if not mcp_result:
                    continue
                
                doc = self._extract_from_mcp_result(mcp_result, url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        else:
            # Modo padrão: scraping da URL base via MCP
            mcp_result = self._scrape_url_mcp(self.url, params=kwargs)
            if mcp_result:
                doc = self._extract_from_mcp_result(mcp_result, self.url)
                if doc and self.validate_data(doc):
                    documents.append(self.normalize_data(doc))
        
        logger.info(f"Scraping Firecrawl MCP concluído: {len(documents)} documentos coletados")
        return documents
