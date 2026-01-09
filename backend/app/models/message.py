"""
Modelo de dados para Mensagem.
Conforme especificação MVP - Seção 4.4
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Integer, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base
import enum


class MessageRole(str, enum.Enum):
    """Papel da mensagem."""
    USER = "user"
    ASSISTANT = "assistant"


class Message(Base):
    """Modelo de mensagem."""
    
    __tablename__ = "messages"
    
    id = Column(String, primary_key=True)  # UUID
    conversation_id = Column(String, ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, index=True)
    role = Column(SQLEnum(MessageRole), nullable=False)
    content = Column(String, nullable=False)  # Conteúdo da mensagem
    message_metadata = Column(JSON, default=dict)  # Metadados adicionais (tokens, model, latency, ragSources)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    conversation = relationship("Conversation", back_populates="messages")
    
    def __repr__(self):
        return f"<Message(id={self.id}, role={self.role}, content_length={len(self.content)})>"
