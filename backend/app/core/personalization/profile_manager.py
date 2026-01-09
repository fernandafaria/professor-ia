"""
Gerenciamento de perfil do estudante para personalização.
"""

from typing import List, Dict, Optional
from app.models.student import Student
from app.schemas.student import StudentProfile
from sqlalchemy.orm import Session


class ProfileManager:
    """Gerenciador de perfis de estudantes."""
    
    def __init__(self, db: Session):
        """Inicializa o gerenciador de perfis."""
        self.db = db
    
    def get_student_profile(self, student_id: int) -> Optional[StudentProfile]:
        """Obtém perfil completo do estudante."""
        student = self.db.query(Student).filter(Student.id == student_id).first()
        
        if not student:
            return None
        
        return StudentProfile(
            id=student.id,
            username=student.username,
            age=student.age,
            grade=student.grade,
            learning_profile_type=student.learning_profile_type,
            interests=student.interests or [],
            interests_weights=student.interests_weights or {},
            neurodivergences=student.neurodivergences or [],
            adaptations_needed=student.adaptations_needed or [],
            preferred_content_format=student.preferred_content_format,
            preferred_difficulty_level=student.preferred_difficulty_level,
            learning_style=student.learning_style,
            difficulties=student.difficulties or [],
            strengths=student.strengths or [],
            points=student.points,
            level=student.level,
            current_learning_path=student.current_learning_path,
        )
    
    def update_interests(
        self,
        student_id: int,
        interests: List[str],
        weights: Optional[Dict[str, float]] = None,
    ) -> bool:
        """Atualiza interesses do estudante."""
        student = self.db.query(Student).filter(Student.id == student_id).first()
        
        if not student:
            return False
        
        student.interests = interests
        
        if weights:
            student.interests_weights = weights
        else:
            # Peso padrão igual para todos
            default_weight = 1.0 / len(interests) if interests else 0.0
            student.interests_weights = {i: default_weight for i in interests}
        
        self.db.commit()
        return True
    
    def get_personalization_context(self, student_id: int) -> Dict:
        """Obtém contexto de personalização para uso no RAG."""
        profile = self.get_student_profile(student_id)
        
        if not profile:
            return {}
        
        return {
            "interests": profile.interests,
            "interests_weights": profile.interests_weights,
            "learning_profile": profile.learning_profile_type,
            "neurodivergences": profile.neurodivergences,
            "adaptations": profile.adaptations_needed,
            "preferred_format": profile.preferred_content_format,
            "difficulty_level": profile.preferred_difficulty_level,
            "learning_style": profile.learning_style,
            "age": profile.age,
            "grade": profile.grade,
        }
    
    def calculate_interest_score(
        self,
        student_id: int,
        content_keywords: List[str],
    ) -> float:
        """
        Calcula score de relevância do conteúdo para os interesses do estudante.
        
        Args:
            student_id: ID do estudante
            content_keywords: Palavras-chave do conteúdo
            
        Returns:
            Score de 0.0 a 1.0
        """
        profile = self.get_student_profile(student_id)
        
        if not profile or not profile.interests:
            return 0.5  # Score neutro
        
        # Mapeamento de interesse para palavras-chave
        interest_keywords = {
            "games": ["game", "jogo", "gaming", "playstation", "xbox", "nintendo"],
            "futebol": ["futebol", "brasileirão", "libertadores", "copa", "seleção"],
            "kpop": ["k-pop", "kpop", "bts", "blackpink", "idol"],
            "musica": ["música", "artista", "cantor", "banda", "álbum"],
        }
        
        # Calcular matching
        total_score = 0.0
        total_weight = 0.0
        
        for interest in profile.interests:
            weight = profile.interests_weights.get(interest, 0.5)
            keywords = interest_keywords.get(interest, [])
            
            # Verificar se algum keyword do interesse está no conteúdo
            matches = sum(1 for kw in keywords if kw.lower() in " ".join(content_keywords).lower())
            
            if matches > 0:
                interest_score = min(1.0, matches / len(keywords)) if keywords else 0.0
                total_score += interest_score * weight
                total_weight += weight
        
        if total_weight == 0:
            return 0.5
        
        return min(1.0, total_score / total_weight)
