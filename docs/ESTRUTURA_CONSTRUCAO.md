# Estrutura de Construção da Plataforma - P1A

**Versão:** 1.0  
**Data:** 2025-01-XX  
**Documento Guia para Estruturação do Projeto**

---

## 1. Visão Geral da Estrutura

Este documento detalha a estrutura recomendada para construção da plataforma educacional P1A, organizando os componentes técnicos de forma sistemática e escalável.

---

## 2. Arquitetura em Camadas

### 2.1 Camada de Apresentação (Frontend)

```
frontend/
├── src/
│   ├── app/                      # Next.js App Router
│   │   ├── layout.tsx            # Layout principal
│   │   ├── page.tsx              # Página inicial
│   │   ├── (auth)/               # Rotas de autenticação
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── (dashboard)/          # Rotas autenticadas
│   │   │   ├── dashboard/        # Dashboard principal
│   │   │   ├── learning/         # Interface de aprendizado
│   │   │   │   ├── chat/         # Chat interativo com IA
│   │   │   │   ├── exercises/    # Exercícios
│   │   │   │   └── progress/     # Acompanhamento de progresso
│   │   │   ├── content/          # Biblioteca de conteúdo
│   │   │   └── profile/          # Perfil do estudante
│   │   │       ├── interests/    # Configuração de interesses
│   │   │       ├── preferences/  # Preferências de aprendizado
│   │   │       └── accessibility/# Configurações de acessibilidade
│   │   └── api/                  # API routes (Next.js)
│   ├── components/               # Componentes React
│   │   ├── ui/                   # Componentes base (shadcn/ui)
│   │   ├── learning/             # Componentes de aprendizado
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── ExerciseCard.tsx
│   │   │   ├── ProgressChart.tsx
│   │   │   └── PersonalizedContent.tsx
│   │   ├── personalization/      # Componentes de personalização
│   │   │   ├── InterestSelector.tsx
│   │   │   ├── LearningProfileSetup.tsx
│   │   │   └── AccessibilitySettings.tsx
│   │   └── layout/               # Componentes de layout
│   │       ├── Header.tsx
│   │       ├── Sidebar.tsx
│   │       └── Footer.tsx
│   ├── lib/                      # Bibliotecas e utils
│   │   ├── api.ts                # Cliente API
│   │   ├── utils.ts
│   │   ├── constants.ts
│   │   └── hooks/                # Custom hooks
│   │       ├── useStudent.ts
│   │       ├── useRAG.ts
│   │       └── usePersonalization.ts
│   ├── store/                    # Estado global (Zustand)
│   │   ├── studentStore.ts
│   │   ├── learningStore.ts
│   │   └── uiStore.ts
│   ├── types/                    # TypeScript types
│   │   ├── student.ts
│   │   ├── content.ts
│   │   └── bncc.ts
│   └── styles/                   # Estilos globais
│       └── globals.css
├── public/                       # Assets estáticos
└── package.json
```

**Stack Frontend:**
- Next.js 14+ (App Router)
- TypeScript
- TailwindCSS
- shadcn/ui (componentes base)
- Zustand (gerenciamento de estado)
- React Query (cache e sincronização)

---

### 2.2 Camada de API (Backend)

```
backend/
├── app/
│   ├── main.py                   # FastAPI application
│   ├── config.py                 # Configurações
│   ├── dependencies.py           # Dependências compartilhadas
│   │
│   ├── api/                      # Endpoints da API
│   │   ├── v1/                   # Versão 1 da API
│   │   │   ├── __init__.py
│   │   │   ├── routes/
│   │   │   │   ├── students.py   # CRUD estudantes
│   │   │   │   ├── learning.py   # Endpoints de aprendizado
│   │   │   │   │   ├── chat.py   # Chat com RAG
│   │   │   │   │   ├── exercises.py
│   │   │   │   │   └── progress.py
│   │   │   │   ├── content.py    # Endpoints de conteúdo
│   │   │   │   ├── personalization.py # Personalização
│   │   │   │   └── bncc.py       # Consultas BNCC
│   │   │   └── dependencies.py   # Auth, rate limiting, etc.
│   │
│   ├── models/                   # Modelos SQLAlchemy
│   │   ├── student.py
│   │   ├── content.py
│   │   ├── interaction.py
│   │   ├── progress.py
│   │   └── bncc.py
│   │
│   ├── schemas/                  # Schemas Pydantic
│   │   ├── student.py
│   │   ├── content.py
│   │   ├── learning.py
│   │   └── requests.py
│   │
│   ├── core/                     # Lógica de negócio
│   │   ├── rag/                  # Sistema RAG
│   │   │   ├── retriever.py      # Motor de recuperação
│   │   │   ├── generator.py      # Geração de respostas
│   │   │   ├── embeddings.py     # Gerenciamento de embeddings
│   │   │   ├── prompts.py        # Templates de prompts
│   │   │   └── reranker.py       # Reranking personalizado
│   │   │
│   │   ├── personalization/      # Motor de personalização
│   │   │   ├── profile_manager.py
│   │   │   ├── recommender.py
│   │   │   ├── adaptor.py        # Adaptação de conteúdo
│   │   │   └── interest_mapper.py
│   │   │
│   │   ├── bncc/                 # Integração BNCC
│   │   │   ├── parser.py         # Parser BNCC
│   │   │   ├── mapper.py         # Mapeamento conteúdo-BNCC
│   │   │   └── validator.py      # Validação de alinhamento
│   │   │
│   │   └── content/              # Gerenciamento de conteúdo
│   │       ├── processor.py      # Processamento de conteúdo
│   │       ├── validator.py      # Validação de qualidade
│   │       └── chunker.py        # Divisão em chunks
│   │
│   ├── services/                 # Serviços externos
│   │   ├── vector_db.py          # Interface Vector DB
│   │   ├── llm_service.py        # Interface LLM (OpenAI/Claude)
│   │   ├── database.py           # Interface banco de dados
│   │   └── cache.py              # Serviço de cache (Redis)
│   │
│   ├── workers/                  # Background workers (Celery)
│   │   ├── scraping_tasks.py     # Tarefas de web scraping
│   │   ├── embedding_tasks.py    # Geração de embeddings
│   │   └── content_tasks.py      # Processamento de conteúdo
│   │
│   └── utils/                    # Utilitários
│       ├── text_processing.py
│       ├── validators.py
│       └── logging.py
│
├── scraping/                     # Sistema de Web Scraping
│   ├── scrapers/                 # Scrapers específicos
│   │   ├── base_scraper.py       # Classe base
│   │   ├── bncc_scraper.py       # Scraper BNCC oficial
│   │   ├── educational_scraper.py # Sites educacionais
│   │   ├── cultural_scraper.py   # Conteúdo cultural
│   │   │   ├── games_scraper.py
│   │   │   ├── football_scraper.py
│   │   │   └── music_scraper.py
│   │   └── news_scraper.py       # Notícias e tendências
│   │
│   ├── processors/               # Processadores de dados
│   │   ├── cleaner.py            # Limpeza de dados
│   │   ├── chunker.py            # Divisão em chunks
│   │   └── extractor.py          # Extração de metadados
│   │
│   └── config/                   # Configurações de scraping
│       ├── sources.yaml          # Fontes de dados
│       └── selectors.yaml        # Seletores CSS/XPath
│
├── alembic/                      # Migrations
│   ├── versions/
│   └── env.py
│
├── tests/                        # Testes
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
└── scripts/                      # Scripts utilitários
    ├── init_db.py
    ├── seed_bncc.py
    └── generate_embeddings.py
```

---

### 2.3 Camada de Dados

```
data/
├── bncc/                         # Dados BNCC estruturados
│   ├── competencias_gerais.json
│   ├── competencias_especificas/
│   │   ├── matematica.json
│   │   ├── linguagens.json
│   │   └── ...
│   ├── habilidades/
│   │   ├── ef_ii/
│   │   └── em/
│   └── objetos_conhecimento/
│
├── interests/                    # Mapeamento de interesses
│   ├── categories.json           # Categorias de interesses
│   ├── keywords/                 # Keywords por categoria
│   └── strategies.json           # Estratégias de personalização
│
├── raw/                          # Dados brutos coletados
│   ├── curriculum/               # Conteúdo curricular
│   ├── cultural/                 # Conteúdo cultural
│   └── metadata/                 # Metadados de scraping
│
└── processed/                    # Dados processados
    ├── embeddings/               # Embeddings pré-calculados
    └── chunks/                   # Chunks processados
```

---

### 2.4 Infraestrutura e DevOps

```
infrastructure/
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   ├── Dockerfile.worker        # Celery workers
│   └── docker-compose.yml
│
├── kubernetes/                   # K8s manifests (opcional)
│   ├── backend/
│   ├── frontend/
│   └── workers/
│
├── nginx/
│   └── nginx.conf
│
└── terraform/                    # IaC (opcional)
    └── main.tf
```

---

## 3. Fluxos de Dados Principais

### 3.1 Fluxo de Ingestão de Conteúdo

```
1. Web Scraping (Celery Task)
   ↓
2. Validação e Limpeza
   ↓
3. Extração de Metadados
   - Tipo (curricular/cultural)
   - Série/ano
   - Matéria
   - Interesses relacionados
   ↓
4. Chunking Inteligente
   ↓
5. Geração de Embeddings (Batch)
   ↓
6. Mapeamento BNCC
   ↓
7. Ingestão no Vector DB
   ↓
8. Indexação e Disponibilização
```

### 3.2 Fluxo de Consulta do Usuário (RAG)

```
1. Usuário faz consulta
   ↓
2. Pré-processamento
   - Carregar perfil do estudante
   - Identificar interesses
   - Verificar histórico
   ↓
3. Busca Semântica (Vector Search)
   - Query → Embedding
   - Busca no Vector DB
   - Filtros por metadata
   ↓
4. Reranking Personalizado
   - Score de relevância semântica
   - Score de personalização
   - Score de alinhamento BNCC
   ↓
5. Seleção de Top-K Chunks
   ↓
6. Construção de Contexto
   - Chunks relevantes
   - Metadados BNCC
   - Contexto do aluno
   ↓
7. Geração LLM
   - Prompt engineering
   - Geração personalizada
   ↓
8. Validação e Pós-processamento
   - Validação BNCC
   - Formatação para apresentação
   ↓
9. Resposta ao usuário
   ↓
10. Logging e Analytics
    - Interação salva
    - Feedback coletado
    - Métricas atualizadas
```

### 3.3 Fluxo de Personalização

```
1. Configuração Inicial do Perfil
   ↓
2. Identificação de Interesses
   ↓
3. Mapeamento para Estratégias
   ↓
4. Adaptação de Conteúdo
   - Por interesse
   - Por perfil de aprendizado
   - Por necessidade especial
   ↓
5. Recomendação de Conteúdo
   ↓
6. Feedback Loop
   - Coleta de feedback
   - Ajuste de recomendações
   - Atualização de perfil
```

---

## 4. Decisões Arquiteturais

### 4.1 Por que FastAPI?
- ⚡ Performance alta (async/await nativo)
- 📚 Documentação automática (OpenAPI/Swagger)
- 🔒 Type safety com Pydantic
- 🐍 Python (ecossistema ML/NLP rico)

### 4.2 Por que ChromaDB?
- 🔍 Busca semântica eficiente
- 📦 Fácil de usar e deployar
- 🔄 Suporte a metadata filtering
- 💾 Armazenamento local ou remoto

### 4.3 Por que Next.js?
- ⚡ Server-side rendering (SSR)
- 📱 App Router moderno
- 🎨 Integração fácil com TailwindCSS
- 🔄 API routes integradas

### 4.4 Por que Celery?
- 🔄 Processamento assíncrono robusto
- 📊 Monitoramento de tasks
- 🔁 Retry automático
- 📈 Escalabilidade horizontal

---

## 5. Próximas Ações de Estruturação

### Imediato
1. ✅ Criar estrutura de diretórios base
2. ⬜ Configurar ambiente de desenvolvimento
3. ⬜ Setup banco de dados (PostgreSQL)
4. ⬜ Setup Vector DB (ChromaDB)
5. ⬜ Configurar Celery + Redis

### Curto Prazo
1. ⬜ Implementar modelos de dados básicos
2. ⬜ Criar endpoints API principais
3. ⬜ Setup sistema RAG básico
4. ⬜ Implementar primeiro scraper

---

**Última Atualização:** 2025-01-XX