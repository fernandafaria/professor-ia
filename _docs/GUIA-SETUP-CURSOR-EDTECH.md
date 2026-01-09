# Guia Completo de Setup do Cursor para Plataforma EdTech

**Autor:** Manus AI  
**Data:** 08 de janeiro de 2026  
**Versão:** 1.0

---

## Sumário Executivo

Este guia fornece instruções completas para configurar o Cursor IDE para desenvolvimento full-stack de uma plataforma educacional com IA. Abrange desde a instalação de extensões e configuração do ambiente até os pacotes necessários para webscraping, backend (Python/Node.js), frontend (React/Next.js), banco de dados (PostgreSQL/MongoDB), sistema RAG com embeddings vetoriais e integração com LLMs.

---

## 1. Pré-requisitos do Sistema

Antes de iniciar, certifique-se de ter instalado no seu sistema operacional:

### 1.1 Ferramentas Essenciais

**Python 3.10+**
```bash
# Verificar versão
python --version  # ou python3 --version

# Instalar (Ubuntu/Debian)
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip

# Instalar (macOS com Homebrew)
brew install python@3.10

# Instalar (Windows)
# Baixar de https://www.python.org/downloads/
```

**Node.js 18+ e npm/pnpm**
```bash
# Verificar versão
node --version
npm --version

# Instalar (Ubuntu/Debian via NodeSource)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Instalar (macOS com Homebrew)
brew install node

# Instalar pnpm (gerenciador de pacotes mais rápido)
npm install -g pnpm
```

**Git**
```bash
# Verificar versão
git --version

# Configurar
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

**PostgreSQL 15+**
```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql@15

# Verificar instalação
psql --version
```

**Docker e Docker Compose (Opcional, mas recomendado)**
```bash
# Instalar Docker Desktop
# https://www.docker.com/products/docker-desktop/

# Verificar instalação
docker --version
docker-compose --version
```

---

## 2. Extensões do Cursor (Essenciais)

Instale estas extensões através do marketplace do Cursor (Ctrl/Cmd + Shift + X):

### 2.1 Python Development

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **Python** | Microsoft | Suporte completo a Python com IntelliSense, linting, debugging |
| **Pylance** | Microsoft | Language server de alta performance para Python |
| **Python Debugger** | Microsoft | Debugging avançado com breakpoints e watch |
| **Jupyter** | Microsoft | Notebooks interativos para prototipagem |
| **autoDocstring** | Nils Werner | Gera docstrings automaticamente (Google/NumPy/Sphinx) |
| **Python Indent** | Kevin Rose | Indentação inteligente para Python |
| **Python Test Explorer** | Little Fox Team | Visualização e execução de testes pytest/unittest |

### 2.2 JavaScript/TypeScript/React

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **ES7+ React/Redux/React-Native snippets** | dsznajder | Snippets para React com hooks |
| **ESLint** | Microsoft | Linting para JavaScript/TypeScript |
| **Prettier** | Prettier | Formatação automática de código |
| **Tailwind CSS IntelliSense** | Tailwind Labs | Autocomplete para classes Tailwind |
| **Auto Rename Tag** | Jun Han | Renomeia tags HTML/JSX automaticamente |
| **Import Cost** | Wix | Mostra tamanho de imports |
| **Console Ninja** | Wallaby.js | Console.log inline no editor |

### 2.3 Banco de Dados

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **PostgreSQL** | Chris Kolkman | Cliente PostgreSQL integrado |
| **MongoDB for VS Code** | MongoDB | Cliente MongoDB com IntelliSense |
| **SQLTools** | Matheus Teixeira | Gerenciador universal de bancos SQL |
| **Database Client** | Weijan Chen | Cliente multi-database (PostgreSQL, MySQL, MongoDB, Redis) |

### 2.4 DevOps e Containers

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **Docker** | Microsoft | Gerenciamento de containers |
| **Remote - SSH** | Microsoft | Desenvolvimento remoto via SSH |
| **Remote - Containers** | Microsoft | Desenvolvimento dentro de containers |
| **YAML** | Red Hat | Suporte a arquivos YAML (Docker Compose, Kubernetes) |

### 2.5 Git e Colaboração

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **GitLens** | GitKraken | Visualização avançada de histórico Git |
| **Git Graph** | mhutchie | Visualização gráfica de branches |
| **GitHub Copilot** | GitHub | Sugestões de código com IA (pago) |
| **GitHub Pull Requests** | GitHub | Gerenciamento de PRs no editor |

### 2.6 Produtividade

| Extensão | Publisher | Descrição |
|----------|-----------|-----------|
| **Better Comments** | Aaron Bond | Comentários coloridos e categorizados |
| **Error Lens** | Alexander | Mostra erros inline no código |
| **Todo Tree** | Gruntfuggly | Visualiza TODOs e FIXMEs |
| **Path Intellisense** | Christian Kohler | Autocomplete de caminhos de arquivos |
| **REST Client** | Huachao Mao | Testa APIs HTTP diretamente no editor |
| **Thunder Client** | Ranga Vadhineni | Cliente REST similar ao Postman |

---

## 3. Configuração do Cursor

### 3.1 Settings.json Global

Crie/edite o arquivo de configurações globais (Ctrl/Cmd + Shift + P → "Preferences: Open User Settings (JSON)"):

```json
{
  // Editor
  "editor.fontSize": 14,
  "editor.fontFamily": "'JetBrains Mono', 'Fira Code', Consolas, monospace",
  "editor.fontLigatures": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true,
    "source.fixAll.eslint": true
  },
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": true,
  "editor.inlineSuggest.enabled": true,
  "editor.suggestSelection": "first",
  "editor.tabSize": 2,
  "editor.rulers": [80, 120],
  
  // Python
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "100"],
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  
  // JavaScript/TypeScript
  "javascript.updateImportsOnFileMove.enabled": "always",
  "typescript.updateImportsOnFileMove.enabled": "always",
  "javascript.suggest.autoImports": true,
  "typescript.suggest.autoImports": true,
  
  // Prettier
  "prettier.singleQuote": true,
  "prettier.trailingComma": "es5",
  "prettier.printWidth": 100,
  
  // ESLint
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact"
  ],
  
  // Files
  "files.autoSave": "onFocusChange",
  "files.exclude": {
    "**/__pycache__": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/node_modules": true,
    "**/.next": true,
    "**/dist": true,
    "**/build": true
  },
  
  // Terminal
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.fontFamily": "'JetBrains Mono', monospace",
  
  // Git
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  
  // Tailwind
  "tailwindCSS.experimental.classRegex": [
    ["cva\\(([^)]*)\\)", "[\"'`]([^\"'`]*).*?[\"'`]"],
    ["cn\\(([^)]*)\\)", "[\"'`]([^\"'`]*).*?[\"'`]"]
  ]
}
```

### 3.2 Configuração por Projeto

Crie uma pasta `.vscode` na raiz do seu projeto com os seguintes arquivos:

**`.vscode/settings.json`** (configurações específicas do projeto):
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/bin/python",
  "python.envFile": "${workspaceFolder}/backend/.env",
  "python.analysis.extraPaths": [
    "${workspaceFolder}/backend/src"
  ],
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.tabSize": 4
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.tabSize": 2
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

**`.vscode/launch.json`** (configuração de debugging):
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "src.main:app",
        "--reload",
        "--host",
        "0.0.0.0",
        "--port",
        "8000"
      ],
      "jinja": true,
      "justMyCode": false,
      "cwd": "${workspaceFolder}/backend"
    },
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": false
    },
    {
      "name": "Next.js: Debug",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "pnpm",
      "runtimeArgs": ["dev"],
      "cwd": "${workspaceFolder}/frontend",
      "port": 9229,
      "console": "integratedTerminal"
    }
  ]
}
```

**`.vscode/extensions.json`** (recomendações de extensões):
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "ms-azuretools.vscode-docker",
    "eamodio.gitlens",
    "rangav.vscode-thunder-client"
  ]
}
```

---

## 4. Estrutura de Pastas do Projeto

```
edtech-platform/
├── backend/                    # API Python (FastAPI)
│   ├── src/
│   │   ├── api/               # Endpoints REST
│   │   ├── core/              # Configurações, segurança
│   │   ├── db/                # Modelos, migrations
│   │   ├── services/          # Lógica de negócio
│   │   ├── rag/               # Sistema RAG
│   │   └── main.py            # Entry point
│   ├── tests/                 # Testes pytest
│   ├── scrapers/              # Scripts de webscraping
│   ├── venv/                  # Ambiente virtual Python
│   ├── requirements.txt       # Dependências Python
│   ├── .env                   # Variáveis de ambiente
│   └── pyproject.toml         # Configuração do projeto
├── frontend/                   # App React/Next.js
│   ├── src/
│   │   ├── app/               # Pages (App Router)
│   │   ├── components/        # Componentes React
│   │   ├── hooks/             # Custom hooks
│   │   ├── lib/               # Utilidades
│   │   └── styles/            # CSS/Tailwind
│   ├── public/                # Assets estáticos
│   ├── package.json           # Dependências Node
│   ├── tsconfig.json          # Config TypeScript
│   ├── tailwind.config.js     # Config Tailwind
│   └── .env.local             # Variáveis de ambiente
├── data/                       # Dados scraped
│   ├── raw/                   # Dados brutos
│   ├── processed/             # Dados processados
│   └── embeddings/            # Vetores para RAG
├── docker/                     # Dockerfiles
│   ├── backend.Dockerfile
│   ├── frontend.Dockerfile
│   └── nginx.Dockerfile
├── .github/                    # CI/CD workflows
├── docs/                       # Documentação
├── docker-compose.yml          # Orquestração de containers
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Documentação principal
```

---

## 5. Pacotes Python (Backend + Webscraping + IA)

### 5.1 Requirements.txt Completo

Crie `backend/requirements.txt`:

```txt
# ===== Framework Web =====
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.3
pydantic-settings==2.1.0

# ===== Banco de Dados =====
sqlalchemy==2.0.25
alembic==1.13.1
psycopg2-binary==2.9.9
asyncpg==0.29.0
redis==5.0.1

# MongoDB (opcional)
motor==3.3.2
pymongo==4.6.1

# ===== Autenticação e Segurança =====
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
bcrypt==4.1.2

# ===== Webscraping =====
requests==2.31.0
httpx==0.26.0
beautifulsoup4==4.12.3
lxml==5.1.0
selenium==4.16.0
playwright==1.40.0
scrapy==2.11.0
aiohttp==3.9.1

# ===== Processamento de Dados =====
pandas==2.1.4
numpy==1.26.3
openpyxl==3.1.2

# ===== IA e LLMs =====
openai==1.6.1
anthropic==0.8.1
langchain==0.1.0
langchain-openai==0.0.2
langchain-community==0.0.10

# ===== RAG e Embeddings =====
chromadb==0.4.22
sentence-transformers==2.2.2
faiss-cpu==1.7.4
tiktoken==0.5.2

# Alternativa: Pinecone
# pinecone-client==3.0.0

# ===== Utilidades =====
python-dotenv==1.0.0
loguru==0.7.2
tqdm==4.66.1
tenacity==8.2.3
ratelimit==2.2.1

# ===== Testes =====
pytest==7.4.4
pytest-asyncio==0.23.3
pytest-cov==4.1.0
httpx==0.26.0

# ===== Linting e Formatação =====
black==23.12.1
flake8==7.0.0
isort==5.13.2
mypy==1.8.0

# ===== Monitoramento =====
sentry-sdk[fastapi]==1.39.2
prometheus-client==0.19.0

# ===== Tarefas Assíncronas (opcional) =====
celery==5.3.4
flower==2.0.1

# ===== Email =====
fastapi-mail==1.4.1

# ===== File Storage =====
boto3==1.34.22  # AWS S3
```

### 5.2 Instalação

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Instalar Playwright browsers (para scraping de SPAs)
playwright install
```

### 5.3 Pyproject.toml (Configuração Moderna)

Crie `backend/pyproject.toml`:

```toml
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 100
multi_line_output = 3

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = "-v --cov=src --cov-report=html --cov-report=term"
```

---

## 6. Pacotes Node.js (Frontend)

### 6.1 Package.json Completo

Crie `frontend/package.json`:

```json
{
  "name": "edtech-platform-frontend",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit",
    "format": "prettier --write \"src/**/*.{js,jsx,ts,tsx,json,css,md}\""
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "next": "^14.0.4",
    
    "@tanstack/react-query": "^5.17.9",
    "axios": "^1.6.5",
    "swr": "^2.2.4",
    
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-tabs": "^1.0.4",
    "@radix-ui/react-toast": "^1.1.5",
    "@radix-ui/react-tooltip": "^1.0.7",
    "@radix-ui/react-avatar": "^1.0.4",
    "@radix-ui/react-progress": "^1.0.3",
    
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.0",
    "tailwindcss-animate": "^1.0.7",
    
    "lucide-react": "^0.303.0",
    "framer-motion": "^10.18.0",
    
    "react-hook-form": "^7.49.3",
    "zod": "^3.22.4",
    "@hookform/resolvers": "^3.3.4",
    
    "recharts": "^2.10.4",
    "react-markdown": "^9.0.1",
    "remark-gfm": "^4.0.0",
    "remark-math": "^6.0.0",
    "rehype-katex": "^7.0.0",
    
    "date-fns": "^3.0.6",
    "zustand": "^4.4.7",
    "immer": "^10.0.3"
  },
  "devDependencies": {
    "@types/node": "^20.10.7",
    "@types/react": "^18.2.47",
    "@types/react-dom": "^18.2.18",
    "typescript": "^5.3.3",
    
    "tailwindcss": "^3.4.1",
    "postcss": "^8.4.33",
    "autoprefixer": "^10.4.16",
    
    "eslint": "^8.56.0",
    "eslint-config-next": "^14.0.4",
    "eslint-config-prettier": "^9.1.0",
    "prettier": "^3.1.1",
    "prettier-plugin-tailwindcss": "^0.5.10",
    
    "@testing-library/react": "^14.1.2",
    "@testing-library/jest-dom": "^6.1.5",
    "vitest": "^1.1.1"
  }
}
```

### 6.2 Instalação

```bash
cd frontend
pnpm install
# ou
npm install
```

### 6.3 Configurações TypeScript

Crie `frontend/tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/hooks/*": ["./src/hooks/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

### 6.4 Configuração Tailwind

Crie `frontend/tailwind.config.js`:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      keyframes: {
        'accordion-down': {
          from: { height: 0 },
          to: { height: 'var(--radix-accordion-content-height)' },
        },
        'accordion-up': {
          from: { height: 'var(--radix-accordion-content-height)' },
          to: { height: 0 },
        },
      },
      animation: {
        'accordion-down': 'accordion-down 0.2s ease-out',
        'accordion-up': 'accordion-up 0.2s ease-out',
      },
    },
  },
  plugins: [require('tailwindcss-animate'), require('@tailwindcss/typography')],
}
```

---

## 7. Banco de Dados

### 7.1 PostgreSQL com pgvector

**Instalação da extensão pgvector:**

```bash
# Ubuntu/Debian
sudo apt install postgresql-15-pgvector

# macOS
brew install pgvector

# Docker (recomendado)
docker run -d \
  --name postgres-pgvector \
  -e POSTGRES_PASSWORD=senha_segura \
  -e POSTGRES_DB=edtech_db \
  -p 5432:5432 \
  ankane/pgvector:latest
```

**Criar banco e extensão:**

```sql
CREATE DATABASE edtech_db;
\c edtech_db
CREATE EXTENSION vector;
```

### 7.2 MongoDB (Opcional)

```bash
# Docker
docker run -d \
  --name mongodb \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=senha_segura \
  -p 27017:27017 \
  mongo:7
```

### 7.3 Redis (Cache e Filas)

```bash
# Docker
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:7-alpine
```

---

## 8. Docker Compose (Ambiente Completo)

Crie `docker-compose.yml` na raiz do projeto:

```yaml
version: '3.8'

services:
  postgres:
    image: ankane/pgvector:latest
    container_name: edtech-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: edtech_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    container_name: edtech-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: ../docker/backend.Dockerfile
    container_name: edtech-backend
    environment:
      DATABASE_URL: postgresql://postgres:postgres@postgres:5432/edtech_db
      REDIS_URL: redis://redis:6379/0
      OPENAI_API_KEY: ${OPENAI_API_KEY}
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
      - ./data:/data
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    command: uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build:
      context: ./frontend
      dockerfile: ../docker/frontend.Dockerfile
    container_name: edtech-frontend
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8000
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
    depends_on:
      - backend
    command: pnpm dev

volumes:
  postgres_data:
  redis_data:
```

**Iniciar todos os serviços:**

```bash
docker-compose up -d
```

---

## 9. Variáveis de Ambiente

### 9.1 Backend (.env)

Crie `backend/.env`:

```env
# Database
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/edtech_db
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=sua_chave_secreta_muito_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview

# Anthropic (Claude)
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-opus-20240229

# Embeddings
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_DIMENSION=1536

# Scraping
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
SCRAPING_DELAY=2
MAX_RETRIES=3

# AWS S3 (opcional)
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=edtech-assets

# Sentry (monitoramento)
SENTRY_DSN=https://...

# Environment
ENVIRONMENT=development
DEBUG=true
```

### 9.2 Frontend (.env.local)

Crie `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=EdTech Platform
NEXT_PUBLIC_ENVIRONMENT=development
```

---

## 10. Scripts Úteis

### 10.1 Makefile (Automação de Tarefas)

Crie `Makefile` na raiz:

```makefile
.PHONY: help install dev test lint format clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make install    - Instala todas as dependências"
	@echo "  make dev        - Inicia ambiente de desenvolvimento"
	@echo "  make test       - Executa todos os testes"
	@echo "  make lint       - Verifica qualidade do código"
	@echo "  make format     - Formata código automaticamente"
	@echo "  make clean      - Remove arquivos temporários"

install:
	cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
	cd frontend && pnpm install

dev:
	docker-compose up -d

test:
	cd backend && pytest
	cd frontend && pnpm test

lint:
	cd backend && flake8 src && mypy src
	cd frontend && pnpm lint

format:
	cd backend && black src && isort src
	cd frontend && pnpm format

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	cd frontend && rm -rf .next node_modules
```

---

## 11. Checklist de Setup

Use este checklist para garantir que tudo está configurado:

### Instalações Base
- [ ] Python 3.10+ instalado e funcionando
- [ ] Node.js 18+ e pnpm instalados
- [ ] Git configurado com nome e email
- [ ] PostgreSQL 15+ instalado ou rodando via Docker
- [ ] Docker e Docker Compose instalados (opcional)

### Extensões do Cursor
- [ ] Python (Microsoft)
- [ ] Pylance (Microsoft)
- [ ] ES7+ React/Redux snippets
- [ ] Tailwind CSS IntelliSense
- [ ] ESLint e Prettier
- [ ] PostgreSQL ou Database Client
- [ ] Docker (se usando containers)
- [ ] GitLens

### Configuração do Projeto
- [ ] Estrutura de pastas criada
- [ ] `.vscode/settings.json` configurado
- [ ] `.vscode/launch.json` para debugging
- [ ] `.gitignore` criado

### Backend
- [ ] Ambiente virtual Python criado (`venv`)
- [ ] `requirements.txt` instalado
- [ ] `.env` configurado com variáveis de ambiente
- [ ] Playwright browsers instalados (se usar scraping de SPAs)
- [ ] PostgreSQL com pgvector funcionando
- [ ] Migrations do banco executadas

### Frontend
- [ ] `package.json` criado
- [ ] Dependências instaladas (`pnpm install`)
- [ ] `tsconfig.json` configurado
- [ ] `tailwind.config.js` configurado
- [ ] `.env.local` criado

### Testes
- [ ] Backend: `pytest` rodando
- [ ] Frontend: `pnpm test` funcionando
- [ ] Linting sem erros (`make lint`)

### Docker (Opcional)
- [ ] `docker-compose.yml` criado
- [ ] Containers iniciando corretamente (`docker-compose up`)
- [ ] Backend acessível em http://localhost:8000
- [ ] Frontend acessível em http://localhost:3000

---

## 12. Próximos Passos

Após completar o setup:

1. **Criar estrutura de banco de dados:** Definir modelos SQLAlchemy para usuários, perfis de alunos, questões, progresso
2. **Implementar autenticação:** JWT tokens, registro, login
3. **Desenvolver scrapers:** Começar com API BNCC e Projeto Ágatha
4. **Configurar sistema RAG:** ChromaDB ou Pinecone para embeddings
5. **Criar endpoints da API:** FastAPI routes para chat, exercícios, progresso
6. **Desenvolver UI:** Componentes React para chat, dashboard, exercícios
7. **Integrar LLM:** OpenAI GPT-4 ou Claude para geração de respostas personalizadas
8. **Testes end-to-end:** Validar fluxo completo de usuário

---

## 13. Recursos Adicionais

**Documentação oficial:**
- FastAPI: https://fastapi.tiangolo.com/
- Next.js: https://nextjs.org/docs
- LangChain: https://python.langchain.com/docs/get_started/introduction
- Tailwind CSS: https://tailwindcss.com/docs
- PostgreSQL: https://www.postgresql.org/docs/

**Tutoriais recomendados:**
- FastAPI + PostgreSQL: https://testdriven.io/blog/fastapi-sqlalchemy/
- Next.js App Router: https://nextjs.org/learn
- RAG com LangChain: https://python.langchain.com/docs/use_cases/question_answering/

---

## 13. Model Context Protocol (MCP) Servers

O Model Context Protocol (MCP) permite que o Cursor acesse ferramentas e dados externos diretamente. Esta seção cobre a configuração dos servidores MCP essenciais para a plataforma EdTech.

### 13.1 Configuração Base

O arquivo `.cursor/mcp.json` na raiz do projeto já está configurado com:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "huggingface": {
      "url": "https://huggingface.co/mcp",
      "transport": "sse"
    }
  }
}
```

### 13.2 Servidores MCP Configurados

#### Figma Make MCP (Remote Server)

**Propósito:** Acesso a arquivos de design do Figma para geração de código.

**Configuração:**
- URL: `https://mcp.figma.com/mcp`
- Transport: SSE (Server-Sent Events)

**Autenticação:**
1. Abra seu arquivo Figma no navegador
2. Ative o **Dev Mode**
3. Clique em **"Set up an MCP client"** no painel à direita
4. Siga o fluxo de autenticação OAuth

**Documentação:** `_docs/CONFIGURACAO-FIGMA-MAKE-MCP.md`

#### Hugging Face MCP

**Propósito:** Acesso a modelos, datasets e Spaces do Hugging Face Hub.

**Configuração:**
- URL: `https://huggingface.co/mcp`
- Transport: SSE

**Autenticação:**
1. Acesse: https://huggingface.co/settings/mcp
2. Faça login na sua conta Hugging Face
3. Selecione **"Cursor"** como cliente
4. Siga as instruções de autenticação

**Documentação:** `_docs/CONFIGURACAO-HUGGINGFACE-MCP.md`

### 13.3 Servidores MCP Adicionais (Opcionais)

#### SymPy / Scientific Calculator

**Status:** Desabilitado temporariamente (problema de compatibilidade)

**Alternativa:** Use SymPy diretamente no código Python via `visualization_utils.py`

**Documentação:** `_docs/CONFIGURACAO-SYMPY-MCP.md`

#### Anki

**Status:** Requer Python 3.10+ e instalação do plugin AnkiConnect

**Alternativa:** Use Anki diretamente via `anki_helper.py`

**Documentação:** `INSTALAR-ANKI-COMPLETO.md`

### 13.4 Visualização de Fórmulas

**Solução Implementada:** Plotly direto no código Python

**Arquivo:** `visualization_utils.py`

**Uso:**
```python
from visualization_utils import plot_function

fig = plot_function("x**2 - 5*x + 6", x_range=(-1, 7))
fig.show()
```

**Documentação:** `_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md`

### 13.5 Documentação MCP Completa

- **Guia Geral:** `_docs/GUIA-MCP-SERVERS.md`
- **Quick Start:** `_docs/QUICK-START-MCP.md`
- **Figma:** `_docs/CONFIGURACAO-FIGMA-MAKE-MCP.md`
- **Hugging Face:** `_docs/CONFIGURACAO-HUGGINGFACE-MCP.md`
- **SymPy:** `_docs/CONFIGURACAO-SYMPY-MCP.md`
- **Visualização:** `_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md`

### 13.6 Verificar Configuração MCP

Após configurar os servidores MCP:

1. Reinicie completamente o Cursor
2. Abra as configurações (`Cmd/Ctrl + ,`)
3. Navegue até **Features > MCP**
4. Verifique se os servidores aparecem na lista
5. Status deve mostrar "Connected" para servidores ativos

---

**Documento elaborado por Manus AI**  
*Para dúvidas ou sugestões, entre em contato através de https://help.manus.im*

**Atualizado com:** Configurações MCP (Figma, Hugging Face) - 2025-01-08
