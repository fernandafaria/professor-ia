# 🔐 Variáveis de Ambiente para Produção

Guia completo das variáveis de ambiente necessárias para deploy do backend.

---

## 📋 Variáveis Obrigatórias

### **1. Banco de Dados**

```env
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
```

**Como obter:**
1. Acesse: https://app.supabase.com
2. Vá em: **Project Settings** → **Database**
3. Em **Connection String**, copie a **URI**
4. Substitua `[YOUR-PASSWORD]` pela senha do banco

**Formato completo:**
```
postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres
```

---

### **2. Segurança (JWT)**

```env
SECRET_KEY=sua-chave-secreta-minimo-32-caracteres-aleatorios
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Gerar SECRET_KEY segura:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Exemplo gerado:**
```
xK9jP2mL8nQ5rT7wV4yZ6bC1dE3fG5hI7jK9lM1nO3pQ5rS7tU9vW1xY3zA5b
```

---

### **3. CORS (Cross-Origin)**

```env
CORS_ORIGINS=https://seu-frontend.vercel.app,https://seu-frontend-vercel.vercel.app,http://localhost:3000
```

**Importante:**
- Adicione TODAS as URLs do frontend
- Separe por vírgula
- Inclua `http://localhost:3000` para desenvolvimento local
- Não deixe espaços após vírgulas

**Exemplo:**
```
CORS_ORIGINS=https://professor-ia.vercel.app,https://professor-ia-git-main.vercel.app,http://localhost:3000
```

---

## 📋 Variáveis Opcionais (mas Recomendadas)

### **4. App Info**

```env
APP_NAME=Plataforma Educacional P1A
APP_VERSION=1.0.0
DEBUG=False
```

**DEBUG:**
- `False` em produção
- `True` apenas em desenvolvimento

---

### **5. Anthropic Claude API**

```env
ANTHROPIC_API_KEY=sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

**Como obter:**
1. Acesse: https://console.anthropic.com/
2. Vá em: **API Keys**
3. Crie uma nova chave ou copie existente

**Modelos disponíveis:**
- `claude-3-5-sonnet-20241022` (recomendado - melhor custo-benefício)
- `claude-3-opus-20240229` (melhor qualidade, mais caro)
- `claude-3-haiku-20240307` (mais rápido e barato)

---

### **6. RAG / Embeddings**

```env
RAG_TABLE_NAME=rag_documents
EMBEDDING_DIMENSION=384
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

**Se usar OpenAI para embeddings (opcional):**
```env
OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_EMBEDDING_MODEL=text-embedding-3-large
```

---

### **7. Logging**

```env
LOG_LEVEL=INFO
```

**Opções:**
- `DEBUG` - Muito verboso (apenas desenvolvimento)
- `INFO` - Informações gerais (recomendado para produção)
- `WARNING` - Apenas avisos
- `ERROR` - Apenas erros

---

### **8. Redis (Opcional - se usar Celery)**

```env
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

**Nota:** Para produção, use Redis Cloud ou Upstash:
```
REDIS_URL=rediss://:password@host:port
```

---

### **9. Firecrawl (Opcional - para web scraping)**

```env
FIRECRAWL_API_KEY=fc-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🔧 Como Configurar no Railway

### **Método 1: Via Dashboard**

1. **No projeto Railway:**
   - Clique no serviço
   - Vá em **"Variables"** (ou clique no serviço → **"Variables"**)

2. **Adicionar variável:**
   - Clique em **"New Variable"**
   - **Name:** Nome da variável (ex: `DATABASE_URL`)
   - **Value:** Valor da variável
   - Clique em **"Add"**

3. **Repetir para todas as variáveis**

### **Método 2: Via arquivo .env (não recomendado para produção)**

Se precisar testar localmente, crie `.env` na raiz do `backend/`:

```bash
cd backend
cp env.example .env
# Edite .env com seus valores
```

**⚠️ IMPORTANTE:** Nunca commite o arquivo `.env` no Git!

---

## 🔧 Como Configurar no Render

1. **No Web Service:**
   - Clique no serviço
   - Vá em **"Environment"**
   - Clique em **"Add Environment Variable"**

2. **Adicionar cada variável:**
   - **Key:** Nome da variável
   - **Value:** Valor da variável
   - Clique em **"Save Changes"**

3. **Render faz redeploy automaticamente** após adicionar variáveis

---

## 📝 Checklist Completo

### **Obrigatórias:**
- [ ] `DATABASE_URL` (do Supabase)
- [ ] `SECRET_KEY` (gerada com secrets.token_urlsafe)
- [ ] `CORS_ORIGINS` (com URL do frontend)

### **Recomendadas:**
- [ ] `ANTHROPIC_API_KEY` (se usar Claude)
- [ ] `DEBUG=False` (em produção)
- [ ] `LOG_LEVEL=INFO` (em produção)

### **Opcionais:**
- [ ] `APP_NAME` e `APP_VERSION`
- [ ] `REDIS_URL` (se usar Celery)
- [ ] `FIRECRAWL_API_KEY` (se usar Firecrawl)
- [ ] `OPENAI_API_KEY` (se usar OpenAI embeddings)

---

## 🔒 Segurança

### **⚠️ NUNCA faça:**
- ❌ Commitar `.env` no Git
- ❌ Compartilhar `SECRET_KEY` publicamente
- ❌ Usar `DEBUG=True` em produção
- ❌ Deixar `CORS_ORIGINS` com `*` em produção

### **✅ SEMPRE faça:**
- ✅ Use variáveis de ambiente do Railway/Render
- ✅ Gere `SECRET_KEY` única e segura
- ✅ Limite `CORS_ORIGINS` apenas às URLs necessárias
- ✅ Use `DEBUG=False` em produção
- ✅ Monitore logs regularmente

---

## 🧪 Testar Variáveis

Após configurar, teste:

```bash
# Health check
curl https://sua-url.railway.app/health

# Root endpoint
curl https://sua-url.railway.app/

# Docs
# Acesse: https://sua-url.railway.app/docs
```

---

## 📚 Referências

- **Railway Variables:** https://docs.railway.app/develop/variables
- **Render Environment:** https://render.com/docs/environment-variables
- **FastAPI Settings:** https://fastapi.tiangolo.com/advanced/settings/
- **Supabase Connection Strings:** https://supabase.com/docs/guides/database/connecting-to-postgres

---

**Pronto!** Todas as variáveis configuradas! 🎉

**Veja também:**
- `DEPLOY-BACKEND.md` - Guia completo de deploy
- `DEPLOY-RAPIDO.md` - Quick start
