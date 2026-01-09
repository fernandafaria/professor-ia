# ⚡ Solução: Build Timed Out no Railway

**Problema:** Build no Railway está demorando mais de 10-15 minutos e timeout

**Causa:** Dependências muito pesadas (torch ~2GB, spacy 568MB, etc.)

**Solução:** Usar `requirements-minimal.txt` sem dependências pesadas

---

## 🚀 Solução Rápida (2 minutos)

### **Passo 1: Configurar Build Command no Railway**

1. **No Railway Dashboard:**
   - Clique no serviço do backend
   - Vá em **Settings** (⚙️)
   - Clique em **"Deploy"** (ou procure "Build & Deploy")

2. **Configurar Build Command:**
   - Procure por **"Build Command"**
   - **Substitua** (se houver algo) por:
   ```
   pip install -r requirements-minimal.txt
   ```
   - Ou deixe vazio se já estiver usando requirements.txt automaticamente

3. **Alternativa - Renomear arquivo:**
   - No Railway, você pode também renomear temporariamente:
   - `requirements.txt` → `requirements-full.txt`
   - `requirements-minimal.txt` → `requirements.txt`
   - Commit e push

---

### **Passo 2: Redeploy**

1. **No Railway:**
   - Clique em **"Deploy"** → **"Redeploy"**
   - Ou aguarde deploy automático após commit

2. **Aguardar:**
   - Build deve completar em 2-5 minutos (vs 10+ minutos antes)

---

## 📦 O que foi removido do Minimal?

**Dependências pesadas removidas:**
- ❌ `torch==2.1.1` (~2GB)
- ❌ `sentence-transformers==2.2.2` (depende de torch)
- ❌ `spacy==3.7.2` + `pt_core_news_lg` (568MB)
- ❌ `chromadb==0.4.18` (pode ser pesado)
- ❌ `scrapy==2.11.0` (não essencial para MVP)
- ❌ `selenium==4.15.2` (não essencial para MVP)
- ❌ `celery==5.3.4` + `redis==5.0.1` (não essencial para MVP)
- ❌ `firecrawl-py==0.0.16` (opcional)
- ❌ Dependências de desenvolvimento (pytest, black, etc.)

**Dependências mantidas (essenciais):**
- ✅ FastAPI + Uvicorn
- ✅ SQLAlchemy + PostgreSQL
- ✅ LangChain + Anthropic (Claude)
- ✅ OpenAI (compatível)
- ✅ Pydantic
- ✅ Autenticação (JWT)
- ✅ Web scraping básico (beautifulsoup4, requests)

---

## 🔧 Método Alternativo: Renomear Arquivos

Se não conseguir configurar Build Command no Railway:

### **Localmente:**

```bash
cd backend

# Fazer backup do requirements completo
cp requirements.txt requirements-full.txt

# Usar minimal como principal
cp requirements-minimal.txt requirements.txt

# Commit e push
git add requirements.txt requirements-full.txt
git commit -m "fix: usa requirements-minimal para evitar timeout no Railway"
git push
```

**Railway vai usar `requirements.txt` automaticamente!**

---

## 🧪 Verificar se Funcionou

Após redeploy:

1. **Ver logs do Railway:**
   - Deployments → Último deploy
   - Deve mostrar build completando em 2-5 minutos
   - Não deve ter timeout

2. **Testar aplicação:**
   ```bash
   curl https://sua-url.railway.app/health
   ```
   - Deve retornar: `{"status": "healthy", "version": "1.0.0"}`

---

## ⚠️ Se Ainda Não Funcionar

### **Opção 1: Remover Mais Dependências**

Edite `requirements-minimal.txt` e remova também:
- `langchain-community` (se não usar)
- `beautifulsoup4`, `lxml` (se não usar web scraping)
- `httpx` (se não usar)

### **Opção 2: Usar Build Cache**

No Railway:
- Settings → Build
- Habilite **"Build Cache"** (se disponível)
- Isso acelera builds subsequentes

### **Opção 3: Deploy em Etapas**

1. **Primeiro deploy:** Apenas FastAPI básico
2. **Depois:** Adicionar dependências gradualmente

---

## 📋 Checklist

- [ ] Build Command configurado para `requirements-minimal.txt`
- [ ] Ou `requirements-minimal.txt` renomeado para `requirements.txt`
- [ ] Mudanças commitadas e no GitHub
- [ ] Redeploy realizado no Railway
- [ ] Build completou sem timeout (2-5 minutos)
- [ ] Health check funciona (`/health`)

---

## 💡 Dica: Adicionar Dependências Depois

Se precisar das dependências pesadas depois:

1. **Instale apenas quando necessário:**
   ```python
   # No código, importe condicionalmente
   try:
       import torch
       import sentence_transformers
   except ImportError:
       # Funcionalidade desabilitada
       pass
   ```

2. **Ou use serviços externos:**
   - Para embeddings: Use API da OpenAI/Anthropic
   - Para NLP: Use APIs externas
   - Para ML: Use serviços cloud (AWS SageMaker, etc.)

---

## 📚 Referências

- **Railway Build Limits:** https://docs.railway.app/develop/builds
- **Requirements Minimal:** `requirements-minimal.txt`
- **Troubleshooting:** `TROUBLESHOOTING-RAILWAY.md`

---

**Pronto!** Build deve completar em 2-5 minutos agora! ⚡

**Veja também:**
- `CORRIGIR-CONFLITO-DEPENDENCIAS.md` - Outros problemas de dependências
- `TROUBLESHOOTING-RAILWAY.md` - Guia completo de troubleshooting
