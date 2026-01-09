# 🐘 Configurar PostgreSQL no Supabase

## 📋 Visão Geral

Este guia configura o PostgreSQL no Supabase para o sistema RAG, incluindo:
- ✅ Extensão `pgvector` para busca vetorial
- ✅ Tabela `rag_documents` para armazenar documentos
- ✅ Índices otimizados para busca semântica
- ✅ Triggers para atualização automática

---

## 🚀 Passo a Passo

### 1. Acessar Supabase Dashboard

1. Acesse: https://app.supabase.com
2. Faça login na sua conta
3. Selecione seu projeto (ou crie um novo)

### 2. Abrir SQL Editor

1. No menu lateral, clique em **SQL Editor**
2. Clique em **New Query**

### 3. Executar Script SQL

1. Abra o arquivo: `backend/setup_supabase_postgresql.sql`
2. Copie todo o conteúdo
3. Cole no SQL Editor do Supabase
4. Clique em **Run** (ou pressione `Cmd+Enter`)

**✅ Resultado esperado:**
```
Success. No rows returned
```

### 4. Verificar Instalação

Execute no SQL Editor:

```sql
-- Verificar extensão pgvector
SELECT * FROM pg_extension WHERE extname = 'vector';

-- Verificar tabela
SELECT 
    column_name, 
    data_type 
FROM information_schema.columns 
WHERE table_name = 'rag_documents';
```

**✅ Deve retornar:**
- Extensão `vector` instalada
- Tabela `rag_documents` com colunas: `id`, `content`, `embedding`, `metadata`, `source`, `subject`, `grade`, `created_at`, `updated_at`

---

## 🔧 Configurar Connection String

### Obter Connection String

1. No Supabase Dashboard, vá em **Settings** → **Database**
2. Role até **Connection string**
3. Selecione a aba **URI**
4. Copie a string (já vem com senha)

**Formato:**
```
postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

### Configurar no `.env`

Edite `/Users/fernandafaria/Downloads/P1A/backend/.env`:

```env
DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

**⚠️ IMPORTANTE:**
- Substitua `[PASSWORD]` pela senha do seu projeto
- Use **Connection Pooling** (porta `5432` ou `6543`) para aplicação
- Use **Direct Connection** (sem `.pooler`) apenas para migrations

---

## 🧪 Testar Conexão

### Via Python

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 -c "
from app.config import settings
from sqlalchemy import create_engine, text
try:
    engine = create_engine(settings.DATABASE_URL)
    with engine.connect() as conn:
        # Verificar extensão pgvector
        result = conn.execute(text(\"SELECT * FROM pg_extension WHERE extname = 'vector'\"))
        if result.fetchone():
            print('✅ pgvector instalado')
        else:
            print('❌ pgvector não encontrado')
        
        # Verificar tabela
        result = conn.execute(text(\"SELECT COUNT(*) FROM rag_documents\"))
        count = result.fetchone()[0]
        print(f'✅ Tabela rag_documents existe ({count} documentos)')
        
        print('✅ Conexão com Supabase OK!')
except Exception as e:
    print(f'❌ Erro: {e}')
"
```

### Via SQL Editor

Execute no Supabase SQL Editor:

```sql
-- Teste de busca vetorial
SELECT 
    id,
    content,
    1 - (embedding <=> '[0.1,0.2,0.3]'::vector(384)) as similarity
FROM rag_documents
WHERE embedding IS NOT NULL
ORDER BY embedding <=> '[0.1,0.2,0.3]'::vector(384)
LIMIT 5;
```

---

## 📊 Estrutura da Tabela

### `rag_documents`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | UUID | ID único do documento |
| `content` | TEXT | Conteúdo do documento |
| `embedding` | vector(384) | Embedding vetorial (384 dimensões) |
| `metadata` | JSONB | Metadados adicionais |
| `source` | VARCHAR(255) | Fonte do documento |
| `subject` | VARCHAR(100) | Matéria/disciplina |
| `grade` | VARCHAR(50) | Série/ano |
| `created_at` | TIMESTAMP | Data de criação |
| `updated_at` | TIMESTAMP | Data de atualização |

### Índices

- **`rag_documents_embedding_idx`**: Índice HNSW para busca vetorial (cosine similarity)
- **`rag_documents_source_idx`**: Índice para filtrar por fonte
- **`rag_documents_subject_idx`**: Índice para filtrar por matéria
- **`rag_documents_grade_idx`**: Índice para filtrar por série
- **`rag_documents_metadata_idx`**: Índice GIN para busca em JSONB

---

## 🔍 Verificar Status

### Script de Verificação

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 backend/scraping/check_setup.py
```

**✅ Deve mostrar:**
```
✅ Supabase: Conectado
✅ pgvector: Instalado
✅ Tabela rag_documents: Existe
```

---

## 🚨 Troubleshooting

### Erro: "extension vector does not exist"

**Solução:**
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### Erro: "relation rag_documents does not exist"

**Solução:**
Execute novamente o script `setup_supabase_postgresql.sql`

### Erro: "password authentication failed"

**Solução:**
- Verifique a senha no `DATABASE_URL`
- A senha é a que você definiu ao criar o projeto no Supabase

### Erro: "too many connections"

**Solução:**
- Use Connection Pooling (porta `5432` ou `6543`)
- Limite no plano free: 60 conexões simultâneas

### Erro: "dimension mismatch" ao inserir embeddings

**Solução:**
- Verifique se o modelo de embedding está gerando vetores de 384 dimensões
- O modelo padrão é `paraphrase-multilingual-MiniLM-L12-v2` (384 dim)

---

## 📝 Próximos Passos

1. ✅ Executar script SQL no Supabase
2. ✅ Configurar `DATABASE_URL` no `.env`
3. ✅ Testar conexão
4. ✅ Executar scraping de papers: `python3 backend/scraping/scrape_neurodivergence_simple.py`
5. ✅ Adicionar papers ao RAG: `python3 backend/scraping/add_papers_to_rag_persistent.py`

---

## 🔗 Referências

- [Documentação pgvector](https://github.com/pgvector/pgvector)
- [Supabase PostgreSQL](https://supabase.com/docs/guides/database)
- [Connection Pooling](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler)

---

**✅ PostgreSQL no Supabase configurado!** 🎉
