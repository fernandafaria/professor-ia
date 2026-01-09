# 🔧 Como Configurar DATABASE_URL para Supabase

**Projeto:** mzhgkbdnslnlpfciduru  
**URL do Projeto:** https://mzhgkbdnslnlpfciduru.supabase.co

---

## 📋 Passo a Passo

### 1. Acessar o Supabase Dashboard

1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru
2. Faça login na sua conta

### 2. Obter a Connection String

1. No menu lateral, clique em **Settings** (⚙️)
2. Clique em **Database**
3. Role até a seção **Connection string**
4. Você verá várias opções de conexão:
   - **URI** (recomendada)
   - **JDBC**
   - **Direct connection**
   - **Connection pooling** (Session mode)
   - **Connection pooling** (Transaction mode)

5. Selecione a aba **URI**
6. Copie a string completa (começa com `postgresql://...`)

### 3. Formato Esperado

A connection string deve ter este formato:

```env
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

**Exemplo real:**
```env
postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA_AQUI@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

### 4. Atualizar o arquivo .env

Edite o arquivo `.env` na raiz do projeto:

```bash
# Abra o arquivo
nano .env
# ou
code .env
```

**Localize esta linha:**
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/p1a_education
```

**Substitua pela connection string do Supabase:**
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Importante:**
- Substitua `SUA_SENHA` pela senha do banco que você definiu ao criar o projeto
- Se você não lembrar a senha, você pode resetá-la no dashboard:
  - Settings → Database → Database password → Reset database password

### 5. Atualizar também o backend/.env

Copie a mesma string para `backend/.env`:

```bash
# Copiar para backend/.env também
cp .env backend/.env
```

Ou edite manualmente o `backend/.env` com a mesma connection string.

### 6. Verificar a Configuração

Execute o script de verificação:

```bash
cd /Users/fernandafaria/Downloads/P1A
PYTHONPATH=/Users/fernandafaria/Downloads/P1A/backend:$PYTHONPATH python3 backend/scraping/check_setup.py
```

**Resultado esperado:**
```
SUPABASE: ✅ OK
  ✅ Supabase: Conectado
  ✅ Tabela rag_documents: Existe
  ✅ pgvector: Instalado
  ✅ Documentos: 0
```

---

## 🔐 Onde Encontrar a Senha do Banco

Se você não lembra a senha do banco:

1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru
2. Settings → **Database**
3. Procure por **Database password**
4. Clique em **Reset database password**
5. Copie a nova senha gerada
6. Use essa senha na connection string

**⚠️ Importante:** Guarde a senha em local seguro! Você precisará dela sempre que for conectar ao banco.

---

## 🧪 Testar Conexão Manualmente

Após atualizar o `.env`, teste a conexão:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 -c "
from app.config import settings
from sqlalchemy import create_engine, text
try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text('SELECT COUNT(*) FROM rag_documents'))
        count = result.scalar()
        print(f'✅ Conexão OK! Documentos no RAG: {count}')
except Exception as e:
    print(f'❌ Erro: {e}')
"
```

**Resultado esperado:**
```
✅ Conexão OK! Documentos no RAG: 0
```

---

## 📝 Exemplo Completo do .env

Depois de configurar, seu `.env` deve ter algo assim:

```env
# ----------------------------------------------------------------------------
# API Keys
# ----------------------------------------------------------------------------
FIRECRAWL_API_KEY=fc-d9e38b1898aa4067be99276054db16be

# ----------------------------------------------------------------------------
# Banco de Dados PostgreSQL / Supabase
# ----------------------------------------------------------------------------
# Connection String obtida do Supabase Dashboard
# Settings → Database → Connection string → URI
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres

# ----------------------------------------------------------------------------
# Segurança
# ----------------------------------------------------------------------------
SECRET_KEY=sua-secret-key-aqui

# ----------------------------------------------------------------------------
# Vector Database (Supabase com pgvector)
# ----------------------------------------------------------------------------
# A tabela rag_documents já está criada no Supabase
# Extensão pgvector já está instalada
# Não é necessário servidor separado - tudo integrado no Supabase

# ----------------------------------------------------------------------------
# CORS
# ----------------------------------------------------------------------------
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
```

---

## ✅ Checklist

- [ ] Acessei o Supabase Dashboard
- [ ] Obtenho a connection string (Settings → Database → URI)
- [ ] Atualizei o `.env` na raiz do projeto
- [ ] Atualizei o `backend/.env` (ou copiei o .env)
- [ ] Executei `check_setup.py` e vi "SUPABASE: ✅ OK"
- [ ] Testei a conexão manualmente

---

## 🚨 Problemas Comuns

### Erro: "connection refused"

**Causa:** DATABASE_URL ainda aponta para localhost  
**Solução:** Certifique-se de que atualizou para a connection string do Supabase

### Erro: "password authentication failed"

**Causa:** Senha incorreta na connection string  
**Solução:** Verifique a senha ou reset-a no dashboard do Supabase

### Erro: "database does not exist"

**Causa:** Nome do banco incorreto (deve ser `postgres`)  
**Solução:** Use `postgres` como nome do banco na connection string

### Erro: "SSL connection required"

**Causa:** Connection string sem SSL  
**Solução:** Use a connection string do dashboard que já inclui SSL

---

**Depois de configurar, você estará pronto para usar o RAG com Supabase!** 🎉
