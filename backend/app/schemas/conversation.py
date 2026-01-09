"""
Schemas Pydantic para Conversa.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models.professor_profile import SubjectType


class ConversationBase(BaseModel):
    """Schema base para conversa."""
    title: str = Field(min_length=1, max_length=200)
    subject: str  # SubjectType como string


class ConversationCreate(ConversationBase):
    """Schema para criação de conversa."""
    profile_id: str


class ConversationUpdate(BaseModel):
    """Schema para atualização de conversa."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    subject: Optional[str] = None


class ConversationResponse(ConversationBase):
    """Schema de resposta para conversa."""
    id: str
    user_id: str
    profile_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_message_at: datetime
    
    class Config:
        from_attributes = True


class ConversationWithMessages(ConversationResponse):
    """Schema de conversa com mensagens."""
    messages: list = []  # Lista de MessageResponse
    
    class Config:
        from_attributes = True
