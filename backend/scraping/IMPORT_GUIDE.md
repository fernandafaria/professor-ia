# Guia de Importação de Dados BNCC

Este guia explica como importar dados BNCC já coletados (como o arquivo `extract-data-2026-01-08 (1).json`) para o sistema RAG.

## Estrutura dos Dados

O arquivo JSON contém dados da BNCC organizados em categorias:

- **`fundamental_education`**: 1.408 itens do Ensino Fundamental
- **`high_school`**: 209 itens do Ensino Médio
- **Total**: 1.617 itens

Cada item contém:
- `code`: Código da habilidade BNCC (ex: "EF01LP01")
- `skill`: Descrição da habilidade
- `competency`: Competência relacionada
- `knowledge_object`: Objeto de conhecimento
- `*_citation`: URLs de referência

## Importação Rápida

### Via CLI

```bash
# Importar todos os dados
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"

# Importar apenas Ensino Fundamental
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --categories fundamental_education

# Importar apenas Ensino Médio
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --categories high_school

# Processar sem adicionar ao RAG (útil para validação)
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json" --no-rag
```

### Via Python

```python
from backend.scraping import BNCCJSONImporter

# Inicializar importador
importer = BNCCJSONImporter("scraping/extract-data-2026-01-08 (1).json")

# Importar todos os dados
stats = importer.import_data(
    categories=None,  # Todas as categorias
    chunk=True,  # Dividir em chunks para RAG
    add_to_rag=True,  # Adicionar ao ChromaDB
    batch_size=100,  # Processar em lotes
)

print(f"Processados: {stats['items_processed']} itens")
print(f"Criados: {stats['chunks_created']} chunks")
print(f"Adicionados ao RAG: {stats['added_to_rag']}")
```

## Processamento

O importador realiza as seguintes operações:

1. **Carregamento**: Lê o arquivo JSON
2. **Normalização**: Converte cada item em formato padrão
3. **Enriquecimento**: Extrai metadados (disciplina, série, nível)
4. **Chunking**: Divide conteúdo longo em chunks (1000 chars, overlap 200)
5. **Validação**: Filtra documentos por qualidade
6. **Indexação**: Adiciona ao ChromaDB com embeddings

## Metadados Extraídos

Para cada item, o sistema extrai automaticamente:

- **Disciplina**: Inferida do código (LP=Língua Portuguesa, MA=Matemática, etc.)
- **Série/Ano**: Inferida do código (EF01=1º ano, EF67=6º/7º ano, etc.)
- **Nível Educacional**: Ensino Fundamental ou Ensino Médio
- **Tipo**: Sempre "bncc_skill"
- **Citações**: URLs de referência preservadas

## Exemplo de Documento Processado

```json
{
  "id": "abc123_chunk_0",
  "content": "Habilidade: Reconhecer que textos são lidos...\n\nCompetência: Reconhecer o texto como lugar...\n\nObjeto de Conhecimento: Protocolos de leitura",
  "metadata": {
    "type": "bncc_skill",
    "code": "EF01LP01",
    "education_level": "Ensino Fundamental",
    "grade": "1º ano EF",
    "discipline": "Língua Portuguesa",
    "knowledge_object": "Protocolos de leitura",
    "source": "BNCC JSON Import",
    "source_url": "https://cientificar1992.pythonanywhere.com/bncc_fundamental/",
    "chunk_index": 0,
    "total_chunks": 1
  }
}
```

## Estatísticas Esperadas

Para o arquivo `extract-data-2026-01-08 (1).json`:

- **Itens processados**: ~1.617
- **Chunks criados**: ~1.617-3.000 (dependendo do tamanho do conteúdo)
- **Tempo estimado**: 5-15 minutos (dependendo do hardware)
- **Tamanho no RAG**: ~50-100 MB (com embeddings)

## Troubleshooting

### Erro: "Arquivo não encontrado"
- Verifique o caminho do arquivo
- Use caminho absoluto se necessário

### Erro: "Erro ao adicionar ao RAG"
- Verifique se o ChromaDB está rodando
- Verifique as configurações em `app/config.py`
- Tente processar sem adicionar ao RAG primeiro (`--no-rag`)

### Processamento lento
- Reduza o `batch_size` se houver problemas de memória
- Processe categorias separadamente
- Use `--no-rag` para apenas validar o processamento

## Próximos Passos

Após importar os dados:

1. **Validar**: Verificar se os documentos foram adicionados corretamente ao RAG
2. **Testar Busca**: Fazer queries de teste no sistema RAG
3. **Complementar**: Usar scrapers para adicionar mais conteúdo (questões, planos de aula)
4. **Monitorar**: Acompanhar qualidade das respostas geradas

## Integração com Scraping

Os dados importados podem ser complementados com scraping:

```python
from backend.scraping import ScrapingPipeline, BNCCJSONImporter

# 1. Importar dados BNCC existentes
importer = BNCCJSONImporter("scraping/extract-data-2026-01-08 (1).json")
importer.import_data(add_to_rag=True)

# 2. Adicionar questões do Projeto Ágatha
pipeline = ScrapingPipeline()
questions = pipeline.scrape_source("Projeto Ágatha Edu", max_questions=100)
pipeline.add_to_rag(questions)

# 3. Adicionar planos de aula da Nova Escola
lesson_plans = pipeline.scrape_source("Nova Escola", max_articles=50)
pipeline.add_to_rag(lesson_plans)
```
