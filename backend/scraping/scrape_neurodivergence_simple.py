"""
Script simplificado para scraping de papers sobre neurodivergências.
Versão standalone que não depende da estrutura completa do projeto.
"""

import requests
import json
import time
import logging
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
from xml.etree import ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SimplePubMedScraper:
    """Scraper simplificado para PubMed"""
    
    def __init__(self):
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.timeout = 60
    
    def search_papers(self, query: str, max_results: int = 20) -> List[Dict]:
        """Busca papers no PubMed"""
        logger.info(f"Buscando no PubMed: '{query}' (max: {max_results})")
        
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
            logger.info(f"Encontrados {len(ids)} IDs")
            
            if not ids:
                return []
            
            # Buscar detalhes
            return self._fetch_details(ids)
        except Exception as e:
            logger.error(f"Erro ao buscar no PubMed: {e}")
            return []
    
    def _fetch_details(self, ids: List[str]) -> List[Dict]:
        """Busca detalhes dos papers"""
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
                paper = self._extract_paper(article)
                if paper:
                    papers.append(paper)
            
            return papers
        except Exception as e:
            logger.error(f"Erro ao buscar detalhes: {e}")
            return []
    
    def _extract_paper(self, article) -> Optional[Dict]:
        """Extrai dados de um paper"""
        try:
            # Título
            title_elem = article.find(".//ArticleTitle")
            title = title_elem.text if title_elem is not None else ""
            
            # Abstract
            abstract_elems = article.findall(".//AbstractText")
            abstract = " ".join([elem.text for elem in abstract_elems if elem.text])
            
            # Autores
            authors = []
            for author in article.findall(".//Author"):
                last_name = author.find("LastName")
                first_name = author.find("ForeName")
                if last_name is not None and first_name is not None:
                    authors.append(f"{first_name.text} {last_name.text}")
            
            # Data
            pub_date = article.find(".//PubDate")
            date_str = ""
            if pub_date is not None:
                year = pub_date.find("Year")
                if year is not None:
                    date_str = year.text
            
            # DOI
            doi_elem = article.find(".//ArticleId[@IdType='doi']")
            doi = doi_elem.text if doi_elem is not None else ""
            
            # PubMed ID
            pmid_elem = article.find(".//PMID")
            pmid = pmid_elem.text if pmid_elem is not None else ""
            url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}" if pmid else ""
            
            return {
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "publication_date": date_str,
                "doi": doi,
                "source_url": url,
                "source_database": "PubMed",
                "language": "en"
            }
        except Exception as e:
            logger.error(f"Erro ao extrair paper: {e}")
            return None


class SimpleSciELOScraper:
    """Scraper simplificado para SciELO"""
    
    def __init__(self):
        self.api_url = "https://api.scielo.org/v1/"
        self.timeout = 60
    
    def search_papers(self, query: str, max_results: int = 20) -> List[Dict]:
        """Busca papers no SciELO"""
        logger.info(f"Buscando no SciELO: '{query}' (max: {max_results})")
        
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
                paper = {
                    "title": item.get("title", [""])[0] if item.get("title") else "",
                    "abstract": item.get("abstract", [""])[0] if item.get("abstract") else "",
                    "authors": item.get("author", []),
                    "publication_date": item.get("publication_date", ""),
                    "doi": item.get("doi", ""),
                    "source_url": item.get("url", ""),
                    "source_database": "SciELO",
                    "language": "pt-BR"
                }
                if paper["title"]:
                    papers.append(paper)
            
            logger.info(f"Encontrados {len(papers)} papers no SciELO")
            return papers
        except Exception as e:
            logger.error(f"Erro ao buscar no SciELO: {e}")
            return []


def process_papers_for_rag(papers: List[Dict], neurodivergence_type: str) -> List[Dict]:
    """Processa papers para formato RAG"""
    logger.info(f"Processando {len(papers)} papers para RAG...")
    
    processed = []
    chunk_size = 2000
    chunk_overlap = 400
    
    for paper in papers:
        # Validar
        if not paper.get("title") or not paper.get("abstract"):
            continue
        
        if len(paper.get("abstract", "")) < 200:
            continue
        
        # Criar conteúdo
        content_parts = [
            f"Título: {paper.get('title', '')}",
            f"\nResumo:\n{paper.get('abstract', '')}"
        ]
        
        authors = paper.get("authors", [])
        if authors:
            content_parts.append(f"\nAutores: {', '.join(authors[:5])}")
        
        content = "\n".join(content_parts)
        
        # Chunking simples
        if len(content) <= chunk_size:
            chunks = [content]
        else:
            chunks = []
            start = 0
            while start < len(content):
                end = start + chunk_size
                if end < len(content):
                    # Quebrar em ponto final
                    last_period = content.rfind(".", start, end)
                    if last_period > start:
                        end = last_period + 1
                chunks.append(content[start:end].strip())
                start = end - chunk_overlap
        
        # Criar documentos
        for i, chunk_text in enumerate(chunks):
            doc = {
                "id": f"{hash(paper.get('source_url', ''))}_{i}",
                "content": chunk_text,
                "metadata": {
                    "title": paper.get("title", ""),
                    "source": paper.get("source_database", ""),
                    "source_url": paper.get("source_url", ""),
                    "authors": authors,
                    "publication_date": paper.get("publication_date", ""),
                    "doi": paper.get("doi", ""),
                    "neurodivergence_type": neurodivergence_type,
                    "language": paper.get("language", "en"),
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "processed_at": datetime.now().isoformat()
                }
            }
            processed.append(doc)
    
    logger.info(f"Criados {len(processed)} chunks de {len(papers)} papers")
    return processed


def save_to_json(papers: List[Dict], filename: str):
    """Salva papers em JSON"""
    output_dir = Path(__file__).parent.parent / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    
    logger.info(f"💾 Papers salvos em: {output_path}")


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Scraping de papers sobre neurodivergências")
    parser.add_argument("--types", nargs="+", default=["ADHD"], 
                       choices=["ADHD", "dyslexia", "autism"],
                       help="Tipos de neurodivergência")
    parser.add_argument("--max-results", type=int, default=10,
                       help="Máximo de resultados por fonte")
    parser.add_argument("--output", type=str, default=None,
                       help="Arquivo de saída JSON")
    
    args = parser.parse_args()
    
    # Termos de busca
    search_terms = {
        "ADHD": ["ADHD educational intervention", "TDAH educação"],
        "dyslexia": ["dyslexia reading intervention", "dislexia aprendizagem"],
        "autism": ["autism educational strategies", "autismo educação"]
    }
    
    logger.info("=" * 60)
    logger.info("SCRAPING DE PAPERS SOBRE NEURODIVERGÊNCIAS")
    logger.info("=" * 60)
    
    all_papers = []
    pubmed_scraper = SimplePubMedScraper()
    scielo_scraper = SimpleSciELOScraper()
    
    for neuro_type in args.types:
        logger.info(f"\n📚 Processando: {neuro_type}")
        terms = search_terms.get(neuro_type, [])
        
        for term in terms[:2]:  # Limitar a 2 termos por tipo
            # PubMed (termos em inglês)
            if not any(c in term for c in "áéíóúãõç"):
                papers = pubmed_scraper.search_papers(term, args.max_results)
                for p in papers:
                    p["neurodivergence_type"] = neuro_type
                    p["search_term"] = term
                all_papers.extend(papers)
                time.sleep(1)  # Rate limiting
            
            # SciELO (termos em português)
            if any(c in term for c in "áéíóúãõç"):
                papers = scielo_scraper.search_papers(term, args.max_results)
                for p in papers:
                    p["neurodivergence_type"] = neuro_type
                    p["search_term"] = term
                all_papers.extend(papers)
                time.sleep(1)  # Rate limiting
    
    # Remover duplicatas
    seen_titles = set()
    unique_papers = []
    for paper in all_papers:
        title = paper.get("title", "").lower().strip()
        if title and title not in seen_titles:
            seen_titles.add(title)
            unique_papers.append(paper)
    
    logger.info(f"\n✅ Total de papers únicos: {len(unique_papers)}")
    
    # Salvar JSON
    if args.output:
        filename = args.output
    else:
        filename = f"papers_neurodivergence_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    save_to_json(unique_papers, filename)
    
    # Processar para RAG
    logger.info("\n📝 Processando para RAG...")
    all_processed = []
    for neuro_type in args.types:
        type_papers = [p for p in unique_papers if p.get("neurodivergence_type") == neuro_type]
        processed = process_papers_for_rag(type_papers, neuro_type)
        all_processed.extend(processed)
    
    # Salvar chunks processados
    chunks_filename = filename.replace(".json", "_chunks.json")
    save_to_json(all_processed, chunks_filename)
    
    logger.info(f"\n✅ Processamento completo!")
    logger.info(f"  - Papers coletados: {len(unique_papers)}")
    logger.info(f"  - Chunks criados: {len(all_processed)}")
    logger.info(f"  - Arquivos salvos: {filename}, {chunks_filename}")
    
    return 0


if __name__ == "__main__":
    exit(main())
