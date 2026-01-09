# 🚀 Quick Start - Supabase

## Setup Rápido (5 minutos)

### 1. Criar Projeto Supabase
1. Acesse: https://supabase.com → **New Project**
2. Anote a **senha do banco** que você criar
3. Aguarde ~2 minutos para criação

### 2. Obter Connection String
1. Dashboard → **Settings** → **Database**
2. Seção **Connection string** → Aba **URI**
3. Copie a URL (já vem com senha)

### 3. Configurar .env

**Opção A - Script automático:**
```bash
cd /Users/fernandafaria/Downloads/P1A/backend
./configure_supabase.sh
```

**Opção B - Manual:**
Edite `backend/.env` e atualize:
```env
DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[SENHA]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

### 4. Executar Migrations
```bash
cd /Users/fernandafaria/Downloads/P1A/backend
alembic upgrade head
```

### 5. Iniciar Servidor
```bash
uvicorn app.main:app --reload --port 8000
```

### 6. Testar
Acesse: http://localhost:8000/docs

---

**✅ Pronto!** Seu backend está rodando com Supabase! 🎉

Para mais detalhes, veja: `SETUP_SUPABASE.md`
