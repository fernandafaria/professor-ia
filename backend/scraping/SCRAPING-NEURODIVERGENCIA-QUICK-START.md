# 🚀 Quick Start - Scraping de Papers sobre Neurodivergências

## 📋 O Que Foi Criado

1. **`neurodivergence_sources.yaml`** - Configuração completa de fontes acadêmicas
2. **`scrapers/academic.py`** - Scrapers para ERIC, PubMed e SciELO
3. **`GUIA-SCRAPING-NEURODIVERGENCIA.md`** - Guia completo

---

## 🎯 Fontes Prioritárias

### 🔴 Críticas (Implementadas)

1. **ERIC** - Base de dados educacional
2. **PubMed** - Papers biomédicos e educacionais
3. **SciELO Brasil** - Papers em português

### 🟡 Alta Prioridade (A Implementar)

4. **Instituto ABCD** - Pesquisas sobre dislexia e TDAH
5. **Autismo & Realidade** - Estratégias para TEA

---

## 💻 Uso Rápido

### Exemplo: Buscar Papers no PubMed

```python
from backend.scraping.scrapers.academic import PubMedScraper

scraper = PubMedScraper()

# Buscar papers sobre TDAH e educação
papers = scraper.search_papers(
    query="ADHD educational intervention",
    max_results=20,
    neurodivergence_type="ADHD"
)

for paper in papers:
    print(f"Título: {paper['title']}")
    print(f"Autores: {', '.join(paper['authors'])}")
    print(f"Abstract: {paper['abstract'][:200]}...")
    print("---")
```

### Exemplo: Buscar Papers no SciELO

```python
from backend.scraping.scrapers.academic import SciELOScraper

scraper = SciELOScraper()

# Buscar papers em português sobre dislexia
papers = scraper.search_papers(
    query="dislexia aprendizagem",
    max_results=20
)

for paper in papers:
    print(f"Título: {paper['title']}")
    print(f"URL: {paper['source_url']}")
    print("---")
```

### Exemplo: Buscar Papers no ERIC

```python
from backend.scraping.scrapers.academic import ERICScraper

# Com API key (recomendado)
scraper = ERICScraper(api_key="sua_chave_aqui")

# Sem API key (web scraping)
scraper = ERICScraper()

papers = scraper.search_papers(
    query="neurodivergent students learning strategies",
    max_results=20
)
```

---

## 🔑 Obter Chaves de API

### ERIC API Key
1. Acesse: https://api.ies.ed.gov/
2. Registre-se para obter chave gratuita
3. Use no código: `ERICScraper(api_key="sua_chave")`

### PubMed
- ✅ **Não requer chave** - API pública e gratuita

### SciELO
- ✅ **Não requer chave** - API pública e gratuita

---

## 📊 Processar e Salvar Papers

```python
from backend.scraping.scrapers.academic import PubMedScraper
import json

scraper = PubMedScraper()
papers = scraper.search_papers("ADHD education", max_results=50)

# Salvar em JSON
with open("papers_neurodivergencia.json", "w", encoding="utf-8") as f:
    json.dump(papers, f, ensure_ascii=False, indent=2)

print(f"✅ {len(papers)} papers salvos!")
```

---

## 🔄 Integrar com RAG

```python
from backend.scraping.scrapers.academic import PubMedScraper
from backend.scraping.populate_rag import add_papers_to_rag

scraper = PubMedScraper()
papers = scraper.search_papers("dyslexia intervention", max_results=20)

# Adicionar ao RAG
for paper in papers:
    add_papers_to_rag(paper)
```

---

## 📝 Termos de Busca Recomendados

### Inglês:
- "ADHD educational intervention"
- "dyslexia reading intervention"
- "autism educational strategies"
- "neurodivergent students"
- "learning differences"

### Português:
- "TDAH educação"
- "dislexia aprendizagem"
- "autismo educação"
- "neurodiversidade"
- "educação inclusiva"

---

## ⚠️ Considerações

1. **Rate Limiting** - Respeite delays entre requisições
2. **Robots.txt** - Sempre verificar antes de fazer scraping
3. **Copyright** - Respeitar direitos autorais
4. **Uso Educacional** - Garantir uso apenas para fins educacionais

---

## 📚 Próximos Passos

1. Obter chave de API do ERIC (opcional)
2. Testar scrapers com buscas específicas
3. Processar papers coletados
4. Integrar com sistema RAG
5. Adicionar mais fontes (Instituto ABCD, Autismo & Realidade)

---

**Documentação Completa:** `GUIA-SCRAPING-NEURODIVERGENCIA.md`
