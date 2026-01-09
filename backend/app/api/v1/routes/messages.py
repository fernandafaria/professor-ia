"""
Endpoints de mensagens.
Conforme especificação MVP - Seção 5.4
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List
import uuid
import json
from app.services.database import get_db
from app.core.auth import get_current_active_user
from app.models.user import User
from app.models.conversation import Conversation
from app.models.message import Message, MessageRole
from app.schemas.message import MessageCreate, MessageResponse
from app.services.llm_service import LLMService

router = APIRouter()


@router.post("/{conversation_id}/messages", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def send_message(
    conversation_id: str,
    message_data: MessageCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Envia mensagem e recebe resposta da IA.
    
    POST /api/conversations/:id/messages
    """
    # Verificar se a conversa pertence ao usuário
    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found"
        )
    
    # Criar mensagem do usuário
    user_message = Message(
        id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        role=MessageRole.USER,
        content=message_data.content,
    )
    
    db.add(user_message)
    db.commit()
    
    # Obter histórico de mensagens
    previous_messages = db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at).all()
    
    # Gerar resposta da IA
    llm_service = LLMService(db)
    assistant_response = await llm_service.generate_response(
        conversation=conversation,
        user_message=message_data.content,
        previous_messages=previous_messages
    )
    
    # Criar mensagem da IA
    assistant_message = Message(
        id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        role=MessageRole.ASSISTANT,
        content=assistant_response["content"],
        message_metadata=assistant_response.get("metadata", {}),
    )
    
    db.add(assistant_message)
    
    # Atualizar last_message_at da conversa
    from sqlalchemy.sql import func
    conversation.last_message_at = func.now()
    
    db.commit()
    db.refresh(assistant_message)
    
    return assistant_message


@router.post("/{conversation_id}/messages/stream")
async def send_message_stream(
    conversation_id: str,
    message_data: MessageCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Envia mensagem e recebe resposta da IA com streaming.
    
    POST /api/conversations/:id/messages/stream
    """
    # Verificar se a conversa pertence ao usuário
    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found"
        )
    
    # Criar mensagem do usuário
    user_message = Message(
        id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        role=MessageRole.USER,
        content=message_data.content,
    )
    
    db.add(user_message)
    db.commit()
    
    # Obter histórico de mensagens
    previous_messages = db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at).all()
    
    # Gerar resposta da IA com streaming
    llm_service = LLMService(db)
    
    async def generate_stream():
        assistant_message_id = str(uuid.uuid4())
        full_content = ""
        
        async for chunk in llm_service.generate_response_stream(
            conversation=conversation,
            user_message=message_data.content,
            previous_messages=previous_messages
        ):
            full_content += chunk
            yield f"data: {json.dumps({'content': chunk, 'done': False, 'message_id': assistant_message_id})}\n\n"
        
        # Salvar mensagem completa no banco
        assistant_message = Message(
            id=assistant_message_id,
            conversation_id=conversation_id,
            role=MessageRole.ASSISTANT,
            content=full_content,
        )
        
        db.add(assistant_message)
        
        # Atualizar last_message_at da conversa
        from sqlalchemy.sql import func
        conversation.last_message_at = func.now()
        
        db.commit()
        
        yield f"data: {json.dumps({'content': '', 'done': True, 'message_id': assistant_message_id})}\n\n"
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


@router.get("/{conversation_id}/messages", response_model=List[MessageResponse])
async def list_messages(
    conversation_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Lista mensagens de uma conversa.
    
    GET /api/conversations/:id/messages
    """
    # Verificar se a conversa pertence ao usuário
    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id,
        Conversation.user_id == current_user.id
    ).first()
    
    if not conversation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found"
        )
    
    messages = db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at).all()
    
    return messages
