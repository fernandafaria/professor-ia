# ✅ RAG Migrado para Supabase com pgvector

## Status: Migração Completa

O sistema RAG foi migrado de ChromaDB para Supabase usando pgvector!

## 🎯 O que foi feito

### 1. ✅ Extensão pgvector habilitada
- Extensão `vector` instalada no Supabase
- Versão: 0.8.0

### 2. ✅ Tabela `rag_documents` criada
- Armazena documentos com embeddings vetoriais
- Índice HNSW para busca vetorial eficiente
- Campos: id, content, embedding, metadata, source, subject, grade
- Triggers para updated_at automático

### 3. ✅ RAGRetriever atualizado
- Novo arquivo: `app/core/rag/retriever_supabase.py`
- Usa Supabase/pgvector ao invés de ChromaDB
- Busca vetorial com cosine similarity
- Suporte a filtros (subject, grade, source)

### 4. ✅ LLMService atualizado
- Integrado com novo RAGRetriever
- Passa sessão do banco para o retriever

## 📊 Estrutura da Tabela

```sql
rag_documents
├── id (UUID, PK)
├── content (TEXT) - Conteúdo do documento
├── embedding (vector(384)) - Embedding vetorial
├── metadata (JSONB) - Metadados adicionais
├── source (VARCHAR) - Fonte do documento
├── subject (VARCHAR) - Matéria
├── grade (VARCHAR) - Série/ano
├── created_at (TIMESTAMPTZ)
└── updated_at (TIMESTAMPTZ)
```

**Índices:**
- `rag_documents_embedding_idx` - HNSW para busca vetorial
- `rag_documents_subject_idx` - Filtro por matéria
- `rag_documents_grade_idx` - Filtro por série
- `rag_documents_source_idx` - Filtro por fonte

## 🔧 Como Usar

### Buscar Documentos (RAG)

O sistema já está integrado! Quando uma mensagem é enviada:

1. Query é convertida em embedding
2. Busca vetorial no Supabase usando cosine similarity
3. Top N documentos retornados
4. Contexto incluído no prompt do Claude

### Adicionar Documentos

```python
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

db = next(get_db())
retriever = RAGRetriever(db=db)

# Adicionar documentos
retriever.add_documents(
    documents=["Conteúdo do documento 1", "Conteúdo do documento 2"],
    metadatas=[
        {"source": "BNCC", "subject": "matematica", "grade": "9º EF"},
        {"source": "Projeto Ágatha", "subject": "portugues", "grade": "1º EM"}
    ],
    ids=["doc-1", "doc-2"],  # Opcional
    db=db
)
```

### Buscar Documentos

```python
results = retriever.retrieve(
    query="Explique equações de segundo grau",
    db=db,
    n_results=5,
    filters={"subject": "matematica"},  # Opcional
    student_interests=["games", "futebol"]  # Opcional
)
```

## 🚀 Vantagens do Supabase

### vs ChromaDB

| Aspecto | ChromaDB | Supabase |
|---------|----------|----------|
| **Deploy** | Servidor separado | Integrado ao banco |
| **Escalabilidade** | Limitada | PostgreSQL nativo |
| **Backup** | Manual | Automático |
| **Queries** | API REST | SQL direto |
| **Filtros** | Limitados | SQL completo |
| **Custo** | Servidor extra | Incluído no Supabase |

### Benefícios

1. ✅ **Tudo em um lugar** - Banco de dados e RAG no mesmo Supabase
2. ✅ **SQL nativo** - Queries complexas com SQL
3. ✅ **Filtros poderosos** - WHERE clauses completas
4. ✅ **Backup automático** - Incluído no Supabase
5. ✅ **Sem servidor extra** - Não precisa rodar ChromaDB
6. ✅ **Escalável** - PostgreSQL é battle-tested

## 📝 Configuração

### Dimensão dos Embeddings

O modelo padrão usa **384 dimensões**:
- Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Dimensão: 384

Se mudar o modelo, atualize a dimensão:

```python
retriever = RAGRetriever(
    db=db,
    embedding_dimension=768  # Para modelos maiores
)
```

### Modelos de Embedding Suportados

- ✅ `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384 dim) - **Padrão**
- ✅ `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` (768 dim)
- ✅ Qualquer modelo do Sentence Transformers

## 🔍 Busca Vetorial

### Como Funciona

1. **Embedding da Query**: Query convertida em vetor 384D
2. **Busca Similaridade**: Cosine similarity no Supabase
3. **Índice HNSW**: Busca rápida mesmo com milhões de documentos
4. **Filtros SQL**: WHERE clauses aplicadas antes da busca vetorial

### Exemplo de Query SQL

```sql
SELECT 
    id, content, metadata, source,
    1 - (embedding <=> '[0.1, 0.2, ...]'::vector) as similarity
FROM rag_documents
WHERE embedding IS NOT NULL
  AND subject = 'matematica'
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 5;
```

## ⚙️ Manutenção

### Verificar Documentos

```sql
SELECT COUNT(*) FROM rag_documents;
SELECT subject, COUNT(*) FROM rag_documents GROUP BY subject;
```

### Limpar Documentos Antigos

```python
retriever.delete_documents(ids=["doc-1", "doc-2"], db=db)
```

### Atualizar Embeddings

Os embeddings são atualizados automaticamente quando você chama `add_documents` com o mesmo ID.

## 📊 Performance

- **Índice HNSW**: Busca em O(log n) mesmo com milhões de documentos
- **Filtros**: Aplicados antes da busca vetorial (mais rápido)
- **Cache**: Embeddings calculados uma vez e armazenados

## ✅ Status

- ✅ pgvector instalado
- ✅ Tabela criada
- ✅ RAGRetriever migrado
- ✅ LLMService integrado
- ✅ Pronto para uso!

---

**RAG agora usa Supabase!** 🎉

Para adicionar documentos, veja os scripts de scraping em `backend/scraping/`
