# 🔐 Como Obter a Senha do Banco Supabase

Para atualizar o `DATABASE_URL`, você precisa da senha do banco de dados do Supabase.

---

## 📋 Informações do Projeto (via MCP)

- **Project Ref:** `mzhgkbdnslnlpfciduru`
- **Project URL:** `mzhgkbdnslnlpfciduru.supabase.co`
- **Tabela RAG:** ✅ `rag_documents` existe

---

## 🔑 Método 1: Obter Senha do Dashboard (Recomendado)

### Passo 1: Acessar Settings do Projeto

1. Acesse: **https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database**
2. Ou navegue: Dashboard → Seu Projeto → Settings → Database

### Passo 2: Encontrar Connection String

1. Role a página até a seção **"Connection string"**
2. Você verá diferentes formatos:
   - **URI** (o que precisamos)
   - **JDBC**
   - **Golang**
   - etc.

### Passo 3: Copiar Senha ou URL Completa

**Opção A: Copiar URL Completa (Mais Fácil)**
- Selecione o modo **"URI"**
- Copie a Connection String completa
- Ela terá o formato:
  ```
  postgresql://postgres.mzhgkbdnslnlpfciduru:[SENHA]@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres
  ```

**Opção B: Copiar Apenas a Senha**
- A senha está entre `postgres.` e `@`
- Exemplo: `postgres.ABC123:MINHA_SENHA_AQUI@db...`
- Copie apenas a parte `MINHA_SENHA_AQUI`

### Passo 4: Atualizar .env

**Se copiou a URL completa:**
```bash
cd backend
# Edite .env manualmente e substitua DATABASE_URL pela URL completa
```

**Se copiou apenas a senha:**
```bash
cd backend
python3 atualizar_database_url_supabase.py [SUA_SENHA_AQUI]
```

---

## 🔑 Método 2: Resetar Senha (Se Não Lembrar)

Se você não lembra a senha ou não tem acesso:

1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database
2. Procure por **"Database password"** ou **"Reset database password"**
3. Clique em **"Reset password"**
4. Uma nova senha será gerada
5. **⚠️ IMPORTANTE:** Copie e salve a nova senha imediatamente (ela não será mostrada novamente)

---

## 🚀 Atualizar DATABASE_URL Automaticamente

Após obter a senha, execute:

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Opção 1: Fornecer apenas a senha
python3 atualizar_database_url_supabase.py [SUA_SENHA]

# Opção 2: Fornecer URL completa
python3 atualizar_database_url_supabase.py "postgresql://postgres.mzhgkbdnslnlpfciduru:[SENHA]@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres"
```

---

## ✅ Verificar Após Atualizar

```bash
cd backend

# 1. Verificar se foi atualizado
python3 -c "
from dotenv import load_dotenv
import os
load_dotenv()
url = os.getenv('DATABASE_URL', '')
if 'supabase' in url.lower():
    print('✅ DATABASE_URL aponta para Supabase')
    print('   URL:', url[:50] + '...')
else:
    print('❌ DATABASE_URL ainda não está configurado para Supabase')
"

# 2. Testar conexão
python3 verificar_supabase.py

# 3. Verificação completa
python3 verificar_pre_requisitos_rag.py
```

---

## 📝 Formato Esperado

O `DATABASE_URL` deve ter este formato:

```
postgresql://postgres.mzhgkbdnslnlpfciduru:[SENHA]@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres
```

Onde `[SENHA]` é a senha do banco de dados.

---

## 🔒 Segurança

- ⚠️ **Nunca compartilhe a senha publicamente**
- ⚠️ **Não commite o arquivo `.env` no Git** (já deve estar no `.gitignore`)
- ✅ **Use variáveis de ambiente em produção**
- ✅ **Rotacione senhas periodicamente**

---

## 💡 Dica Rápida

Se você já tem a Connection String completa do Supabase, pode atualizar diretamente no `.env`:

```bash
cd backend
# Edite .env e substitua a linha DATABASE_URL
nano .env
# ou
code .env
```

---

**Próximo passo:** Após atualizar o DATABASE_URL, execute `python3 verificar_supabase.py` para confirmar que está funcionando.
