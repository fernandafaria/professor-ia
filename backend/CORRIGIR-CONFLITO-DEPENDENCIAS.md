# 🔧 Corrigir Conflito de Dependências - OpenAI

**Problema:** Conflito entre `openai==1.3.7` e `langchain-openai==0.0.2`

**Solução:** Atualizar versão do OpenAI para compatível

---

## 🐛 Erro Encontrado

```
ERROR: Cannot install -r requirements.txt (line 14) and openai==1.3.7 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested openai==1.3.7
    langchain-openai 0.0.2 depends on openai<2.0.0 and >=1.6.1
```

**Causa:**
- `openai==1.3.7` é muito antiga
- `langchain-openai==0.0.2` requer `openai>=1.6.1,<2.0.0`

---

## ✅ Solução Aplicada

**Antes:**
```txt
openai==1.3.7  # Mantido para embeddings (opcional)
```

**Depois:**
```txt
openai>=1.6.1,<2.0.0  # Compatível com langchain-openai 0.0.2
```

---

## 🧪 Testar Correção

```bash
cd backend
pip install -r requirements.txt
```

**Deve instalar sem erros de conflito.**

---

## 📦 Versão Minimal (Para Railway)

Se o build no Railway estiver muito lento ou falhando devido a dependências pesadas, use:

**`requirements-minimal.txt`** - Versão otimizada sem:
- `torch` (~2GB)
- `sentence-transformers` (depende de torch)
- `spacy` + `pt_core_news_lg` (568MB)
- `chromadb` (pode ser pesado)
- Outras dependências não essenciais para MVP

**Como usar no Railway:**
1. No Railway → Settings → Deploy
2. **Build Command:** `pip install -r requirements-minimal.txt`
3. Redeploy

---

## 🔍 Verificar Outros Conflitos

Se encontrar outros conflitos:

```bash
# Verificar dependências
pip check

# Tentar resolver automaticamente
pip install --upgrade -r requirements.txt
```

---

## 📚 Referências

- **OpenAI Python SDK:** https://github.com/openai/openai-python
- **LangChain OpenAI:** https://python.langchain.com/docs/integrations/llms/openai
- **Pip Dependency Resolution:** https://pip.pypa.io/en/latest/topics/dependency-resolution/

---

**Correção aplicada!** Agora `pip install -r requirements.txt` deve funcionar! ✅
