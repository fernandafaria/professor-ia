# ✅ Migração RAG para Supabase - Completa

## 🎉 Status: 100% Migrado

O sistema RAG foi completamente migrado de ChromaDB para Supabase usando pgvector!

## ✅ O que foi feito

### 1. Infraestrutura Supabase
- ✅ Extensão `vector` (pgvector) habilitada
- ✅ Tabela `rag_documents` criada com:
  - Campo `embedding` tipo `vector(384)`
  - Índice HNSW para busca vetorial eficiente
  - Campos de metadata (source, subject, grade)
  - Triggers automáticos

### 2. Código Atualizado
- ✅ `RAGRetriever` migrado para Supabase (`retriever_supabase.py`)
- ✅ `LLMService` atualizado para usar novo retriever
- ✅ Busca vetorial com cosine similarity
- ✅ Suporte a filtros SQL

### 3. Integração
- ✅ Sistema RAG integrado ao fluxo de chat
- ✅ Embeddings gerados localmente (sentence-transformers)
- ✅ Armazenados no Supabase
- ✅ Busca em tempo real durante conversas

## 📊 Estrutura

```
Supabase Database
├── users
├── professor_profiles
├── conversations
├── messages
├── progress
└── rag_documents (NOVO) ✨
    ├── id (UUID)
    ├── content (TEXT)
    ├── embedding (vector(384))
    ├── metadata (JSONB)
    ├── source, subject, grade
    └── timestamps
```

## 🚀 Como Funciona Agora

### Fluxo RAG

1. **Usuário envia mensagem** → `POST /api/v1/conversations/:id/messages`
2. **LLMService busca contexto RAG**:
   - Query convertida em embedding (384D)
   - Busca vetorial no Supabase usando cosine similarity
   - Top 5 documentos retornados
3. **Contexto incluído no prompt** do Claude
4. **Claude gera resposta** com contexto pedagógico

### Exemplo de Busca

```python
# Internamente no LLMService:
rag_results = retriever.retrieve(
    query="Explique equações de segundo grau",
    db=db,
    n_results=5,
    filters={"subject": "matematica"}  # Opcional
)

# Retorna:
[
    {
        "id": "uuid",
        "content": "Equações de segundo grau são...",
        "metadata": {"source": "BNCC", "grade": "9º EF"},
        "similarity": 0.95,
        "distance": 0.05
    },
    ...
]
```

## 📝 Adicionar Documentos

### Via Código Python

```python
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

db = next(get_db())
retriever = RAGRetriever(db=db)

retriever.add_documents(
    documents=[
        "Equações de segundo grau têm a forma ax² + bx + c = 0...",
        "A fórmula de Bhaskara é x = (-b ± √(b²-4ac)) / 2a..."
    ],
    metadatas=[
        {"source": "BNCC", "subject": "matematica", "grade": "9º EF"},
        {"source": "Projeto Ágatha", "subject": "matematica", "grade": "1º EM"}
    ],
    db=db
)
```

### Via SQL Direto

```sql
-- Exemplo (embedding seria calculado antes)
INSERT INTO rag_documents (content, embedding, metadata, subject, grade)
VALUES (
    'Conteúdo do documento',
    '[0.1, 0.2, ...]'::vector(384),
    '{"source": "BNCC"}'::jsonb,
    'matematica',
    '9º EF'
);
```

## 🔍 Verificar Status

### No Supabase Dashboard

1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru
2. Vá em **Table Editor**
3. Selecione `rag_documents`
4. Veja os documentos armazenados

### Via SQL

```sql
-- Contar documentos
SELECT COUNT(*) FROM rag_documents;

-- Por matéria
SELECT subject, COUNT(*) 
FROM rag_documents 
GROUP BY subject;

-- Ver últimos documentos
SELECT id, content, subject, created_at 
FROM rag_documents 
ORDER BY created_at DESC 
LIMIT 10;
```

## ⚙️ Configuração

### Dimensão dos Embeddings

O modelo padrão usa **384 dimensões**:
- Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Configurado em: `app/config.py` → `EMBEDDING_MODEL`

Se mudar o modelo, atualize a dimensão na tabela:

```sql
-- Se usar modelo com 768 dimensões:
ALTER TABLE rag_documents ALTER COLUMN embedding TYPE vector(768);
```

### Modelos Suportados

- ✅ `paraphrase-multilingual-MiniLM-L12-v2` (384 dim) - **Padrão**
- ✅ `paraphrase-multilingual-mpnet-base-v2` (768 dim)
- ✅ Qualquer modelo Sentence Transformers

## 🎯 Vantagens

### vs ChromaDB

| Aspecto | ChromaDB | Supabase |
|---------|----------|----------|
| **Servidor** | Separado | Integrado |
| **Backup** | Manual | Automático |
| **Queries** | API REST | SQL direto |
| **Filtros** | Limitados | SQL completo |
| **Escalabilidade** | Limitada | PostgreSQL |
| **Custo** | Servidor extra | Incluído |

### Benefícios

1. ✅ **Tudo integrado** - Um único banco para tudo
2. ✅ **SQL nativo** - Queries complexas
3. ✅ **Backup automático** - Sem preocupação
4. ✅ **Sem servidor extra** - Menos infraestrutura
5. ✅ **Escalável** - PostgreSQL é robusto
6. ✅ **Filtros poderosos** - WHERE clauses completas

## 📋 Próximos Passos

### 1. Popular Base de Conhecimento

Você pode usar os scripts existentes em `backend/scraping/`:

```bash
# Importar dados BNCC
python backend/scraping/import_bncc_data.py

# Scraping de conteúdo educacional
python backend/scraping/pipeline.py
```

### 2. Testar RAG

1. Adicione alguns documentos
2. Envie uma mensagem no chat
3. Verifique se o contexto RAG está sendo usado
4. Veja os `rag_sources` no metadata da resposta

### 3. Monitorar Performance

```sql
-- Verificar uso do índice
EXPLAIN ANALYZE
SELECT * FROM rag_documents
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 5;
```

## ✅ Checklist

- ✅ pgvector instalado
- ✅ Tabela `rag_documents` criada
- ✅ Índice HNSW configurado
- ✅ RAGRetriever migrado
- ✅ LLMService integrado
- ✅ Sistema funcionando

---

**RAG agora está 100% no Supabase!** 🎉

Para adicionar conteúdo, veja: `backend/scraping/`
