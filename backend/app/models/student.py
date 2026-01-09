"""
Modelo de dados para Estudante.
"""

from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base


class Student(Base):
    """Modelo de estudante."""
    
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Dados demográficos
    age = Column(Integer)
    grade = Column(String)  # "6º EF", "1º EM", etc.
    school_name = Column(String)
    
    # Perfil de aprendizado
    learning_profile_type = Column(String)  # "dificuldade", "neurodivergente", "desmotivado"
    learning_style = Column(String)  # "visual", "auditivo", "cinestesico", "misto"
    difficulties = Column(JSON)  # Lista de dificuldades específicas
    strengths = Column(JSON)  # Lista de pontos fortes
    
    # Neurodivergências
    neurodivergences = Column(JSON)  # ["TDAH", "dislexia", "TEA", ...]
    adaptations_needed = Column(JSON)  # Adaptações específicas necessárias
    
    # Interesses e personalização
    interests = Column(JSON)  # ["games", "futebol", "kpop", "musica", ...]
    interests_weights = Column(JSON)  # Pesos para cada interesse
    
    # Preferências
    preferred_content_format = Column(String)  # "texto", "video", "audio", "interativo"
    preferred_difficulty_level = Column(String)  # "iniciante", "intermediario", "avancado"
    
    # Configurações de gamificação
    gamification_enabled = Column(Boolean, default=True)
    points = Column(Integer, default=0)
    level = Column(Integer, default=1)
    achievements = Column(JSON)  # Lista de conquistas
    
    # Progresso
    current_learning_path = Column(JSON)  # Caminho de aprendizado atual
    completed_content_ids = Column(JSON)  # IDs de conteúdos completados
    
    # Metadata
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    # Relacionamentos
    interactions = relationship("Interaction", back_populates="student")
    progress_records = relationship("ProgressRecord", back_populates="student")
    
    def __repr__(self):
        return f"<Student(id={self.id}, username={self.username}, email={self.email})>"
