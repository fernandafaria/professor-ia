# Guia de Configuração de Desenvolvimento

## Pré-requisitos

### Software Necessário
- **Python 3.10+**: [Download](https://www.python.org/downloads/)
- **Node.js 18+**: [Download](https://nodejs.org/)
- **PostgreSQL 14+**: [Download](https://www.postgresql.org/download/)
- **Redis**: [Download](https://redis.io/download)
- **Docker** (opcional): [Download](https://www.docker.com/)

### Ferramentas Recomendadas
- **Git**: Controle de versão
- **VS Code / Cursor**: Editor de código
- **Postman / Insomnia**: Teste de APIs

## Configuração do Ambiente

### 1. Clone o Repositório

```bash
git clone <repository-url>
cd P1A
```

### 2. Configurar Variáveis de Ambiente

Copie o arquivo de exemplo e configure:

```bash
cp .env.example .env
```

Edite `.env` com suas configurações:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/p1a_db

# ChromaDB
CHROMA_HOST=localhost
CHROMA_PORT=8000

# OpenAI
OPENAI_API_KEY=your_openai_key_here

# Redis
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Security
SECRET_KEY=your_secret_key_here

# App
DEBUG=True
LOG_LEVEL=DEBUG
```

### 3. Configurar Python Environment

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências
cd backend
pip install -r requirements.txt

# Instalar spaCy model português
python -m spacy download pt_core_news_lg
```

### 4. Configurar Banco de Dados

```bash
# Criar banco de dados
createdb p1a_db

# Rodar migrations
cd backend
alembic upgrade head

# Seed dados iniciais (BNCC, etc)
python scripts/seed_bncc.py
```

### 5. Configurar ChromaDB

```bash
# Instalar ChromaDB server
pip install chromadb

# Iniciar ChromaDB (modo servidor)
chroma run --path ./chroma_db --port 8000
```

### 6. Configurar Redis

```bash
# Instalar Redis (Linux/Mac)
brew install redis  # Mac
sudo apt-get install redis  # Ubuntu

# Iniciar Redis
redis-server

# Ou usando Docker
docker run -d -p 6379:6379 redis:alpine
```

### 7. Iniciar Serviços

#### Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

#### Celery Worker (Background Tasks)

```bash
cd backend
celery -A app.workers.celery_app worker --loglevel=info
```

#### Celery Beat (Scheduled Tasks)

```bash
cd backend
celery -A app.workers.celery_app beat --loglevel=info
```

#### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

## Estrutura de Desenvolvimento

### Convenções de Código

#### Python
- **Style**: PEP 8
- **Formatter**: Black
- **Linter**: Flake8
- **Type Hints**: Obrigatório
- **Docstrings**: Google style

```bash
# Formatar código
black backend/

# Verificar estilo
flake8 backend/

# Verificar tipos
mypy backend/
```

#### TypeScript
- **Style**: Airbnb (via ESLint)
- **Formatter**: Prettier
- **Type Safety**: Strict mode

```bash
# Formatar código
npm run format

# Verificar estilo
npm run lint
```

### Git Workflow

1. **Branches**:
   - `main`: Produção
   - `develop`: Desenvolvimento
   - `feature/*`: Novas funcionalidades
   - `fix/*`: Correções de bugs

2. **Commits**: Conventional Commits
   ```
   feat: adicionar sistema de personalização
   fix: corrigir bug no retriever RAG
   docs: atualizar documentação da API
   ```

### Testes

#### Backend

```bash
cd backend
# Todos os testes
pytest

# Com coverage
pytest --cov=app tests/

# Teste específico
pytest tests/unit/test_retriever.py
```

#### Frontend

```bash
cd frontend
# Testes
npm test

# Com coverage
npm test -- --coverage
```

## Troubleshooting

### Erro: "Could not connect to database"
- Verifique se PostgreSQL está rodando
- Confirme `DATABASE_URL` no `.env`
- Teste conexão: `psql $DATABASE_URL`

### Erro: "ChromaDB connection failed"
- Verifique se ChromaDB está rodando
- Confirme `CHROMA_HOST` e `CHROMA_PORT`
- Teste: `curl http://localhost:8000/api/v1/heartbeat`

### Erro: "Redis connection refused"
- Verifique se Redis está rodando
- Teste: `redis-cli ping`

### Erro: "spaCy model not found"
```bash
python -m spacy download pt_core_news_lg
```

## Próximos Passos

1. Configurar ambiente de desenvolvimento
2. Rodar testes para validar setup
3. Explorar documentação da API (`/docs`)
4. Consultar guias específicos:
   - [RAG System](./architecture/RAG_SYSTEM.md)
   - [Personalization Engine](./architecture/PERSONALIZATION.md)
   - [Web Scraping](./architecture/WEB_SCRAPING.md)
