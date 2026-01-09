# Estrutura do Projeto P1A

## Organização de Diretórios

```
P1A/
├── backend/                          # Backend Python
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                   # FastAPI application
│   │   ├── config.py                 # Configurações
│   │   ├── models/                   # Modelos de dados (SQLAlchemy/Pydantic)
│   │   │   ├── __init__.py
│   │   │   ├── student.py            # Modelo de estudante
│   │   │   ├── content.py            # Modelo de conteúdo
│   │   │   ├── interaction.py        # Modelo de interação
│   │   │   └── bncc.py               # Modelo BNCC
│   │   ├── schemas/                  # Schemas Pydantic (validação)
│   │   │   ├── __init__.py
│   │   │   ├── student.py
│   │   │   ├── content.py
│   │   │   └── requests.py
│   │   ├── api/                      # Endpoints da API
│   │   │   ├── __init__.py
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── students.py       # CRUD estudantes
│   │   │   │   ├── content.py        # Endpoints de conteúdo
│   │   │   │   ├── learning.py       # Endpoints de aprendizado
│   │   │   │   ├── personalization.py # Personalização
│   │   │   │   └── progress.py       # Progresso e analytics
│   │   │   └── dependencies.py       # Dependências compartilhadas
│   │   ├── core/                     # Lógica de negócio
│   │   │   ├── __init__.py
│   │   │   ├── rag/                  # Sistema RAG
│   │   │   │   ├── __init__.py
│   │   │   │   ├── retriever.py      # Motor de recuperação
│   │   │   │   ├── generator.py      # Geração de respostas
│   │   │   │   ├── embeddings.py     # Gerenciamento de embeddings
│   │   │   │   └── prompts.py        # Templates de prompts
│   │   │   ├── personalization/      # Motor de personalização
│   │   │   │   ├── __init__.py
│   │   │   │   ├── profile_manager.py # Gerenciamento de perfil
│   │   │   │   ├── recommender.py    # Sistema de recomendações
│   │   │   │   ├── adaptor.py        # Adaptação de conteúdo
│   │   │   │   └── interest_mapper.py # Mapeamento de interesses
│   │   │   ├── bncc/                 # Integração BNCC
│   │   │   │   ├── __init__.py
│   │   │   │   ├── parser.py         # Parser BNCC
│   │   │   │   ├── mapper.py         # Mapeamento conteúdo-BNCC
│   │   │   │   └── validator.py      # Validação de alinhamento
│   │   │   └── content/              # Gerenciamento de conteúdo
│   │   │       ├── __init__.py
│   │   │       ├── processor.py      # Processamento de conteúdo
│   │   │       └── validator.py      # Validação de conteúdo
│   │   ├── services/                 # Serviços externos
│   │   │   ├── __init__.py
│   │   │   ├── vector_db.py          # Interface Vector DB
│   │   │   ├── llm_service.py        # Interface LLM (OpenAI/Claude)
│   │   │   └── database.py           # Interface banco de dados
│   │   ├── workers/                  # Background workers (Celery)
│   │   │   ├── __init__.py
│   │   │   ├── scraping_tasks.py     # Tarefas de web scraping
│   │   │   ├── embedding_tasks.py    # Geração de embeddings
│   │   │   └── content_tasks.py      # Processamento de conteúdo
│   │   └── utils/                    # Utilitários
│   │       ├── __init__.py
│   │       ├── text_processing.py    # Processamento de texto
│   │       ├── validators.py         # Validadores customizados
│   │       └── logging.py            # Configuração de logs
│   ├── scraping/                     # Sistema de Web Scraping
│   │   ├── __init__.py
│   │   ├── scrapers/                 # Scrapers específicos
│   │   │   ├── __init__.py
│   │   │   ├── base_scraper.py       # Classe base
│   │   │   ├── bncc_scraper.py       # Scraper BNCC
│   │   │   ├── educational_scraper.py # Sites educacionais
│   │   │   ├── cultural_scraper.py   # Conteúdo cultural
│   │   │   └── news_scraper.py       # Notícias e tendências
│   │   ├── processors/               # Processadores de dados
│   │   │   ├── __init__.py
│   │   │   ├── cleaner.py            # Limpeza de dados
│   │   │   ├── chunker.py            # Divisão em chunks
│   │   │   └── extractor.py          # Extração de metadados
│   │   └── config/                   # Configurações de scraping
│   │       ├── __init__.py
│   │       ├── sources.yaml          # Fontes de dados
│   │       └── selectors.yaml        # Seletores CSS/XPath
│   ├── tests/                        # Testes
│   │   ├── __init__.py
│   │   ├── unit/
│   │   ├── integration/
│   │   └── fixtures/
│   ├── alembic/                      # Migrations (SQLAlchemy)
│   │   ├── versions/
│   │   └── env.py
│   ├── scripts/                      # Scripts utilitários
│   │   ├── init_db.py                # Inicialização do banco
│   │   ├── seed_bncc.py              # Seed dados BNCC
│   │   └── generate_embeddings.py    # Geração de embeddings
│   └── requirements.txt              # Dependências Python
│
├── frontend/                         # Frontend React/Next.js
│   ├── src/
│   │   ├── app/                      # Next.js App Router
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   ├── (dashboard)/
│   │   │   │   ├── dashboard/
│   │   │   │   ├── learning/
│   │   │   │   ├── content/
│   │   │   │   └── profile/
│   │   │   └── api/                  # API routes (Next.js)
│   │   ├── components/               # Componentes React
│   │   │   ├── ui/                   # Componentes base (shadcn/ui)
│   │   │   ├── learning/             # Componentes de aprendizado
│   │   │   ├── personalization/      # Componentes de personalização
│   │   │   └── layout/               # Componentes de layout
│   │   ├── lib/                      # Bibliotecas e utils
│   │   │   ├── api.ts                # Cliente API
│   │   │   ├── utils.ts
│   │   │   └── constants.ts
│   │   ├── hooks/                    # Custom hooks
│   │   ├── store/                    # Estado global (Zustand/Redux)
│   │   ├── types/                    # TypeScript types
│   │   └── styles/                   # Estilos globais
│   ├── public/                       # Assets estáticos
│   ├── package.json
│   └── tsconfig.json
│
├── data/                             # Dados e recursos
│   ├── bncc/                         # Dados BNCC estruturados
│   │   ├── competencias.json
│   │   ├── habilidades.json
│   │   └── objetos_conhecimento.json
│   ├── interests/                    # Mapeamento de interesses
│   │   └── categories.json
│   ├── raw/                          # Dados brutos coletados
│   └── processed/                    # Dados processados
│
├── infrastructure/                   # Infraestrutura e DevOps
│   ├── docker/
│   │   ├── Dockerfile.backend
│   │   ├── Dockerfile.frontend
│   │   └── docker-compose.yml
│   ├── kubernetes/                   # K8s manifests (opcional)
│   ├── nginx/
│   │   └── nginx.conf
│   └── terraform/                    # IaC (opcional)
│
├── docs/                             # Documentação
│   ├── api/                          # Documentação da API
│   ├── architecture/                 # Arquitetura detalhada
│   ├── development/                  # Guias de desenvolvimento
│   └── deployment/                   # Guias de deploy
│
├── .env.example                      # Template de variáveis
├── .gitignore
├── README.md
├── ARCHITECTURE.md                   # Este arquivo
└── PROJECT_STRUCTURE.md              # Estrutura detalhada
```

## Principais Módulos

### Backend Core

1. **RAG System** (`app/core/rag/`)
   - Recuperação semântica de conteúdo
   - Geração de respostas personalizadas
   - Gerenciamento de embeddings

2. **Personalization Engine** (`app/core/personalization/`)
   - Gerenciamento de perfil do estudante
   - Sistema de recomendações
   - Adaptação de conteúdo por perfil

3. **BNCC Integration** (`app/core/bncc/`)
   - Parser e validação BNCC
   - Mapeamento conteúdo-currículo
   - Rastreabilidade curricular

4. **Web Scraping** (`scraping/`)
   - Scrapers especializados
   - Processamento e limpeza
   - Ingestão em base de conhecimento

### Frontend

1. **Learning Interface**
   - Interface de aprendizado personalizada
   - Visualização de progresso
   - Feedback interativo

2. **Personalization UI**
   - Configuração de interesses
   - Ajustes de preferências
   - Visualização de perfil

3. **Content Display**
   - Renderização de conteúdo contextualizado
   - Exercícios interativos
   - Gamificação

## Convenções

- **Python**: PEP 8, type hints, docstrings
- **TypeScript**: ESLint, Prettier, strict mode
- **Git**: Conventional Commits
- **Testing**: pytest (backend), Jest (frontend)
- **Documentation**: Markdown, OpenAPI/Swagger
