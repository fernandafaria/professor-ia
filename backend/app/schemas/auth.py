"""
Schemas Pydantic para Autenticação.
"""

from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """Schema para token de acesso."""
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


class TokenData(BaseModel):
    """Dados do token."""
    user_id: Optional[str] = None
    email: Optional[str] = None
