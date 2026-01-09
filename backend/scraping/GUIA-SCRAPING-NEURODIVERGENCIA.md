# 📚 Guia de Scraping de Papers sobre Neurodivergências

## 🎯 Objetivo

Este guia fornece fontes e estratégias para coletar papers acadêmicos, artigos e recursos educacionais sobre neurodivergências (TDAH, dislexia, TEA) para enriquecer a base de conhecimento da plataforma.

---

## 📊 Fontes Prioritárias

### 🔴 Críticas (Alta Prioridade)

1. **ERIC (Education Resources Information Center)**
   - **URL:** https://eric.ed.gov
   - **Tipo:** Base de dados acadêmica
   - **API:** Disponível (requer chave)
   - **Conteúdo:** Papers educacionais sobre TDAH, dislexia, TEA
   - **Acesso:** Gratuito (alguns papers requerem assinatura)

2. **PubMed**
   - **URL:** https://pubmed.ncbi.nlm.nih.gov
   - **Tipo:** Base de dados biomédica
   - **API:** Disponível (gratuita)
   - **Conteúdo:** Papers sobre intervenções educacionais
   - **Acesso:** Gratuito

3. **SciELO Brasil**
   - **URL:** https://www.scielo.org
   - **Tipo:** Base de dados brasileira
   - **API:** Disponível
   - **Conteúdo:** Papers em português sobre educação inclusiva
   - **Acesso:** Gratuito

4. **Instituto ABCD**
   - **URL:** https://institutoabcd.org.br
   - **Tipo:** Organização de pesquisa
   - **Conteúdo:** Pesquisas sobre dislexia e TDAH no Brasil
   - **Acesso:** Gratuito

5. **Autismo & Realidade**
   - **URL:** https://autismoerealidade.org.br
   - **Tipo:** Organização de pesquisa
   - **Conteúdo:** Estratégias pedagógicas para TEA
   - **Acesso:** Gratuito

---

## 🔧 Estratégias de Scraping

### 1. APIs (Recomendado)

**Vantagens:**
- ✅ Mais rápido e confiável
- ✅ Dados estruturados
- ✅ Respeita rate limits
- ✅ Menos chance de bloqueio

**APIs Disponíveis:**
- ERIC API (requer chave)
- PubMed E-utilities (gratuita)
- SciELO API (gratuita)
- JSTOR API (requer assinatura)

### 2. Web Scraping Direto

**Quando usar:**
- Sites sem API
- Organizações brasileiras
- Blogs e recursos educacionais

**Ferramentas:**
- BeautifulSoup (HTML parsing)
- Scrapy (framework completo)
- Playwright (SPAs dinâmicas)
- Firecrawl MCP (já configurado)

---

## 📝 Termos de Busca Recomendados

### Em Inglês:
- "ADHD educational intervention"
- "dyslexia reading intervention"
- "autism educational strategies"
- "neurodivergent students"
- "learning differences"
- "executive function education"
- "special educational needs"

### Em Português:
- "TDAH educação"
- "dislexia aprendizagem"
- "autismo educação"
- "neurodiversidade"
- "educação inclusiva"
- "dificuldades de aprendizagem"
- "estratégias pedagógicas TDAH"

---

## 🛠️ Implementação

### Script Base para ERIC

```python
import requests
from bs4 import BeautifulSoup

def search_eric(query, api_key=None):
    """Busca papers no ERIC"""
    base_url = "https://api.ies.ed.gov/eric/"
    params = {
        "search": query,
        "format": "json"
    }
    if api_key:
        params["key"] = api_key
    
    response = requests.get(base_url, params=params)
    return response.json()
```

### Script Base para PubMed

```python
import requests
from xml.etree import ElementTree as ET

def search_pubmed(query, max_results=100):
    """Busca papers no PubMed"""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    # Buscar IDs
    search_url = f"{base_url}esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(search_url, params=params)
    ids = response.json()["esearchresult"]["idlist"]
    
    # Buscar detalhes
    fetch_url = f"{base_url}efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    response = requests.get(fetch_url, params=params)
    return ET.fromstring(response.content)
```

### Script Base para SciELO

```python
import requests

def search_scielo(query, lang="pt"):
    """Busca papers no SciELO"""
    api_url = "https://api.scielo.org/v1/"
    params = {
        "q": query,
        "lang": lang,
        "format": "json"
    }
    response = requests.get(api_url, params=params)
    return response.json()
```

---

## 📦 Estrutura de Dados

### Formato JSON para Papers

```json
{
  "title": "Intervenções Educacionais para Estudantes com TDAH",
  "abstract": "Resumo do paper...",
  "authors": ["Autor 1", "Autor 2"],
  "publication_date": "2024-01-15",
  "doi": "10.1234/example",
  "source_url": "https://example.com/paper",
  "pdf_url": "https://example.com/paper.pdf",
  "keywords": ["TDAH", "educação", "intervenção"],
  "neurodivergence_type": "TDAH",
  "educational_level": "EF II",
  "subject_area": "geral",
  "intervention_type": "estratégia pedagógica",
  "language": "pt-BR",
  "full_text": "Texto completo do paper...",
  "citations": 15,
  "references": ["ref1", "ref2"]
}
```

---

## 🔄 Processamento para RAG

### Chunking de Papers

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_paper(paper_text, chunk_size=2000, chunk_overlap=400):
    """Divide paper em chunks para RAG"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = splitter.split_text(paper_text)
    return chunks
```

### Adicionar Metadados aos Chunks

```python
def add_metadata_to_chunks(chunks, paper_metadata):
    """Adiciona metadados aos chunks"""
    chunks_with_metadata = []
    for i, chunk in enumerate(chunks):
        chunk_data = {
            "text": chunk,
            "chunk_index": i,
            "paper_title": paper_metadata["title"],
            "authors": paper_metadata["authors"],
            "neurodivergence_type": paper_metadata["neurodivergence_type"],
            "subject_area": paper_metadata["subject_area"],
            "source": paper_metadata["source_url"]
        }
        chunks_with_metadata.append(chunk_data)
    return chunks_with_metadata
```

---

## 📋 Checklist de Implementação

- [ ] Configurar APIs (chaves quando necessário)
- [ ] Criar scrapers para cada fonte prioritária
- [ ] Implementar busca com termos relevantes
- [ ] Processar e estruturar dados
- [ ] Adicionar metadados (tipo de neurodivergência, nível educacional)
- [ ] Chunking para RAG
- [ ] Ingestão no ChromaDB
- [ ] Testar recuperação de informações

---

## ⚠️ Considerações Legais e Éticas

1. **Respeitar robots.txt** - Sempre verificar antes de fazer scraping
2. **Rate Limiting** - Não sobrecarregar servidores
3. **Termos de Uso** - Verificar políticas de cada site
4. **Copyright** - Respeitar direitos autorais dos papers
5. **Uso Educacional** - Garantir uso apenas para fins educacionais

---

## 🔗 Links Úteis

- **ERIC API Docs:** https://eric.ed.gov/?api
- **PubMed API Docs:** https://www.ncbi.nlm.nih.gov/books/NBK25497/
- **SciELO API Docs:** https://api.scielo.org/docs/
- **Firecrawl MCP:** Já configurado no projeto

---

## 📚 Próximos Passos

1. Implementar scrapers para fontes prioritárias
2. Configurar pipeline de processamento
3. Integrar com sistema RAG existente
4. Criar interface para busca de papers
5. Monitorar qualidade dos dados coletados

---

**Última Atualização:** 2025-01-08
