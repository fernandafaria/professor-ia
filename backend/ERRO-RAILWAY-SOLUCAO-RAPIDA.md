# ⚡ Solução Rápida: Deploy Não Funciona no Railway

**Guia de 2 minutos para resolver o problema mais comum.**

---

## 🎯 Problema Mais Comum: Root Directory

**90% dos problemas são isso!**

### **Solução em 30 segundos:**

1. **No Railway Dashboard:**
   - Clique no serviço do backend
   - Vá em **Settings** (⚙️)
   - Procure **"Root Directory"**
   - **Digite:** `backend`
   - **Salve**

2. **Redeploy:**
   - Clique em **"Deploy"** → **"Redeploy"**

**Pronto!** Isso resolve a maioria dos problemas.

---

## 🔍 Se Ainda Não Funcionar

### **Passo 1: Ver Logs**

1. Railway → Serviço → **Deployments**
2. Clique no último deploy
3. Veja as últimas 20-30 linhas
4. **Procure por erros em vermelho**

### **Passo 2: Verificar Variáveis**

Railway → Serviço → **Variables**

**Deve ter:**
- ✅ `DATABASE_URL` (obrigatória)
- ✅ `SECRET_KEY` (obrigatória)
- ✅ `CORS_ORIGINS` (obrigatória)

**Se faltar, adicione!**

---

## 🐛 Erros Específicos

### **"No Procfile found"**
```bash
cd backend
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
git add Procfile && git commit -m "fix: Procfile" && git push
```

### **"ModuleNotFoundError: No module named 'app'"**
- Root Directory = `backend` no Railway

### **"DATABASE_URL not found"**
- Adicione variável `DATABASE_URL` no Railway

### **"Build timeout"**
- Dependências muito pesadas
- Veja: `TROUBLESHOOTING-RAILWAY.md`

---

## ✅ Checklist Rápido

- [ ] Root Directory = `backend` no Railway
- [ ] `DATABASE_URL` configurada
- [ ] `SECRET_KEY` configurada
- [ ] `CORS_ORIGINS` configurada
- [ ] Logs verificados (últimas 30 linhas)

---

## 🆘 Ainda Não Funciona?

**Me envie:**
1. Últimas 30 linhas dos logs do Railway
2. Screenshot do Root Directory
3. Lista de variáveis (sem valores)

**Veja guias completos:**
- `DIAGNOSTICAR-ERRO-RAILWAY.md` - Diagnóstico passo a passo
- `TROUBLESHOOTING-RAILWAY.md` - Soluções completas

---

**99% dos problemas são Root Directory!** Verifique primeiro! 🎯
