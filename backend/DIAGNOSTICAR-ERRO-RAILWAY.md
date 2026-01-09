# 🔍 Diagnosticar Erro no Railway - Passo a Passo

Guia rápido para identificar e resolver o problema específico do seu deploy.

---

## 🚨 Passo 1: Ver os Logs do Railway

**O mais importante é ver os logs!**

1. **Acesse:** https://railway.app
2. **Entre no seu projeto**
3. **Clique no serviço do backend**
4. **Vá em "Deployments"** (ou "Deploys")
5. **Clique no último deploy** (que falhou)
6. **Veja os logs completos**

**Procure por:**
- ❌ Mensagens em **vermelho**
- ❌ Palavras: "Error", "Failed", "Exception", "ModuleNotFound"
- ❌ Últimas 20-30 linhas dos logs

**Copie as últimas linhas dos logs e me envie!**

---

## 🔍 Passo 2: Verificar Configurações Básicas

### **A. Root Directory**

1. **No Railway:**
   - Clique no serviço → **Settings** (⚙️)
   - Procure por **"Root Directory"**
   - **Deve estar:** `backend`
   - Se estiver vazio ou diferente, **corrija!**

### **B. Start Command**

1. **No Railway:**
   - Settings → **Deploy**
   - Procure por **"Start Command"**
   - **Deve estar vazio** (usa Procfile) OU
   - `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### **C. Build Command**

1. **No Railway:**
   - Settings → **Deploy**
   - Procure por **"Build Command"**
   - **Deve estar vazio** (auto) OU
   - `pip install -r requirements.txt`

---

## 🔍 Passo 3: Verificar Arquivos

### **Verificar localmente:**

```bash
cd backend

# Verificar se Procfile existe
ls -la Procfile
cat Procfile
# Deve mostrar: web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

# Verificar se runtime.txt existe
ls -la runtime.txt
cat runtime.txt
# Deve mostrar: python-3.11

# Verificar se requirements.txt existe
ls -la requirements.txt
head -5 requirements.txt
# Deve mostrar dependências do FastAPI
```

---

## 🔍 Passo 4: Verificar Variáveis de Ambiente

1. **No Railway:**
   - Clique no serviço → **Variables**
   - Verifique se existem:

**Obrigatórias:**
- [ ] `DATABASE_URL` (formato: `postgresql://...`)
- [ ] `SECRET_KEY` (32+ caracteres)
- [ ] `CORS_ORIGINS` (URLs separadas por vírgula)

**Se faltar alguma, adicione!**

---

## 🐛 Erros Mais Comuns

### **Erro 1: "No Procfile found"**

**Solução:**
```bash
cd backend
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
git add Procfile
git commit -m "fix: adiciona Procfile"
git push
```

### **Erro 2: "ModuleNotFoundError: No module named 'app'"**

**Solução:**
- No Railway → Settings → Root Directory = `backend`
- Redeploy

### **Erro 3: "DATABASE_URL not found"**

**Solução:**
- No Railway → Variables → Add Variable
- Key: `DATABASE_URL`
- Value: Sua URL do Supabase
- Redeploy

### **Erro 4: "Build timeout" ou "Build taking too long"**

**Causa:** Dependências muito pesadas (torch, sentence-transformers)

**Solução temporária:**
- Criar `requirements-minimal.txt` com apenas o essencial
- No Railway → Settings → Build Command
- Altere para: `pip install -r requirements-minimal.txt`

---

## 📋 Checklist Rápido

Antes de tentar deploy novamente:

- [ ] Root Directory = `backend` no Railway
- [ ] `Procfile` existe e está correto
- [ ] `runtime.txt` existe
- [ ] `requirements.txt` existe
- [ ] `DATABASE_URL` configurada
- [ ] `SECRET_KEY` configurada
- [ ] `CORS_ORIGINS` configurada
- [ ] Código commitado e no GitHub
- [ ] Logs do Railway verificados

---

## 🆘 Ainda Não Funciona?

**Me envie:**

1. **Últimas 30 linhas dos logs do Railway** (copie e cole)
2. **Screenshot das configurações:**
   - Root Directory
   - Start Command
   - Build Command
3. **Lista de variáveis** configuradas (sem valores sensíveis)
4. **Estrutura do projeto:**
   ```bash
   tree backend -L 2
   ```

Com essas informações, consigo identificar o problema específico!

---

## 🚀 Teste Local Primeiro

Antes de tentar deploy no Railway, teste localmente:

```bash
cd backend

# Instalar dependências
pip install -r requirements.txt

# Testar se app inicia
uvicorn app.main:app --reload
```

**Se funcionar localmente:**
- Problema é configuração do Railway

**Se não funcionar localmente:**
- Problema é código/dependências

---

## 📚 Guias Relacionados

- **Troubleshooting Completo:** `TROUBLESHOOTING-RAILWAY.md`
- **Deploy Rápido:** `DEPLOY-RAPIDO.md`
- **Deploy Completo:** `DEPLOY-BACKEND.md`

---

**Compartilhe os logs do Railway para diagnóstico específico!** 🔍
