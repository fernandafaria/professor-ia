"""
Schemas Pydantic para Progresso.
"""

from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, List, Dict


class Badge(BaseModel):
    """Schema para badge."""
    id: str
    name: str
    description: str
    icon: str
    unlocked_at: datetime


class ProgressBase(BaseModel):
    """Schema base para progresso."""
    subject: str
    xp: int = Field(default=0, ge=0)
    level: int = Field(default=1, ge=1)
    streak: int = Field(default=0, ge=0)


class ProgressCreate(ProgressBase):
    """Schema para criação de progresso."""
    pass


class ProgressUpdate(BaseModel):
    """Schema para atualização de progresso."""
    xp: Optional[int] = Field(None, ge=0)
    level: Optional[int] = Field(None, ge=1)
    streak: Optional[int] = Field(None, ge=0)
    last_study_date: Optional[datetime] = None
    badges: Optional[List[Dict]] = None


class ProgressResponse(ProgressBase):
    """Schema de resposta para progresso."""
    id: str
    user_id: str
    last_study_date: Optional[datetime] = None
    badges: List[Dict] = []
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ProgressSummary(BaseModel):
    """Resumo de progresso do usuário."""
    total_xp: int
    current_level: int
    total_streak: int
    badges_count: int
    subjects_progress: List[ProgressResponse] = []
