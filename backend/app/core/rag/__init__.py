"""
Sistema RAG (Retrieval-Augmented Generation).
"""

# Importar o retriever do Supabase (padrão)
from app.core.rag.retriever_supabase import RAGRetriever

# RAG agora usa exclusivamente Supabase/pgvector
# O retriever antigo (ChromaDB) foi removido

__all__ = ["RAGRetriever"]
