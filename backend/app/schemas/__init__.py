"""
Schemas Pydantic para validação de dados.
"""

# Schemas antigos (Student) - manter para compatibilidade
from app.schemas.student import (
    StudentBase,
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    StudentProfile,
)

# Novos schemas conforme especificação MVP
from app.schemas.user import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserResponse,
    UserLogin,
)
from app.schemas.professor_profile import (
    ProfessorProfileBase,
    ProfessorProfileCreate,
    ProfessorProfileUpdate,
    ProfessorProfileResponse,
)
from app.schemas.conversation import (
    ConversationBase,
    ConversationCreate,
    ConversationUpdate,
    ConversationResponse,
    ConversationWithMessages,
)
from app.schemas.message import (
    MessageBase,
    MessageCreate,
    MessageResponse,
    MessageStream,
    MessageMetadata,
)
from app.schemas.progress import (
    ProgressBase,
    ProgressCreate,
    ProgressUpdate,
    ProgressResponse,
    ProgressSummary,
    Badge,
)
from app.schemas.auth import (
    Token,
    TokenData,
)

__all__ = [
    # Student (legacy)
    "StudentBase",
    "StudentCreate",
    "StudentUpdate",
    "StudentResponse",
    "StudentProfile",
    # User
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "UserLogin",
    # Professor Profile
    "ProfessorProfileBase",
    "ProfessorProfileCreate",
    "ProfessorProfileUpdate",
    "ProfessorProfileResponse",
    # Conversation
    "ConversationBase",
    "ConversationCreate",
    "ConversationUpdate",
    "ConversationResponse",
    "ConversationWithMessages",
    # Message
    "MessageBase",
    "MessageCreate",
    "MessageResponse",
    "MessageStream",
    "MessageMetadata",
    # Progress
    "ProgressBase",
    "ProgressCreate",
    "ProgressUpdate",
    "ProgressResponse",
    "ProgressSummary",
    "Badge",
    # Auth
    "Token",
    "TokenData",
]
