"""
Endpoints de perfil do professor.
Conforme especificação MVP - Seção 5.4
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid
from app.services.database import get_db
from app.core.auth import get_current_active_user
from app.models.user import User
from app.models.professor_profile import ProfessorProfile
from app.schemas.professor_profile import (
    ProfessorProfileCreate,
    ProfessorProfileUpdate,
    ProfessorProfileResponse,
)

router = APIRouter()


@router.post("", response_model=ProfessorProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: ProfessorProfileCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Cria perfil do professor (onboarding completo).
    
    POST /api/profile
    """
    profile = ProfessorProfile(
        id=str(uuid.uuid4()),
        user_id=current_user.id,
        professor_name=profile_data.professor_name,
        personality=profile_data.personality,
        subject=profile_data.subject,
        level=profile_data.level,
        interests=profile_data.interests,
        hobbies=profile_data.hobbies,
        goal=profile_data.goal,
        favorite_subjects=[s.value for s in profile_data.favorite_subjects],
    )
    
    db.add(profile)
    db.commit()
    db.refresh(profile)
    
    return profile


@router.get("/{profile_id}", response_model=ProfessorProfileResponse)
async def get_profile(
    profile_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Obtém perfil específico.
    
    GET /api/profile/:id
    """
    profile = db.query(ProfessorProfile).filter(
        ProfessorProfile.id == profile_id,
        ProfessorProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    return profile


@router.get("", response_model=List[ProfessorProfileResponse])
async def list_profiles(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Lista todos os perfis do usuário.
    
    GET /api/profile
    """
    profiles = db.query(ProfessorProfile).filter(
        ProfessorProfile.user_id == current_user.id
    ).all()
    
    return profiles


@router.put("/{profile_id}", response_model=ProfessorProfileResponse)
async def update_profile(
    profile_id: str,
    profile_data: ProfessorProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Atualiza perfil do professor.
    
    PUT /api/profile/:id
    """
    profile = db.query(ProfessorProfile).filter(
        ProfessorProfile.id == profile_id,
        ProfessorProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    # Atualizar campos fornecidos
    update_data = profile_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        if field == "favorite_subjects" and value:
            setattr(profile, field, [s.value if hasattr(s, 'value') else s for s in value])
        else:
            setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    
    return profile


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    profile_id: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Deleta perfil do professor.
    
    DELETE /api/profile/:id
    """
    profile = db.query(ProfessorProfile).filter(
        ProfessorProfile.id == profile_id,
        ProfessorProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    db.delete(profile)
    db.commit()
    
    return None
