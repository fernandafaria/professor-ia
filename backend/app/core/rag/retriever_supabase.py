"""
Motor de recuperação de informações (Retriever) para o sistema RAG usando Supabase/pgvector.
"""

from sqlalchemy.orm import Session
from sqlalchemy import text, bindparam
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer
import numpy as np
import json
from app.config import settings
from app.services.database import get_db


class RAGRetriever:
    """Motor de recuperação semântica para RAG usando Supabase com pgvector."""
    
    def __init__(
        self,
        db: Optional[Session] = None,
        embedding_model: str = None,
        embedding_dimension: int = 384,  # Dimensão do modelo padrão
    ):
        """
        Inicializa o retriever.
        
        Args:
            db: Sessão do banco de dados (opcional, pode ser passado nos métodos)
            embedding_model: Nome do modelo de embedding
            embedding_dimension: Dimensão dos embeddings (384 para multilingual-MiniLM)
        """
        self.embedding_model_name = embedding_model or settings.EMBEDDING_MODEL
        self.embedding_dimension = embedding_dimension or settings.EMBEDDING_DIMENSION
        
        # Carregar modelo de embedding
        self.embedding_model = SentenceTransformer(self.embedding_model_name)
        
        # Verificar dimensão do modelo
        test_embedding = self.embedding_model.encode("test")
        actual_dimension = len(test_embedding)
        if actual_dimension != embedding_dimension:
            print(f"⚠️  Aviso: Dimensão do modelo ({actual_dimension}) diferente da configurada ({embedding_dimension})")
            self.embedding_dimension = actual_dimension
    
    def encode_query(self, query: str) -> List[float]:
        """Converte query em embedding."""
        embedding = self.embedding_model.encode(query, convert_to_numpy=True)
        return embedding.tolist()
    
    def retrieve(
        self,
        query: str,
        db: Optional[Session] = None,
        n_results: int = 5,
        filters: Optional[Dict] = None,
        student_interests: Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Recupera documentos relevantes para a query usando busca vetorial no Supabase.
        
        Args:
            query: Query do usuário
            db: Sessão do banco de dados (obrigatório se não foi passado no __init__)
            n_results: Número de resultados a retornar
            filters: Filtros adicionais (ex: {"subject": "matematica", "grade": "9º EF"})
            student_interests: Interesses do estudante para personalização
        
        Returns:
            Lista de documentos relevantes com metadata
        """
        if db is None:
            raise ValueError("Session do banco de dados é obrigatória. Passe 'db' como parâmetro.")
        
        # Adicionar contexto de interesses à query se disponível
        enriched_query = self._enrich_query_with_interests(query, student_interests)
        
        # Converter query em embedding
        query_embedding = self.encode_query(enriched_query)
        
        # Construir query SQL com busca vetorial
        # Usa cosine distance (1 - cosine similarity)
        sql = f"""
        SELECT 
            id,
            content,
            metadata,
            source,
            subject,
            grade,
            1 - (embedding <=> CAST(:embedding AS vector)) as similarity
        FROM {settings.RAG_TABLE_NAME}
        WHERE embedding IS NOT NULL
        """
        
        # Adicionar filtros
        params = {"embedding": str(query_embedding)}
        if filters:
            if "subject" in filters:
                sql += " AND subject = :subject"
                params["subject"] = filters["subject"]
            if "grade" in filters:
                sql += " AND grade = :grade"
                params["grade"] = filters["grade"]
            if "source" in filters:
                sql += " AND source = :source"
                params["source"] = filters["source"]
        
        # Ordenar por similaridade e limitar resultados
        sql += " ORDER BY embedding <=> CAST(:embedding AS vector) LIMIT :limit"
        params["limit"] = n_results
        
        # Executar query
        try:
            result = db.execute(text(sql), params)
            rows = result.fetchall()
            
            # Formatar resultados
            documents = []
            for row in rows:
                doc = {
                    "id": str(row[0]),
                    "content": row[1],
                    "metadata": row[2] if row[2] else {},
                    "source": row[3],
                    "subject": row[4],
                    "grade": row[5],
                    "similarity": float(row[6]),
                    "distance": 1 - float(row[6]),  # Converter similarity para distance
                }
                # Adicionar source ao metadata se existir
                if row[3]:
                    doc["metadata"]["source"] = row[3]
                
                documents.append(doc)
            
            return documents
        except Exception as e:
            print(f"Erro ao buscar documentos no Supabase: {e}")
            return []
    
    def _enrich_query_with_interests(
        self,
        query: str,
        interests: Optional[List[str]]
    ) -> str:
        """Enriquece a query com interesses do estudante."""
        if not interests:
            return query
        
        interests_str = ", ".join(interests)
        enriched = f"{query} [contexto: interesses do aluno incluem {interests_str}]"
        return enriched
    
    def add_documents(
        self,
        documents: List[str],
        metadatas: List[Dict],
        ids: Optional[List[str]] = None,
        db: Optional[Session] = None,
    ):
        """
        Adiciona documentos à base de conhecimento no Supabase.
        
        Args:
            documents: Lista de textos dos documentos
            metadatas: Lista de metadados (um por documento)
            ids: Lista de IDs (opcional, será gerado UUID se não fornecido)
            db: Sessão do banco de dados (obrigatório se não foi passado no __init__)
        """
        if db is None:
            raise ValueError("Session do banco de dados é obrigatória. Passe 'db' como parâmetro.")
        
        if len(documents) != len(metadatas):
            raise ValueError("Número de documentos deve ser igual ao número de metadados")
        
        # Gerar embeddings
        embeddings = self.embedding_model.encode(
            documents,
            convert_to_numpy=True,
            show_progress_bar=True,
        )
        
        # Preparar dados para inserção
        for i, (doc, metadata) in enumerate(zip(documents, metadatas)):
            doc_id = ids[i] if ids and i < len(ids) else None
            embedding = embeddings[i].tolist()
            
            # Extrair campos comuns do metadata
            source = metadata.get("source")
            subject = metadata.get("subject")
            grade = metadata.get("grade")
            
            # Inserir no banco
            # Converter metadata para JSON string se necessário
            metadata_json = json.dumps(metadata) if isinstance(metadata, dict) else metadata
            
            # Construir SQL usando :param (SQLAlchemy style)
            embedding_str = str(embedding)
            
            if doc_id:
                # Com ID fornecido
                sql = f"""
                INSERT INTO {settings.RAG_TABLE_NAME} (id, content, embedding, metadata, source, subject, grade)
                VALUES (
                    :id::uuid,
                    :content,
                    :embedding::vector,
                    :metadata::jsonb,
                    :source,
                    :subject,
                    :grade
                )
                ON CONFLICT (id) DO UPDATE SET
                    content = EXCLUDED.content,
                    embedding = EXCLUDED.embedding,
                    metadata = EXCLUDED.metadata,
                    source = EXCLUDED.source,
                    subject = EXCLUDED.subject,
                    grade = EXCLUDED.grade,
                    updated_at = NOW()
                """
                params = {
                    "id": doc_id,
                    "content": doc,
                    "embedding": embedding_str,
                    "metadata": metadata_json,
                    "source": source,
                    "subject": subject,
                    "grade": grade,
                }
            else:
                # Sem ID - gerar UUID automaticamente
                sql = f"""
                INSERT INTO {settings.RAG_TABLE_NAME} (content, embedding, metadata, source, subject, grade)
                VALUES (
                    :content,
                    :embedding::vector,
                    :metadata::jsonb,
                    :source,
                    :subject,
                    :grade
                )
                """
                params = {
                    "content": doc,
                    "embedding": embedding_str,
                    "metadata": metadata_json,
                    "source": source,
                    "subject": subject,
                    "grade": grade,
                }
            
            try:
                # Usar função PostgreSQL para fazer cast do vector
                # Formato do embedding: '[0.1, 0.2, ...]' precisa ser convertido para vector
                if doc_id:
                    sql = f"""
                    INSERT INTO {settings.RAG_TABLE_NAME} (id, content, embedding, metadata, source, subject, grade)
                    VALUES (
                        :id::uuid,
                        :content,
                        CAST(:embedding AS vector),
                        CAST(:metadata AS jsonb),
                        :source,
                        :subject,
                        :grade
                    )
                    ON CONFLICT (id) DO UPDATE SET
                        content = EXCLUDED.content,
                        embedding = EXCLUDED.embedding,
                        metadata = EXCLUDED.metadata,
                        source = EXCLUDED.source,
                        subject = EXCLUDED.subject,
                        grade = EXCLUDED.grade,
                        updated_at = NOW()
                    """
                    params = {
                        "id": doc_id,
                        "content": doc,
                        "embedding": embedding_str,
                        "metadata": metadata_json,
                        "source": source,
                        "subject": subject,
                        "grade": grade,
                    }
                else:
                    sql = f"""
                    INSERT INTO {settings.RAG_TABLE_NAME} (content, embedding, metadata, source, subject, grade)
                    VALUES (
                        :content,
                        CAST(:embedding AS vector),
                        CAST(:metadata AS jsonb),
                        :source,
                        :subject,
                        :grade
                    )
                    """
                    params = {
                        "content": doc,
                        "embedding": embedding_str,
                        "metadata": metadata_json,
                        "source": source,
                        "subject": subject,
                        "grade": grade,
                    }
                
                db.execute(text(sql), params)
            except Exception as e:
                print(f"Erro ao inserir documento {i}: {e}")
                continue
        
        # Commit das inserções
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(f"Erro ao commitar documentos: {e}")
    
    def delete_documents(
        self,
        ids: List[str],
        db: Optional[Session] = None,
    ):
        """
        Remove documentos da base de conhecimento.
        
        Args:
            ids: Lista de IDs dos documentos a remover
            db: Sessão do banco de dados
        """
        if db is None:
            raise ValueError("Session do banco de dados é obrigatória.")
        
        sql = f"DELETE FROM {settings.RAG_TABLE_NAME} WHERE id = ANY(:ids::uuid[])"
        
        try:
            db.execute(text(sql), {"ids": ids})
            db.commit()
        except Exception as e:
            db.rollback()
            raise Exception(f"Erro ao deletar documentos: {e}")
