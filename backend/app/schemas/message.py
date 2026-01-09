"""
Schemas Pydantic para Mensagem.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, List
from app.models.message import MessageRole


class MessageMetadata(BaseModel):
    """Metadados da mensagem."""
    tokens: Optional[int] = None
    model: Optional[str] = None
    latency: Optional[int] = None  # em ms
    rag_sources: Optional[List[str]] = None


class MessageBase(BaseModel):
    """Schema base para mensagem."""
    content: str = Field(min_length=1)
    role: MessageRole


class MessageCreate(BaseModel):
    """Schema para criação de mensagem."""
    content: str = Field(min_length=1)


class MessageResponse(MessageBase):
    """Schema de resposta para mensagem."""
    id: str
    conversation_id: str
    metadata: Dict = Field(default_factory=dict, alias="message_metadata")  # Mapeia message_metadata para metadata na API
    
    class Config:
        from_attributes = True
        populate_by_name = True  # Permite usar tanto 'metadata' quanto 'message_metadata'


class MessageStream(BaseModel):
    """Schema para streaming de mensagem."""
    content: str
    done: bool = False
    message_id: Optional[str] = None
