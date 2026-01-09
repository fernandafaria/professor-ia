# 🚀 Próximos Passos - Plataforma P1A

**Data:** 2026-01-08  
**Status:** Sistema de Scraping Completo ✅  
**Próxima Fase:** Validação e Integração

---

## ✅ O que já está pronto

1. ✅ **Sistema de Scraping Completo**
   - Scrapers para todas as fontes do mapeamento
   - Processadores de conteúdo
   - Pipeline integrado com RAG
   - Importador para dados BNCC já coletados

2. ✅ **Estrutura Base**
   - FastAPI configurado
   - Sistema RAG (ChromaDB + Sentence Transformers)
   - Configurações e schemas básicos

3. ✅ **Dados Disponíveis**
   - Arquivo JSON com 1.617 itens BNCC (EF + EM)
   - Mapeamento completo de fontes

---

## 🎯 Próximos Passos Priorizados

### 🔥 FASE 1: Validação e Testes (Esta Semana)

#### 1.1 Testar Importação de Dados BNCC ⚡ **URGENTE**

**Objetivo:** Validar que os dados coletados podem ser importados e indexados no RAG.

```bash
# 1. Verificar se ChromaDB está configurado
# 2. Testar importação
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --no-rag

# 3. Se funcionar, importar com RAG
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"
```

**Checklist:**
- [ ] ChromaDB rodando e acessível
- [ ] Importação sem erros
- [ ] Documentos processados corretamente
- [ ] Metadados extraídos (disciplina, série, etc.)
- [ ] Chunks criados adequadamente
- [ ] Dados adicionados ao ChromaDB

**Tempo estimado:** 2-3 horas

---

#### 1.2 Validar Sistema RAG ⚡ **URGENTE**

**Objetivo:** Garantir que o RAG consegue buscar e recuperar documentos.

```python
# Criar script de teste
from app.core.rag.retriever import RAGRetriever

retriever = RAGRetriever()
results = retriever.retrieve(
    query="Como funciona a leitura de textos?",
    n_results=5,
    filters={"discipline": "Língua Portuguesa"}
)

print(f"Encontrados {len(results)} documentos")
for doc in results:
    print(f"- {doc['metadata'].get('title', 'Sem título')}")
```

**Checklist:**
- [ ] RAG consegue buscar documentos
- [ ] Embeddings funcionando corretamente
- [ ] Filtros por metadata funcionam
- [ ] Resultados são relevantes
- [ ] Performance aceitável (< 2s)

**Tempo estimado:** 2-3 horas

---

#### 1.3 Criar Script de Setup/Validação

**Objetivo:** Script que valida todo o ambiente antes de começar.

```bash
# Criar: backend/scripts/validate_setup.py
python backend/scripts/validate_setup.py
```

**Validações:**
- [ ] PostgreSQL conectado
- [ ] ChromaDB acessível
- [ ] Redis rodando
- [ ] Variáveis de ambiente configuradas
- [ ] Dependências instaladas
- [ ] Modelos de embedding carregados

**Tempo estimado:** 1-2 horas

---

### 🏗️ FASE 2: API e Integração (Próxima Semana)

#### 2.1 Criar Endpoints de RAG

**Objetivo:** API para fazer queries no sistema RAG.

**Endpoints necessários:**
- `POST /api/v1/rag/query` - Buscar conteúdo
- `GET /api/v1/rag/stats` - Estatísticas da base
- `POST /api/v1/rag/add-documents` - Adicionar documentos manualmente

**Arquivo:** `backend/app/api/v1/routes/rag.py`

**Tempo estimado:** 4-6 horas

---

#### 2.2 Criar Endpoint de Scraping

**Objetivo:** API para executar scraping via HTTP.

**Endpoints:**
- `POST /api/v1/scraping/run` - Executar scraping de fonte
- `GET /api/v1/scraping/sources` - Listar fontes disponíveis
- `GET /api/v1/scraping/status/{job_id}` - Status do job

**Arquivo:** `backend/app/api/v1/routes/scraping.py`

**Tempo estimado:** 3-4 horas

---

#### 2.3 Integrar com Celery (Background Jobs)

**Objetivo:** Executar scraping em background.

**Tarefas:**
- [ ] Configurar Celery workers
- [ ] Criar tasks para scraping
- [ ] Sistema de monitoramento de jobs
- [ ] Retry automático em caso de falha

**Tempo estimado:** 4-5 horas

---

### 🧪 FASE 3: Testes e Qualidade (2 Semanas)

#### 3.1 Testes Unitários

**Cobertura mínima:**
- [ ] Testes dos scrapers
- [ ] Testes dos processadores
- [ ] Testes do RAG retriever
- [ ] Testes da pipeline

**Tempo estimado:** 6-8 horas

---

#### 3.2 Testes de Integração

**Cenários:**
- [ ] Importação completa de dados BNCC
- [ ] Scraping de fonte real
- [ ] Query RAG end-to-end
- [ ] Performance e carga

**Tempo estimado:** 4-6 horas

---

### 📊 FASE 4: Monitoramento e Observabilidade (2-3 Semanas)

#### 4.1 Logging Estruturado

**Objetivo:** Logs detalhados para debugging.

- [ ] Configurar structlog
- [ ] Logs de scraping
- [ ] Logs de RAG queries
- [ ] Métricas de performance

**Tempo estimado:** 3-4 horas

---

#### 4.2 Métricas e Dashboard

**Objetivo:** Monitorar saúde do sistema.

- [ ] Prometheus metrics
- [ ] Dashboard básico (Grafana ou similar)
- [ ] Alertas para falhas

**Tempo estimado:** 4-6 horas

---

### 🎨 FASE 5: Frontend e UX (3-4 Semanas)

#### 5.1 Interface de Administração

**Funcionalidades:**
- [ ] Dashboard de scraping
- [ ] Visualização de documentos no RAG
- [ ] Teste de queries
- [ ] Gerenciamento de fontes

**Tempo estimado:** 2-3 semanas

---

## 📋 Checklist Rápido - Começar Agora

### Setup Inicial (30 minutos)

```bash
# 1. Verificar ambiente
cd backend
python --version  # Deve ser 3.10+

# 2. Instalar dependências (se ainda não fez)
pip install -r requirements.txt

# 3. Configurar .env
cp .env.example .env
# Editar .env com suas configurações

# 4. Iniciar ChromaDB
chroma run --path ./chroma_db --port 8000

# 5. Iniciar Redis (se usar Celery)
redis-server
```

### Teste Rápido (15 minutos)

```bash
# 1. Testar importação (sem RAG primeiro)
python -m backend.scraping.import_bncc_data \
  "scraping/extract-data-2026-01-08 (1).json" \
  --no-rag \
  --categories fundamental_education

# 2. Verificar se processou corretamente
# Deve mostrar estatísticas de processamento
```

### Validação RAG (30 minutos)

```python
# Criar: backend/test_rag.py
from app.core.rag.retriever import RAGRetriever

retriever = RAGRetriever()

# Testar busca
results = retriever.retrieve("matemática", n_results=3)
print(f"Encontrados: {len(results)}")
for r in results:
    print(f"- {r['metadata'].get('title')}")
```

---

## 🎯 Prioridades por Urgência

### ⚡ **URGENTE (Esta Semana)**
1. ✅ Testar importação de dados BNCC
2. ✅ Validar sistema RAG
3. ✅ Criar script de validação de setup

### 🔥 **ALTA (Próxima Semana)**
4. ✅ Criar endpoints de API
5. ✅ Integrar scraping com API
6. ✅ Testes básicos

### 📈 **MÉDIA (2-3 Semanas)**
7. ✅ Celery para background jobs
8. ✅ Testes completos
9. ✅ Monitoramento básico

### 💡 **BAIXA (1 Mês+)**
10. ✅ Frontend admin
11. ✅ Dashboard avançado
12. ✅ Otimizações de performance

---

## 🛠️ Comandos Úteis

### Desenvolvimento

```bash
# Rodar API
uvicorn app.main:app --reload

# Rodar scraping
python -m backend.scraping.cli --source "API BNCC Cientificar"

# Importar dados
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"

# Testes
pytest backend/tests/
```

### Debugging

```bash
# Ver logs do ChromaDB
tail -f chroma_db/logs/*.log

# Verificar conexão Redis
redis-cli ping

# Verificar PostgreSQL
psql -U postgres -d p1a_db -c "SELECT 1"
```

---

## 📚 Documentação de Referência

- **Scraping:** `backend/scraping/README.md`
- **Importação:** `backend/scraping/IMPORT_GUIDE.md`
- **Arquitetura:** `ARCHITECTURE.md`
- **Setup:** `docs/DEVELOPMENT_SETUP.md`

---

## 🆘 Troubleshooting

### Problema: ChromaDB não conecta
```bash
# Verificar se está rodando
chroma run --path ./chroma_db --port 8000

# Verificar configuração em app/config.py
CHROMA_HOST=localhost
CHROMA_PORT=8000
```

### Problema: Importação falha
```bash
# Testar sem RAG primeiro
python -m backend.scraping.import_bncc_data \
  "scraping/extract-data-2026-01-08 (1).json" \
  --no-rag

# Verificar logs
# Ajustar batch_size se necessário
```

### Problema: RAG não encontra documentos
```python
# Verificar se documentos foram adicionados
from app.core.rag.retriever import RAGRetriever
retriever = RAGRetriever()
collection = retriever.collection
print(f"Documentos na collection: {collection.count()}")
```

---

## ✅ Próxima Ação Imediata

**Execute agora:**

```bash
# 1. Validar setup
cd backend
python -c "from app.config import settings; print('Config OK')"

# 2. Testar importação (sem RAG)
python -m backend.scraping.import_bncc_data \
  "../scraping/extract-data-2026-01-08 (1).json" \
  --no-rag \
  --categories fundamental_education

# 3. Se funcionar, importar com RAG
python -m backend.scraping.import_bncc_data \
  "../scraping/extract-data-2026-01-08 (1).json" \
  --categories fundamental_education
```

**Tempo estimado:** 30-60 minutos  
**Resultado esperado:** Dados BNCC importados e indexados no RAG

---

**Última Atualização:** 2026-01-08  
**Próxima Revisão:** Após completar Fase 1
