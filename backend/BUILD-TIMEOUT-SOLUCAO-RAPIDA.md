# ⚡ Solução Rápida: Build Timed Out (30 segundos)

**Problema:** Railway timeout no build (dependências muito pesadas)

**Solução:** Usar `requirements-minimal.txt` (sem torch, spacy, etc.)

---

## 🚀 Solução em 30 Segundos

**Já foi feito automaticamente!** ✅

- `requirements.txt` agora usa versão minimal (rápida)
- `requirements-full.txt` salva versão completa (para depois)

**Railway vai usar `requirements.txt` automaticamente!**

---

## ✅ Próximo Passo

**Apenas faça commit e push:**

```bash
git commit -m "fix: usa requirements-minimal para evitar timeout no Railway"
git push
```

**Railway vai detectar e fazer deploy automaticamente!**

---

## 📦 O que mudou?

**Removido (muito pesado):**
- ❌ torch (~2GB)
- ❌ sentence-transformers
- ❌ spacy + pt_core_news_lg (568MB)
- ❌ chromadb
- ❌ scrapy, selenium
- ❌ celery, redis

**Mantido (essencial):**
- ✅ FastAPI + Uvicorn
- ✅ SQLAlchemy + PostgreSQL
- ✅ LangChain + Anthropic (Claude)
- ✅ OpenAI
- ✅ Autenticação JWT
- ✅ Web scraping básico

---

## 🧪 Verificar

Após deploy:

```bash
curl https://sua-url.railway.app/health
```

**Deve funcionar!** Build deve completar em 2-5 minutos (vs timeout antes).

---

## 💡 Se Precisar das Dependências Pesadas Depois

1. **Renomear de volta:**
   ```bash
   cp requirements-full.txt requirements.txt
   git add requirements.txt
   git commit -m "feat: adiciona dependências completas"
   git push
   ```

2. **Ou instalar apenas quando necessário:**
   - Use APIs externas para ML/NLP
   - Ou adicione gradualmente

---

**Pronto!** Commit e push para fazer deploy! 🚀

**Veja guia completo:** `SOLUCAO-BUILD-TIMEOUT.md`
