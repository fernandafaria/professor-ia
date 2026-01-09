"""
Modelo de dados para Conversa.
Conforme especificação MVP - Seção 4.3
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base
from app.models.professor_profile import SubjectType


class Conversation(Base):
    """Modelo de conversa."""
    
    __tablename__ = "conversations"
    
    id = Column(String, primary_key=True)  # UUID
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    profile_id = Column(String, ForeignKey("professor_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String, nullable=False)
    subject = Column(String, nullable=False)  # SubjectType como string para flexibilidade
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_message_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relacionamentos
    user = relationship("User", back_populates="conversations")
    profile = relationship("ProfessorProfile", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan", order_by="Message.created_at")
    
    def __repr__(self):
        return f"<Conversation(id={self.id}, title={self.title}, subject={self.subject})>"
