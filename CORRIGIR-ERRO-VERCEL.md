# 🔧 Corrigir Erro: "No Next.js version detected" no Vercel

O erro ocorre porque o Vercel não está encontrando o `package.json` do Next.js. Isso acontece quando o **Root Directory** não está configurado corretamente.

---

## ❌ Erro

```
No Next.js version detected. Make sure your package.json has "next" in either 
"dependencies" or "devDependencies". Also check your Root Directory setting 
matches the directory of your package.json file.
```

---

## ✅ Solução: Configurar Root Directory no Vercel

### **Passo 1: Acessar Configurações do Projeto**

1. **No Vercel Dashboard:**
   - Acesse seu projeto: https://vercel.com/dashboard
   - Clique no projeto `professor-ia` (ou nome que você deu)

2. **Vá em Settings:**
   - Clique em **"Settings"** (no menu superior)
   - Ou acesse diretamente: Settings → General

### **Passo 2: Configurar Root Directory**

1. **Na seção "General":**
   - Procure por **"Root Directory"**
   - Clique em **"Edit"**

2. **Configure:**
   - **Root Directory:** `frontend`
   - Clique em **"Save"**

3. **Importante:**
   - O Vercel vai procurar `package.json` em `frontend/package.json`
   - Certifique-se de que o caminho está correto

### **Passo 3: Verificar Build Settings**

1. **Na mesma página (Settings → General):**
   - Procure por **"Build & Development Settings"**
   - Clique em **"Override"** (se necessário)

2. **Verifique:**
   - **Framework Preset:** Next.js (deve detectar automaticamente)
   - **Build Command:** `npm run build` (ou deixe vazio para auto-detect)
   - **Output Directory:** `.next` (ou deixe vazio para auto-detect)
   - **Install Command:** `npm install` (ou deixe vazio para auto-detect)

3. **Salve as configurações**

### **Passo 4: Fazer Redeploy**

1. **No Vercel Dashboard:**
   - Vá em **"Deployments"**
   - Clique nos **3 pontinhos** do último deploy
   - Clique em **"Redeploy"**
   - Ou crie um novo deploy

2. **Aguarde o build:**
   - O Vercel vai:
     - Instalar dependências em `frontend/`
     - Executar `npm run build`
     - Fazer deploy

---

## 🔍 Verificar Configuração

### **No Vercel, verifique:**

1. **Root Directory:** `frontend` ✅
2. **Framework:** Next.js ✅
3. **Build Command:** `npm run build` (ou auto) ✅
4. **Output Directory:** `.next` (ou auto) ✅

### **No seu repositório, verifique:**

```bash
# O package.json deve estar em:
frontend/package.json

# E deve conter:
{
  "dependencies": {
    "next": "^14.0.0",
    ...
  }
}
```

---

## 🆘 Se Ainda Não Funcionar

### **Opção 1: Criar vercel.json na Raiz**

Crie um arquivo `vercel.json` na raiz do projeto:

```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/.next",
  "installCommand": "cd frontend && npm install",
  "framework": "nextjs",
  "rootDirectory": "frontend"
}
```

### **Opção 2: Mover package.json para Raiz (NÃO RECOMENDADO)**

Se quiser manter tudo na raiz, você precisaria:
- Mover `frontend/package.json` para raiz
- Ajustar todos os paths
- Mais complexo, não recomendado

**Melhor solução:** Configurar Root Directory no Vercel (Passo 2 acima)

---

## 📋 Checklist de Correção

- [ ] Root Directory configurado como `frontend` no Vercel
- [ ] Build Settings verificados
- [ ] Redeploy realizado
- [ ] Build funcionando sem erros
- [ ] Deploy bem-sucedido

---

## ✅ Após Corrigir

Quando o build funcionar, você verá:

```
✓ Build completed successfully
✓ Deployed to https://seu-projeto.vercel.app
```

**Acesse a URL** e verifique se a aplicação está funcionando!

---

## 📚 Referências

- **Vercel Docs - Root Directory:** https://vercel.com/docs/projects/configuration#root-directory
- **Vercel Docs - Build Settings:** https://vercel.com/docs/projects/configuration#build-settings

---

**Solução:** Configure **Root Directory: `frontend`** nas Settings do Vercel! 🚀
