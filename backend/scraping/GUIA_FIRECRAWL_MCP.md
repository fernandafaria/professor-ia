# 🔥 Guia: Scraping com Firecrawl MCP

Este guia explica como fazer scraping usando o Firecrawl através do MCP (Model Context Protocol).

## 🎯 O Que é Firecrawl MCP?

O Firecrawl MCP é um servidor MCP que expõe ferramentas para fazer web scraping. Ele usa a mesma API do Firecrawl, mas através do protocolo MCP.

**Vantagens:**
- ✅ Funciona com sites JavaScript (SPA)
- ✅ Bypassa proteções anti-bot
- ✅ Extrai conteúdo limpo e estruturado
- ✅ Suporta crawling de sites inteiros

## 🚀 Uso Rápido

### Via Script Dedicado

```bash
# Scraping de uma fonte usando MCP
python -m backend.scraping.scrape_with_mcp \
    --source "Nova Escola" \
    --crawl \
    --max-pages 50
```

### Via Pipeline

```python
from backend.scraping.pipeline import ScrapingPipeline

pipeline = ScrapingPipeline()

# Usar MCP do Firecrawl (padrão quando use_firecrawl=True)
documents = pipeline.scrape_source(
    "Nova Escola",
    use_firecrawl=True,  # Ativa Firecrawl
    use_mcp=True,        # Usa MCP (padrão: True)
    crawl=True,
    max_pages=50
)
```

### Via CLI

```bash
# O pipeline já usa MCP por padrão quando use_firecrawl=True
python -m backend.scraping.cli \
    --source "Nova Escola" \
    --use-firecrawl \
    --crawl \
    --max-pages 50
```

## 📋 Configuração

### 1. API Key

A API key já está configurada no MCP:
```
FIRECRAWL_API_KEY=fc-d9e38b1898aa4067be99276054db16be
```

Para usar programaticamente:
```bash
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'
```

### 2. Dependências

```bash
pip install firecrawl-py
```

A biblioteca `firecrawl-py` é compatível com a API que o MCP usa.

## 💡 Exemplos Práticos

### Exemplo 1: Scraping de URL Única

```python
from backend.scraping.scrapers.firecrawl_mcp_simple import FirecrawlMCPSimpleScraper

scraper = FirecrawlMCPSimpleScraper({
    "name": "Nova Escola",
    "url": "https://novaescola.org.br/conteudo/12345/plano-de-aula",
    "type": "educational",
    "priority": "high",
})

documents = scraper.scrape()
print(f"Coletados {len(documents)} documentos")
```

### Exemplo 2: Crawling de Site

```python
scraper = FirecrawlMCPSimpleScraper({
    "name": "Nova Escola",
    "url": "https://novaescola.org.br",
    "type": "educational",
    "priority": "high",
})

# Fazer crawling de 50 páginas
documents = scraper.scrape(crawl=True, max_pages=50)
```

### Exemplo 3: Múltiplas URLs

```python
urls = [
    "https://novaescola.org.br/conteudo/12345/plano-de-aula",
    "https://novaescola.org.br/conteudo/12346/plano-de-aula",
    "https://novaescola.org.br/conteudo/12347/plano-de-aula",
]

documents = scraper.scrape(urls=urls)
```

### Exemplo 4: Pipeline Completo com MCP

```python
from backend.scraping.pipeline import ScrapingPipeline

pipeline = ScrapingPipeline()

# Fontes prioritárias
sources = [
    "Nova Escola",
    "Projeto Ágatha Edu",
]

all_documents = []

for source in sources:
    print(f"Processando: {source}")
    
    docs = pipeline.scrape_source(
        source,
        use_firecrawl=True,  # Usa MCP automaticamente
        use_mcp=True,
        crawl=True,
        max_pages=20
    )
    
    all_documents.extend(docs)
    print(f"  ✓ {len(docs)} documentos coletados")

# Adicionar ao RAG
pipeline.add_to_rag(all_documents)
```

## 🔄 Diferença: MCP vs API Direta

### MCP (Model Context Protocol)
- Usado quando integrado com Cursor/IDEs
- Expõe ferramentas através do protocolo MCP
- Útil para uso interativo

### API Direta (firecrawl-py)
- Usado programaticamente em Python
- Mais simples e direto
- **Recomendado para scripts automatizados**

**Nota:** O scraper `FirecrawlMCPSimpleScraper` usa `firecrawl-py` internamente, que é compatível com a API que o MCP usa. Isso garante compatibilidade total.

## 📊 Fontes que Usam MCP por Padrão

As seguintes fontes usam Firecrawl MCP automaticamente:

- Nova Escola
- Projeto Ágatha Edu
- Fandom Wikis
- Liquipedia
- Globo Esporte
- ESPN Brasil
- Letras.mus.br

## ⚙️ Parâmetros Disponíveis

### Scraping de URL

```python
scraper.scrape(
    urls=["https://example.com"],  # URLs específicas
    formats=["markdown"],            # Formato (markdown, html, text)
    onlyMainContent=True,           # Apenas conteúdo principal
)
```

### Crawling

```python
scraper.scrape(
    crawl=True,
    max_pages=50,                   # Número máximo de páginas
    limit=50,                       # Limite de páginas
    maxDepth=3,                     # Profundidade máxima
)
```

## 🧪 Testar MCP

```bash
# Testar scraping de uma URL
python -m backend.scraping.scrape_with_mcp \
    --source "Nova Escola" \
    --crawl \
    --max-pages 5

# Verificar se está funcionando
python -c "
from backend.scraping.scrapers.firecrawl_mcp_simple import FirecrawlMCPSimpleScraper
scraper = FirecrawlMCPSimpleScraper({
    'name': 'Test',
    'url': 'https://example.com',
    'type': 'test',
    'priority': 'low'
})
docs = scraper.scrape()
print(f'✓ MCP funcionando! {len(docs)} documentos coletados')
"
```

## ⚠️ Troubleshooting

### Erro: "FIRECRAWL_API_KEY não configurada"

```bash
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'
```

### Erro: "firecrawl-py não instalado"

```bash
pip install firecrawl-py
```

### Poucos documentos coletados

- Verificar se a URL está correta
- Aumentar `max_pages` gradualmente
- Verificar logs para erros específicos

### MCP não responde

O scraper `FirecrawlMCPSimpleScraper` usa `firecrawl-py` diretamente, que é mais confiável que tentar se comunicar com o servidor MCP via subprocess. Se houver problemas, o scraper automaticamente usa a API direta.

## 📚 Próximos Passos

1. **Popular RAG com MCP:**
   ```bash
   python -m backend.scraping.populate_rag --phase mvp
   ```
   (Já usa MCP por padrão quando `use_firecrawl=True`)

2. **Testar diferentes fontes:**
   ```bash
   python -m backend.scraping.scrape_with_mcp --source "Projeto Ágatha Edu" --crawl --max-pages 20
   ```

3. **Integrar com pipeline completo:**
   ```python
   pipeline = ScrapingPipeline()
   docs = pipeline.scrape_source("Nova Escola", use_firecrawl=True, use_mcp=True)
   ```

---

**Última atualização:** 2026-01-08
