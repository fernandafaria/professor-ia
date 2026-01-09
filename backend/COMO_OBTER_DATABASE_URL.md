# 🔗 Como Obter a Database URL do Supabase

## 📋 Passo a Passo

### 1. Acessar o Dashboard do Supabase

1. Acesse: https://app.supabase.com
2. Faça login na sua conta
3. Selecione o projeto: **mzhgkbdnslnlpfciduru** (ou o projeto que você criou)

### 2. Navegar até Database Settings

1. No menu lateral esquerdo, clique em **Settings** (⚙️)
2. Clique em **Database** (ícone de banco de dados)

### 3. Encontrar Connection String

Role a página até a seção **Connection string**

Você verá várias abas:
- **URI** - Para conexão direta
- **JDBC** - Para Java
- **Golang** - Para Go
- **Node.js** - Para JavaScript
- **Python** - Para Python
- **Pooler** - Para connection pooling (recomendado)

### 4. Escolher o Tipo de Conexão

#### Opção A: Connection Pooling (Recomendado para Aplicação) ✅

**Use esta para:** Aplicação em produção, múltiplas conexões simultâneas

1. Selecione a aba **Pooler**
2. Selecione **Transaction mode** (ou **Session mode** se precisar)
3. Copie a string que aparece

**Formato:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

**Exemplo:**
```
postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

#### Opção B: Direct Connection (Para Migrations) ✅

**Use esta para:** Executar migrations (Alembic), scripts únicos

1. Selecione a aba **URI**
2. Copie a string que aparece

**Formato:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
```

**Exemplo:**
```
postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres
```

### 5. Substituir a Senha

⚠️ **IMPORTANTE:** A URL vem com `[YOUR-PASSWORD]` como placeholder.

**Você precisa substituir pela senha que você definiu ao criar o projeto Supabase.**

Se você esqueceu a senha:
1. Vá em **Settings** → **Database**
2. Role até **Database password**
3. Clique em **Reset database password**
4. Anote a nova senha (ela só aparece uma vez!)

### 6. Configurar no .env

Edite o arquivo `backend/.env`:

```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA_AQUI@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Substitua:**
- `SUA_SENHA_AQUI` pela senha do banco
- `sa-east-1` pela região do seu projeto (pode ser diferente)

## 🎯 Qual Usar?

### Para Aplicação (uvicorn, produção):
```env
DATABASE_URL=postgresql://postgres.[REF]:[SENHA]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

### Para Migrations (alembic):
```env
DATABASE_URL=postgresql://postgres.[REF]:[SENHA]@db.[REF].supabase.co:5432/postgres
```

## 🔍 Verificar se Funcionou

Depois de configurar, teste a conexão:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 -c "
from app.config import settings
from sqlalchemy import create_engine, text
try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text('SELECT version()'))
        print('✅ Conexão OK!')
        print(f'PostgreSQL: {result.fetchone()[0][:50]}...')
except Exception as e:
    print(f'❌ Erro: {e}')
"
```

## 📸 Onde Encontrar no Dashboard

```
Supabase Dashboard
└── Settings (⚙️)
    └── Database
        └── Connection string
            ├── URI (Direct)
            ├── Pooler (Recomendado)
            └── Outras abas...
```

## 💡 Dicas

1. **Senha Segura:** Use uma senha forte e anote em local seguro
2. **Connection Pooling:** Sempre use para aplicação (mais eficiente)
3. **Direct Connection:** Use apenas para migrations e scripts
4. **Não Compartilhe:** A URL contém sua senha - nunca commite no git!

## ⚠️ Segurança

- ✅ A URL está no `.env` (já está no `.gitignore`)
- ✅ Nunca commite a URL com senha
- ✅ Use variáveis de ambiente em produção
- ✅ Rotacione a senha periodicamente

---

**Pronto!** Agora você tem a Database URL configurada! 🎉
