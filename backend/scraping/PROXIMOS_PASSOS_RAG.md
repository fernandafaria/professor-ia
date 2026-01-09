# 🚀 Próximos Passos para Criar Conteúdo para RAG

Guia passo a passo para popular a base de conhecimento RAG com conteúdo educacional.

## 📋 Checklist de Preparação

### 1. Verificar Configurações

```bash
# Verificar se ChromaDB está rodando
# ChromaDB deve estar em localhost:8000 (padrão)

# Verificar variáveis de ambiente
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'
export DATABASE_URL='postgresql://user:pass@localhost/dbname'
export SECRET_KEY='sua-secret-key-aqui'
```

### 2. Instalar Dependências

```bash
cd backend
pip install -r requirements.txt
```

### 3. Verificar Infraestrutura

- ✅ ChromaDB rodando (porta 8000)
- ✅ PostgreSQL configurado (se necessário)
- ✅ Redis rodando (para Celery, se usar)

---

## 🎯 Passo 1: Popular RAG com Conteúdo MVP

### Opção A: Script Automatizado (Recomendado)

```bash
# Popular com fontes prioritárias (MVP)
python -m backend.scraping.populate_rag --phase mvp

# Com Firecrawl (recomendado)
python -m backend.scraping.populate_rag --phase mvp

# Sem Firecrawl (scrapers tradicionais)
python -m backend.scraping.populate_rag --phase mvp --no-firecrawl
```

### Opção B: Via CLI Individual

```bash
# 1. Coletar dados BNCC
python -m backend.scraping.cli --source "API BNCC Cientificar"

# 2. Coletar questões do Projeto Ágatha (com Firecrawl)
python -m backend.scraping.cli \
    --source "Projeto Ágatha Edu" \
    --use-firecrawl \
    --crawl \
    --max-pages 50

# 3. Coletar planos de aula da Nova Escola (com Firecrawl)
python -m backend.scraping.cli \
    --source "Nova Escola" \
    --use-firecrawl \
    --crawl \
    --max-pages 100
```

### Opção C: Via Python (Programático)

```python
from backend.scraping.populate_rag import RAGPopulator

populator = RAGPopulator()

# Popular MVP
stats = populator.populate_phase1_mvp(use_firecrawl=True)

print(f"Total de chunks: {stats['total_chunks']}")
print(f"Adicionado ao RAG: {stats['added_to_rag']}")
```

---

## 📊 Passo 2: Verificar Conteúdo Coletado

```bash
# Verificar quantos documentos estão no RAG
python -m backend.scraping.populate_rag --phase verify

# Testar recuperação
python -m backend.scraping.populate_rag --phase test --test-query "matemática básica"
```

---

## 🎨 Passo 3: Adicionar Conteúdo Cultural (Opcional)

Para personalização com interesses dos alunos:

```bash
# Popular conteúdo cultural (games, futebol, música)
python -m backend.scraping.populate_rag --phase cultural --max-pages 20
```

---

## 🔄 Passo 4: Pipeline Completo

```bash
# Executar todas as fases
python -m backend.scraping.populate_rag --phase all
```

---

## 📈 Sequência Recomendada (Fase por Fase)

### Fase 1: MVP (Prioridade Crítica)

**Objetivo:** Ter conteúdo básico funcionando

```bash
# 1. Começar com API BNCC (mais rápido, não precisa scraping)
python -m backend.scraping.cli --source "API BNCC Cientificar"

# 2. Adicionar questões (Projeto Ágatha)
python -m backend.scraping.cli \
    --source "Projeto Ágatha Edu" \
    --use-firecrawl \
    --crawl \
    --max-pages 20  # Começar pequeno para testar

# 3. Adicionar planos de aula (Nova Escola)
python -m backend.scraping.cli \
    --source "Nova Escola" \
    --use-firecrawl \
    --crawl \
    --max-pages 30  # Começar pequeno
```

**Meta:** 500-1000 chunks no RAG

### Fase 2: Expansão

**Objetivo:** Aumentar volume e qualidade

```bash
# Aumentar volume das fontes principais
python -m backend.scraping.cli \
    --source "Projeto Ágatha Edu" \
    --use-firecrawl \
    --crawl \
    --max-pages 100

python -m backend.scraping.cli \
    --source "Nova Escola" \
    --use-firecrawl \
    --crawl \
    --max-pages 200
```

**Meta:** 5000-10000 chunks no RAG

### Fase 3: Personalização

**Objetivo:** Adicionar conteúdo cultural

```bash
# Conteúdo cultural
python -m backend.scraping.populate_rag --phase cultural
```

**Meta:** 10000+ chunks com diversidade de conteúdo

---

## 🧪 Testar o RAG

### Teste Básico

```python
from backend.app.core.rag.retriever import RAGRetriever

retriever = RAGRetriever()

# Testar recuperação
results = retriever.retrieve("equações de segundo grau", n_results=5)

for doc in results:
    print(f"Título: {doc['metadata'].get('title', 'N/A')}")
    print(f"Conteúdo: {doc['content'][:200]}...")
    print("-" * 60)
```

### Teste com Personalização

```python
# Testar com interesses do aluno
results = retriever.retrieve(
    "explicar funções matemáticas",
    n_results=5,
    student_interests=["Fortnite", "futebol"]
)
```

---

## 📝 Monitoramento e Manutenção

### Verificar Status do RAG

```bash
# Verificar quantos documentos
python -m backend.scraping.populate_rag --phase verify
```

### Atualizar Conteúdo

```bash
# Re-executar para atualizar
python -m backend.scraping.populate_rag --phase mvp
```

### Logs

Os logs mostram:
- Quantos documentos foram coletados por fonte
- Quantos chunks foram criados
- Se foram adicionados ao RAG com sucesso
- Erros (se houver)

---

## ⚠️ Troubleshooting

### Problema: ChromaDB não conecta

```bash
# Verificar se ChromaDB está rodando
# Instalar e iniciar ChromaDB:
pip install chromadb
chroma run --host localhost --port 8000
```

### Problema: Firecrawl não funciona

```bash
# Verificar API key
echo $FIRECRAWL_API_KEY

# Usar scrapers tradicionais
python -m backend.scraping.populate_rag --phase mvp --no-firecrawl
```

### Problema: Poucos documentos coletados

- Verificar se as URLs estão corretas no `sources.yaml`
- Testar scraping manual de uma URL
- Verificar logs para erros específicos
- Aumentar `max_pages` gradualmente

---

## 🎯 Metas por Fase

| Fase | Chunks Mínimos | Chunks Ideais | Fontes |
|------|----------------|---------------|--------|
| MVP | 500 | 1.000 | BNCC, Ágatha, Nova Escola |
| Expansão | 5.000 | 10.000 | + Olimpíadas, QConcursos |
| Personalização | 10.000 | 20.000+ | + Conteúdo cultural |

---

## 📚 Próximos Passos Após Popular RAG

1. **Testar Queries Reais**
   - Criar queries de alunos reais
   - Verificar qualidade das respostas
   - Ajustar prompts se necessário

2. **Otimizar Embeddings**
   - Testar diferentes modelos
   - Ajustar chunk_size e overlap
   - Melhorar metadados

3. **Adicionar Filtros**
   - Filtrar por série/ano
   - Filtrar por disciplina
   - Filtrar por tipo de conteúdo

4. **Monitorar Performance**
   - Tempo de recuperação
   - Relevância dos resultados
   - Uso de recursos

---

## 🚀 Comando Rápido para Começar

```bash
# Tudo em um comando (MVP completo)
python -m backend.scraping.populate_rag --phase mvp
```

Este comando vai:
1. ✅ Coletar dados da API BNCC
2. ✅ Coletar questões do Projeto Ágatha (50 páginas)
3. ✅ Coletar planos de aula da Nova Escola (100 páginas)
4. ✅ Processar e fazer chunking
5. ✅ Adicionar tudo ao RAG
6. ✅ Mostrar estatísticas finais

**Tempo estimado:** 30-60 minutos (dependendo do volume)

---

**Última atualização:** 2026-01-08
