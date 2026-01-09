# 🚀 Como Fazer Deploy e Testar Online

Guia completo para colocar sua aplicação no ar e testar em ambiente online.

---

## 🎯 Opções de Deploy

### **Opção 1: Vercel (Recomendado para Next.js)** ⭐

**Vantagens:**
- ✅ Gratuito
- ✅ Deploy automático do GitHub
- ✅ Otimizado para Next.js
- ✅ SSL automático
- ✅ CDN global
- ✅ Preview deployments

**Ideal para:** Frontend Next.js

---

### **Opção 2: Railway**

**Vantagens:**
- ✅ Gratuito (com limites)
- ✅ Suporta Python (FastAPI) e Node.js
- ✅ Deploy automático
- ✅ Banco de dados incluído
- ✅ SSL automático

**Ideal para:** Backend FastAPI + Frontend

---

### **Opção 3: Render**

**Vantagens:**
- ✅ Gratuito (com limites)
- ✅ Suporta Python e Node.js
- ✅ Deploy automático
- ✅ SSL automático

**Ideal para:** Backend e Frontend separados

---

### **Opção 4: Supabase (Backend já configurado)**

**Vantagens:**
- ✅ Você já tem Supabase configurado
- ✅ Backend pode usar Supabase Edge Functions
- ✅ Banco de dados já está lá

**Ideal para:** Backend via Supabase

---

## 🚀 Deploy Completo: Vercel (Frontend) + Railway (Backend)

### **Parte 1: Deploy do Frontend no Vercel**

#### **Passo 1: Preparar o Projeto**

1. **Criar arquivo `.env.production`:**

```bash
cd frontend
touch .env.production
```

Adicione (você vai preencher depois do deploy do backend):
```env
NEXT_PUBLIC_API_URL=https://seu-backend.railway.app
```

#### **Passo 2: Criar Conta no Vercel**

1. Acesse: https://vercel.com
2. Clique em **"Sign Up"**
3. Escolha: **"Continue with GitHub"** (recomendado)

#### **Passo 3: Conectar Repositório**

1. **No Vercel Dashboard:**
   - Clique em **"Add New Project"**
   - Conecte seu repositório GitHub (ou faça upload)
   - Selecione o repositório do projeto

2. **Configurar Projeto:**
   - **Root Directory:** `frontend`
   - **Framework Preset:** Next.js (detecta automaticamente)
   - **Build Command:** `npm run build` (automático)
   - **Output Directory:** `.next` (automático)

3. **Variáveis de Ambiente:**
   - Adicione: `NEXT_PUBLIC_API_URL` = `https://seu-backend.railway.app`
   - (Você vai atualizar depois do deploy do backend)

4. **Deploy:**
   - Clique em **"Deploy"**
   - Aguarde alguns minutos
   - ✅ Seu frontend estará online!

**URL será:** `https://seu-projeto.vercel.app`

---

### **Parte 2: Deploy do Backend no Railway**

#### **Passo 1: Preparar o Backend**

1. **Criar arquivo `Procfile` (se não existir):**

```bash
cd backend
touch Procfile
```

Adicione:
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

2. **Atualizar `requirements.txt`:**

Certifique-se de que tem:
```
fastapi
uvicorn[standard]
# ... outras dependências
```

#### **Passo 2: Criar Conta no Railway**

1. Acesse: https://railway.app
2. Clique em **"Start a New Project"**
3. Escolha: **"Login with GitHub"**

#### **Passo 3: Deploy do Backend**

1. **Criar Novo Projeto:**
   - Clique em **"New Project"**
   - Escolha **"Deploy from GitHub repo"**
   - Selecione seu repositório

2. **Configurar:**
   - **Root Directory:** `backend`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Railway detecta Python automaticamente

3. **Variáveis de Ambiente:**
   - Adicione todas as variáveis do `.env`:
     - `DATABASE_URL` (do Supabase)
     - `SECRET_KEY`
     - `CORS_ORIGINS` (adicione a URL do Vercel)
     - Outras variáveis necessárias

4. **Deploy:**
   - Railway faz deploy automaticamente
   - Aguarde alguns minutos
   - ✅ Seu backend estará online!

**URL será:** `https://seu-backend.railway.app`

#### **Passo 4: Atualizar CORS no Backend**

No Railway, adicione variável de ambiente:
```
CORS_ORIGINS=https://seu-projeto.vercel.app,http://localhost:3000
```

---

### **Parte 3: Conectar Frontend e Backend**

1. **No Vercel (Frontend):**
   - Vá em **Settings** → **Environment Variables**
   - Atualize `NEXT_PUBLIC_API_URL` = `https://seu-backend.railway.app`
   - Clique em **"Redeploy"**

2. **Testar:**
   - Acesse: `https://seu-projeto.vercel.app`
   - Verifique se conecta com o backend
   - Teste as funcionalidades

---

## 🎯 Deploy Alternativo: Render

### **Frontend no Render:**

1. **Acesse:** https://render.com
2. **Crie conta** (GitHub login)
3. **New** → **Static Site**
4. **Configure:**
   - **Name:** `p1a-frontend`
   - **Repository:** Seu repositório GitHub
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `frontend/.next`
   - **Environment:** `NEXT_PUBLIC_API_URL=https://seu-backend.onrender.com`

### **Backend no Render:**

1. **New** → **Web Service**
2. **Configure:**
   - **Name:** `p1a-backend`
   - **Repository:** Seu repositório GitHub
   - **Root Directory:** `backend`
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables:** Adicione todas do `.env`

---

## 🔧 Configurações Importantes

### **1. Variáveis de Ambiente**

#### **Frontend (.env.production ou Vercel):**
```env
NEXT_PUBLIC_API_URL=https://seu-backend.railway.app
```

#### **Backend (Railway/Render):**
```env
DATABASE_URL=postgresql://... (do Supabase)
SECRET_KEY=sua-chave-secreta
CORS_ORIGINS=https://seu-frontend.vercel.app,http://localhost:3000
DEBUG=False
```

### **2. CORS no Backend**

Certifique-se de que o backend permite requisições do frontend:

```python
# backend/app/config.py
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
```

### **3. Database URL**

Use a URL do Supabase (já configurada):
- Acesse: Supabase Dashboard → Settings → Database
- Copie a **Connection String**
- Use como `DATABASE_URL` no Railway/Render

---

## 📋 Checklist de Deploy

### **Antes do Deploy:**
- [ ] Código commitado no GitHub
- [ ] `.env.example` criado (sem valores sensíveis)
- [ ] `requirements.txt` atualizado
- [ ] `package.json` atualizado
- [ ] CORS configurado no backend
- [ ] Variáveis de ambiente documentadas

### **Deploy Frontend:**
- [ ] Conta criada no Vercel/Render
- [ ] Repositório conectado
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy realizado
- [ ] URL do frontend anotada

### **Deploy Backend:**
- [ ] Conta criada no Railway/Render
- [ ] Repositório conectado
- [ ] Variáveis de ambiente configuradas (DATABASE_URL, SECRET_KEY, etc.)
- [ ] CORS configurado com URL do frontend
- [ ] Deploy realizado
- [ ] URL do backend anotada

### **Pós-Deploy:**
- [ ] Frontend atualizado com URL do backend
- [ ] Testado no navegador
- [ ] API funcionando (testar endpoints)
- [ ] Sem erros no console
- [ ] Responsivo funcionando

---

## 🧪 Testar Aplicação Online

### **1. Testar Frontend:**

Acesse: `https://seu-projeto.vercel.app`

**Verificar:**
- ✅ Página carrega corretamente
- ✅ Design aparece completo
- ✅ Sem erros no console (F12)
- ✅ Botões funcionam
- ✅ Responsivo (teste em mobile)

### **2. Testar Backend:**

Acesse: `https://seu-backend.railway.app/docs`

**Verificar:**
- ✅ Swagger UI carrega
- ✅ Endpoints aparecem
- ✅ Testar endpoint `/health`
- ✅ Testar endpoint `/api/v1/auth/register`

### **3. Testar Integração:**

1. **No frontend online:**
   - Tente criar conta
   - Tente fazer login
   - Verifique se conecta com backend

2. **Verificar Network:**
   - F12 → Network
   - Veja se requisições vão para o backend correto
   - Verifique se não há erros CORS

---

## 🆘 Problemas Comuns

### ❌ "CORS Error"

**Solução:**
- Verifique `CORS_ORIGINS` no backend
- Adicione URL do frontend (com `https://`)
- Reinicie o backend após mudar

### ❌ "Cannot connect to backend"

**Solução:**
- Verifique `NEXT_PUBLIC_API_URL` no frontend
- Certifique-se de que o backend está rodando
- Verifique se a URL está correta (com `https://`)

### ❌ "Database connection error"

**Solução:**
- Verifique `DATABASE_URL` no backend
- Certifique-se de que a URL do Supabase está correta
- Verifique se o Supabase permite conexões externas

### ❌ "Build failed"

**Solução:**
- Verifique logs de build no Vercel/Railway
- Certifique-se de que `requirements.txt` está completo
- Verifique se não há erros de sintaxe

---

## 💡 Dicas

1. **Use GitHub:**
   - Facilita deploy automático
   - Permite preview deployments
   - Versionamento do código

2. **Variáveis Sensíveis:**
   - Nunca commite `.env` no GitHub
   - Use `.env.example` como template
   - Configure variáveis nas plataformas de deploy

3. **Monitoramento:**
   - Use logs das plataformas para debug
   - Configure alertas se disponível
   - Monitore uso de recursos

4. **Custom Domain (Opcional):**
   - Vercel permite domínio customizado grátis
   - Railway/Render também suportam
   - Configure DNS conforme instruções

---

## 📚 Recursos

- **Vercel Docs:** https://vercel.com/docs
- **Railway Docs:** https://docs.railway.app
- **Render Docs:** https://render.com/docs
- **Supabase Docs:** https://supabase.com/docs

---

## ✅ Resumo Rápido

1. **Frontend (Vercel):**
   - Conecte GitHub → Deploy automático
   - Configure `NEXT_PUBLIC_API_URL`

2. **Backend (Railway):**
   - Conecte GitHub → Deploy automático
   - Configure variáveis de ambiente
   - Configure CORS

3. **Teste:**
   - Acesse URLs geradas
   - Teste funcionalidades
   - Verifique integração

---

**Pronto!** Sua aplicação estará online e acessível de qualquer lugar! 🌐

**Última atualização:** 2026-01-09
