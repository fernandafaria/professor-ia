"""
FastAPI application principal da Plataforma Educacional P1A.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings

# Criar aplicação FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Plataforma educacional hiper-personalizada para estudantes brasileiros",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    """Endpoint raiz da API."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
    }


# Importar routers da API
from app.api.v1.routes import auth, profile, conversations, messages

# Autenticação
app.include_router(
    auth.router,
    prefix=f"{settings.API_V1_PREFIX}/auth",
    tags=["Authentication"],
)

# Perfil do Professor
app.include_router(
    profile.router,
    prefix=f"{settings.API_V1_PREFIX}/profile",
    tags=["Professor Profile"],
)

# Conversas
app.include_router(
    conversations.router,
    prefix=f"{settings.API_V1_PREFIX}/conversations",
    tags=["Conversations"],
)

# Mensagens
app.include_router(
    messages.router,
    prefix=f"{settings.API_V1_PREFIX}/conversations",
    tags=["Messages"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )