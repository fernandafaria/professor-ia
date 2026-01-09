# 🎯 Guia Visual - Database URL do Supabase

## 🚀 Acesso Rápido

**Seu projeto:** `mzhgkbdnslnlpfciduru`  
**Dashboard:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru

---

## 📍 Onde Encontrar (Passo a Passo Visual)

### Passo 1: Abrir o Dashboard
```
https://app.supabase.com/project/mzhgkbdnslnlpfciduru
```

### Passo 2: Menu Lateral
```
┌─────────────────┐
│ 🏠 Project Home │
│ ⚙️  Settings    │ ← CLIQUE AQUI
│ 📊 Database     │
│ 🔐 Auth         │
│ ...             │
└─────────────────┘
```

### Passo 3: Settings → Database
```
┌─────────────────────────────┐
│ Settings                    │
├─────────────────────────────┤
│ General                     │
│ Database          ← CLIQUE   │
│ API                          │
│ Auth                         │
│ Storage                      │
└─────────────────────────────┘
```

### Passo 4: Connection String
```
Role a página até encontrar:

┌─────────────────────────────────────┐
│ Connection string                  │
├─────────────────────────────────────┤
│ [URI] [Pooler] [JDBC] [Node.js] ... │
│                                     │
│ ┌───────────────────────────────┐   │
│ │ postgresql://postgres...      │   │
│ │ [YOUR-PASSWORD]               │   │
│ └───────────────────────────────┘   │
│                                     │
│ [📋 Copy] button                    │
└─────────────────────────────────────┘
```

**Clique na aba "Pooler"** e depois em **"📋 Copy"**

---

## 🔑 O Que Fazer com a URL Copiada

A URL vai vir assim:
```
postgresql://postgres.mzhgkbdnslnlpfciduru:[YOUR-PASSWORD]@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

### ⚠️ IMPORTANTE: Substituir [YOUR-PASSWORD]

1. A URL tem `[YOUR-PASSWORD]` como placeholder
2. Você precisa substituir pela **senha real do banco**
3. A senha é a que você definiu ao criar o projeto

### Se Esqueceu a Senha:

1. No mesmo lugar (Settings → Database)
2. Role até **"Database password"**
3. Clique em **"Reset database password"**
4. **Anote a nova senha** (ela só aparece uma vez!)

---

## 💻 Configurar no .env

Edite o arquivo: `backend/.env`

```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA_AQUI@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Substitua `SUA_SENHA_AQUI` pela senha do banco!**

---

## 🛠️ Script de Ajuda

Execute o script para ver instruções detalhadas:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 obter_database_url.py
```

Se você já tiver a senha, pode gerar a URL automaticamente:

```bash
python3 obter_database_url.py SUA_SENHA sa-east-1
```

---

## ✅ Testar se Funcionou

Depois de configurar o `.env`, teste:

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
        print('PostgreSQL conectado com sucesso!')
except Exception as e:
    print(f'❌ Erro: {e}')
    print('Verifique se a senha está correta no DATABASE_URL')
"
```

---

## 🆘 Ainda Não Conseguiu?

### Opção 1: Resetar Senha
1. Settings → Database
2. Database password → Reset
3. Copie a nova senha
4. Use no DATABASE_URL

### Opção 2: Usar o Script
```bash
python3 obter_database_url.py
```
O script mostra todas as instruções passo a passo.

### Opção 3: Verificar no Dashboard
- Certifique-se de estar logado
- Verifique se está no projeto correto
- A Connection String está na seção "Database" dentro de "Settings"

---

**Dica:** A senha é sensível - ela não aparece na interface por segurança.  
Você precisa resetá-la se esqueceu, ou usar a que você anotou ao criar o projeto.
