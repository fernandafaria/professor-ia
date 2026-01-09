"""
Schemas Pydantic para Usuário.
"""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from app.models.user import SubscriptionType


class UserBase(BaseModel):
    """Schema base para usuário."""
    email: EmailStr
    name: str = Field(min_length=1, max_length=200)


class UserCreate(UserBase):
    """Schema para criação de usuário."""
    password: str = Field(min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Schema para atualização de usuário."""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    subscription: Optional[SubscriptionType] = None


class UserResponse(UserBase):
    """Schema de resposta para usuário."""
    id: str
    subscription: SubscriptionType
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """Schema para login."""
    email: EmailStr
    password: str
