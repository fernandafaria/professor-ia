# 🔗 Database URL - Guia Super Simples

## ⚡ 3 Passos

### 1️⃣ Acesse
https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database

### 2️⃣ Role até "Connection string"
Você vai ver várias abas. Clique em **"Pooler"**

### 3️⃣ Copie a URL
A URL vai aparecer. Ela vai ter `[YOUR-PASSWORD]` - você precisa substituir pela senha do banco!

---

## 🔑 E se eu não sei a senha?

1. Na mesma página (Settings → Database)
2. Role até **"Database password"**
3. Clique em **"Reset database password"**
4. **Anote a senha** (ela só aparece uma vez!)

---

## 💻 Depois de copiar

Edite `backend/.env`:

```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Substitua `SUA_SENHA` pela senha que você copiou/resetou!**

---

## 🛠️ Script de Ajuda

Execute no terminal:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 obter_database_url.py
```

Isso vai mostrar todas as instruções passo a passo!

---

## ✅ Testar

Depois de configurar, teste:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 obter_database_url.py SUA_SENHA
```

Isso vai gerar a URL completa para você copiar!

---

**Link direto:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database
