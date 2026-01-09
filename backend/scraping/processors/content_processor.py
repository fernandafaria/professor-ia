"""
Processadores de conteúdo coletado via scraping.
"""

import logging
import hashlib
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class ContentProcessor:
    """Processa e normaliza conteúdo coletado."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Inicializa processador.
        
        Args:
            chunk_size: Tamanho máximo de chunk em caracteres
            chunk_overlap: Sobreposição entre chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def generate_id(self, document: Dict[str, Any]) -> str:
        """
        Gera ID único para documento baseado em URL e conteúdo.
        
        Args:
            document: Documento a processar
            
        Returns:
            ID único (hash)
        """
        url = document.get("url", "")
        title = document.get("title", "")
        content_preview = document.get("content", "")[:100]
        
        content_to_hash = f"{url}|{title}|{content_preview}"
        return hashlib.md5(content_to_hash.encode()).hexdigest()
    
    def chunk_content(self, content: str) -> List[str]:
        """
        Divide conteúdo em chunks para RAG.
        
        Args:
            content: Conteúdo a dividir
            
        Returns:
            Lista de chunks
        """
        if len(content) <= self.chunk_size:
            return [content]
        
        chunks = []
        start = 0
        
        while start < len(content):
            end = start + self.chunk_size
            
            # Tentar quebrar em ponto final ou quebra de linha
            if end < len(content):
                # Buscar último ponto final antes do limite
                last_period = content.rfind(".", start, end)
                last_newline = content.rfind("\n", start, end)
                
                # Usar o mais próximo do limite
                break_point = max(last_period, last_newline)
                
                if break_point > start:
                    end = break_point + 1
            
            chunk = content[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Mover start considerando overlap
            start = end - self.chunk_overlap
            if start < 0:
                start = 0
        
        return chunks
    
    def process_document(
        self,
        document: Dict[str, Any],
        chunk: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Processa um documento coletado.
        
        Args:
            document: Documento bruto do scraper
            chunk: Se deve dividir em chunks
            
        Returns:
            Lista de documentos processados (pode ser múltiplos se chunk=True)
        """
        base_id = self.generate_id(document)
        
        if not chunk:
            # Retornar documento único
            return [{
                "id": base_id,
                "content": document.get("content", ""),
                "metadata": {
                    **document.get("metadata", {}),
                    "source": document.get("source", ""),
                    "source_url": document.get("source_url", ""),
                    "title": document.get("title", ""),
                    "url": document.get("url", ""),
                    "tags": document.get("tags", []),
                    "processed_at": datetime.utcnow().isoformat(),
                },
            }]
        
        # Dividir em chunks
        content = document.get("content", "")
        chunks = self.chunk_content(content)
        
        processed_docs = []
        for i, chunk_text in enumerate(chunks):
            chunk_id = f"{base_id}_chunk_{i}"
            
            processed_doc = {
                "id": chunk_id,
                "content": chunk_text,
                "metadata": {
                    **document.get("metadata", {}),
                    "source": document.get("source", ""),
                    "source_url": document.get("source_url", ""),
                    "title": document.get("title", ""),
                    "url": document.get("url", ""),
                    "tags": document.get("tags", []),
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "processed_at": datetime.utcnow().isoformat(),
                },
            }
            
            processed_docs.append(processed_doc)
        
        return processed_docs
    
    def enrich_with_bncc(
        self,
        document: Dict[str, Any],
        bncc_mapper: Optional[Any] = None
    ) -> Dict[str, Any]:
        """
        Enriquece documento com informações BNCC.
        
        Args:
            document: Documento a enriquecer
            bncc_mapper: Mapper BNCC (opcional, para implementação futura)
            
        Returns:
            Documento enriquecido
        """
        metadata = document.get("metadata", {})
        
        # Extrair habilidades BNCC se presentes
        bncc_skills = metadata.get("bncc_skills", [])
        if bncc_skills:
            metadata["bncc_aligned"] = True
            metadata["bncc_skills_list"] = bncc_skills
        
        # Tentar inferir série/ano do título ou conteúdo
        grade = metadata.get("grade")
        if not grade:
            # Lógica simples de inferência (pode ser melhorada)
            title_lower = document.get("title", "").lower()
            content_lower = document.get("content", "").lower()[:500]
            
            for grade_term in ["6º", "7º", "8º", "9º", "1º ano", "2º ano", "3º ano"]:
                if grade_term in title_lower or grade_term in content_lower:
                    metadata["inferred_grade"] = grade_term
                    break
        
        document["metadata"] = metadata
        return document
    
    def filter_by_quality(
        self,
        documents: List[Dict[str, Any]],
        min_content_length: int = 100,
        min_title_length: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Filtra documentos por qualidade.
        
        Args:
            documents: Lista de documentos
            min_content_length: Tamanho mínimo de conteúdo
            min_title_length: Tamanho mínimo de título
            
        Returns:
            Lista de documentos filtrados
        """
        filtered = []
        
        for doc in documents:
            content = doc.get("content", "")
            title = doc.get("title", "")
            
            # Verificar tamanhos mínimos
            if len(content) < min_content_length:
                logger.debug(f"Documento rejeitado: conteúdo muito curto ({len(content)} chars)")
                continue
            
            if len(title) < min_title_length:
                logger.debug(f"Documento rejeitado: título muito curto ({len(title)} chars)")
                continue
            
            # Verificar se não é apenas espaços
            if not content.strip() or not title.strip():
                logger.debug("Documento rejeitado: conteúdo vazio")
                continue
            
            filtered.append(doc)
        
        logger.info(f"Filtrados {len(documents)} -> {len(filtered)} documentos por qualidade")
        return filtered
