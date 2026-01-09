"""
Serviço de integração com LLM (Anthropic Claude).
Conforme especificação MVP - Seção 5.2 e 5.3
"""

from sqlalchemy.orm import Session
from typing import List, Dict, AsyncGenerator
from anthropic import AsyncAnthropic
from app.config import settings
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.professor_profile import ProfessorProfile
from app.core.rag.retriever_supabase import RAGRetriever
from app.core.rag.prompts import PromptTemplates
import time

class LLMService:
    """Serviço de integração com LLM (Claude)."""
    
    def __init__(self, db: Session):
        """Inicializa o serviço LLM."""
        self.db = db
        self.client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.rag_retriever = RAGRetriever(db=db)
    
    async def generate_response(
        self,
        conversation: Conversation,
        user_message: str,
        previous_messages: List[Message]
    ) -> Dict:
        """Gera resposta da IA para uma mensagem."""
        start_time = time.time()
        
        # Obter perfil do professor
        profile = self.db.query(ProfessorProfile).filter(
            ProfessorProfile.id == conversation.profile_id
        ).first()
        
        if not profile:
            raise ValueError("Profile not found")
        
        # Construir histórico de conversa
        conversation_history = []
        for msg in previous_messages[-10:]:  # Últimas 10 mensagens
            conversation_history.append({
                "role": msg.role.value,
                "content": msg.content
            })
        
        # Buscar contexto RAG
        rag_context = []
        rag_results = []
        try:
            rag_results = self.rag_retriever.retrieve(user_message, db=self.db, n_results=5)
            rag_context = [r.get("content", "") for r in rag_results]
        except Exception as e:
            print(f"Erro ao buscar contexto RAG: {e}")
        
        # Construir prompt do sistema
        system_prompt = self._build_system_prompt(profile, rag_context)
        
        # Construir mensagens para o Claude
        # Claude usa formato diferente: system é separado e messages são apenas user/assistant
        messages = []
        
        # Adicionar histórico (converter formato)
        for msg in conversation_history:
            # Claude não aceita "system" nas messages, apenas user/assistant
            if msg["role"] == "system":
                continue
            messages.append({
                "role": msg["role"],  # user ou assistant
                "content": msg["content"]
            })
        
        # Adicionar mensagem atual
        messages.append({"role": "user", "content": user_message})
        
        # Chamar Claude API
        try:
            response = await self.client.messages.create(
                model=settings.ANTHROPIC_MODEL,
                max_tokens=1024,
                temperature=0.7,
                system=system_prompt,
                messages=messages,
            )
            
            # Claude retorna texto diretamente no primeiro content block
            content = response.content[0].text if response.content else ""
            
            # Obter informações de uso
            tokens_used = response.usage.input_tokens + response.usage.output_tokens if hasattr(response, 'usage') else 0
            latency = int((time.time() - start_time) * 1000)  # em ms
            
            return {
                "content": content,
                "metadata": {
                    "tokens": tokens_used,
                    "input_tokens": response.usage.input_tokens if hasattr(response, 'usage') else 0,
                    "output_tokens": response.usage.output_tokens if hasattr(response, 'usage') else 0,
                    "model": settings.ANTHROPIC_MODEL,
                    "latency": latency,
                    "rag_sources": [r.get("metadata", {}).get("source", "") for r in rag_results] if rag_context else []
                }
            }
        except Exception as e:
            raise Exception(f"Erro ao gerar resposta: {str(e)}")
    
    async def generate_response_stream(
        self,
        conversation: Conversation,
        user_message: str,
        previous_messages: List[Message]
    ) -> AsyncGenerator[str, None]:
        """Gera resposta da IA com streaming."""
        # Obter perfil do professor
        profile = self.db.query(ProfessorProfile).filter(
            ProfessorProfile.id == conversation.profile_id
        ).first()
        
        if not profile:
            raise ValueError("Profile not found")
        
        # Construir histórico de conversa
        conversation_history = []
        for msg in previous_messages[-10:]:
            conversation_history.append({
                "role": msg.role.value,
                "content": msg.content
            })
        
        # Buscar contexto RAG
        rag_context = []
        rag_results = []
        try:
            rag_results = self.rag_retriever.retrieve(user_message, db=self.db, n_results=5)
            rag_context = [r.get("content", "") for r in rag_results]
        except Exception as e:
            print(f"Erro ao buscar contexto RAG: {e}")
        
        # Construir prompt do sistema
        system_prompt = self._build_system_prompt(profile, rag_context)
        
        # Construir mensagens para o Claude
        messages = []
        
        # Adicionar histórico (converter formato)
        for msg in conversation_history:
            if msg["role"] == "system":
                continue
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        messages.append({"role": "user", "content": user_message})
        
        # Chamar Claude API com streaming
        try:
            async with self.client.messages.stream(
                model=settings.ANTHROPIC_MODEL,
                max_tokens=1024,
                temperature=0.7,
                system=system_prompt,
                messages=messages,
            ) as stream:
                async for text in stream.text_stream:
                    yield text
        except Exception as e:
            raise Exception(f"Erro ao gerar resposta com streaming: {str(e)}")
    
    def _build_system_prompt(
        self,
        profile: ProfessorProfile,
        rag_context: List[str]
    ) -> str:
        """Constrói prompt do sistema conforme especificação MVP - Seção 5.3."""
        # Diretrizes por personalidade
        personality_guidelines = {
            "motivador": """
- Use linguagem encorajadora e positiva
- Celebre pequenas conquistas
- Proponha desafios progressivos
- Use emojis de celebração (🎉, 🚀, ⭐)
- Frases: "Você consegue!", "Ótimo raciocínio!", "Vamos nessa!"
""",
            "paciente": """
- Explique de múltiplas formas
- Não demonstre pressa ou frustração
- Ofereça pausas e revisões
- Use analogias simples
- Frases: "Vamos com calma", "Não tem problema errar", "Quer que eu explique de outra forma?"
""",
            "desafiador": """
- Proponha exercícios difíceis
- Questione respostas superficiais
- Estimule pensamento crítico
- Use tom direto
- Frases: "Você pode ir além", "Pense mais profundamente", "Esse raciocínio está incompleto"
""",
            "amigavel": """
- Use gírias e linguagem informal
- Insira referências pop
- Use emojis frequentemente (😎, 🤙, 🔥)
- Crie conexão emocional
- Frases: "Opa, beleza?", "Bora lá!", "Massa demais!"
""",
        }
        
        # Construir contexto RAG
        context_text = "\n\n".join([f"- {c}" for c in rag_context]) if rag_context else "Nenhum contexto específico disponível."
        
        # Construir prompt completo
        prompt = f"""Você é {profile.professor_name}, um professor de {profile.subject.value} com personalidade {profile.personality.value}.

PERFIL DO ALUNO:
- Nível: {profile.level.value}
- Interesses: {', '.join(profile.interests) if profile.interests else 'Nenhum especificado'}
- Objetivo: {profile.goal or 'Não especificado'}
- Matérias favoritas: {', '.join(profile.favorite_subjects) if profile.favorite_subjects else 'Nenhuma especificada'}

DIRETRIZES DE COMUNICAÇÃO:
{personality_guidelines.get(profile.personality.value, '')}

CONTEXTO PEDAGÓGICO (BNCC):
{context_text}

HISTÓRICO DA CONVERSA:
[Será preenchido com as mensagens anteriores]

INSTRUÇÃO:
Responda de forma clara, adaptando exemplos aos interesses do aluno. Use exemplos relacionados a {', '.join(profile.interests[:2]) if profile.interests else 'interesses gerais'} quando apropriado.
"""
        return prompt
