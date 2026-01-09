"""
Pipeline principal de scraping integrado com RAG.
"""

import logging
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session
from app.core.rag.retriever_supabase import RAGRetriever
from app.config import settings
from app.services.database import get_db

from .scrapers import (
    BNCCAPIScraper,
    ProjetoAgathaScraper,
    NovaEscolaScraper,
    CulturalScraper,
    WikiScraper,
    FirecrawlScraper,
    FirecrawlMCPSimpleScraper,
)
from .processors import ContentProcessor

logger = logging.getLogger(__name__)


class ScrapingPipeline:
    """Pipeline de scraping integrado com sistema RAG."""
    
    def __init__(
        self,
        sources_config_path: Optional[str] = None,
        retriever: Optional[RAGRetriever] = None,
    ):
        """
        Inicializa pipeline de scraping.
        
        Args:
            sources_config_path: Caminho para arquivo sources.yaml
            retriever: Instância do RAGRetriever (opcional)
        """
        # Carregar configuração de fontes
        if sources_config_path is None:
            sources_config_path = Path(__file__).parent / "config" / "sources.yaml"
        
        with open(sources_config_path, "r", encoding="utf-8") as f:
            self.sources_config = yaml.safe_load(f)
        
        # Inicializar processador
        scraping_config = self.sources_config.get("scraping_config", {})
        self.processor = ContentProcessor(
            chunk_size=scraping_config.get("chunk_size", 1000),
            chunk_overlap=scraping_config.get("chunk_overlap", 200),
        )
        
        # Inicializar retriever se não fornecido
        # Nota: RAGRetriever com Supabase não precisa de sessão no __init__
        self.retriever = retriever or RAGRetriever()
        
        # Mapear scrapers por tipo
        self.scraper_classes = {
            "api": BNCCAPIScraper,
            "educational": NovaEscolaScraper,
            "questions": ProjetoAgathaScraper,
            "news": CulturalScraper,
            "wiki": WikiScraper,
            "lyrics": CulturalScraper,
            "data": CulturalScraper,
            "firecrawl": FirecrawlScraper,  # Tipo especial para usar Firecrawl
        }
        
        # Verificar se fonte deve usar Firecrawl
        self.use_firecrawl_for = [
            "Nova Escola",
            "Projeto Ágatha Edu",
            "Fandom Wikis",
            "Liquipedia",
            "Globo Esporte",
            "ESPN Brasil",
            "Letras.mus.br",
        ]
        
        # Usar MCP do Firecrawl por padrão
        self.use_mcp_firecrawl = True
    
    def _create_scraper(self, source_config: Dict[str, Any], use_firecrawl: bool = False, use_mcp: bool = True):
        """
        Cria instância de scraper apropriado.
        
        Args:
            source_config: Configuração da fonte
            use_firecrawl: Se deve usar Firecrawl (sobrescreve tipo padrão)
            use_mcp: Se deve usar MCP do Firecrawl (padrão: True)
            
        Returns:
            Instância do scraper
        """
        # Verificar se deve usar Firecrawl
        source_name = source_config.get("name", "")
        if use_firecrawl or source_name in self.use_firecrawl_for:
            # Usar MCP do Firecrawl se solicitado
            if use_mcp and self.use_mcp_firecrawl:
                try:
                    return FirecrawlMCPSimpleScraper(source_config)
                except Exception as e:
                    logger.warning(f"Erro ao criar Firecrawl MCP scraper: {e}. Usando Firecrawl padrão.")
                    return FirecrawlScraper(source_config)
            else:
                return FirecrawlScraper(source_config)
        
        source_type = source_config.get("type", "news")
        scraper_class = self.scraper_classes.get(source_type, CulturalScraper)
        
        return scraper_class(source_config)
    
    def scrape_source(
        self,
        source_name: str,
        use_firecrawl: bool = False,
        use_mcp: bool = True,
        **scraper_kwargs
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de uma fonte específica.
        
        Args:
            source_name: Nome da fonte (como no sources.yaml)
            **scraper_kwargs: Argumentos específicos do scraper
            
        Returns:
            Lista de documentos coletados e processados
        """
        # Encontrar configuração da fonte
        source_config = None
        
        # Buscar em curricular_sources
        for source in self.sources_config.get("curricular_sources", []):
            if source.get("name") == source_name:
                source_config = source
                break
        
        # Buscar em question_sources
        if not source_config:
            for source in self.sources_config.get("question_sources", []):
                if source.get("name") == source_name:
                    source_config = source
                    break
        
        # Buscar em cultural_sources
        if not source_config:
            for category in self.sources_config.get("cultural_sources", {}).values():
                if isinstance(category, list):
                    for source in category:
                        if source.get("name") == source_name:
                            source_config = source
                            break
        
        if not source_config:
            logger.error(f"Fonte '{source_name}' não encontrada no sources.yaml")
            return []
        
        # Criar e executar scraper
        logger.info(f"Iniciando scraping de: {source_name} (use_firecrawl={use_firecrawl}, use_mcp={use_mcp})")
        scraper = self._create_scraper(source_config, use_firecrawl=use_firecrawl, use_mcp=use_mcp)
        
        try:
            raw_documents = scraper.scrape(**scraper_kwargs)
        except Exception as e:
            logger.error(f"Erro ao fazer scraping de {source_name}: {e}", exc_info=True)
            return []
        
        # Processar documentos
        processed_documents = []
        for raw_doc in raw_documents:
            processed = self.processor.process_document(raw_doc, chunk=True)
            processed_documents.extend(processed)
        
        # Filtrar por qualidade
        processed_documents = self.processor.filter_by_quality(processed_documents)
        
        logger.info(
            f"Scraping de {source_name} concluído: "
            f"{len(raw_documents)} documentos -> {len(processed_documents)} chunks processados"
        )
        
        return processed_documents
    
    def scrape_by_priority(
        self,
        priority: str = "critical",
        max_sources: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Faz scraping de todas as fontes com prioridade especificada.
        
        Args:
            priority: Prioridade a processar (critical, very_high, high, medium, low)
            max_sources: Número máximo de fontes a processar
            
        Returns:
            Lista de todos os documentos coletados
        """
        all_documents = []
        sources_processed = 0
        
        # Processar fontes curriculares
        for source in self.sources_config.get("curricular_sources", []):
            if source.get("priority") == priority:
                if max_sources and sources_processed >= max_sources:
                    break
                
                docs = self.scrape_source(source.get("name"))
                all_documents.extend(docs)
                sources_processed += 1
        
        # Processar fontes de questões
        for source in self.sources_config.get("question_sources", []):
            if source.get("priority") == priority:
                if max_sources and sources_processed >= max_sources:
                    break
                
                docs = self.scrape_source(source.get("name"))
                all_documents.extend(docs)
                sources_processed += 1
        
        logger.info(
            f"Scraping por prioridade '{priority}' concluído: "
            f"{sources_processed} fontes, {len(all_documents)} documentos"
        )
        
        return all_documents
    
    def add_to_rag(
        self,
        documents: List[Dict[str, Any]],
        batch_size: int = 100,
        db: Optional[Session] = None
    ):
        """
        Adiciona documentos processados ao sistema RAG usando Supabase.
        
        Args:
            documents: Lista de documentos processados
            batch_size: Tamanho do lote para processamento
            db: Sessão do banco de dados (opcional, será criada se não fornecida)
        """
        if not documents:
            logger.warning("Nenhum documento para adicionar ao RAG")
            return
        
        logger.info(f"Adicionando {len(documents)} documentos ao RAG (batch_size={batch_size})")
        
        # Obter sessão do banco de dados se não fornecida
        if db is None:
            db_gen = get_db()
            db = next(db_gen)
            should_close = True
        else:
            should_close = False
        
        try:
            # Processar em lotes
            for i in range(0, len(documents), batch_size):
                batch = documents[i:i + batch_size]
                
                # Extrair dados para RAGRetriever
                contents = [doc["content"] for doc in batch]
                metadatas = [doc["metadata"] for doc in batch]
                ids = [doc["id"] for doc in batch]
                
                try:
                    self.retriever.add_documents(
                        documents=contents,
                        metadatas=metadatas,
                        ids=ids,
                        db=db
                    )
                    logger.info(f"Lote {i // batch_size + 1} adicionado ao RAG ({len(batch)} documentos)")
                except Exception as e:
                    logger.error(f"Erro ao adicionar lote ao RAG: {e}", exc_info=True)
                    db.rollback()
            
            logger.info(f"Todos os documentos adicionados ao RAG")
        finally:
            # Fechar sessão se foi criada aqui
            if should_close:
                db.close()
    
    def run_full_pipeline(
        self,
        priorities: List[str] = ["critical", "very_high", "high"],
        add_to_rag: bool = True
    ) -> Dict[str, Any]:
        """
        Executa pipeline completo de scraping.
        
        Args:
            priorities: Lista de prioridades a processar
            add_to_rag: Se deve adicionar documentos ao RAG
            
        Returns:
            Estatísticas do pipeline
        """
        logger.info("Iniciando pipeline completo de scraping")
        
        all_documents = []
        stats = {
            "sources_processed": 0,
            "documents_collected": 0,
            "chunks_created": 0,
            "errors": [],
        }
        
        for priority in priorities:
            logger.info(f"Processando fontes com prioridade: {priority}")
            
            try:
                docs = self.scrape_by_priority(priority=priority)
                all_documents.extend(docs)
                stats["documents_collected"] += len(docs)
            except Exception as e:
                error_msg = f"Erro ao processar prioridade {priority}: {e}"
                logger.error(error_msg, exc_info=True)
                stats["errors"].append(error_msg)
        
        stats["chunks_created"] = len(all_documents)
        
        # Adicionar ao RAG se solicitado
        if add_to_rag and all_documents:
            try:
                self.add_to_rag(all_documents)
                stats["added_to_rag"] = True
            except Exception as e:
                error_msg = f"Erro ao adicionar ao RAG: {e}"
                logger.error(error_msg, exc_info=True)
                stats["errors"].append(error_msg)
                stats["added_to_rag"] = False
        
        logger.info(f"Pipeline concluído: {stats}")
        return stats
