# ✅ Checklist Pré-Deploy

Verifique tudo antes de fazer deploy online.

---

## 📋 Antes do Deploy

### **1. Código no Git**

- [ ] Código commitado no GitHub/GitLab
- [ ] `.gitignore` configurado (não commitar `.env`)
- [ ] `.env.example` criado (template sem valores sensíveis)
- [ ] README atualizado (opcional)

### **2. Frontend (Next.js)**

- [ ] `package.json` com scripts corretos:
  ```json
  {
    "scripts": {
      "build": "next build",
      "start": "next start"
    }
  }
  ```
- [ ] `.env.example` criado
- [ ] Build funciona localmente: `npm run build`
- [ ] Sem erros de TypeScript/ESLint
- [ ] Variáveis de ambiente documentadas

### **3. Backend (FastAPI)**

- [ ] `requirements.txt` atualizado com todas as dependências
- [ ] `Procfile` criado (para Railway/Render)
- [ ] `runtime.txt` criado (versão Python, se necessário)
- [ ] `.env.example` criado
- [ ] CORS configurado para aceitar URL do frontend
- [ ] `DATABASE_URL` do Supabase anotada
- [ ] `SECRET_KEY` gerada (não commitar!)

### **4. Variáveis de Ambiente**

#### **Frontend:**
- [ ] `NEXT_PUBLIC_API_URL` (URL do backend)

#### **Backend:**
- [ ] `DATABASE_URL` (do Supabase)
- [ ] `SECRET_KEY` (chave secreta para JWT)
- [ ] `CORS_ORIGINS` (URLs permitidas, separadas por vírgula)
- [ ] `ANTHROPIC_API_KEY` (se usar Claude)
- [ ] Outras variáveis necessárias

---

## 🧪 Testes Locais

### **Frontend:**
- [ ] `npm run build` funciona sem erros
- [ ] `npm run dev` funciona
- [ ] Página carrega corretamente
- [ ] Sem erros no console

### **Backend:**
- [ ] `uvicorn app.main:app` funciona
- [ ] API responde em `/health`
- [ ] Swagger UI funciona em `/docs`
- [ ] Conexão com banco funciona

### **Integração:**
- [ ] Frontend conecta com backend local
- [ ] Teste de registro/login funciona
- [ ] Sem erros CORS

---

## 📝 Arquivos Necessários

### **Frontend:**
- [ ] `package.json`
- [ ] `.env.example`
- [ ] `next.config.js` (se houver configurações)

### **Backend:**
- [ ] `requirements.txt`
- [ ] `Procfile` (para Railway/Render)
- [ ] `runtime.txt` (opcional, para versão Python específica)
- [ ] `.env.example`

---

## 🔒 Segurança

- [ ] `.env` não está no Git (verificar `.gitignore`)
- [ ] `SECRET_KEY` não está no código
- [ ] `DATABASE_URL` não está no código
- [ ] API keys não estão no código
- [ ] CORS configurado corretamente

---

## 📚 Documentação

- [ ] Variáveis de ambiente documentadas
- [ ] Instruções de deploy documentadas
- [ ] URLs de produção anotadas

---

## ✅ Após Deploy

- [ ] Frontend acessível online
- [ ] Backend acessível online
- [ ] Frontend conecta com backend
- [ ] Teste de funcionalidades básicas
- [ ] Sem erros no console
- [ ] Responsivo funcionando

---

## 🆘 Se Algo Der Errado

1. **Verifique logs:**
   - Vercel: Deployments → Logs
   - Railway: Deploy Logs

2. **Verifique variáveis de ambiente:**
   - Certifique-se de que todas estão configuradas
   - Verifique se valores estão corretos

3. **Verifique CORS:**
   - Backend deve permitir URL do frontend
   - Verifique formato (com `https://`)

4. **Verifique build:**
   - Teste build localmente primeiro
   - Corrija erros antes de deploy

---

**Tudo verificado?** Pronto para deploy! 🚀

Veja: `DEPLOY-RAPIDO.md` para começar.
