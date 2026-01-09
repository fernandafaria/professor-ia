"""
Schemas Pydantic para validação de dados de Estudante.
"""

from pydantic import BaseModel, EmailStr, Field, validator
from typing import List, Optional, Dict
from datetime import datetime


class InterestBase(BaseModel):
    """Base para interesse."""
    category: str
    weight: float = Field(ge=0.0, le=1.0, default=0.5)


class StudentBase(BaseModel):
    """Schema base para estudante."""
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    full_name: str = Field(min_length=1, max_length=200)
    age: Optional[int] = Field(None, ge=12, le=19)
    grade: Optional[str] = None  # "6º EF", "1º EM", etc.
    school_name: Optional[str] = None


class StudentCreate(StudentBase):
    """Schema para criação de estudante."""
    password: str = Field(min_length=8, max_length=100)
    learning_profile_type: Optional[str] = Field(None, regex="^(dificuldade|neurodivergente|desmotivado)$")
    interests: List[str] = []
    neurodivergences: List[str] = []
    
    @validator("interests")
    def validate_interests(cls, v):
        valid_interests = [
            "games", "futebol", "kpop", "musica", "cinema",
            "tecnologia", "esportes"
        ]
        invalid = [i for i in v if i not in valid_interests]
        if invalid:
            raise ValueError(f"Interesses inválidos: {invalid}")
        return v
    
    @validator("neurodivergences")
    def validate_neurodivergences(cls, v):
        valid_neurodivergences = ["TDAH", "dislexia", "TEA", "outro"]
        invalid = [n for n in v if n not in valid_neurodivergences]
        if invalid:
            raise ValueError(f"Neurodivergências inválidas: {invalid}")
        return v


class StudentUpdate(BaseModel):
    """Schema para atualização de estudante."""
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=12, le=19)
    grade: Optional[str] = None
    school_name: Optional[str] = None
    interests: Optional[List[str]] = None
    interests_weights: Optional[Dict[str, float]] = None
    preferred_content_format: Optional[str] = Field(None, regex="^(texto|video|audio|interativo)$")
    preferred_difficulty_level: Optional[str] = Field(None, regex="^(iniciante|intermediario|avancado)$")
    learning_style: Optional[str] = Field(None, regex="^(visual|auditivo|cinestesico|misto)$")
    gamification_enabled: Optional[bool] = None


class StudentResponse(StudentBase):
    """Schema de resposta para estudante."""
    id: int
    learning_profile_type: Optional[str] = None
    interests: List[str] = []
    interests_weights: Dict[str, float] = {}
    preferred_content_format: Optional[str] = None
    preferred_difficulty_level: Optional[str] = None
    learning_style: Optional[str] = None
    neurodivergences: List[str] = []
    points: int = 0
    level: int = 1
    gamification_enabled: bool = True
    is_active: bool = True
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class StudentProfile(BaseModel):
    """Perfil completo do estudante para personalização."""
    id: int
    username: str
    age: Optional[int] = None
    grade: Optional[str] = None
    learning_profile_type: Optional[str] = None
    interests: List[str] = []
    interests_weights: Dict[str, float] = {}
    neurodivergences: List[str] = []
    adaptations_needed: List[str] = []
    preferred_content_format: Optional[str] = None
    preferred_difficulty_level: Optional[str] = None
    learning_style: Optional[str] = None
    difficulties: List[str] = []
    strengths: List[str] = []
    points: int = 0
    level: int = 1
    current_learning_path: Optional[Dict] = None
    
    class Config:
        from_attributes = True
