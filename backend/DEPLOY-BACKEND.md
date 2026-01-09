# 🚀 Deploy do Backend FastAPI - Guia Completo

Guia passo a passo para fazer deploy do backend FastAPI da plataforma P1A.

---

## 📋 Pré-requisitos

- [x] Backend FastAPI configurado
- [x] `Procfile` criado
- [x] `requirements.txt` atualizado
- [x] `runtime.txt` com versão Python
- [x] Variáveis de ambiente configuradas
- [x] Banco de dados Supabase configurado

---

## 🎯 Opções de Deploy

### **Opção 1: Railway (Recomendado)** ⭐

**Vantagens:**
- ✅ Gratuito (com limites generosos)
- ✅ Deploy automático do GitHub
- ✅ Suporta Python/FastAPI nativamente
- ✅ SSL automático
- ✅ Variáveis de ambiente fáceis
- ✅ Logs em tempo real

**Ideal para:** Produção rápida e fácil

---

### **Opção 2: Render**

**Vantagens:**
- ✅ Gratuito (com limites)
- ✅ Deploy automático
- ✅ SSL automático
- ✅ Banco de dados incluído (opcional)

**Ideal para:** Alternativa ao Railway

---

### **Opção 3: Fly.io**

**Vantagens:**
- ✅ Gratuito (com limites)
- ✅ Performance global
- ✅ Deploy via CLI

**Ideal para:** Produção com múltiplas regiões

---

## 🚀 Deploy no Railway (Recomendado)

### **Passo 1: Verificar Arquivos de Deploy**

Certifique-se de que existem:

**1. `Procfile` (raiz do backend/):**
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**2. `runtime.txt` (raiz do backend/):**
```
python-3.11
```

**3. `requirements.txt` (raiz do backend/):**
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
# ... outras dependências
```

---

### **Passo 2: Criar Conta no Railway**

1. **Acesse:** https://railway.app
2. **Clique em:** "Start a New Project"
3. **Escolha:** "Login with GitHub" (recomendado)
4. **Autorize** Railway a acessar seu GitHub

---

### **Passo 3: Criar Novo Projeto**

1. **No Dashboard do Railway:**
   - Clique em **"New Project"**
   - Escolha **"Deploy from GitHub repo"**
   - Selecione o repositório: `professor-ia` (ou nome do seu repo)
   - Autorize Railway a acessar o repositório

2. **Railway vai detectar o projeto:**
   - Pode detectar automaticamente como Python
   - Se não detectar, clique em **"Configure"**

---

### **Passo 4: Configurar Serviço**

1. **Railway detecta automaticamente:**
   - Framework: Python
   - Build Command: Instala dependências automaticamente
   - Start Command: Detecta `Procfile`

2. **Configurar Root Directory:**
   - Clique em **"Settings"** (⚙️)
   - Em **"Root Directory"**, digite: `backend`
   - Isso é **CRÍTICO** para monorepo!

3. **Configurar Start Command (se necessário):**
   - Clique em **"Settings"** → **"Deploy"**
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Ou deixe vazio (usa Procfile)

---

### **Passo 5: Configurar Variáveis de Ambiente**

**⚠️ IMPORTANTE:** Configure TODAS as variáveis antes do primeiro deploy!

1. **No projeto Railway:**
   - Clique em **"Variables"** (ou clique no serviço → **"Variables"**)

2. **Adicione as variáveis necessárias:**

```env
# App
APP_NAME=Plataforma Educacional P1A
APP_VERSION=1.0.0
DEBUG=False

# Banco de Dados Supabase
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres

# JWT / Autenticação
SECRET_KEY=sua-chave-secreta-aqui-minimo-32-caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS (adicione a URL do frontend Vercel)
CORS_ORIGINS=https://seu-frontend.vercel.app,http://localhost:3000

# Anthropic Claude API
ANTHROPIC_API_KEY=sk-ant-sua-chave-anthropic
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# RAG (opcional)
RAG_TABLE_NAME=rag_documents
EMBEDDING_DIMENSION=384
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

# Logging
LOG_LEVEL=INFO
```

**💡 Dica:** Para gerar uma SECRET_KEY segura:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**🔒 Como obter DATABASE_URL do Supabase:**
1. Acesse: https://app.supabase.com
2. Vá em: **Project Settings** → **Database**
3. Em **Connection String**, copie a **URI**
4. Formato: `postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres`

---

### **Passo 6: Fazer Deploy**

1. **Railway inicia o deploy automaticamente:**
   - Após adicionar as variáveis, o deploy inicia
   - Ou clique em **"Deploy"** → **"Redeploy"**

2. **Acompanhar o build:**
   - Clique no serviço
   - Vá em **"Deployments"**
   - Veja os logs em tempo real

3. **Aguardar:**
   - Primeiro deploy: 3-5 minutos
   - Instala dependências
   - Faz build
   - Inicia servidor

---

### **Passo 7: Obter URL do Backend**

1. **No Railway:**
   - Clique no serviço
   - Vá em **"Settings"** → **"Networking"**
   - Ou clique em **"Generate Domain"**

2. **Railway gera automaticamente:**
   - URL será algo como: `https://seu-projeto-production.up.railway.app`
   - Ou pode configurar domínio customizado

3. **Testar:**
   - Acesse: `https://sua-url.railway.app/health`
   - Deve retornar: `{"status": "healthy", "version": "1.0.0"}`
   - Acesse: `https://sua-url.railway.app/docs`
   - Deve abrir a documentação Swagger do FastAPI

---

### **Passo 8: Configurar CORS para Frontend**

1. **Adicionar URL do Frontend:**
   - No Railway, vá em **"Variables"**
   - Atualize `CORS_ORIGINS`:
   ```
   CORS_ORIGINS=https://seu-frontend.vercel.app,https://seu-frontend.vercel.app,http://localhost:3000
   ```

2. **Redeploy:**
   - Clique em **"Deploy"** → **"Redeploy"**
   - Ou Railway faz automaticamente ao atualizar variáveis

---

## 🚀 Deploy no Render (Alternativa)

### **Passo 1: Criar Conta**

1. **Acesse:** https://render.com
2. **Clique em:** "Get Started for Free"
3. **Escolha:** "Sign Up with GitHub"

---

### **Passo 2: Criar Web Service**

1. **No Dashboard:**
   - Clique em **"New +"**
   - Escolha **"Web Service"**

2. **Conectar Repositório:**
   - Conecte com GitHub
   - Selecione o repositório: `professor-ia`

---

### **Passo 3: Configurar**

**Settings:**
- **Name:** `p1a-backend` (ou nome desejado)
- **Region:** Escolha mais próxima (ex: `Oregon (US West)`)
- **Branch:** `main`
- **Root Directory:** `backend` ⚠️ **IMPORTANTE!**
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Environment:**
- Adicione todas as variáveis de ambiente (mesmas do Railway)
- Clique em **"Add Environment Variable"** para cada uma

---

### **Passo 4: Deploy**

1. **Clique em:** "Create Web Service"
2. **Render faz deploy automaticamente**
3. **Aguarde:** 3-5 minutos
4. **URL será:** `https://p1a-backend.onrender.com`

---

## 🔍 Verificar Deploy

### **1. Health Check**

```bash
curl https://sua-url.railway.app/health
```

**Deve retornar:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

### **2. Root Endpoint**

```bash
curl https://sua-url.railway.app/
```

**Deve retornar:**
```json
{
  "name": "Plataforma Educacional P1A",
  "version": "1.0.0",
  "status": "running",
  "docs": "/docs"
}
```

### **3. Documentação Swagger**

Acesse: `https://sua-url.railway.app/docs`

Deve abrir a interface Swagger com todos os endpoints.

---

## 🔧 Troubleshooting

### **Erro: "No module named 'app'"**

**Solução:**
- Verifique se **Root Directory** está configurado como `backend`
- Verifique se `requirements.txt` está na raiz do `backend/`

### **Erro: "DATABASE_URL not found"**

**Solução:**
- Verifique se a variável `DATABASE_URL` foi adicionada no Railway/Render
- Verifique se o formato está correto (começa com `postgresql://`)

### **Erro: "Port already in use"**

**Solução:**
- Certifique-se de usar `$PORT` no comando start
- Railway/Render fornece a porta via variável `$PORT`

### **Erro: CORS bloqueado**

**Solução:**
- Adicione a URL do frontend em `CORS_ORIGINS`
- Formato: `https://seu-frontend.vercel.app,http://localhost:3000`
- Faça redeploy após atualizar

### **Build lento no primeiro deploy**

**Normal:** O primeiro deploy é mais lento porque:
- Instala todas as dependências do Python
- Pode baixar modelos grandes (se usar sentence-transformers)
- Aguarde 5-10 minutos no primeiro deploy

---

## 📝 Checklist de Deploy

- [ ] `Procfile` criado e correto
- [ ] `runtime.txt` com versão Python
- [ ] `requirements.txt` atualizado
- [ ] Root Directory configurado como `backend`
- [ ] `DATABASE_URL` configurada (Supabase)
- [ ] `SECRET_KEY` gerada e configurada
- [ ] `CORS_ORIGINS` configurada com URL do frontend
- [ ] `ANTHROPIC_API_KEY` configurada (se usar Claude)
- [ ] Deploy realizado com sucesso
- [ ] Health check funcionando (`/health`)
- [ ] Documentação acessível (`/docs`)
- [ ] Frontend conectando com backend

---

## 🎯 Próximos Passos

Após deploy do backend:

1. **Atualizar Frontend:**
   - No Vercel, atualize `NEXT_PUBLIC_API_URL` com a URL do backend
   - Exemplo: `https://seu-backend.railway.app`

2. **Testar Integração:**
   - Acesse o frontend
   - Teste login/registro
   - Verifique se API está respondendo

3. **Monitorar:**
   - Use logs do Railway/Render para debug
   - Monitore health checks
   - Configure alertas se necessário

---

## 📚 Referências

- **Railway Docs:** https://docs.railway.app
- **Render Docs:** https://render.com/docs
- **FastAPI Deploy:** https://fastapi.tiangolo.com/deployment/
- **Supabase Docs:** https://supabase.com/docs

---

**Pronto!** Seu backend está deployado! 🎉

**Veja também:**
- `DEPLOY-ONLINE.md` - Guia geral de deploy
- `DEPLOY-RAPIDO.md` - Quick start
- `../VERCEL-DEPLOY.md` - Deploy do frontend
