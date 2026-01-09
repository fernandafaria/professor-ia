# ⚡ Executar Scraping Agora

## 🚀 Comando Rápido

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 scraping/scrape_neurodivergence_papers.py
```

---

## 📋 O Que Acontece

1. ✅ Busca papers no PubMed e SciELO
2. ✅ Processa e valida papers
3. ✅ Cria chunks para RAG
4. ✅ Adiciona ao ChromaDB
5. ✅ Salva papers em JSON

**Tempo estimado:** 5-10 minutos

---

## ⚙️ Pré-requisitos

### 1. ChromaDB Rodando

```bash
# Iniciar ChromaDB
chroma run --path ./chroma_db --port 8000
```

### 2. Variáveis de Ambiente (Opcional)

```bash
# ERIC API Key (opcional)
export ERIC_API_KEY="sua_chave"

# ChromaDB (se não usar padrão)
export CHROMA_HOST="localhost"
export CHROMA_PORT=8000
```

---

## 🎯 Opções de Execução

### Execução Completa (Recomendado)

```bash
python3 scraping/scrape_neurodivergence_papers.py
```

### Apenas TDAH

```bash
python3 scraping/scrape_neurodivergence_papers.py --types ADHD
```

### Apenas Coletar (Sem RAG)

```bash
python3 scraping/scrape_neurodivergence_papers.py --no-rag
```

### Teste Rápido (Poucos Resultados)

```bash
python3 scraping/scrape_neurodivergence_papers.py --max-results 5
```

---

## 📊 Resultados Esperados

- **Papers coletados:** ~100-200 papers únicos
- **Chunks criados:** ~300-600 chunks
- **Arquivos JSON:** `backend/data/raw/papers_*.json`
- **RAG:** Papers indexados no ChromaDB

---

## ✅ Verificar Sucesso

```bash
# Ver arquivos criados
ls -lh backend/data/raw/papers_*.json

# Verificar RAG (Python)
python3 -c "
from backend.app.core.rag.retriever import RAGRetriever
r = RAGRetriever()
results = r.retrieve('TDAH educação', n_results=3)
print(f'Encontrados: {len(results)} documentos')
"
```

---

**Pronto para executar!** 🎯
