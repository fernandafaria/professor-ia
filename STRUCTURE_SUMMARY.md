# Resumo da Estrutura - Plataforma Educacional P1A

## Visão Geral

A plataforma foi estruturada para suportar um sistema educacional hiper-personalizado baseado em RAG (Retrieval-Augmented Generation), com foco em estudantes brasileiros de 12-19 anos.

## Componentes Principais

### 1. Backend (Python/FastAPI)

#### Estrutura Principal
```
backend/
├── app/                    # Aplicação principal
│   ├── models/            # Modelos de dados (SQLAlchemy)
│   ├── schemas/           # Schemas Pydantic (validação)
│   ├── api/               # Endpoints da API
│   ├── core/              # Lógica de negócio
│   │   ├── rag/          # Sistema RAG
│   │   ├── personalization/  # Motor de personalização
│   │   ├── bncc/         # Integração BNCC
│   │   └── content/      # Gerenciamento de conteúdo
│   ├── services/         # Serviços externos
│   ├── workers/          # Background workers (Celery)
│   └── utils/            # Utilitários
├── scraping/             # Sistema de Web Scraping
├── tests/                # Testes
└── scripts/              # Scripts utilitários
```

#### Tecnologias
- **FastAPI**: Framework web moderno e rápido
- **SQLAlchemy**: ORM para banco de dados
- **ChromaDB**: Vector database para RAG
- **LangChain**: Framework para RAG e LLMs
- **Celery**: Processamento assíncrono
- **Redis**: Cache e filas

### 2. Sistema RAG

#### Componentes
- **Retriever** (`app/core/rag/retriever.py`): Motor de recuperação semântica
- **Prompts** (`app/core/rag/prompts.py`): Templates de prompts personalizados
- **Embeddings**: Sentence Transformers (português)

#### Fluxo
1. Query do usuário
2. Enriquecimento com perfil do estudante
3. Busca semântica no Vector DB
4. Reranking e filtragem
5. Geração de resposta com LLM

### 3. Personalização

#### Perfil do Estudante
- Dados demográficos (idade, série, escola)
- Perfil de aprendizado (tipo, dificuldades, pontos fortes)
- Interesses e pesos
- Neurodivergências (TDAH, dislexia, TEA)
- Preferências (formato, dificuldade, estilo)

#### Motor de Personalização
- **ProfileManager**: Gerenciamento de perfil
- **Interest Mapper**: Mapeamento de interesses
- **Content Adaptor**: Adaptação de conteúdo
- **Recommender**: Sistema de recomendações

### 4. Web Scraping

#### Fontes
- **Curriculares**: BNCC oficial, Nova Escola, Khan Academy
- **Culturais**: Games, Futebol, K-pop, Música
- **Notícias**: Tendências e atualidades

#### Pipeline
1. Coleta (scrapers especializados)
2. Limpeza e normalização
3. Estruturação e chunking
4. Extração de metadados
5. Geração de embeddings
6. Ingestão no Vector DB

### 5. Integração BNCC

#### Componentes
- Parser de dados BNCC
- Mapeamento conteúdo-currículo
- Validação de alinhamento
- Tracking de progresso curricular

## Arquivos de Configuração

### Principais
- `ARCHITECTURE.md`: Documentação da arquitetura técnica
- `PROJECT_STRUCTURE.md`: Estrutura detalhada de diretórios
- `IMPLEMENTATION_ROADMAP.md`: Roadmap de implementação
- `docs/DEVELOPMENT_SETUP.md`: Guia de setup de desenvolvimento

### Configurações
- `backend/requirements.txt`: Dependências Python
- `backend/.env.example`: Template de variáveis de ambiente
- `scraping/config/sources.yaml`: Fontes de web scraping
- `data/interests/categories.json`: Categorias de interesses

## Modelos de Dados Principais

### Student
- Informações básicas e autenticação
- Perfil de aprendizado e interesses
- Neurodivergências e adaptações
- Progresso e gamificação

### Content
- Conteúdo educacional
- Metadados (série, matéria, BNCC)
- Embeddings para busca semântica
- Tags de personalização

### Interaction
- Histórico de interações
- Perguntas e respostas
- Feedback do estudante
- Métricas de engajamento

## Próximos Passos

### Imediatos
1. Configurar ambiente de desenvolvimento
2. Setup banco de dados e Vector DB
3. Implementar modelos de dados básicos
4. Criar API base com FastAPI

### Curto Prazo (1-2 semanas)
1. Implementar RAG básico
2. Sistema de web scraping inicial
3. Integração BNCC básica
4. Personalização básica

### Médio Prazo (1-2 meses)
1. Frontend base
2. Sistema completo de personalização
3. Gamificação
4. Analytics básico

## Recursos Importantes

### Documentação
- Arquitetura: `ARCHITECTURE.md`
- Estrutura: `PROJECT_STRUCTURE.md`
- Roadmap: `IMPLEMENTATION_ROADMAP.md`
- Setup: `docs/DEVELOPMENT_SETUP.md`

### Código Base
- Modelos: `backend/app/models/`
- Schemas: `backend/app/schemas/`
- Core RAG: `backend/app/core/rag/`
- Personalização: `backend/app/core/personalization/`

### Configurações
- Fontes scraping: `scraping/config/sources.yaml`
- Interesses: `data/interests/categories.json`
- Env example: `backend/.env.example`

## Convenções

### Python
- PEP 8 style guide
- Type hints obrigatórios
- Docstrings (Google style)
- Black formatter

### Git
- Conventional Commits
- Branches: `main`, `develop`, `feature/*`, `fix/*`

### Testing
- pytest para backend
- Coverage > 80%

---

**Última Atualização**: 2025-01-XX
**Versão**: 1.0.0
