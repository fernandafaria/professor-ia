# ⚡ Deploy Rápido do Backend - Quick Start

Guia rápido para fazer deploy do backend em 5 minutos.

---

## 🚀 Railway (Recomendado)

### **1. Criar Conta**
- Acesse: https://railway.app
- Login com GitHub

### **2. Criar Projeto**
- Clique em **"New Project"**
- **"Deploy from GitHub repo"**
- Selecione: `professor-ia`

### **3. Configurar Root Directory**
- Clique no serviço → **Settings**
- **Root Directory:** `backend` ⚠️

### **4. Adicionar Variáveis de Ambiente**

No Railway → **Variables**, adicione:

```env
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
SECRET_KEY=sua-chave-secreta-32-caracteres-minimo
CORS_ORIGINS=https://seu-frontend.vercel.app,http://localhost:3000
ANTHROPIC_API_KEY=sk-ant-sua-chave
DEBUG=False
```

**Gerar SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### **5. Deploy Automático**
- Railway detecta Python automaticamente
- Usa `Procfile` para iniciar
- Deploy inicia automaticamente

### **6. Obter URL**
- Settings → **Networking**
- URL: `https://seu-projeto.up.railway.app`

### **7. Testar**
```bash
curl https://sua-url.railway.app/health
# Deve retornar: {"status": "healthy", "version": "1.0.0"}
```

---

## ✅ Verificar

- [ ] Health check funciona: `/health`
- [ ] Docs funcionam: `/docs`
- [ ] Frontend conecta (atualize `NEXT_PUBLIC_API_URL`)

---

## 📖 Guia Completo

Veja `DEPLOY-BACKEND.md` para instruções detalhadas.

---

**Pronto em ~5 minutos!** 🎉
