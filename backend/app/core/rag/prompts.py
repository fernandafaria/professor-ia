"""
Templates de prompts para geração de conteúdo personalizado.
"""

from typing import Dict, List, Optional


class PromptTemplates:
    """Templates de prompts para o sistema RAG."""
    
    BASE_EDUCATIONAL_PROMPT = """
Você é um tutor educacional especializado em ajudar estudantes brasileiros do Ensino Fundamental II e Médio.

Contexto do estudante:
- Idade: {age} anos
- Série: {grade}
- Perfil de aprendizado: {learning_profile}
- Interesses: {interests}
- Dificuldades: {difficulties}
- Estilo de aprendizado preferido: {learning_style}

Conteúdo relevante:
{context}

Instruções:
1. Use o contexto fornecido para responder à pergunta do estudante
2. Adapte a explicação aos interesses e perfil do estudante
3. Use exemplos relacionados aos interesses mencionados quando apropriado
4. Mantenha uma linguagem apropriada para a idade (12-19 anos)
5. Seja claro, paciente e encorajador
6. Alinhe o conteúdo com a BNCC quando aplicável

Pergunta do estudante: {question}

Resposta:
"""

    EXERCISE_GENERATION_PROMPT = """
Você é um professor criativo especializado em criar exercícios educacionais personalizados.

Contexto do estudante:
- Idade: {age} anos
- Série: {grade}
- Interesses: {interests}
- Dificuldade atual: {difficulty_level}
- Matéria: {subject}
- Tema: {topic}

Objetivo da BNCC:
{bncc_objective}

Crie um exercício que:
1. Esteja alinhado com o objetivo da BNCC
2. Seja contextualizado com os interesses do estudante ({interests})
3. Esteja no nível de dificuldade apropriado ({difficulty_level})
4. Seja envolvente e motivador
5. Inclua instruções claras

Exercício:
"""

    EXPLANATION_PERSONALIZED_PROMPT = """
Explique o seguinte conceito para um estudante brasileiro de {age} anos, cursando {grade}.

Conceito: {concept}
Matéria: {subject}

Contexto do estudante:
- Interesses: {interests}
- Estilo de aprendizado: {learning_style}
- Perfil: {learning_profile}

Use exemplos relacionados aos interesses do estudante ({interests}) para tornar a explicação mais envolvente e memorável.

Explicação:
"""

    ADAPTATION_PROMPT = """
Adapte o seguinte conteúdo educacional para um estudante com as seguintes características:

Estudante:
- Perfil: {learning_profile}
- Neurodivergências: {neurodivergences}
- Adaptações necessárias: {adaptations}
- Interesses: {interests}

Conteúdo original:
{original_content}

Matéria: {subject}
Tema: {topic}

Instruções de adaptação:
1. Mantenha o conteúdo pedagógico essencial
2. Adapte o formato conforme necessário (visual, auditivo, etc.)
3. Simplifique se necessário, mas mantenha o rigor educacional
4. Use exemplos dos interesses do estudante
5. Torne o conteúdo mais acessível sem reduzir a qualidade

Conteúdo adaptado:
"""

    @staticmethod
    def format_educational_prompt(
        question: str,
        context: List[str],
        age: Optional[int] = None,
        grade: Optional[str] = None,
        learning_profile: Optional[str] = None,
        interests: Optional[List[str]] = None,
        difficulties: Optional[List[str]] = None,
        learning_style: Optional[str] = None,
    ) -> str:
        """Formata prompt educacional personalizado."""
        context_text = "\n\n".join([f"- {c}" for c in context])
        
        return PromptTemplates.BASE_EDUCATIONAL_PROMPT.format(
            age=age or "N/A",
            grade=grade or "N/A",
            learning_profile=learning_profile or "N/A",
            interests=", ".join(interests) if interests else "N/A",
            difficulties=", ".join(difficulties) if difficulties else "N/A",
            learning_style=learning_style or "N/A",
            context=context_text,
            question=question,
        )
    
    @staticmethod
    def format_exercise_prompt(
        subject: str,
        topic: str,
        bncc_objective: str,
        age: Optional[int] = None,
        grade: Optional[str] = None,
        interests: Optional[List[str]] = None,
        difficulty_level: Optional[str] = None,
    ) -> str:
        """Formata prompt para geração de exercício."""
        return PromptTemplates.EXERCISE_GENERATION_PROMPT.format(
            age=age or "N/A",
            grade=grade or "N/A",
            interests=", ".join(interests) if interests else "N/A",
            difficulty_level=difficulty_level or "intermediario",
            subject=subject,
            topic=topic,
            bncc_objective=bncc_objective,
        )
    
    @staticmethod
    def format_explanation_prompt(
        concept: str,
        subject: str,
        age: Optional[int] = None,
        grade: Optional[str] = None,
        interests: Optional[List[str]] = None,
        learning_style: Optional[str] = None,
        learning_profile: Optional[str] = None,
    ) -> str:
        """Formata prompt para explicação personalizada."""
        return PromptTemplates.EXPLANATION_PERSONALIZED_PROMPT.format(
            age=age or "N/A",
            grade=grade or "N/A",
            concept=concept,
            subject=subject,
            interests=", ".join(interests) if interests else "N/A",
            learning_style=learning_style or "N/A",
            learning_profile=learning_profile or "N/A",
        )
