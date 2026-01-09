"""
Script para fazer scraping de papers sobre neurodivergências e organizar para RAG.
"""

import os
import sys
import logging
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from tqdm import tqdm

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.scraping.scrapers.academic import (
    PubMedScraper,
    SciELOScraper,
    ERICScraper
)
from backend.scraping.processors.content_processor import ContentProcessor
from backend.app.core.rag.retriever_supabase import RAGRetriever
from backend.app.services.database import get_db
from backend.app.config import settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NeurodivergencePaperScraper:
    """Scraper e organizador de papers sobre neurodivergências para RAG."""
    
    def __init__(
        self,
        chunk_size: int = 2000,
        chunk_overlap: int = 400,
        min_abstract_length: int = 200
    ):
        """
        Inicializa o scraper.
        
        Args:
            chunk_size: Tamanho dos chunks para RAG
            chunk_overlap: Sobreposição entre chunks
            min_abstract_length: Tamanho mínimo do abstract
        """
        # Scrapers
        self.pubmed_scraper = PubMedScraper()
        self.scielo_scraper = SciELOScraper()
        self.eric_scraper = ERICScraper(api_key=os.getenv("ERIC_API_KEY"))
        
        # Processador
        self.processor = ContentProcessor(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        # RAG Retriever
        self.retriever = RAGRetriever()
        
        # Configurações
        self.min_abstract_length = min_abstract_length
        
        # Termos de busca
        self.search_terms = {
            "ADHD": [
                "ADHD educational intervention",
                "ADHD learning strategies",
                "attention deficit hyperactivity disorder education",
                "TDAH educação",
                "TDAH aprendizagem"
            ],
            "dyslexia": [
                "dyslexia reading intervention",
                "dyslexia learning support",
                "dislexia aprendizagem",
                "dislexia leitura"
            ],
            "autism": [
                "autism educational strategies",
                "autism spectrum disorder education",
                "autismo educação",
                "TEA educação"
            ],
            "neurodivergence": [
                "neurodivergent students",
                "learning differences",
                "neurodiversidade",
                "educação inclusiva"
            ]
        }
    
    def search_all_sources(
        self,
        neurodivergence_type: str,
        max_results_per_source: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Busca papers em todas as fontes para um tipo de neurodivergência.
        
        Args:
            neurodivergence_type: Tipo (ADHD, dyslexia, autism, neurodivergence)
            max_results_per_source: Máximo de resultados por fonte
        
        Returns:
            Lista de papers coletados
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"Buscando papers sobre: {neurodivergence_type}")
        logger.info(f"{'='*60}\n")
        
        all_papers = []
        terms = self.search_terms.get(neurodivergence_type, [])
        
        if not terms:
            logger.warning(f"Nenhum termo de busca para {neurodivergence_type}")
            return []
        
        # Buscar no PubMed
        logger.info("🔍 Buscando no PubMed...")
        for term in terms[:2]:  # Limitar termos para não exceder rate limits
            try:
                papers = self.pubmed_scraper.search_papers(
                    query=term,
                    max_results=max_results_per_source,
                    neurodivergence_type=neurodivergence_type
                )
                for paper in papers:
                    paper["source_database"] = "PubMed"
                    paper["search_term"] = term
                all_papers.extend(papers)
                logger.info(f"  ✓ {term}: {len(papers)} papers encontrados")
            except Exception as e:
                logger.error(f"  ✗ Erro ao buscar {term} no PubMed: {e}")
        
        # Buscar no SciELO (apenas termos em português)
        logger.info("\n🔍 Buscando no SciELO...")
        portuguese_terms = [t for t in terms if any(c in t for c in "áéíóúãõç")]
        for term in portuguese_terms[:2]:
            try:
                papers = self.scielo_scraper.search_papers(
                    query=term,
                    max_results=max_results_per_source
                )
                for paper in papers:
                    paper["source_database"] = "SciELO"
                    paper["search_term"] = term
                all_papers.extend(papers)
                logger.info(f"  ✓ {term}: {len(papers)} papers encontrados")
            except Exception as e:
                logger.error(f"  ✗ Erro ao buscar {term} no SciELO: {e}")
        
        # Buscar no ERIC (se API key disponível)
        if os.getenv("ERIC_API_KEY"):
            logger.info("\n🔍 Buscando no ERIC...")
            for term in terms[:2]:
                try:
                    papers = self.eric_scraper.search_papers(
                        query=term,
                        max_results=max_results_per_source
                    )
                    for paper in papers:
                        paper["source_database"] = "ERIC"
                        paper["search_term"] = term
                    all_papers.extend(papers)
                    logger.info(f"  ✓ {term}: {len(papers)} papers encontrados")
                except Exception as e:
                    logger.error(f"  ✗ Erro ao buscar {term} no ERIC: {e}")
        else:
            logger.info("\n⚠️  ERIC API key não configurada. Pulando ERIC.")
        
        # Remover duplicatas (por título)
        seen_titles = set()
        unique_papers = []
        for paper in all_papers:
            title = paper.get("title", "").lower().strip()
            if title and title not in seen_titles:
                seen_titles.add(title)
                unique_papers.append(paper)
        
        logger.info(f"\n✅ Total de papers únicos: {len(unique_papers)}")
        return unique_papers
    
    def process_papers_for_rag(
        self,
        papers: List[Dict[str, Any]],
        neurodivergence_type: str
    ) -> List[Dict[str, Any]]:
        """
        Processa papers para formato RAG.
        
        Args:
            papers: Lista de papers brutos
            neurodivergence_type: Tipo de neurodivergência
        
        Returns:
            Lista de documentos processados para RAG
        """
        logger.info(f"\n📝 Processando {len(papers)} papers para RAG...")
        
        processed_docs = []
        
        for paper in tqdm(papers, desc="Processando papers"):
            try:
                # Validar paper
                if not self._validate_paper(paper):
                    continue
                
                # Criar conteúdo combinado (título + abstract + keywords)
                content = self._create_paper_content(paper)
                
                # Criar documento base
                doc = {
                    "title": paper.get("title", ""),
                    "content": content,
                    "url": paper.get("source_url", ""),
                    "metadata": {
                        "source": paper.get("source_database", "unknown"),
                        "source_url": paper.get("source_url", ""),
                        "title": paper.get("title", ""),
                        "authors": paper.get("authors", []),
                        "publication_date": paper.get("publication_date", ""),
                        "doi": paper.get("doi", ""),
                        "keywords": paper.get("keywords", []),
                        "neurodivergence_type": neurodivergence_type,
                        "language": paper.get("language", "en"),
                        "search_term": paper.get("search_term", ""),
                        "paper_type": "academic",
                        "processed_at": datetime.now().isoformat()
                    },
                    "tags": paper.get("keywords", []) + [neurodivergence_type]
                }
                
                # Processar documento (chunking)
                processed = self.processor.process_document(doc, chunk=True)
                processed_docs.extend(processed)
                
            except Exception as e:
                logger.error(f"Erro ao processar paper '{paper.get('title', 'unknown')}': {e}")
                continue
        
        logger.info(f"✅ {len(processed_docs)} chunks criados de {len(papers)} papers")
        return processed_docs
    
    def _validate_paper(self, paper: Dict[str, Any]) -> bool:
        """Valida se paper tem qualidade mínima."""
        title = paper.get("title", "").strip()
        abstract = paper.get("abstract", "").strip()
        
        if not title or len(title) < 10:
            return False
        
        if not abstract or len(abstract) < self.min_abstract_length:
            return False
        
        return True
    
    def _create_paper_content(self, paper: Dict[str, Any]) -> str:
        """Cria conteúdo combinado do paper."""
        parts = []
        
        # Título
        title = paper.get("title", "")
        if title:
            parts.append(f"Título: {title}")
        
        # Abstract
        abstract = paper.get("abstract", "")
        if abstract:
            parts.append(f"\nResumo:\n{abstract}")
        
        # Autores
        authors = paper.get("authors", [])
        if authors:
            authors_str = ", ".join(authors[:5])  # Limitar a 5 autores
            parts.append(f"\nAutores: {authors_str}")
        
        # Keywords
        keywords = paper.get("keywords", [])
        if keywords:
            keywords_str = ", ".join(keywords[:10])  # Limitar a 10 keywords
            parts.append(f"\nPalavras-chave: {keywords_str}")
        
        return "\n".join(parts)
    
    def add_to_rag(
        self,
        documents: List[Dict[str, Any]],
        batch_size: int = 50
    ) -> Dict[str, Any]:
        """
        Adiciona documentos ao RAG (Supabase/pgvector).
        
        Args:
            documents: Lista de documentos processados
            batch_size: Tamanho do batch para inserção
        
        Returns:
            Estatísticas da inserção
        """
        logger.info(f"\n📚 Adicionando {len(documents)} documentos ao RAG...")
        
        stats = {
            "total_documents": len(documents),
            "batches": 0,
            "success": 0,
            "errors": 0,
            "errors_list": []
        }
        
        # Obter sessão do banco de dados
        db_gen = get_db()
        db = next(db_gen)
        try:
            # Processar em batches
            for i in range(0, len(documents), batch_size):
                batch = documents[i:i + batch_size]
                stats["batches"] += 1
                
                try:
                    # Extrair dados para Supabase
                    texts = [doc["content"] for doc in batch]
                    metadatas = [doc["metadata"] for doc in batch]
                    ids = [doc["id"] for doc in batch]
                    
                    # Adicionar ao Supabase
                    self.retriever.add_documents(
                        documents=texts,
                        metadatas=metadatas,
                        ids=ids,
                        db=db
                    )
                    
                    stats["success"] += len(batch)
                    logger.info(f"  ✓ Batch {stats['batches']}: {len(batch)} documentos adicionados")
                    
                except Exception as e:
                    error_msg = f"Erro no batch {stats['batches']}: {e}"
                    logger.error(error_msg)
                    stats["errors"] += len(batch)
                    stats["errors_list"].append(error_msg)
        finally:
            db.close()
        
        logger.info(f"\n✅ Adicionados {stats['success']} documentos ao RAG")
        if stats["errors"] > 0:
            logger.warning(f"⚠️  {stats['errors']} documentos com erro")
        
        return stats
    
    def save_papers_json(
        self,
        papers: List[Dict[str, Any]],
        output_file: str
    ):
        """Salva papers em arquivo JSON."""
        output_path = Path(__file__).parent.parent / "data" / "raw" / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(papers, f, ensure_ascii=False, indent=2)
        
        logger.info(f"💾 Papers salvos em: {output_path}")
    
    def run_full_pipeline(
        self,
        neurodivergence_types: List[str] = None,
        max_results_per_source: int = 20,
        save_json: bool = True,
        add_to_rag: bool = True
    ) -> Dict[str, Any]:
        """
        Executa pipeline completo: busca, processa e adiciona ao RAG.
        
        Args:
            neurodivergence_types: Lista de tipos a buscar (None = todos)
            max_results_per_source: Máximo de resultados por fonte
            save_json: Se deve salvar papers em JSON
            add_to_rag: Se deve adicionar ao RAG
        
        Returns:
            Estatísticas completas
        """
        if neurodivergence_types is None:
            neurodivergence_types = ["ADHD", "dyslexia", "autism", "neurodivergence"]
        
        logger.info("=" * 60)
        logger.info("PIPELINE COMPLETO: Scraping de Papers sobre Neurodivergências")
        logger.info("=" * 60)
        
        stats = {
            "started_at": datetime.now().isoformat(),
            "neurodivergence_types": neurodivergence_types,
            "papers_by_type": {},
            "total_papers": 0,
            "total_chunks": 0,
            "rag_stats": {},
            "errors": []
        }
        
        all_processed_docs = []
        
        # Buscar papers para cada tipo
        for neuro_type in neurodivergence_types:
            try:
                # Buscar papers
                papers = self.search_all_sources(
                    neurodivergence_type=neuro_type,
                    max_results_per_source=max_results_per_source
                )
                
                stats["papers_by_type"][neuro_type] = len(papers)
                stats["total_papers"] += len(papers)
                
                # Salvar JSON se solicitado
                if save_json and papers:
                    self.save_papers_json(
                        papers,
                        f"papers_{neuro_type}_{datetime.now().strftime('%Y%m%d')}.json"
                    )
                
                # Processar para RAG
                processed = self.process_papers_for_rag(papers, neuro_type)
                all_processed_docs.extend(processed)
                
            except Exception as e:
                error_msg = f"Erro ao processar {neuro_type}: {e}"
                logger.error(error_msg, exc_info=True)
                stats["errors"].append(error_msg)
        
        stats["total_chunks"] = len(all_processed_docs)
        
        # Adicionar ao RAG se solicitado
        if add_to_rag and all_processed_docs:
            rag_stats = self.add_to_rag(all_processed_docs)
            stats["rag_stats"] = rag_stats
        
        stats["completed_at"] = datetime.now().isoformat()
        
        return stats


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Scraping de papers sobre neurodivergências e organização para RAG"
    )
    
    parser.add_argument(
        "--types",
        nargs="+",
        choices=["ADHD", "dyslexia", "autism", "neurodivergence"],
        default=["ADHD", "dyslexia", "autism"],
        help="Tipos de neurodivergência a buscar"
    )
    
    parser.add_argument(
        "--max-results",
        type=int,
        default=20,
        help="Máximo de resultados por fonte (padrão: 20)"
    )
    
    parser.add_argument(
        "--no-rag",
        action="store_true",
        help="Não adicionar ao RAG (apenas coletar e processar)"
    )
    
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Não salvar papers em JSON"
    )
    
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=2000,
        help="Tamanho dos chunks para RAG (padrão: 2000)"
    )
    
    args = parser.parse_args()
    
    # Criar scraper
    scraper = NeurodivergencePaperScraper(chunk_size=args.chunk_size)
    
    # Executar pipeline
    try:
        stats = scraper.run_full_pipeline(
            neurodivergence_types=args.types,
            max_results_per_source=args.max_results,
            save_json=not args.no_save,
            add_to_rag=not args.no_rag
        )
        
        # Mostrar resumo
        print("\n" + "=" * 60)
        print("RESUMO DA EXECUÇÃO")
        print("=" * 60)
        print(f"Tipos processados: {', '.join(stats['neurodivergence_types'])}")
        print(f"Total de papers: {stats['total_papers']}")
        print(f"Total de chunks: {stats['total_chunks']}")
        
        print("\nPapers por tipo:")
        for neuro_type, count in stats['papers_by_type'].items():
            print(f"  - {neuro_type}: {count}")
        
        if stats.get('rag_stats'):
            print(f"\nRAG:")
            print(f"  - Documentos adicionados: {stats['rag_stats'].get('success', 0)}")
            print(f"  - Erros: {stats['rag_stats'].get('errors', 0)}")
        
        if stats.get('errors'):
            print(f"\n⚠️  Erros encontrados: {len(stats['errors'])}")
            for error in stats['errors'][:5]:  # Mostrar apenas os 5 primeiros
                print(f"  - {error}")
        
        print("\n" + "=" * 60)
        
    except KeyboardInterrupt:
        logger.info("\n⚠️  Processo interrompido pelo usuário")
        return 1
    except Exception as e:
        logger.error(f"Erro durante execução: {e}", exc_info=True)
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
