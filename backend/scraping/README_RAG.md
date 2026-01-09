# 📚 Guia Rápido: Popular RAG com Conteúdo Educacional

## 🚀 Comando Mais Rápido

```bash
# Verificar se tudo está OK
python -m backend.scraping.check_setup

# Popular RAG (MVP completo)
python -m backend.scraping.populate_rag --phase mvp
```

**Pronto!** Isso vai coletar conteúdo das 3 fontes prioritárias e adicionar ao RAG.

---

## 📋 O Que Acontece

1. **API BNCC Cientificar** → Estrutura curricular completa
2. **Projeto Ágatha Edu** → Questões ENEM/vestibulares (50 páginas)
3. **Nova Escola** → Planos de aula (100 páginas)

Tudo é processado, dividido em chunks e adicionado ao ChromaDB (RAG).

---

## ⚙️ Pré-requisitos

### 1. Variáveis de Ambiente

```bash
export FIRECRAWL_API_KEY='fc-d9e38b1898aa4067be99276054db16be'
export DATABASE_URL='postgresql://user:pass@localhost/dbname'  # Se usar PostgreSQL
export SECRET_KEY='sua-secret-key-aqui'
```

### 2. ChromaDB Rodando

```bash
# Instalar ChromaDB
pip install chromadb

# Iniciar servidor
chroma run --host localhost --port 8000
```

### 3. Dependências

```bash
pip install -r backend/requirements.txt
```

---

## 🎯 Opções de Execução

### Opção 1: MVP Completo (Recomendado para começar)

```bash
python -m backend.scraping.populate_rag --phase mvp
```

### Opção 2: Apenas Conteúdo Cultural

```bash
python -m backend.scraping.populate_rag --phase cultural
```

### Opção 3: Tudo (MVP + Cultural)

```bash
python -m backend.scraping.populate_rag --phase all
```

### Opção 4: Verificar Status do RAG

```bash
python -m backend.scraping.populate_rag --phase verify
```

### Opção 5: Testar Recuperação

```bash
python -m backend.scraping.populate_rag --phase test --test-query "equações de segundo grau"
```

---

## 📊 Monitoramento

O script mostra progresso em tempo real:

```
[1/3] Coletando dados da API BNCC Cientificar...
✓ BNCC: 150 chunks coletados

[2/3] Coletando questões do Projeto Ágatha Edu...
✓ Projeto Ágatha: 320 chunks coletados

[3/3] Coletando planos de aula da Nova Escola...
✓ Nova Escola: 450 chunks coletados

📚 Adicionando 920 chunks ao RAG...
✓ Documentos adicionados ao RAG com sucesso!
```

---

## 🔧 Troubleshooting

### ChromaDB não conecta

```bash
# Verificar se está rodando
curl http://localhost:8000/api/v1/heartbeat

# Iniciar se não estiver
chroma run --host localhost --port 8000
```

### Firecrawl não funciona

```bash
# Verificar API key
echo $FIRECRAWL_API_KEY

# Usar scrapers tradicionais
python -m backend.scraping.populate_rag --phase mvp --no-firecrawl
```

### Poucos documentos coletados

- Aumentar `max_pages` gradualmente
- Verificar logs para erros específicos
- Testar scraping manual de uma URL

---

## 📈 Próximos Passos Após Popular

1. **Testar Queries**
   ```python
   from backend.app.core.rag.retriever import RAGRetriever
   
   retriever = RAGRetriever()
   results = retriever.retrieve("matemática básica", n_results=5)
   ```

2. **Integrar com API**
   - Usar RAGRetriever na API
   - Criar endpoints para queries
   - Testar com frontend

3. **Otimizar**
   - Ajustar chunk_size
   - Melhorar metadados
   - Adicionar filtros

---

## 📚 Documentação Completa

- [Próximos Passos Detalhados](./PROXIMOS_PASSOS_RAG.md)
- [Guia do Firecrawl](./FIRECRAWL_GUIDE.md)
- [README do Scraping](./README.md)

---

**Tempo estimado para MVP:** 30-60 minutos
