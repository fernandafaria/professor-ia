"""
Modelo de dados para Perfil do Professor.
Conforme especificação MVP - Seção 4.2
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base
import enum


class PersonalityType(str, enum.Enum):
    """Tipo de personalidade do professor."""
    MOTIVADOR = "motivador"
    PACIENTE = "paciente"
    DESAFIADOR = "desafiador"
    AMIGAVEL = "amigavel"


class SubjectType(str, enum.Enum):
    """Tipo de matéria."""
    TODAS = "todas"
    PORTUGUES = "portugues"
    MATEMATICA = "matematica"
    HISTORIA = "historia"
    GEOGRAFIA = "geografia"
    CIENCIAS = "ciencias"
    BIOLOGIA = "biologia"
    FISICA = "fisica"
    QUIMICA = "quimica"
    INGLES = "ingles"
    ESPANHOL = "espanhol"
    ARTES = "artes"
    EDUCACAO_FISICA = "educacao_fisica"
    FILOSOFIA = "filosofia"
    SOCIOLOGIA = "sociologia"


class LevelType(str, enum.Enum):
    """Nível de conhecimento."""
    INICIANTE = "iniciante"
    INTERMEDIARIO = "intermediario"
    AVANCADO = "avancado"


class ProfessorProfile(Base):
    """Modelo de perfil do professor."""
    
    __tablename__ = "professor_profiles"
    
    id = Column(String, primary_key=True)  # UUID
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    professor_name = Column(String, nullable=False)
    personality = Column(SQLEnum(PersonalityType), nullable=False)
    subject = Column(SQLEnum(SubjectType), nullable=False)
    level = Column(SQLEnum(LevelType), nullable=False)
    interests = Column(JSON, default=list)  # Lista de interesses selecionados
    hobbies = Column(String)  # Texto livre
    goal = Column(String)  # Objetivo de estudo
    favorite_subjects = Column(JSON, default=list)  # Lista de matérias favoritas
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    user = relationship("User", back_populates="professor_profiles")
    conversations = relationship("Conversation", back_populates="profile", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<ProfessorProfile(id={self.id}, professor_name={self.professor_name}, subject={self.subject})>"
