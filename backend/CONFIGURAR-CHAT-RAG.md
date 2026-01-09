# 🚀 Guia de Configuração: Chat com RAG

Este guia te ajudará a configurar completamente o sistema de chat com RAG (Retrieval-Augmented Generation) na plataforma P1A.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ Python 3.10+ instalado
- ✅ Supabase configurado com PostgreSQL e pgvector
- ✅ Tabela `rag_documents` criada no Supabase
- ✅ Variáveis de ambiente configuradas (`.env`)

---

## 🔧 Passo 1: Configurar Variáveis de Ambiente

### 1.1 Criar arquivo `.env`

Copie o arquivo de exemplo:

```bash
cd backend
cp env.example .env
```

### 1.2 Configurar variáveis essenciais

Edite o arquivo `.env` e configure as seguintes variáveis:

```env
# Banco de Dados (Supabase)
DATABASE_URL=postgresql://postgres:[SUA-SENHA]@db.[SEU-PROJECT-REF].supabase.co:5432/postgres

# Anthropic Claude API (obrigatório para chat)
ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# RAG Configuration
RAG_TABLE_NAME=rag_documents
EMBEDDING_DIMENSION=384
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

# JWT / Auth
SECRET_KEY=sua-chave-secreta-aqui-minimo-32-caracteres
```

### 1.3 Obter chaves necessárias

**Anthropic API Key:**
1. Acesse: https://console.anthropic.com/
2. Crie uma conta ou faça login
3. Vá em "API Keys"
4. Crie uma nova chave
5. Copie e cole no `.env`

**Database URL (Supabase):**
1. Acesse: https://app.supabase.com/
2. Selecione seu projeto
3. Vá em Settings → Database
4. Copie a "Connection String" (URI mode)
5. Substitua `[YOUR-PASSWORD]` pela senha do seu banco

**Secret Key (JWT):**
Gere uma chave secreta forte:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🗄️ Passo 2: Verificar Configuração do Banco de Dados

### 2.1 Verificar se a tabela RAG existe

Execute o script de verificação:

```bash
cd backend
python verificar_supabase.py
```

Você deve ver:
```
✅ Tabela rag_documents existe
✅ Tabela rag_documents tem X documentos
```

### 2.2 Se a tabela não existir, criar

Execute o script SQL de setup:

```bash
# Opção 1: Via Supabase Dashboard
# 1. Acesse: https://app.supabase.com/project/[seu-project]/sql/new
# 2. Cole o conteúdo de: backend/setup_supabase_postgresql.sql
# 3. Execute

# Opção 2: Via psql
psql [SUA-DATABASE-URL] -f backend/setup_supabase_postgresql.sql
```

---

## 📚 Passo 3: Popular a Base RAG (Opcional mas Recomendado)

### 3.1 Verificar se há conteúdo no RAG

```bash
cd backend
python -c "
from app.services.database import get_db
from sqlalchemy import text
db = next(get_db())
result = db.execute(text('SELECT COUNT(*) FROM rag_documents'))
print(f'Documentos no RAG: {result.scalar()}')
"
```

### 3.2 Popular com conteúdo educacional

**Opção A: Popular com papers sobre neurodivergência**

```bash
cd backend/scraping
python scrape_neurodivergence_papers.py --add-to-rag
```

**Opção B: Popular com dados da BNCC**

```bash
cd backend/scraping
python -m importers.bncc_json_importer --add-to-rag
```

**Opção C: Popular com pipeline completo**

```bash
cd backend/scraping
python populate_rag.py --phase mvp
```

---

## 🧪 Passo 4: Testar a Integração RAG

### 4.1 Testar busca RAG diretamente

Crie um arquivo `test_rag.py`:

```python
from app.services.database import get_db
from app.core.rag.retriever_supabase import RAGRetriever

db = next(get_db())
retriever = RAGRetriever(db=db)

# Testar busca
results = retriever.retrieve("matemática básica", db=db, n_results=3)

print(f"Encontrados {len(results)} documentos:")
for i, doc in enumerate(results, 1):
    print(f"\n{i}. Similaridade: {doc['similarity']:.3f}")
    print(f"   Conteúdo: {doc['content'][:100]}...")
    print(f"   Fonte: {doc.get('source', 'N/A')}")
```

Execute:

```bash
cd backend
python test_rag.py
```

### 4.2 Testar chat completo

Use o endpoint de mensagens:

```bash
# 1. Iniciar o servidor
cd backend
uvicorn app.main:app --reload

# 2. Em outro terminal, testar via curl
curl -X POST "http://localhost:8000/api/v1/conversations/{conversation_id}/messages" \
  -H "Authorization: Bearer {seu-token}" \
  -H "Content-Type: application/json" \
  -d '{"content": "Explique o que é uma equação quadrática"}'
```

---

## 🔍 Passo 5: Verificar Funcionamento do Chat com RAG

### 5.1 Como o RAG funciona no chat

1. **Usuário envia mensagem** → `/api/v1/conversations/{id}/messages`
2. **LLMService busca contexto RAG**:
   - Converte a mensagem em embedding
   - Busca documentos similares no Supabase
   - Retorna top 5 documentos mais relevantes
3. **Claude recebe contexto**:
   - Sistema prompt inclui contexto RAG
   - Resposta é gerada com base no contexto
4. **Resposta inclui metadata**:
   - `rag_sources`: Fontes dos documentos usados
   - `tokens`: Uso de tokens
   - `latency`: Tempo de resposta

### 5.2 Verificar se RAG está sendo usado

Na resposta da API, verifique o campo `metadata.rag_sources`:

```json
{
  "content": "Resposta do assistente...",
  "metadata": {
    "rag_sources": ["neurodivergence_papers", "bncc"],
    "tokens": 450,
    "latency": 1200
  }
}
```

Se `rag_sources` estiver vazio, o RAG pode não estar encontrando documentos relevantes.

---

## ⚙️ Passo 6: Configurações Avançadas

### 6.1 Ajustar número de resultados RAG

Edite `backend/app/services/llm_service.py`:

```python
# Linha 55 - Ajustar n_results
rag_results = self.rag_retriever.retrieve(
    user_message, 
    db=self.db, 
    n_results=5  # ← Altere aqui (padrão: 5)
)
```

### 6.2 Filtrar por matéria/série

No `LLMService`, você pode adicionar filtros:

```python
# Exemplo: Filtrar apenas documentos de matemática
rag_results = self.rag_retriever.retrieve(
    user_message,
    db=self.db,
    n_results=5,
    filters={"subject": "matematica", "grade": "9º EF"}
)
```

### 6.3 Personalizar prompt do sistema

Edite `backend/app/core/rag/prompts.py` ou `backend/app/services/llm_service.py`:

```python
# No método _build_system_prompt
context_text = "\n\n".join([
    f"📚 Fonte: {r.get('source', 'N/A')}\n{r.get('content', '')}" 
    for r in rag_results
]) if rag_context else "Nenhum contexto específico disponível."
```

### 6.4 Usar modelo de embedding diferente

No `.env`:

```env
# Modelos disponíveis:
# - sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (384 dim, padrão)
# - sentence-transformers/paraphrase-multilingual-mpnet-base-v2 (768 dim, melhor qualidade)
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-mpnet-base-v2
EMBEDDING_DIMENSION=768
```

**⚠️ Importante:** Se mudar a dimensão, você precisa:
1. Recriar a tabela `rag_documents` com a nova dimensão
2. Repopular todos os documentos

---

## 🐛 Troubleshooting

### Problema: "Erro ao buscar contexto RAG"

**Solução:**
1. Verifique se `DATABASE_URL` está correto
2. Verifique se a tabela `rag_documents` existe:
   ```bash
   python verificar_supabase.py
   ```
3. Verifique se há documentos na tabela:
   ```sql
   SELECT COUNT(*) FROM rag_documents;
   ```

### Problema: RAG não retorna resultados

**Possíveis causas:**
1. **Nenhum documento no RAG**: Popule a base primeiro
2. **Query muito específica**: Tente uma query mais genérica
3. **Embedding dimension mismatch**: Verifique se `EMBEDDING_DIMENSION` corresponde ao modelo

**Solução:**
```python
# Testar busca diretamente
from app.core.rag.retriever_supabase import RAGRetriever
retriever = RAGRetriever(db=db)
results = retriever.retrieve("teste", db=db)
print(f"Resultados: {len(results)}")
```

### Problema: "relation rag_documents does not exist"

**Solução:**
Execute o script de setup:
```bash
# Via Supabase Dashboard ou psql
psql [DATABASE_URL] -f backend/setup_supabase_postgresql.sql
```

### Problema: Chat funciona mas não usa RAG

**Verificar:**
1. Veja os logs do servidor ao enviar uma mensagem
2. Verifique se há erros como: `"Erro ao buscar contexto RAG: ..."`
3. Teste o RAG diretamente (Passo 4.1)

**Solução:**
- Se houver erro, corrija a causa
- Se não houver erro mas `rag_sources` estiver vazio, pode ser que não há documentos relevantes para a query

---

## 📊 Monitoramento

### Verificar uso do RAG

```sql
-- Contar documentos por fonte
SELECT source, COUNT(*) 
FROM rag_documents 
GROUP BY source;

-- Ver documentos mais recentes
SELECT id, source, subject, grade, created_at
FROM rag_documents
ORDER BY created_at DESC
LIMIT 10;
```

### Verificar performance

No metadata das respostas, monitore:
- `latency`: Tempo total de resposta (deve ser < 3s)
- `tokens`: Uso de tokens (custo)
- `rag_sources`: Quantas fontes foram usadas

---

## ✅ Checklist de Configuração

- [ ] Variáveis de ambiente configuradas (`.env`)
- [ ] `DATABASE_URL` válido e acessível
- [ ] `ANTHROPIC_API_KEY` configurada
- [ ] Tabela `rag_documents` criada
- [ ] Extensão `pgvector` habilitada no Supabase
- [ ] Base RAG populada (pelo menos alguns documentos)
- [ ] Teste de busca RAG funcionando
- [ ] Chat respondendo com contexto RAG
- [ ] `rag_sources` aparecendo no metadata das respostas

---

## 🎯 Próximos Passos

1. **Popular mais conteúdo**: Adicione mais documentos educacionais ao RAG
2. **Otimizar busca**: Ajuste `n_results` e filtros conforme necessário
3. **Monitorar uso**: Acompanhe métricas de latência e qualidade das respostas
4. **Personalizar prompts**: Ajuste os prompts do sistema para melhor qualidade

---

## 📚 Referências

- [Migração RAG Completa](./MIGRACAO_RAG_COMPLETA.md)
- [Setup Supabase](./CONFIGURAR-SUPABASE-POSTGRESQL.md)
- [Documentação RAG](./RAG_SUPABASE_MIGRADO.md)
- [Claude Integrado](./CLAUDE_INTEGRADO.md)

---

**Dúvidas?** Verifique os logs do servidor ou consulte a documentação específica de cada componente.
