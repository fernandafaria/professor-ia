# Guia de Uso do Firecrawl para Web Scraping

Este guia explica como usar o Firecrawl para fazer web scraping das fontes mapeadas no documento `mapeamento_webscraping_edtech.md`.

## 📋 Índice

1. [Configuração](#configuração)
2. [Uso Básico](#uso-básico)
3. [Integração com Pipeline](#integração-com-pipeline)
4. [Fontes Prioritárias](#fontes-prioritárias)
5. [Exemplos Práticos](#exemplos-práticos)

---

## 🔧 Configuração

### 1. Instalar Dependências

```bash
# Instalar biblioteca Firecrawl
pip install firecrawl-py

# Ou via requirements.txt
pip install -r backend/requirements.txt
```

### 2. Configurar API Key

O Firecrawl já está configurado no MCP com a API key:
```
fc-d9e38b1898aa4067be99276054db16be
```

Para usar programaticamente, configure a variável de ambiente:

```bash
# Linux/Mac
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'

# Windows
set FIRECRAWL_API_KEY=fc-d9e38b1898aa4067be99276054db16be
```

Ou adicione ao arquivo `.env`:

```env
FIRECRAWL_API_KEY=fc-d9e38b1898aa4067be99276054db16be
```

---

## 🚀 Uso Básico

### Scraping de URL Única

```python
from backend.scraping.scrapers.firecrawl import FirecrawlScraper

source_config = {
    "name": "Nova Escola",
    "url": "https://novaescola.org.br/conteudo/12345/plano-de-aula",
    "type": "educational",
    "priority": "high",
}

scraper = FirecrawlScraper(source_config)
documents = scraper.scrape()

for doc in documents:
    print(f"Título: {doc['title']}")
    print(f"Conteúdo: {doc['content'][:200]}...")
```

### Crawling de Site Inteiro

```python
scraper = FirecrawlScraper(source_config)

# Coletar até 10 páginas do site
documents = scraper.scrape(crawl=True, max_pages=10)
```

### Lista de URLs Específicas

```python
urls = [
    "https://novaescola.org.br/conteudo/12345/plano-de-aula",
    "https://novaescola.org.br/conteudo/12346/plano-de-aula",
    "https://novaescola.org.br/conteudo/12347/plano-de-aula",
]

documents = scraper.scrape(urls=urls)
```

---

## 🔄 Integração com Pipeline

### Usar Firecrawl através do Pipeline

```python
from backend.scraping.pipeline import ScrapingPipeline

pipeline = ScrapingPipeline()

# Fazer scraping usando Firecrawl
documents = pipeline.scrape_source(
    "Nova Escola",
    use_firecrawl=True,  # Usar Firecrawl em vez de scraper tradicional
    crawl=True,
    max_pages=5
)

# Adicionar ao RAG
pipeline.add_to_rag(documents)
```

### Fontes que Usam Firecrawl por Padrão

As seguintes fontes usam Firecrawl automaticamente:
- Nova Escola
- Projeto Ágatha Edu
- Fandom Wikis
- Liquipedia
- Globo Esporte
- ESPN Brasil
- Letras.mus.br

---

## 🎯 Fontes Prioritárias

### Fase 1 - MVP (Prioridade Crítica/Alta)

#### 1. API BNCC Cientificar
**Nota:** Esta é uma API REST, não precisa de scraping. Use o `BNCCAPIScraper`.

#### 2. Projeto Ágatha Edu
```python
source_config = {
    "name": "Projeto Ágatha Edu",
    "url": "https://www.projetoagathaedu.com.br",
    "type": "questions",
    "priority": "very_high",
}

scraper = FirecrawlScraper(source_config)
documents = scraper.scrape(crawl=True, max_pages=50)
```

#### 3. Nova Escola
```python
source_config = {
    "name": "Nova Escola",
    "url": "https://novaescola.org.br",
    "type": "educational",
    "priority": "high",
}

scraper = FirecrawlScraper(source_config)

# Coletar planos de aula
documents = scraper.scrape_article_list(
    list_url="https://novaescola.org.br/conteudo",
    article_selector="a[href*='/conteudo/']",
    max_articles=100
)
```

### Fase 2 - Expansão

#### Fontes Culturais (Games, Futebol, Música)

```python
# Games - Fandom Wikis
games_config = {
    "name": "Fandom Wikis",
    "url": "https://www.fandom.com",
    "type": "wiki",
    "priority": "high",
}

# Futebol - Globo Esporte
futebol_config = {
    "name": "Globo Esporte",
    "url": "https://ge.globo.com",
    "type": "news",
    "priority": "medium",
}

# Música - Letras.mus.br
musica_config = {
    "name": "Letras.mus.br",
    "url": "https://www.letras.mus.br",
    "type": "lyrics",
    "priority": "medium",
}
```

---

## 💡 Exemplos Práticos

### Exemplo 1: Coletar Planos de Aula da Nova Escola

```python
from backend.scraping.scrapers.firecrawl import FirecrawlScraper
from backend.scraping.pipeline import ScrapingPipeline

# Configuração
source_config = {
    "name": "Nova Escola",
    "url": "https://novaescola.org.br",
    "type": "educational",
    "priority": "high",
}

# Criar scraper
scraper = FirecrawlScraper(source_config)

# Coletar artigos de uma página de listagem
documents = scraper.scrape_article_list(
    list_url="https://novaescola.org.br/conteudo",
    article_selector="a[href*='/conteudo/']",
    max_articles=50
)

print(f"Coletados {len(documents)} planos de aula")

# Adicionar ao RAG
pipeline = ScrapingPipeline()
pipeline.add_to_rag(documents)
```

### Exemplo 2: Coletar Questões do Projeto Ágatha

```python
source_config = {
    "name": "Projeto Ágatha Edu",
    "url": "https://www.projetoagathaedu.com.br",
    "type": "questions",
    "priority": "very_high",
}

scraper = FirecrawlScraper(source_config)

# Fazer crawling do site
documents = scraper.scrape(crawl=True, max_pages=100)

# Filtrar apenas questões
questions = [
    doc for doc in documents 
    if "questão" in doc["content"].lower() or "enem" in doc["content"].lower()
]

print(f"Coletadas {len(questions)} questões")
```

### Exemplo 3: Pipeline Completo com Firecrawl

```python
from backend.scraping.pipeline import ScrapingPipeline

pipeline = ScrapingPipeline()

# Fontes prioritárias
priority_sources = [
    "Nova Escola",
    "Projeto Ágatha Edu",
]

all_documents = []

for source_name in priority_sources:
    print(f"Processando: {source_name}")
    
    # Usar Firecrawl para estas fontes
    docs = pipeline.scrape_source(
        source_name,
        use_firecrawl=True,
        crawl=True,
        max_pages=10
    )
    
    all_documents.extend(docs)
    print(f"  ✓ {len(docs)} documentos coletados")

# Adicionar tudo ao RAG
pipeline.add_to_rag(all_documents)

print(f"\nTotal: {len(all_documents)} documentos adicionados ao RAG")
```

---

## 📝 Parâmetros do Firecrawl

### Parâmetros de Scraping

```python
scraper.scrape(
    urls=None,              # Lista de URLs específicas
    crawl=False,            # Se True, faz crawling do site
    max_pages=None,         # Número máximo de páginas (para crawl)
    formats=["markdown"],    # Formatos: markdown, html, text
    onlyMainContent=True,   # Apenas conteúdo principal
    includeTags=["article"], # Tags HTML a incluir
)
```

### Parâmetros de Crawling

```python
scraper.scrape(
    crawl=True,
    max_pages=50,
    limit=50,               # Limite de páginas
    maxDepth=3,             # Profundidade máxima
    allowBackwardLinks=True, # Permitir links para trás
)
```

---

## ⚠️ Considerações Importantes

### 1. Rate Limiting
- Firecrawl gerencia rate limiting automaticamente
- Respeite os limites da sua conta
- Para grandes volumes, considere processar em lotes

### 2. Custos
- Firecrawl é um serviço pago (com tier gratuito limitado)
- Monitore o uso através do dashboard
- Use `max_pages` para controlar custos

### 3. Qualidade dos Dados
- Firecrawl extrai conteúdo limpo e estruturado
- Sempre valide os dados coletados
- Use `validate_data()` antes de adicionar ao RAG

### 4. Sites com JavaScript
- Firecrawl renderiza JavaScript automaticamente
- Ideal para SPAs (Single Page Applications)
- Não precisa de Selenium/Playwright

---

## 🔍 Debugging

### Ver Logs Detalhados

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

### Verificar Dados Coletados

```python
documents = scraper.scrape()

for doc in documents:
    print(f"Título: {doc['title']}")
    print(f"URL: {doc['url']}")
    print(f"Tamanho: {len(doc['content'])} caracteres")
    print(f"Metadados: {doc['metadata']}")
    print("-" * 60)
```

---

## 📚 Recursos Adicionais

- [Documentação Firecrawl](https://docs.firecrawl.dev/)
- [API Reference](https://docs.firecrawl.dev/api-reference)
- [Mapeamento de Fontes](./mapeamento_webscraping_edtech.md)

---

## 🆘 Suporte

Para problemas ou dúvidas:
1. Verifique se a API key está configurada corretamente
2. Consulte os logs para erros específicos
3. Teste com uma URL simples primeiro
4. Verifique a documentação do Firecrawl

---

**Última atualização:** 2026-01-08
