# 🔧 Troubleshooting: Deploy no Railway Não Funciona

Guia completo para resolver problemas comuns no deploy do Railway.

---

## 🚨 Problemas Comuns e Soluções

### **1. Erro: "No Procfile found" ou "No start command"**

**Sintoma:**
```
Error: No Procfile found
```

**Solução:**

1. **Verificar se Procfile existe:**
   ```bash
   cd backend
   ls -la Procfile
   ```

2. **Se não existir, criar:**
   ```bash
   echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
   ```

3. **Verificar conteúdo do Procfile:**
   ```bash
   cat Procfile
   ```
   
   **Deve mostrar:**
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Commit e push:**
   ```bash
   git add Procfile
   git commit -m "fix: adiciona Procfile para Railway"
   git push
   ```

---

### **2. Erro: "Root Directory not found" ou "Module not found"**

**Sintoma:**
```
ModuleNotFoundError: No module named 'app'
```

**Solução:**

1. **No Railway Dashboard:**
   - Clique no serviço
   - Vá em **Settings** (⚙️)
   - Em **"Root Directory"**, digite: `backend`
   - **Salve**

2. **Verificar estrutura:**
   ```bash
   # Deve existir:
   backend/
   ├── Procfile
   ├── runtime.txt
   ├── requirements.txt
   └── app/
       └── main.py
   ```

3. **Redeploy:**
   - No Railway, clique em **"Deploy"** → **"Redeploy"**

---

### **3. Erro: "Python version not found"**

**Sintoma:**
```
Error: Python 3.11 not found
```

**Solução:**

1. **Verificar runtime.txt:**
   ```bash
   cat backend/runtime.txt
   ```
   
   **Deve mostrar:**
   ```
   python-3.11
   ```
   
   **Ou versões suportadas:**
   ```
   python-3.12
   python-3.10
   ```

2. **Se não existir, criar:**
   ```bash
   echo "python-3.11" > backend/runtime.txt
   ```

3. **Commit e push:**
   ```bash
   git add backend/runtime.txt
   git commit -m "fix: adiciona runtime.txt"
   git push
   ```

---

### **4. Erro: "Failed to install dependencies"**

**Sintoma:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solução:**

1. **Verificar requirements.txt:**
   ```bash
   cat backend/requirements.txt
   ```

2. **Problemas comuns:**
   - URLs do GitHub (ex: spacy-models)
   - Versões incompatíveis
   - Dependências muito pesadas (torch, etc.)

3. **Solução temporária - requirements simplificado:**
   
   Crie `requirements-railway.txt` com apenas o essencial:
   ```txt
   fastapi==0.104.1
   uvicorn[standard]==0.24.0
   python-multipart==0.0.6
   sqlalchemy==2.0.23
   alembic==1.12.1
   psycopg2-binary==2.9.9
   pydantic==2.5.0
   pydantic-settings==2.1.0
   python-dotenv==1.0.0
   python-jose[cryptography]==3.3.0
   passlib[bcrypt]==1.7.4
   ```

4. **No Railway:**
   - Settings → Build → Build Command
   - Altere para: `pip install -r requirements-railway.txt`
   - Ou renomeie o arquivo

---

### **5. Erro: "Port already in use" ou "Address already in use"**

**Sintoma:**
```
Error: Address already in use
```

**Solução:**

1. **Verificar Procfile:**
   ```bash
   cat backend/Procfile
   ```
   
   **Deve usar `$PORT`:**
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
   
   **❌ ERRADO:**
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

2. **Corrigir Procfile:**
   ```bash
   echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > backend/Procfile
   ```

3. **Commit e push**

---

### **6. Erro: "DATABASE_URL not found"**

**Sintoma:**
```
Error: DATABASE_URL environment variable not set
```

**Solução:**

1. **No Railway Dashboard:**
   - Clique no serviço
   - Vá em **"Variables"**
   - Verifique se `DATABASE_URL` existe

2. **Adicionar DATABASE_URL:**
   - Clique em **"+ New Variable"**
   - **Key:** `DATABASE_URL`
   - **Value:** Sua URL do Supabase
   - Formato: `postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres`

3. **Verificar outras variáveis obrigatórias:**
   - `SECRET_KEY`
   - `CORS_ORIGINS`

4. **Redeploy após adicionar variáveis**

---

### **7. Erro: "Build timeout" ou "Build taking too long"**

**Sintoma:**
```
Build timeout after 10 minutes
```

**Solução:**

1. **Causa comum:** Dependências pesadas (torch, sentence-transformers)

2. **Solução - Otimizar requirements.txt:**
   
   Remova dependências não essenciais para o MVP:
   ```txt
   # Remover (se não usar RAG ainda):
   # torch==2.1.1
   # sentence-transformers==2.2.2
   # chromadb==0.4.18
   # spacy==3.7.2
   ```

3. **Ou criar requirements-minimal.txt:**
   ```txt
   fastapi==0.104.1
   uvicorn[standard]==0.24.0
   sqlalchemy==2.0.23
   psycopg2-binary==2.9.9
   pydantic==2.5.0
   pydantic-settings==2.1.0
   python-jose[cryptography]==3.3.0
   passlib[bcrypt]==1.7.4
   ```

4. **No Railway:**
   - Settings → Build → Build Command
   - Altere para usar arquivo minimal

---

### **8. Erro: "Health check failed"**

**Sintoma:**
```
Health check failed: Connection refused
```

**Solução:**

1. **Verificar se app está rodando:**
   - Veja logs do Railway
   - Procure por erros de inicialização

2. **Verificar variáveis de ambiente:**
   - `DATABASE_URL` está correta?
   - `SECRET_KEY` está configurada?

3. **Verificar logs:**
   - Railway → Deployments → Clique no último deploy
   - Veja logs completos
   - Procure por erros específicos

---

### **9. Erro: "CORS error" no frontend**

**Sintoma:**
```
Access to fetch at '...' from origin '...' has been blocked by CORS policy
```

**Solução:**

1. **No Railway, adicionar/atualizar CORS_ORIGINS:**
   ```
   CORS_ORIGINS=https://seu-frontend.vercel.app,http://localhost:3000
   ```

2. **Verificar formato:**
   - Separe por vírgula
   - Sem espaços após vírgulas
   - URLs completas com `https://`

3. **Redeploy após atualizar**

---

## 🔍 Como Diagnosticar o Problema

### **Passo 1: Ver Logs do Railway**

1. **No Railway Dashboard:**
   - Clique no serviço
   - Vá em **"Deployments"**
   - Clique no último deploy (que falhou)
   - Veja logs completos

2. **Procurar por:**
   - Erros em vermelho
   - Mensagens de "Error", "Failed", "Exception"
   - Últimas linhas dos logs

### **Passo 2: Verificar Configurações**

1. **Root Directory:**
   - Settings → Root Directory = `backend`

2. **Start Command:**
   - Settings → Deploy → Start Command
   - Deve estar vazio (usa Procfile) OU
   - `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Build Command:**
   - Settings → Deploy → Build Command
   - Deve estar vazio (auto) OU
   - `pip install -r requirements.txt`

### **Passo 3: Verificar Variáveis**

1. **Variables:**
   - Verifique se todas as obrigatórias estão configuradas:
     - `DATABASE_URL`
     - `SECRET_KEY`
     - `CORS_ORIGINS`

2. **Valores corretos:**
   - `DATABASE_URL` começa com `postgresql://`
   - `SECRET_KEY` tem 32+ caracteres
   - `CORS_ORIGINS` tem URLs válidas

---

## ✅ Checklist de Verificação

Antes de tentar deploy novamente:

- [ ] `Procfile` existe em `backend/Procfile`
- [ ] `runtime.txt` existe em `backend/runtime.txt`
- [ ] `requirements.txt` existe e está atualizado
- [ ] Root Directory configurado como `backend` no Railway
- [ ] `DATABASE_URL` configurada no Railway
- [ ] `SECRET_KEY` configurada no Railway
- [ ] `CORS_ORIGINS` configurada no Railway
- [ ] Código commitado e no GitHub
- [ ] Railway conectado ao repositório correto

---

## 🚀 Deploy Limpo (Reset)

Se nada funcionar, tente deploy limpo:

1. **No Railway:**
   - Delete o serviço atual
   - Crie novo serviço
   - Conecte ao mesmo repositório
   - Configure Root Directory: `backend`
   - Adicione todas as variáveis
   - Deploy

2. **Ou via CLI:**
   ```bash
   railway login
   railway init
   railway link
   railway up
   ```

---

## 📝 Logs Úteis para Compartilhar

Se precisar de ajuda, compartilhe:

1. **Últimas linhas dos logs do Railway**
2. **Configurações:**
   - Root Directory
   - Start Command
   - Build Command
3. **Variáveis configuradas** (sem valores sensíveis)
4. **Estrutura do projeto:**
   ```bash
   tree backend -L 2
   ```

---

## 🆘 Ainda Não Funciona?

1. **Verifique logs completos** no Railway
2. **Teste localmente primeiro:**
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
3. **Se funcionar localmente, problema é configuração do Railway**
4. **Se não funcionar localmente, problema é código**

---

## 📚 Referências

- **Railway Docs:** https://docs.railway.app
- **Railway Troubleshooting:** https://docs.railway.app/help
- **FastAPI Deploy:** https://fastapi.tiangolo.com/deployment/

---

**Compartilhe os logs do Railway para diagnóstico mais específico!** 🔍
