# Setup Completo - MVP Backend

## ✅ O que foi feito

1. ✅ **Arquivo `.env` criado** a partir de `env.example`
2. ✅ **Migration inicial criada** (`alembic/versions/001_initial_migration_mvp_models.py`)
3. ✅ **Modelo Message corrigido** (campo `metadata` renomeado para `message_metadata`)

## 📋 Próximos Passos

### 1. Configurar o arquivo `.env`

Edite o arquivo `/Users/fernandafaria/Downloads/P1A/backend/.env` e configure:

```env
# Banco de Dados PostgreSQL
DATABASE_URL=postgresql://usuario:senha@localhost:5432/p1a_db

# JWT - Já tem uma chave gerada, mas você pode gerar uma nova
SECRET_KEY=lZnbqL-oNPZohl6W982SBqOECeaaAfRbpvyJDsnTx_w

# OpenAI API - Adicione sua chave
OPENAI_API_KEY=sk-your-key-here
```

### 2. Instalar PostgreSQL (se ainda não tiver)

**macOS:**
```bash
brew install postgresql@14
brew services start postgresql@14
```

**Linux:**
```bash
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### 3. Criar o banco de dados

```bash
# Conectar ao PostgreSQL
psql postgres

# Criar banco de dados
CREATE DATABASE p1a_db;

# Criar usuário (opcional)
CREATE USER p1a_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE p1a_db TO p1a_user;

# Sair
\q
```

### 4. Atualizar DATABASE_URL no .env

```env
DATABASE_URL=postgresql://p1a_user:sua_senha@localhost:5432/p1a_db
```

### 5. Executar as migrations

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Executar migration
alembic upgrade head
```

Se o comando `alembic` não estiver disponível, use:
```bash
python3 -c "from alembic.config import Config; from alembic import command; cfg = Config('alembic.ini'); command.upgrade(cfg, 'head')"
```

### 6. Verificar se funcionou

```bash
# Conectar ao banco e verificar tabelas
psql p1a_db

# Listar tabelas
\dt

# Você deve ver:
# - users
# - professor_profiles
# - conversations
# - messages
# - progress

# Sair
\q
```

### 7. Iniciar o servidor

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
uvicorn app.main:app --reload --port 8000
```

A API estará disponível em:
- **API:** http://localhost:8000
- **Documentação Swagger:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🧪 Testar a API

### 1. Registrar um usuário

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "teste@example.com",
    "name": "Usuário Teste",
    "password": "senha123456"
  }'
```

### 2. Fazer login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "teste@example.com",
    "password": "senha123456"
  }'
```

Você receberá um token JWT. Use esse token nos próximos requests:

```bash
TOKEN="seu-token-aqui"

# Obter dados do usuário
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer $TOKEN"
```

## ⚠️ Problemas Comuns

### Erro: "connection to server at localhost failed"

**Solução:** PostgreSQL não está rodando. Inicie o serviço:
```bash
# macOS
brew services start postgresql@14

# Linux
sudo systemctl start postgresql
```

### Erro: "database does not exist"

**Solução:** Crie o banco de dados (veja passo 3 acima).

### Erro: "password authentication failed"

**Solução:** Verifique o usuário e senha no `DATABASE_URL` do arquivo `.env`.

### Erro ao executar migrations

**Solução:** Certifique-se de que:
1. PostgreSQL está rodando
2. O banco de dados existe
3. As credenciais no `.env` estão corretas
4. O usuário tem permissões no banco

## 📝 Notas

- O arquivo `.env` foi criado automaticamente a partir de `env.example`
- A migration foi criada manualmente e está pronta para ser executada
- Todos os modelos estão corretos e compatíveis com PostgreSQL
- O campo `metadata` no modelo Message foi renomeado para `message_metadata` (palavra reservada do SQLAlchemy)

---

**Última Atualização:** 08 de janeiro de 2026
