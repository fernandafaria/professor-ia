# 🔄 Pipeline Completo: Scraping → RAG

## 📋 Visão Geral

Pipeline completo para coletar papers sobre neurodivergências e organizar para RAG.

```
1. Scraping → 2. Processamento → 3. RAG
```

---

## 🚀 Execução Completa

### Passo 1: Executar Scraping

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Buscar papers (TDAH, dislexia, autismo)
python3 scraping/scrape_neurodivergence_simple.py \
  --types ADHD dyslexia autism \
  --max-results 20
```

**Resultado:**
- `papers_neurodivergence_YYYYMMDD_HHMMSS.json` - Papers coletados
- `papers_neurodivergence_YYYYMMDD_HHMMSS_chunks.json` - Chunks processados

### Passo 2: Adicionar ao RAG

**Pré-requisito:** ChromaDB rodando

```bash
# Iniciar ChromaDB (se não estiver rodando)
chroma run --path ./chroma_db --port 8000
```

**Adicionar papers ao RAG:**

```bash
# Usar o arquivo de chunks mais recente
python3 scraping/add_papers_to_rag.py \
  --file data/raw/papers_neurodivergence_*_chunks.json \
  --collection neurodivergence_papers
```

---

## 📊 Resultados do Teste

**Execução de teste realizada:**
- ✅ 5 papers coletados do PubMed
- ✅ 6 chunks criados
- ✅ Arquivos JSON salvos

**Arquivos criados:**
- `backend/data/raw/papers_neurodivergence_20260108_224656.json`
- `backend/data/raw/papers_neurodivergence_20260108_224656_chunks.json`

---

## 🔧 Scripts Disponíveis

### 1. `scrape_neurodivergence_simple.py`
**Versão simplificada e standalone**

```bash
# Uso básico
python3 scraping/scrape_neurodivergence_simple.py --types ADHD --max-results 10

# Buscar todos os tipos
python3 scraping/scrape_neurodivergence_simple.py \
  --types ADHD dyslexia autism \
  --max-results 20

# Especificar arquivo de saída
python3 scraping/scrape_neurodivergence_simple.py \
  --types ADHD \
  --output meus_papers.json
```

### 2. `add_papers_to_rag.py`
**Adiciona papers processados ao ChromaDB**

```bash
python3 scraping/add_papers_to_rag.py \
  --file data/raw/papers_neurodivergence_*_chunks.json \
  --collection neurodivergence_papers
```

### 3. `scrape_neurodivergence_papers.py`
**Versão completa (requer estrutura do projeto)**

```bash
# Requer configuração completa do projeto
python3 scraping/scrape_neurodivergence_papers.py \
  --types ADHD dyslexia autism \
  --max-results 20
```

---

## 📁 Estrutura de Dados

### Papers Coletados (JSON)

```json
{
  "title": "Educational Interventions for ADHD",
  "abstract": "Resumo do paper...",
  "authors": ["Autor 1", "Autor 2"],
  "publication_date": "2024",
  "doi": "10.1234/example",
  "source_url": "https://pubmed.ncbi.nlm.nih.gov/12345",
  "source_database": "PubMed",
  "neurodivergence_type": "ADHD",
  "language": "en"
}
```

### Chunks para RAG (JSON)

```json
{
  "id": "hash_chunk_0",
  "content": "Título: ...\nResumo: ...\nAutores: ...",
  "metadata": {
    "title": "...",
    "source": "PubMed",
    "neurodivergence_type": "ADHD",
    "chunk_index": 0,
    "total_chunks": 2,
    "processed_at": "2025-01-08T22:46:56"
  }
}
```

---

## ✅ Verificar RAG

### Verificar Collection

```python
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_api_impl="rest",
    chroma_server_host="localhost",
    chroma_server_http_port=8000,
))

collection = client.get_collection("neurodivergence_papers")
print(f"Total de documentos: {collection.count()}")
```

### Buscar Papers

```python
from backend.app.core.rag.retriever import RAGRetriever

retriever = RAGRetriever(collection_name="neurodivergence_papers")

# Buscar papers sobre TDAH
results = retriever.retrieve(
    query="estratégias educacionais para TDAH",
    n_results=5,
    filters={"neurodivergence_type": "ADHD"}
)

for doc in results:
    print(f"Título: {doc['metadata'].get('title')}")
    print(f"Fonte: {doc['metadata'].get('source')}")
    print(f"Conteúdo: {doc['content'][:200]}...")
    print("---")
```

---

## 📈 Estatísticas Esperadas

### Por Execução Completa:

- **Papers coletados:** ~60-100 papers únicos
  - ADHD: ~20-30 papers
  - Dyslexia: ~20-30 papers
  - Autism: ~20-30 papers

- **Chunks criados:** ~150-300 chunks
  - Depende do tamanho dos abstracts
  - Chunk size: 2000 caracteres
  - Overlap: 400 caracteres

- **Tempo de execução:**
  - Scraping: ~5-10 minutos
  - Processamento: ~1 minuto
  - Adição ao RAG: ~2-5 minutos

---

## 🔄 Workflow Recomendado

### 1. Coleta Inicial

```bash
# Coletar papers de todos os tipos
python3 scraping/scrape_neurodivergence_simple.py \
  --types ADHD dyslexia autism \
  --max-results 30
```

### 2. Adicionar ao RAG

```bash
# Encontrar arquivo mais recente
LATEST_CHUNKS=$(ls -t backend/data/raw/*_chunks.json | head -1)

# Adicionar ao RAG
python3 scraping/add_papers_to_rag.py --file "$LATEST_CHUNKS"
```

### 3. Verificar e Testar

```python
# Usar código de verificação acima
```

### 4. Atualizações Periódicas

```bash
# Executar mensalmente para novos papers
python3 scraping/scrape_neurodivergence_simple.py \
  --types ADHD dyslexia autism \
  --max-results 10
```

---

## ⚠️ Troubleshooting

### Erro: "ChromaDB connection refused"
```bash
# Iniciar ChromaDB
chroma run --path ./chroma_db --port 8000
```

### Erro: "No module named 'chromadb'"
```bash
pip install chromadb sentence-transformers
```

### Erro: "SciELO connection failed"
- Normal se houver problemas de rede
- O script continua com PubMed
- Tente novamente mais tarde

### Papers duplicados
- O script remove duplicatas automaticamente
- Baseado no título (case-insensitive)

---

## 📚 Próximos Passos

1. ✅ **Scraping funcionando** - Coletou 5 papers no teste
2. ⏳ **Adicionar ao RAG** - Executar `add_papers_to_rag.py`
3. ⏳ **Testar recuperação** - Verificar busca no RAG
4. ⏳ **Integrar com chat** - Usar papers para contextualizar respostas
5. ⏳ **Coletar mais papers** - Executar com mais resultados

---

**Última Atualização:** 2025-01-08  
**Status:** ✅ Scraping funcionando, pronto para adicionar ao RAG
