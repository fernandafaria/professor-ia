# 🔧 Configurar DATABASE_URL para Supabase

## ⚠️ Situação Atual

O `DATABASE_URL` está configurado para PostgreSQL local (`localhost`), mas o projeto usa **Supabase**.

## ✅ Passo 1: Obter Connection String do Supabase

1. Acesse: https://app.supabase.com
2. Selecione seu projeto
3. Vá em **Settings** → **Database**
4. Role até **Connection string**
5. Selecione a aba **URI**
6. Copie a string (já vem com a senha)

**Formato esperado:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

## ✅ Passo 2: Atualizar arquivo `.env`

Edite `/Users/fernandafaria/Downloads/P1A/backend/.env`:

```env
# Substitua esta linha:
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/p1a_db

# Por esta (com sua Connection String do Supabase):
DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

**⚠️ IMPORTANTE:**
- Substitua `[PASSWORD]` pela senha do seu projeto Supabase
- A senha é a que você definiu ao criar o projeto
- Use **Connection Pooling** (porta `5432` ou `6543`) para aplicação

## ✅ Passo 3: Verificar

```bash
cd backend
python3 verificar_supabase.py
```

**Deve mostrar:**
```
✅ DATABASE_URL configurado
✅ Conectado ao PostgreSQL
✅ Extensão pgvector instalada
✅ Tabela rag_documents existe
```

## 🔍 Exemplo de Connection String

**Connection Pooling (Recomendado para aplicação):**
```
postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Direct Connection (Para migrations):**
```
postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres
```

---

**Após configurar, execute:** `python3 verificar_supabase.py`
