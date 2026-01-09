# ✅ Migração Completa: ChromaDB → Supabase

**Data:** 2026-01-08  
**Status:** ✅ Migração Concluída

---

## 🎯 Resumo da Migração

O sistema RAG foi completamente migrado de **ChromaDB** para **Supabase com pgvector**!

### ✅ O que foi feito

1. **Código Atualizado:**
   - ✅ `RAGRetriever` migrado para `retriever_supabase.py`
   - ✅ Todas as importações atualizadas
   - ✅ `pipeline.py` adaptado para usar Supabase
   - ✅ `populate_rag.py` atualizado
   - ✅ `import_bncc_data.py` atualizado
   - ✅ `llm_service.py` já estava usando Supabase

2. **Configurações Atualizadas:**
   - ✅ `config.py` - Removidas configurações ChromaDB
   - ✅ `.env` - Removidas variáveis ChromaDB
   - ✅ `check_setup.py` - Atualizado para verificar Supabase

3. **Infraestrutura:**
   - ✅ Tabela `rag_documents` já existe no Supabase
   - ✅ Extensão `pgvector` instalada
   - ✅ Índices HNSW configurados

---

## 📋 Arquivos Modificados

### Código Principal
- `backend/app/core/rag/__init__.py` - Atualizado para usar retriever_supabase
- `backend/app/core/rag/retriever.py` - Mantido para compatibilidade (não usado)
- `backend/app/core/rag/retriever_supabase.py` - **Usado agora**
- `backend/app/config.py` - Removidas configurações ChromaDB
- `backend/scraping/pipeline.py` - Atualizado para Supabase
- `backend/scraping/populate_rag.py` - Atualizado para Supabase
- `backend/scraping/importers/bncc_json_importer.py` - Atualizado para Supabase
- `backend/scraping/scrape_neurodivergence_papers.py` - Atualizado para Supabase
- `backend/scraping/check_setup.py` - Atualizado para verificar Supabase

### Configuração
- `.env` - Removidas variáveis CHROMA_*
- `backend/.env` - Removidas variáveis CHROMA_*

---

## 🔄 Mudanças Principais

### Antes (ChromaDB)
```python
# Inicialização
retriever = RAGRetriever()  # Conecta a servidor ChromaDB

# Adicionar documentos
retriever.add_documents(documents, metadatas, ids)

# Buscar documentos
results = retriever.retrieve(query, n_results=5)
```

### Depois (Supabase)
```python
# Inicialização (sem sessão no __init__)
retriever = RAGRetriever()

# Adicionar documentos (precisa de sessão do banco)
db = next(get_db())
retriever.add_documents(documents, metadatas, ids, db=db)

# Buscar documentos (precisa de sessão do banco)
results = retriever.retrieve(query, db=db, n_results=5)
```

---

## ⚙️ Configuração Necessária

### 1. DATABASE_URL no .env

Você precisa atualizar o `DATABASE_URL` no `.env` para apontar para o Supabase:

```env
# Formato da URL do Supabase
DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

**Como obter:**
1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru
2. Vá em **Settings** → **Database**
3. Role até **Connection string**
4. Selecione a aba **URI**
5. Copie a string completa

**Exemplo:**
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

### 2. Verificar pgvector

A extensão `pgvector` já está instalada no seu Supabase. Se precisar verificar:

```sql
-- Verificar se está instalado
SELECT * FROM pg_extension WHERE extname = 'vector';

-- Se não estiver, instalar:
CREATE EXTENSION vector;
```

### 3. Verificar Tabela rag_documents

A tabela `rag_documents` já existe no Supabase. Estrutura:

```sql
CREATE TABLE rag_documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding vector(384),  -- pgvector
    metadata JSONB DEFAULT '{}',
    source VARCHAR,
    subject VARCHAR,
    grade VARCHAR,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Índice HNSW para busca vetorial
CREATE INDEX rag_documents_embedding_idx 
ON rag_documents 
USING hnsw (embedding vector_cosine_ops);
```

---

## 🚀 Como Usar Agora

### 1. Popular RAG

```bash
# Popular com dados MVP
python -m backend.scraping.populate_rag --phase mvp

# Importar dados BNCC
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"
```

### 2. Buscar Documentos

```python
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

# Obter sessão do banco
db = next(get_db())

# Criar retriever
retriever = RAGRetriever()

# Buscar documentos
results = retriever.retrieve(
    query="equações de segundo grau",
    db=db,
    n_results=5,
    filters={"subject": "matematica"}  # Opcional
)

# Fechar sessão
db.close()
```

### 3. Adicionar Documentos

```python
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

db = next(get_db())
retriever = RAGRetriever()

retriever.add_documents(
    documents=["Conteúdo 1", "Conteúdo 2"],
    metadatas=[
        {"source": "BNCC", "subject": "matematica", "grade": "9º EF"},
        {"source": "Projeto Ágatha", "subject": "portugues", "grade": "1º EM"}
    ],
    ids=["doc-1", "doc-2"],  # Opcional
    db=db
)

db.close()
```

---

## 📊 Status Atual

| Componente | Status | Observação |
|------------|--------|------------|
| **Código Migrado** | ✅ Completo | Todos os arquivos atualizados |
| **Tabela rag_documents** | ✅ Existe | Já criada no Supabase |
| **pgvector** | ✅ Instalado | Extensão ativa |
| **DATABASE_URL** | ⚠️ Pendente | Precisa apontar para Supabase |
| **Scripts ChromaDB** | ⚠️ Pendente | Podem ser removidos |

---

## 🗑️ Arquivos/Scripts que podem ser removidos

Os seguintes arquivos são relacionados ao ChromaDB e não são mais necessários:

- `iniciar_chromadb.sh`
- `parar_chromadb.sh`
- `verificar_chromadb.sh`
- `backend/scraping/start_chromadb_server.py`
- `CHROMADB-SETUP.md`
- `chroma_db/` (diretório local, se existir)

**Nota:** Você pode mantê-los como referência ou removê-los.

---

## ✅ Próximos Passos

1. **Atualizar DATABASE_URL:**
   - Obter connection string do Supabase Dashboard
   - Atualizar no `.env` e `backend/.env`

2. **Testar Conexão:**
   ```bash
   python -m backend.scraping.check_setup
   ```
   Deve mostrar: `SUPABASE: ✅ OK`

3. **Popular RAG:**
   ```bash
   python -m backend.scraping.populate_rag --phase mvp
   ```

4. **Verificar Documentos:**
   ```sql
   SELECT COUNT(*) FROM rag_documents;
   SELECT subject, COUNT(*) FROM rag_documents GROUP BY subject;
   ```

---

## 🎉 Vantagens da Migração

### vs ChromaDB

| Aspecto | ChromaDB | Supabase |
|---------|----------|----------|
| **Servidor** | Separado (porta 8000) | Integrado |
| **Backup** | Manual | Automático |
| **Escalabilidade** | Limitada | PostgreSQL nativo |
| **Queries** | API REST | SQL direto |
| **Filtros** | Limitados | SQL completo |
| **Custo** | Servidor extra | Incluído |
| **Manutenção** | Servidor extra | Zero |

### Benefícios

1. ✅ **Tudo integrado** - Um único banco para tudo
2. ✅ **SQL nativo** - Queries complexas sem API REST
3. ✅ **Backup automático** - Sem preocupação
4. ✅ **Sem servidor extra** - Menos infraestrutura
5. ✅ **Escalável** - PostgreSQL é battle-tested
6. ✅ **Filtros poderosos** - WHERE clauses completas
7. ✅ **Índices avançados** - HNSW para busca vetorial rápida

---

**Migração concluída!** 🎉

O sistema RAG agora usa exclusivamente **Supabase com pgvector**.
