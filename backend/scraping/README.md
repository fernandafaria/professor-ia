# Sistema de Web Scraping - P1A

Sistema integrado de web scraping para coleta de conteúdo educacional e cultural, baseado no mapeamento estratégico definido em `mapeamento_webscraping_edtech.md`.

## Estrutura

```
scraping/
├── __init__.py              # Exports principais
├── pipeline.py              # Pipeline principal integrado com RAG
├── cli.py                    # CLI para execução
├── utils.py                  # Utilitários
├── config/
│   └── sources.yaml         # Configuração de todas as fontes
├── scrapers/
│   ├── __init__.py
│   ├── base.py              # Classe base abstrata
│   ├── bncc_api.py          # Scraper API BNCC
│   ├── projeto_agatha.py     # Scraper Projeto Ágatha
│   ├── nova_escola.py        # Scraper Nova Escola
│   └── cultural.py          # Scrapers culturais (games, futebol, música)
└── processors/
    ├── __init__.py
    └── content_processor.py  # Processamento e chunking de conteúdo
```

## Fontes Suportadas

### Fontes Curriculares (Prioridade Crítica/Alta)
- **API BNCC Cientificar**: Estrutura curricular completa
- **Projeto Ágatha Edu**: 27.615+ questões ENEM/vestibulares (usa Firecrawl)
- **Nova Escola**: 7.000+ planos de aula alinhados à BNCC (usa Firecrawl)
- **AVAMEC**: Recursos educacionais do MEC
- **Repositórios REA**: Materiais com licença aberta

### Scraping com Firecrawl

O sistema agora suporta **Firecrawl** para web scraping avançado, especialmente útil para:
- Sites com JavaScript (SPA)
- Páginas com proteção anti-bot
- Extração de conteúdo limpo e estruturado
- Scraping em larga escala

**Configuração:** A API key do Firecrawl já está configurada no MCP:
```
FIRECRAWL_API_KEY=fc-d9e38b1898aa4067be99276054db16be
```

Veja o [Guia do Firecrawl](./FIRECRAWL_GUIDE.md) para mais detalhes.

### Fontes de Questões
- QConcursos ENEM
- ZBS Educa
- Olimpíadas científicas (OBM, OBA, OBF)

### Fontes Culturais
- **Games**: Fandom Wikis, Liquipedia, Steam Charts, GameSpot, IGN
- **Futebol**: Transfermarkt, Globo Esporte, ESPN Brasil
- **Música**: Spotify Charts, Letras.mus.br, Rolling Stone
- **K-pop**: Soompi, Allkpop

### Fontes de Acessibilidade
- Instituto ABCD
- Autismo & Realidade
- SciELO

## Uso

### Importação de Dados Já Coletados

Se você já tem dados coletados em formato JSON (ex: dados da API BNCC), pode importá-los diretamente:

```bash
# Importar todos os dados BNCC
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"

# Importar apenas Ensino Fundamental
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --categories fundamental_education

# Processar sem adicionar ao RAG
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --no-rag
```

### Via CLI (Scraping)

```bash
# Scraping de fonte específica
python -m backend.scraping.cli --source "API BNCC Cientificar"

# Scraping usando Firecrawl
python -m backend.scraping.cli --source "Nova Escola" --use-firecrawl

# Scraping por prioridade
python -m backend.scraping.cli --priority critical

# Pipeline completo (todas as fontes críticas/altas)
python -m backend.scraping.cli

# Salvar documentos sem adicionar ao RAG
python -m backend.scraping.cli --source "Nova Escola" --no-rag --save output.json

# Apenas coletar, não adicionar ao RAG
python -m backend.scraping.cli --priority high --no-rag

# Crawling com Firecrawl (múltiplas páginas)
python -m backend.scraping.cli --source "Projeto Ágatha Edu" --use-firecrawl --crawl --max-pages 50
```

### Via Python

#### Importação de Dados Existentes

```python
from backend.scraping import BNCCJSONImporter

# Importar dados BNCC já coletados
importer = BNCCJSONImporter("scraping/extract-data-2026-01-08 (1).json")

# Importar todos os dados
stats = importer.import_data(
    categories=None,  # Todas as categorias
    chunk=True,
    add_to_rag=True,
)

# Importar apenas Ensino Fundamental
stats = importer.import_data(
    categories=["fundamental_education"],
    chunk=True,
    add_to_rag=True,
)
```

#### Scraping de Novos Dados

```python
from backend.scraping import ScrapingPipeline

# Inicializar pipeline
pipeline = ScrapingPipeline()

# Scraping de fonte específica
documents = pipeline.scrape_source("API BNCC Cientificar")

# Adicionar ao RAG
pipeline.add_to_rag(documents)

# Pipeline completo
stats = pipeline.run_full_pipeline(
    priorities=["critical", "very_high", "high"],
    add_to_rag=True
)
```

## Configuração

As fontes são configuradas em `config/sources.yaml`. Cada fonte deve ter:

- `name`: Nome da fonte
- `url`: URL base
- `type`: Tipo (api, educational, questions, news, wiki, etc.)
- `priority`: Prioridade (critical, very_high, high, medium, low)
- `frequency`: Frequência de atualização
- `selectors`: Seletores CSS (para scraping HTML)

## Processamento

O sistema processa automaticamente:

1. **Coleta**: Scraping das fontes configuradas
2. **Normalização**: Formato padrão de documentos
3. **Chunking**: Divisão em chunks para RAG (1000 chars, overlap 200)
4. **Validação**: Filtro por qualidade (tamanho mínimo, conteúdo válido)
5. **Enriquecimento**: Metadados BNCC quando disponível
6. **Indexação**: Adição ao ChromaDB (RAG)

## Integração com RAG

Os documentos coletados são automaticamente:

- Convertidos em embeddings (usando modelo multilíngue)
- Armazenados no ChromaDB com metadados enriquecidos
- Indexados para busca semântica

Metadados incluídos:
- Tipo de conteúdo (bncc_skill, question, lesson_plan, cultural_content)
- Disciplina/série
- Habilidades BNCC (quando disponível)
- Tags e categorias
- URL original
- Timestamp de processamento

## Exemplo de Documento Processado

```json
{
  "id": "abc123_chunk_0",
  "content": "Texto do chunk...",
  "metadata": {
    "type": "bncc_skill",
    "source": "API BNCC Cientificar",
    "source_url": "https://cientificar1992.pythonanywhere.com",
    "title": "EF67LP01 - Analisar textos...",
    "url": "https://...",
    "codigo": "EF67LP01",
    "disciplina": "Língua Portuguesa",
    "serie": "6º/7º ano",
    "chunk_index": 0,
    "total_chunks": 3,
    "processed_at": "2026-01-08T10:30:00"
  }
}
```

## Próximos Passos

1. **Validação Legal**: Consultar advogado sobre legalidade de scraping
2. **Prova de Conceito**: Testar scrapers com fontes prioritárias
3. **Monitoramento**: Implementar sistema de monitoramento de mudanças
4. **Atualização Incremental**: Sistema de atualização apenas de conteúdo novo
5. **Curadoria**: Interface para revisão humana de conteúdo coletado

## Notas Importantes

- Respeita `robots.txt` por padrão
- Implementa delays entre requisições
- Retry automático em caso de falhas
- Rate limiting por domínio
- Validação de qualidade de conteúdo
- Logging detalhado para debugging
