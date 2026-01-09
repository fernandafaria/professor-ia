# 🚀 Deploy no Vercel - Passo a Passo

Guia específico para fazer deploy do frontend Next.js no Vercel.

---

## ✅ Pré-requisitos

- [ ] Código no GitHub (ou GitLab/Bitbucket)
- [ ] Conta no Vercel (gratuita)
- [ ] Backend deployado (Railway/Render) - para ter a URL da API

---

## 📋 Passo a Passo

### **1. Preparar o Projeto**

Certifique-se de que o `frontend/package.json` tem os scripts corretos:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

### **2. Criar Conta no Vercel**

1. Acesse: https://vercel.com
2. Clique em **"Sign Up"**
3. Escolha **"Continue with GitHub"** (recomendado)
4. Autorize o Vercel a acessar seus repositórios

### **3. Conectar Repositório**

1. **No Dashboard do Vercel:**
   - Clique em **"Add New..."** → **"Project"**
   - Ou clique em **"Import Project"**

2. **Selecione seu repositório:**
   - Se não aparecer, clique em **"Adjust GitHub App Permissions"**
   - Selecione o repositório do projeto

3. **Configure o Projeto:**
   
   **Project Settings:**
   - **Project Name:** `p1a-frontend` (ou o nome que preferir)
   - **Framework Preset:** Next.js (detecta automaticamente)
   - **Root Directory:** `frontend` ⚠️ **IMPORTANTE!** (deve apontar para pasta frontend/)
   - **Build Command:** `npm run build` (automático após configurar Root Directory)
   - **Output Directory:** `.next` (automático)
   - **Install Command:** `npm install` (automático)
   
   **OU use o arquivo vercel.json:**
   - O projeto já tem `vercel.json` na raiz
   - Ele configura automaticamente o Root Directory como `frontend`
   - O Vercel deve detectar automaticamente

### **4. Configurar Variáveis de Ambiente**

**Antes de fazer deploy, configure:**

1. **Na seção "Environment Variables":**
   - Clique em **"Add"**
   - **Name:** `NEXT_PUBLIC_API_URL`
   - **Value:** `https://seu-backend.railway.app` (ou URL do seu backend)
   - **Environment:** Production, Preview, Development (marque todos)

2. **Se tiver mais variáveis:**
   - Adicione todas as que começam com `NEXT_PUBLIC_`
   - Exemplo: `NEXT_PUBLIC_SUPABASE_URL` (se usar)

### **5. Fazer Deploy**

1. **Clique em "Deploy"**
2. **Aguarde o build:**
   - Vercel vai instalar dependências
   - Executar `npm run build`
   - Fazer deploy
   - ⏱️ Geralmente leva 2-5 minutos

3. **Quando terminar:**
   - ✅ Você verá "Congratulations! Your project has been deployed"
   - **URL:** `https://seu-projeto.vercel.app`

### **6. Testar**

1. **Acesse a URL:**
   - Exemplo: `https://p1a-frontend.vercel.app`
   - Verifique se a página carrega

2. **Teste funcionalidades:**
   - Navegação
   - Botões
   - Conexão com backend (se já deployado)

3. **Verifique Console:**
   - F12 → Console
   - Veja se há erros
   - Verifique se API calls funcionam

---

## 🔄 Atualizações Automáticas

**O Vercel faz deploy automático quando você:**

1. **Faz push no GitHub:**
   - Push para `main` → Deploy em produção
   - Push para outras branches → Preview deployment

2. **Preview Deployments:**
   - Cada PR/branch tem sua própria URL
   - Útil para testar antes de merge

---

## ⚙️ Configurações Avançadas

### **Custom Domain (Opcional):**

1. **No Vercel:**
   - Settings → Domains
   - Adicione seu domínio
   - Configure DNS conforme instruções

### **Environment Variables por Ambiente:**

- **Production:** Variáveis para produção
- **Preview:** Variáveis para preview deployments
- **Development:** Variáveis para `vercel dev`

### **Build Settings:**

Se precisar ajustar:

1. **Settings → General → Build & Development Settings**
2. **Override:**
   - Build Command
   - Output Directory
   - Install Command

---

## 🆘 Problemas Comuns

### ❌ "Build Failed"

**Solução:**
1. Veja os logs de build no Vercel
2. Verifique erros de TypeScript/ESLint
3. Certifique-se de que todas as dependências estão em `package.json`

### ❌ "Cannot find module"

**Solução:**
- Verifique se `node_modules` não está no `.gitignore` (não deve estar)
- Verifique se todas as dependências estão em `package.json`
- Tente limpar cache: Settings → Clear Build Cache

### ❌ "API calls não funcionam"

**Solução:**
- Verifique `NEXT_PUBLIC_API_URL` nas variáveis de ambiente
- Certifique-se de que o backend está online
- Verifique CORS no backend

### ❌ "404 em rotas"

**Solução:**
- Next.js App Router funciona automaticamente
- Verifique se as rotas estão em `app/`
- Verifique se não há erros de build

---

## 📊 Monitoramento

### **Analytics (Opcional):**

1. **Settings → Analytics**
2. **Ative Vercel Analytics** (gratuito)
3. Veja métricas de performance

### **Logs:**

1. **Deployments → Selecione um deploy → Logs**
2. Veja logs de build e runtime
3. Útil para debug

---

## ✅ Checklist Final

- [ ] Código commitado no GitHub
- [ ] Conta Vercel criada
- [ ] Repositório conectado
- [ ] Root Directory: `frontend`
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy realizado
- [ ] URL funcionando
- [ ] Testado no navegador
- [ ] Sem erros no console

---

## 🎯 Próximos Passos

1. **Deploy do Backend:**
   - Veja: `DEPLOY-ONLINE.md` → Seção Railway/Render

2. **Atualizar Frontend:**
   - Atualize `NEXT_PUBLIC_API_URL` com URL do backend
   - Redeploy no Vercel

3. **Testar Integração:**
   - Teste criar conta
   - Teste login
   - Verifique se tudo funciona

---

**Pronto!** Seu frontend está online no Vercel! 🎉

**URL:** `https://seu-projeto.vercel.app`

---

**Última atualização:** 2026-01-09
