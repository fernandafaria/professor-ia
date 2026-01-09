"""
Importador para dados BNCC já coletados em formato JSON.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import hashlib

from ..processors import ContentProcessor
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class BNCCJSONImporter:
    """Importa dados BNCC de arquivo JSON já coletado."""
    
    def __init__(
        self,
        json_file_path: str,
        retriever: Optional[RAGRetriever] = None,
        processor: Optional[ContentProcessor] = None,
    ):
        """
        Inicializa importador.
        
        Args:
            json_file_path: Caminho para arquivo JSON
            retriever: Instância do RAGRetriever (opcional)
            processor: Instância do ContentProcessor (opcional)
        """
        self.json_file_path = Path(json_file_path)
        self.processor = processor or ContentProcessor()
        self.retriever = retriever or RAGRetriever()
    
    def _generate_id(self, item: Dict[str, Any], category: str) -> str:
        """Gera ID único para item BNCC."""
        code = item.get("code", "")
        content_preview = item.get("skill", "")[:50]
        content_to_hash = f"{category}|{code}|{content_preview}"
        return hashlib.md5(content_to_hash.encode()).hexdigest()
    
    def _process_bncc_item(
        self,
        item: Dict[str, Any],
        category: str,
        chunk: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Processa um item BNCC.
        
        Args:
            item: Item BNCC do JSON
            category: Categoria (fundamental_education, high_school)
            chunk: Se deve dividir em chunks
            
        Returns:
            Lista de documentos processados
        """
        code = item.get("code", "")
        skill = item.get("skill", "")
        competency = item.get("competency", "")
        knowledge_object = item.get("knowledge_object", "")
        
        # Construir conteúdo completo
        content_parts = []
        
        if skill:
            content_parts.append(f"Habilidade: {skill}")
        
        if competency:
            # Competency pode ser muito longo, truncar se necessário
            competency_short = competency[:500] + "..." if len(competency) > 500 else competency
            content_parts.append(f"\nCompetência: {competency_short}")
        
        if knowledge_object:
            content_parts.append(f"\nObjeto de Conhecimento: {knowledge_object}")
        
        content = "\n".join(content_parts)
        
        # Determinar nível educacional
        education_level = "Ensino Fundamental" if category == "fundamental_education" else "Ensino Médio"
        
        # Extrair série/ano do código se possível
        grade = None
        if code.startswith("EF01"):
            grade = "1º ano EF"
        elif code.startswith("EF02"):
            grade = "2º ano EF"
        elif code.startswith("EF03"):
            grade = "3º ano EF"
        elif code.startswith("EF04"):
            grade = "4º ano EF"
        elif code.startswith("EF05"):
            grade = "5º ano EF"
        elif code.startswith("EF67"):
            grade = "6º/7º ano EF"
        elif code.startswith("EF89"):
            grade = "8º/9º ano EF"
        elif code.startswith("EM"):
            grade = "Ensino Médio"
        
        # Extrair disciplina do código
        discipline = None
        if "LP" in code:
            discipline = "Língua Portuguesa"
        elif "MA" in code:
            discipline = "Matemática"
        elif "CI" in code:
            discipline = "Ciências"
        elif "HI" in code:
            discipline = "História"
        elif "GE" in code:
            discipline = "Geografia"
        elif "AR" in code:
            discipline = "Arte"
        elif "EF" in code and "LP" not in code and "MA" not in code:
            discipline = "Educação Física"
        elif "LI" in code:
            discipline = "Língua Inglesa"
        
        # Criar documento base
        base_doc = {
            "title": f"{code} - {skill[:100]}" if skill else code,
            "content": content,
            "metadata": {
                "type": "bncc_skill",
                "code": code,
                "education_level": education_level,
                "grade": grade,
                "discipline": discipline,
                "knowledge_object": knowledge_object,
                "source": "BNCC JSON Import",
                "source_url": item.get("code_citation", ""),
                "skill_citation": item.get("skill_citation", ""),
                "competency_citation": item.get("competency_citation", ""),
                "knowledge_object_citation": item.get("knowledge_object_citation", ""),
            },
            "tags": [discipline, grade] if discipline and grade else ([discipline] if discipline else []),
            "url": item.get("code_citation", ""),
        }
        
        # Processar com ContentProcessor
        processed = self.processor.process_document(base_doc, chunk=chunk)
        
        return processed
    
    def load_json(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Carrega arquivo JSON.
        
        Returns:
            Dicionário com dados BNCC
        """
        logger.info(f"Carregando arquivo JSON: {self.json_file_path}")
        
        try:
            with open(self.json_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            logger.info(f"Arquivo carregado: {len(data)} categorias")
            for category, items in data.items():
                logger.info(f"  - {category}: {len(items)} itens")
            
            return data
        except Exception as e:
            logger.error(f"Erro ao carregar JSON: {e}", exc_info=True)
            raise
    
    def import_data(
        self,
        categories: Optional[List[str]] = None,
        chunk: bool = True,
        add_to_rag: bool = True,
        batch_size: int = 100
    ) -> Dict[str, Any]:
        """
        Importa dados do JSON.
        
        Args:
            categories: Categorias a importar (None = todas)
            chunk: Se deve dividir em chunks
            add_to_rag: Se deve adicionar ao RAG
            batch_size: Tamanho do lote para adicionar ao RAG
            
        Returns:
            Estatísticas da importação
        """
        # Carregar dados
        data = self.load_json()
        
        # Filtrar categorias se especificado
        if categories:
            data = {k: v for k, v in data.items() if k in categories}
        
        stats = {
            "categories_processed": 0,
            "items_processed": 0,
            "documents_created": 0,
            "chunks_created": 0,
            "errors": [],
        }
        
        all_documents = []
        
        # Processar cada categoria
        for category, items in data.items():
            logger.info(f"Processando categoria: {category} ({len(items)} itens)")
            stats["categories_processed"] += 1
            
            for item in items:
                try:
                    processed = self._process_bncc_item(item, category, chunk=chunk)
                    all_documents.extend(processed)
                    stats["items_processed"] += 1
                    stats["documents_created"] += len(processed)
                except Exception as e:
                    error_msg = f"Erro ao processar item {item.get('code', 'unknown')}: {e}"
                    logger.error(error_msg, exc_info=True)
                    stats["errors"].append(error_msg)
        
        stats["chunks_created"] = len(all_documents)
        
        # Filtrar por qualidade
        all_documents = self.processor.filter_by_quality(all_documents)
        stats["documents_after_filter"] = len(all_documents)
        
        # Adicionar ao RAG se solicitado
        if add_to_rag and all_documents:
            logger.info(f"Adicionando {len(all_documents)} documentos ao RAG")
            try:
                # Obter sessão do banco de dados
                db_gen = get_db()
                db = next(db_gen)
                try:
                    # Processar em lotes
                    for i in range(0, len(all_documents), batch_size):
                        batch = all_documents[i:i + batch_size]
                        self.retriever.add_documents(
                            documents=[doc["content"] for doc in batch],
                            metadatas=[doc["metadata"] for doc in batch],
                            ids=[doc["id"] for doc in batch],
                            db=db
                        )
                        logger.info(f"Lote {i // batch_size + 1} adicionado ({len(batch)} documentos)")
                    
                    stats["added_to_rag"] = True
                    logger.info("✓ Documentos adicionados ao RAG com sucesso")
                finally:
                    db.close()
            except Exception as e:
                error_msg = f"Erro ao adicionar ao RAG: {e}"
                logger.error(error_msg, exc_info=True)
                stats["errors"].append(error_msg)
                stats["added_to_rag"] = False
        else:
            stats["added_to_rag"] = False
        
        logger.info(f"Importação concluída: {stats}")
        return stats
