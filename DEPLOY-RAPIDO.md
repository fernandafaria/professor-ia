# ⚡ Deploy Rápido - 10 Minutos

Guia ultra rápido para colocar sua aplicação no ar.

---

## 🚀 Quick Start

### **Opção 1: Vercel (Frontend) + Railway (Backend)** ⭐

#### **1. Frontend no Vercel (5 min):**

1. **Acesse:** https://vercel.com
2. **Login com GitHub**
3. **"Add New Project"**
4. **Conecte repositório:**
   - Selecione seu repo
   - **Root Directory:** `frontend`
   - **Framework:** Next.js (auto-detect)
5. **Environment Variables:**
   - `NEXT_PUBLIC_API_URL` = `https://seu-backend.railway.app`
   - (Atualize depois do backend)
6. **Deploy!** ✅

**URL:** `https://seu-projeto.vercel.app`

---

#### **2. Backend no Railway (5 min):**

1. **Acesse:** https://railway.app
2. **Login com GitHub**
3. **"New Project"** → **"Deploy from GitHub"**
4. **Configure:**
   - **Root Directory:** `backend`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Environment Variables:**
   - `DATABASE_URL` = (URL do Supabase)
   - `SECRET_KEY` = (sua chave)
   - `CORS_ORIGINS` = `https://seu-projeto.vercel.app`
6. **Deploy!** ✅

**URL:** `https://seu-backend.railway.app`

---

#### **3. Conectar:**

1. **No Vercel:**
   - Settings → Environment Variables
   - Atualize `NEXT_PUBLIC_API_URL` = URL do Railway
   - Redeploy

2. **Teste:**
   - Acesse URL do Vercel
   - ✅ Aplicação online!

---

## 📋 Checklist Rápido

- [ ] Código no GitHub
- [ ] Frontend deployado no Vercel
- [ ] Backend deployado no Railway
- [ ] Variáveis de ambiente configuradas
- [ ] CORS configurado
- [ ] Testado no navegador

---

## 🆘 Problemas Rápidos

**CORS Error?**
→ Adicione URL do frontend em `CORS_ORIGINS` no backend

**Cannot connect?**
→ Verifique `NEXT_PUBLIC_API_URL` no frontend

**Build failed?**
→ Verifique logs na plataforma

---

**Pronto!** Sua aplicação está online! 🎉

Veja guia completo: `DEPLOY-ONLINE.md`
