# ⚡ Quick Start - Database URL

## 🚀 3 Passos Rápidos

### 1. Acesse o Supabase
https://app.supabase.com/project/mzhgkbdnslnlpfciduru

### 2. Vá em Settings → Database

### 3. Copie a Connection String

**Para Aplicação (recomendado):**
- Aba **Pooler** → **Transaction mode**
- Copie a URL

**Para Migrations:**
- Aba **URI**
- Copie a URL

## 📝 Exemplo

A URL vai parecer com:
```
postgresql://postgres.mzhgkbdnslnlpfciduru:[SENHA]@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Substitua `[SENHA]` pela senha do banco!**

## ✅ Configurar

Edite `backend/.env`:
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

## 🔑 Esqueceu a Senha?

1. Settings → Database
2. Role até **Database password**
3. Clique em **Reset database password**
4. Anote a nova senha!

---

**Para mais detalhes, veja:** `COMO_OBTER_DATABASE_URL.md`
