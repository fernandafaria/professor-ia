"""
Configurações da aplicação.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configurações da aplicação."""
    
    # App
    APP_NAME: str = "Plataforma Educacional P1A"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:3001"  # Separado por vírgula no .env
    
    @property
    def cors_origins_list(self) -> list[str]:
        """Converte CORS_ORIGINS string em lista."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
    
    # Banco de dados
    DATABASE_URL: str
    DATABASE_ECHO: bool = False
    
    # Vector Database (Supabase com pgvector)
    RAG_TABLE_NAME: str = "rag_documents"  # Tabela para armazenar documentos RAG
    EMBEDDING_DIMENSION: int = 384  # Dimensão do modelo padrão (multilingual-MiniLM-L12-v2)
    
    # Anthropic Claude / LLM
    ANTHROPIC_API_KEY: Optional[str] = None
    ANTHROPIC_MODEL: str = "claude-3-5-sonnet-20241022"  # ou "claude-3-opus-20240229" para melhor qualidade
    
    # Embeddings (ainda usando OpenAI para embeddings, ou pode usar sentence-transformers)
    OPENAI_EMBEDDING_MODEL: Optional[str] = "text-embedding-3-large"  # Opcional, para embeddings
    OPENAI_API_KEY: Optional[str] = None  # Opcional, apenas se usar embeddings da OpenAI
    
    # Sentence Transformers (backup)
    EMBEDDING_MODEL: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    
    # Redis (Celery e cache)
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    
    # JWT / Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Web Scraping
    SCRAPING_DELAY_MIN: float = 1.0
    SCRAPING_DELAY_MAX: float = 3.0
    SCRAPING_USER_AGENT: str = "Mozilla/5.0 (Educational Platform Bot)"
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Web Scraping - Firecrawl
    FIRECRAWL_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Ignorar campos extras no .env


settings = Settings()
