# Quick Start - Firecrawl para Web Scraping

Guia rápido para começar a usar o Firecrawl para fazer web scraping das fontes educacionais.

## 🚀 Início Rápido

### 1. Configurar API Key

```bash
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'
```

### 2. Instalar Dependências

```bash
pip install firecrawl-py
```

### 3. Executar Exemplo

```bash
python backend/scraping/firecrawl_example.py
```

## 📝 Exemplos Rápidos

### Exemplo 1: Scraping de uma página

```python
from backend.scraping.scrapers.firecrawl import FirecrawlScraper

scraper = FirecrawlScraper({
    "name": "Nova Escola",
    "url": "https://novaescola.org.br/conteudo/12345/plano-de-aula",
    "type": "educational",
    "priority": "high",
})

documents = scraper.scrape()
print(f"Coletados {len(documents)} documentos")
```

### Exemplo 2: Via CLI

```bash
# Scraping de uma fonte usando Firecrawl
python -m backend.scraping.cli \
    --source "Nova Escola" \
    --use-firecrawl

# Crawling de múltiplas páginas
python -m backend.scraping.cli \
    --source "Projeto Ágatha Edu" \
    --use-firecrawl \
    --crawl \
    --max-pages 50
```

### Exemplo 3: Pipeline completo

```python
from backend.scraping.pipeline import ScrapingPipeline

pipeline = ScrapingPipeline()

# Coletar usando Firecrawl
documents = pipeline.scrape_source(
    "Nova Escola",
    use_firecrawl=True,
    crawl=True,
    max_pages=10
)

# Adicionar ao RAG
pipeline.add_to_rag(documents)
```

## 🎯 Fontes Prioritárias

### Fase 1 - MVP

1. **Nova Escola** (planos de aula)
   ```bash
   python -m backend.scraping.cli --source "Nova Escola" --use-firecrawl --crawl --max-pages 100
   ```

2. **Projeto Ágatha Edu** (questões ENEM)
   ```bash
   python -m backend.scraping.cli --source "Projeto Ágatha Edu" --use-firecrawl --crawl --max-pages 200
   ```

## 📚 Documentação Completa

- [Guia Completo do Firecrawl](./FIRECRAWL_GUIDE.md)
- [Mapeamento de Fontes](../../mapeamento_webscraping_edtech.md)
- [README do Scraping](./README.md)
