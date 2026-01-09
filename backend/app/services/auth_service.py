"""
Serviço de autenticação.
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
import uuid
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.auth import (
    verify_password,
    get_password_hash,
    create_access_token,
)
from app.config import settings
from app.schemas.auth import Token


class AuthService:
    """Serviço de autenticação."""
    
    def __init__(self, db: Session):
        """Inicializa o serviço de autenticação."""
        self.db = db
    
    def register(self, user_data: UserCreate) -> User:
        """Registra novo usuário."""
        # Verificar se email já existe
        existing_user = self.db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Criar novo usuário
        user = User(
            id=str(uuid.uuid4()),
            email=user_data.email,
            name=user_data.name,
            hashed_password=get_password_hash(user_data.password),
        )
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    def login(self, credentials: UserLogin) -> Token:
        """Autentica usuário e retorna token."""
        user = self.db.query(User).filter(User.email == credentials.email).first()
        
        if not user or not verify_password(credentials.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Criar token de acesso
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.id, "email": user.email},
            expires_delta=access_token_expires
        )
        
        return Token(access_token=access_token, token_type="bearer")
    
    def get_user_by_id(self, user_id: str) -> User:
        """Obtém usuário por ID."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user
