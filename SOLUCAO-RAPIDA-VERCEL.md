# ⚡ Solução Rápida: Erro Vercel "No Next.js version detected"

**Problema:** Vercel não encontra o `package.json` do Next.js.

**Causa:** Root Directory não está configurado como `frontend`.

---

## ✅ Solução em 2 Passos

### **Passo 1: No Vercel Dashboard**

1. **Acesse seu projeto no Vercel**
2. **Vá em:** Settings → General
3. **Procure:** "Root Directory"
4. **Clique em:** "Edit"
5. **Configure:** `frontend`
6. **Salve**

### **Passo 2: Redeploy**

1. **Vá em:** Deployments
2. **Clique nos 3 pontinhos** do último deploy
3. **Clique em:** "Redeploy"
4. **Aguarde** o build

---

## ✅ Arquivo vercel.json Criado

O projeto já tem um arquivo `vercel.json` na raiz que configura automaticamente:

```json
{
  "rootDirectory": "frontend",
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/.next",
  "framework": "nextjs"
}
```

**Se o Vercel ainda não detectar:**
- Configure manualmente o Root Directory como `frontend` nas Settings

---

## 🔍 Verificar

Após configurar, o build deve:
- ✅ Encontrar `frontend/package.json`
- ✅ Detectar Next.js
- ✅ Instalar dependências
- ✅ Fazer build com sucesso

---

**Pronto!** Configure Root Directory como `frontend` e faça redeploy! 🚀

Veja guia completo: `CORRIGIR-ERRO-VERCEL.md`
