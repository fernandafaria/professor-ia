"""
Dependências compartilhadas da API v1.
Inclui autenticação, rate limiting, etc.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# TODO: Implementar autenticação JWT
# TODO: Implementar rate limiting
# TODO: Implementar verificação de permissões

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependência para obter o usuário atual.
    
    TODO: Implementar validação de JWT e retorno do usuário.
    """
    # Placeholder
    return {"user_id": "1", "email": "student@example.com"}


async def verify_student_access(
    current_user: dict = Depends(get_current_user)
):
    """Verifica se o usuário tem acesso de estudante."""
    # TODO: Implementar verificação de permissões
    return current_user