"""
Endpoints de autenticação.
Conforme especificação MVP - Seção 5.4
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.schemas.auth import Token
from app.core.auth import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Registra novo usuário.
    
    POST /api/auth/register
    """
    auth_service = AuthService(db)
    user = auth_service.register(user_data)
    return user


@router.post("/login", response_model=Token)
async def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Autentica usuário e retorna token.
    
    POST /api/auth/login
    """
    auth_service = AuthService(db)
    token = auth_service.login(credentials)
    return token


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: User = Depends(get_current_active_user)
):
    """
    Obtém informações do usuário logado.
    
    GET /api/auth/me
    """
    return current_user


@router.post("/logout")
async def logout():
    """
    Logout do usuário.
    Nota: Com JWT stateless, o logout é feito no cliente removendo o token.
    
    POST /api/auth/logout
    """
    return {"message": "Logged out successfully"}


@router.post("/refresh", response_model=Token)
async def refresh_token(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Atualiza token de acesso.
    
    POST /api/auth/refresh
    """
    from app.core.auth import create_access_token
    from datetime import timedelta
    from app.config import settings
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": current_user.id, "email": current_user.email},
        expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="bearer")
