"""
Schemas Pydantic para Perfil do Professor.
Conforme especificação MVP - Seção 3.2
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from app.models.professor_profile import PersonalityType, SubjectType, LevelType


class ProfessorProfileBase(BaseModel):
    """Schema base para perfil do professor."""
    professor_name: str = Field(min_length=1, max_length=50)
    personality: PersonalityType
    subject: SubjectType
    level: LevelType


class ProfessorProfileCreate(ProfessorProfileBase):
    """Schema para criação de perfil (onboarding completo)."""
    interests: List[str] = Field(default_factory=list)
    hobbies: Optional[str] = Field(None, max_length=500)
    goal: Optional[str] = Field(None, max_length=500)
    favorite_subjects: List[SubjectType] = Field(default_factory=list)


class ProfessorProfileUpdate(BaseModel):
    """Schema para atualização de perfil."""
    professor_name: Optional[str] = Field(None, min_length=1, max_length=50)
    personality: Optional[PersonalityType] = None
    subject: Optional[SubjectType] = None
    level: Optional[LevelType] = None
    interests: Optional[List[str]] = None
    hobbies: Optional[str] = Field(None, max_length=500)
    goal: Optional[str] = Field(None, max_length=500)
    favorite_subjects: Optional[List[SubjectType]] = None


class ProfessorProfileResponse(ProfessorProfileBase):
    """Schema de resposta para perfil do professor."""
    id: str
    user_id: str
    interests: List[str] = []
    hobbies: Optional[str] = None
    goal: Optional[str] = None
    favorite_subjects: List[str] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
