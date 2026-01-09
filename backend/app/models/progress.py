"""
Modelo de dados para Progresso.
Conforme especificação MVP - Seção 4.5
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.services.database import Base


class Progress(Base):
    """Modelo de progresso do usuário."""
    
    __tablename__ = "progress"
    
    id = Column(String, primary_key=True)  # UUID
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    subject = Column(String, nullable=False)  # Matéria
    xp = Column(Integer, default=0, nullable=False)  # Pontos de experiência
    level = Column(Integer, default=1, nullable=False)  # Nível de gamificação
    streak = Column(Integer, default=0, nullable=False)  # Dias consecutivos
    last_study_date = Column(DateTime(timezone=True))  # Última sessão de estudo
    badges = Column(JSON, default=list)  # Lista de badges conquistados
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    user = relationship("User", back_populates="progress_records")
    
    def __repr__(self):
        return f"<Progress(id={self.id}, user_id={self.user_id}, subject={self.subject}, xp={self.xp}, level={self.level})>"
