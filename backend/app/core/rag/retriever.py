"""
Motor de recuperação de informações (Retriever) para o sistema RAG.
"""

import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer
import numpy as np
from app.config import settings


class RAGRetriever:
    """Motor de recuperação semântica para RAG."""
    
    def __init__(
        self,
        collection_name: str = None,
        embedding_model: str = None,
    ):
        """Inicializa o retriever."""
        self.collection_name = collection_name or settings.CHROMA_COLLECTION_NAME
        self.embedding_model_name = embedding_model or settings.EMBEDDING_MODEL
        
        # Inicializar ChromaDB
        self.chroma_client = chromadb.Client(
            ChromaSettings(
                chroma_api_impl="rest",
                chroma_server_host=settings.CHROMA_HOST,
                chroma_server_http_port=settings.CHROMA_PORT,
            )
        )
        
        # Carregar ou criar collection
        try:
            self.collection = self.chroma_client.get_collection(name=self.collection_name)
        except:
            self.collection = self.chroma_client.create_collection(
                name=self.collection_name,
                metadata={"description": "Educational content for RAG"}
            )
        
        # Carregar modelo de embedding
        self.embedding_model = SentenceTransformer(self.embedding_model_name)
    
    def encode_query(self, query: str) -> List[float]:
        """Converte query em embedding."""
        embedding = self.embedding_model.encode(query, convert_to_numpy=True)
        return embedding.tolist()
    
    def retrieve(
        self,
        query: str,
        n_results: int = 5,
        filters: Optional[Dict] = None,
        student_interests: Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Recupera documentos relevantes para a query.
        
        Args:
            query: Query do usuário
            n_results: Número de resultados a retornar
            filters: Filtros adicionais (ex: {"grade": "9º EF"})
            student_interests: Interesses do estudante para personalização
        
        Returns:
            Lista de documentos relevantes com metadata
        """
        # Adicionar contexto de interesses à query se disponível
        enriched_query = self._enrich_query_with_interests(query, student_interests)
        
        # Converter query em embedding
        query_embedding = self.encode_query(enriched_query)
        
        # Preparar filtros
        where = filters or {}
        
        # Buscar no ChromaDB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            where=where,
        )
        
        # Formatar resultados
        documents = []
        if results["ids"] and len(results["ids"][0]) > 0:
            for i in range(len(results["ids"][0])):
                doc = {
                    "id": results["ids"][0][i],
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else None,
                }
                documents.append(doc)
        
        return documents
    
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
        ids: List[str],
    ):
        """Adiciona documentos à base de conhecimento."""
        # Gerar embeddings
        embeddings = self.embedding_model.encode(
            documents,
            convert_to_numpy=True,
            show_progress_bar=True,
        ).tolist()
        
        # Adicionar ao ChromaDB
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids,
        )
