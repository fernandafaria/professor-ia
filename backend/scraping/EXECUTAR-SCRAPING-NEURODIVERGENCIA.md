# 🚀 Executar Scraping de Papers sobre Neurodivergências

## 📋 Script Criado

**Arquivo:** `scrape_neurodivergence_papers.py`

Este script executa o scraping completo de papers acadêmicos sobre neurodivergências e organiza os dados para RAG.

---

## 🎯 Funcionalidades

1. **Busca em múltiplas fontes:**
   - PubMed (API pública)
   - SciELO Brasil (API pública)
   - ERIC (se API key configurada)

2. **Processamento:**
   - Validação de qualidade
   - Chunking para RAG
   - Enriquecimento de metadados

3. **Organização para RAG:**
   - Adiciona ao ChromaDB
   - Metadados estruturados
   - Indexação semântica

---

## 🚀 Uso Rápido

### Execução Básica

```bash
cd backend
python scraping/scrape_neurodivergence_papers.py
```

**O que faz:**
- Busca papers sobre TDAH, dislexia e autismo
- Processa e organiza para RAG
- Adiciona ao ChromaDB automaticamente
- Salva papers em JSON

### Opções Disponíveis

```bash
# Buscar apenas TDAH
python scraping/scrape_neurodivergence_papers.py --types ADHD

# Buscar todos os tipos
python scraping/scrape_neurodivergence_papers.py --types ADHD dyslexia autism neurodivergence

# Limitar resultados (mais rápido)
python scraping/scrape_neurodivergence_papers.py --max-results 10

# Apenas coletar, não adicionar ao RAG
python scraping/scrape_neurodivergence_papers.py --no-rag

# Não salvar JSON
python scraping/scrape_neurodivergence_papers.py --no-save

# Ajustar tamanho dos chunks
python scraping/scrape_neurodivergence_papers.py --chunk-size 1500
```

---

## ⚙️ Configuração

### Variáveis de Ambiente (Opcional)

```bash
# ERIC API Key (opcional, mas recomendado)
export ERIC_API_KEY="sua_chave_aqui"

# ChromaDB (se não usar padrão)
export CHROMA_HOST="localhost"
export CHROMA_PORT=8000
```

### Obter ERIC API Key

1. Acesse: https://api.ies.ed.gov/
2. Registre-se para obter chave gratuita
3. Configure: `export ERIC_API_KEY="sua_chave"`

---

## 📊 O Que Será Coletado

### Tipos de Neurodivergência

- **ADHD/TDAH** - Transtorno de Déficit de Atenção e Hiperatividade
- **Dyslexia/Dislexia** - Dificuldades de leitura
- **Autism/TEA** - Transtorno do Espectro Autista
- **Neurodivergence** - Geral sobre neurodiversidade

### Por Tipo, Busca:

- **PubMed:** Papers em inglês sobre intervenções educacionais
- **SciELO:** Papers em português sobre educação inclusiva
- **ERIC:** Papers educacionais (se API key configurada)

---

## 📁 Estrutura de Dados

### Papers Coletados (JSON)

Salvos em: `backend/data/raw/papers_{tipo}_{data}.json`

```json
{
  "title": "Intervenções Educacionais para TDAH",
  "abstract": "Resumo do paper...",
  "authors": ["Autor 1", "Autor 2"],
  "publication_date": "2024-01-15",
  "doi": "10.1234/example",
  "source_url": "https://pubmed.ncbi.nlm.nih.gov/12345",
  "keywords": ["TDAH", "educação", "intervenção"],
  "source_database": "PubMed",
  "language": "en"
}
```

### Chunks para RAG

Cada paper é dividido em chunks com:
- **Conteúdo:** Título + Abstract + Autores + Keywords
- **Metadados:**
  - Tipo de neurodivergência
  - Fonte (PubMed, SciELO, ERIC)
  - Autores, DOI, data
  - Keywords
  - Idioma

---

## 🔄 Pipeline Completo

```
1. Busca Papers
   ├── PubMed (API)
   ├── SciELO (API)
   └── ERIC (API/Web)
   
2. Validação
   ├── Título mínimo
   ├── Abstract mínimo
   └── Remoção de duplicatas
   
3. Processamento
   ├── Criação de conteúdo combinado
   ├── Chunking (2000 chars, 400 overlap)
   └── Enriquecimento de metadados
   
4. Organização RAG
   ├── Geração de embeddings
   ├── Adição ao ChromaDB
   └── Indexação semântica
```

---

## 📈 Estatísticas Esperadas

### Por Tipo de Neurodivergência:

- **ADHD:** ~30-50 papers (PubMed + SciELO)
- **Dyslexia:** ~30-50 papers
- **Autism:** ~30-50 papers
- **Neurodivergence:** ~20-30 papers

**Total estimado:** ~100-200 papers únicos
**Total de chunks:** ~300-600 chunks (dependendo do tamanho dos abstracts)

---

## ✅ Verificar Resultados

### Verificar Papers Coletados

```bash
# Listar arquivos JSON
ls -lh backend/data/raw/papers_*.json

# Ver conteúdo de um arquivo
cat backend/data/raw/papers_ADHD_*.json | head -50
```

### Verificar RAG

```python
from backend.app.core.rag.retriever import RAGRetriever

retriever = RAGRetriever()

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

## ⚠️ Considerações

1. **Rate Limiting:**
   - PubMed: 3 requisições/segundo
   - SciELO: Respeitar delays
   - ERIC: Depende da API key

2. **Tempo de Execução:**
   - ~5-10 minutos para buscar todos os tipos
   - Depende da quantidade de resultados

3. **Qualidade dos Dados:**
   - Apenas papers com abstract mínimo são processados
   - Duplicatas são removidas automaticamente

4. **Armazenamento:**
   - Papers salvos em JSON (~1-5 MB por tipo)
   - Chunks no ChromaDB (depende do tamanho)

---

## 🔧 Troubleshooting

### Erro: "Connection refused"
- Verifique se ChromaDB está rodando
- Configure `CHROMA_HOST` e `CHROMA_PORT`

### Erro: "No papers found"
- Verifique conexão com internet
- Tente reduzir `--max-results`
- Verifique se termos de busca estão corretos

### Erro: "API rate limit exceeded"
- Aguarde alguns minutos
- Reduza `--max-results`
- Use `--no-rag` para apenas coletar

---

## 📚 Próximos Passos

Após executar o scraping:

1. **Verificar qualidade dos dados:**
   ```bash
   python scraping/scrape_neurodivergence_papers.py --no-rag --no-save
   ```

2. **Testar recuperação:**
   ```python
   # Usar o código de verificação acima
   ```

3. **Integrar com sistema de chat:**
   - Os papers já estarão disponíveis no RAG
   - O sistema pode usar para contextualizar respostas

---

**Última Atualização:** 2025-01-08
