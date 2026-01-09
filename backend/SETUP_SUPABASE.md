# Setup com Supabase 🚀

## Por que Supabase?

- ✅ PostgreSQL gerenciado (sem necessidade de instalar localmente)
- ✅ Interface web para gerenciar dados
- ✅ Connection pooling automático
- ✅ Backups automáticos
- ✅ Gratuito até 500MB de banco
- ✅ SSL por padrão

## 📋 Passo a Passo

### 1. Criar projeto no Supabase

1. Acesse: https://supabase.com
2. Faça login ou crie uma conta
3. Clique em "New Project"
4. Preencha:
   - **Name:** P1A EdTech (ou o nome que preferir)
   - **Database Password:** Crie uma senha forte (anote bem!)
   - **Region:** Escolha a mais próxima (ex: South America - São Paulo)
5. Aguarde a criação do projeto (~2 minutos)

### 2. Obter Connection String

1. No dashboard do Supabase, vá em **Settings** → **Database**
2. Role até a seção **Connection string**
3. Selecione a aba **URI**
4. Copie a string de conexão (ela já vem com a senha)

**Formato da URL:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
```

**OU use a Connection Pooling (recomendado):**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

### 3. Configurar arquivo `.env`

Edite `/Users/fernandafaria/Downloads/P1A/backend/.env`:

```env
# Substitua pela Connection String do Supabase
DATABASE_URL=postgresql://postgres.xxxxxxxxxxxxx:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres

# As outras configurações permanecem iguais
SECRET_KEY=lZnbqL-oNPZohl6W982SBqOECeaaAfRbpvyJDsnTx_w
OPENAI_API_KEY=sk-sua-chave-aqui
```

**⚠️ IMPORTANTE:**
- Substitua `SUA_SENHA` pela senha que você criou ao criar o projeto
- A URL já vem com o formato correto, só precisa substituir a senha

### 4. Executar Migrations

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Executar migration
alembic upgrade head
```

Se o comando `alembic` não estiver disponível:
```bash
python3 -c "from alembic.config import Config; from alembic import command; cfg = Config('alembic.ini'); command.upgrade(cfg, 'head')"
```

### 5. Verificar no Supabase

1. No dashboard do Supabase, vá em **Table Editor**
2. Você deve ver as tabelas criadas:
   - ✅ `users`
   - ✅ `professor_profiles`
   - ✅ `conversations`
   - ✅ `messages`
   - ✅ `progress`

### 6. Iniciar o servidor

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
uvicorn app.main:app --reload --port 8000
```

## 🔒 Segurança

### Connection Pooling vs Direct Connection

**Connection Pooling (Recomendado):**
- URL termina em `:5432` ou `:6543`
- Melhor para produção
- Limite de conexões simultâneas
- Mais eficiente

**Direct Connection:**
- URL termina em `:5432` mas sem `.pooler`
- Melhor para migrations e scripts
- Menos conexões simultâneas permitidas

**Para migrations, use Direct Connection:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
```

**Para aplicação, use Connection Pooling:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

## 🧪 Testar Conexão

Você pode testar a conexão antes de executar as migrations:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 -c "
from app.config import settings
from sqlalchemy import create_engine, text
try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text('SELECT version()'))
        print('✅ Conexão com Supabase OK!')
        print(f'PostgreSQL: {result.fetchone()[0]}')
except Exception as e:
    print(f'❌ Erro: {e}')
"
```

## 📊 Gerenciar Dados no Supabase

### Table Editor
- Visualize e edite dados diretamente no navegador
- Acesse: Dashboard → Table Editor

### SQL Editor
- Execute queries SQL customizadas
- Acesse: Dashboard → SQL Editor

### API REST Automática
- Supabase gera automaticamente uma API REST
- Acesse: Dashboard → API → REST

## ⚠️ Troubleshooting

### Erro: "password authentication failed"
- Verifique se a senha no `DATABASE_URL` está correta
- A senha é a que você definiu ao criar o projeto

### Erro: "connection timeout"
- Verifique se está usando a URL correta (pooler ou direct)
- Para migrations, use direct connection
- Para aplicação, use connection pooling

### Erro: "too many connections"
- Use connection pooling para a aplicação
- Limite de conexões no plano free: 60 simultâneas

### Erro ao executar migrations
- Certifique-se de usar a **Direct Connection** URL (sem `.pooler`)
- Verifique se a senha está correta
- Tente executar novamente

## 🎯 Próximos Passos

1. ✅ Configurar `.env` com a URL do Supabase
2. ✅ Executar migrations
3. ✅ Verificar tabelas no Supabase Dashboard
4. ✅ Iniciar servidor
5. ✅ Testar API em http://localhost:8000/docs

## 📝 Notas

- O Supabase é 100% compatível com PostgreSQL
- Todas as migrations do Alembic funcionam normalmente
- Você pode usar tanto o SQL Editor quanto o Table Editor
- A API REST do Supabase é opcional (você já tem sua própria API)

---

**Pronto para usar Supabase!** 🚀
