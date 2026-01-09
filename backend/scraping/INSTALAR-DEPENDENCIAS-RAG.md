# 📦 Instalar Dependências para RAG

## ⚠️ Dependências Necessárias

Para adicionar papers ao RAG, você precisa:

1. **ChromaDB** - Banco de dados vetorial
2. **sentence-transformers** - Modelo de embeddings
3. **ChromaDB rodando** - Servidor em execução

---

## 🚀 Instalação Rápida

### Opção 1: Instalar Globalmente

```bash
pip3 install chromadb sentence-transformers
```

### Opção 2: Instalar no Ambiente Virtual (Recomendado)

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Criar ambiente virtual (se não existir)
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install chromadb sentence-transformers
```

---

## 🗄️ Iniciar ChromaDB

### Opção 1: ChromaDB Standalone

```bash
# Instalar ChromaDB CLI (se necessário)
pip install chromadb

# Iniciar servidor
chroma run --path ./chroma_db --port 8000
```

### Opção 2: ChromaDB via Python

```python
import chromadb

# Criar cliente persistente
client = chromadb.PersistentClient(path="./chroma_db")
```

---

## ✅ Verificar Instalação

```bash
# Verificar bibliotecas
python3 -c "import chromadb; import sentence_transformers; print('✅ OK')"

# Verificar ChromaDB rodando
curl http://localhost:8000/api/v1/heartbeat
```

---

## 🔧 Usar Script de Verificação

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Verificar dependências e ChromaDB
python3 scraping/add_papers_to_rag_standalone.py --check-only
```

---

## 📝 Após Instalar

1. **Iniciar ChromaDB:**
   ```bash
   chroma run --path ./chroma_db --port 8000
   ```

2. **Adicionar papers ao RAG:**
   ```bash
   python3 scraping/add_papers_to_rag_standalone.py \
     --file data/raw/papers_neurodivergence_*_chunks.json
   ```

---

**Última Atualização:** 2025-01-08
