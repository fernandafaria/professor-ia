"""
Modelo de dados para Usuário.
Conforme especificação MVP - Seção 4.1
"""

from sqlalchemy import Column, String, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base
import enum


class SubscriptionType(str, enum.Enum):
    """Tipo de assinatura."""
    FREE = "free"
    PREMIUM = "premium"


class User(Base):
    """Modelo de usuário."""
    
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)  # UUID
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    subscription = Column(SQLEnum(SubscriptionType), default=SubscriptionType.FREE, nullable=False)
    
    # Relacionamentos
    professor_profiles = relationship("ProfessorProfile", back_populates="user", cascade="all, delete-orphan")
    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")
    progress_records = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, subscription={self.subscription})>"
