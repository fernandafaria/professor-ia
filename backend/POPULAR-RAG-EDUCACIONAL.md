# 📚 Popular RAG com Conteúdo Educacional

**Status Atual:** Apenas papers sobre neurodivergência foram adicionados (6 documentos)

**Falta:** Conteúdo educacional (BNCC, planos de aula, questões, etc.)

---

## 📊 Status Atual do RAG

```
📊 Documentos no RAG por fonte:
   PubMed: 6 documentos (apenas papers sobre neurodivergência)
```

**Não há conteúdo educacional ainda!**

---

## 🎯 Opções para Adicionar Conteúdo Educacional

### Opção 1: Usar Pipeline Completo (Recomendado)

O script `populate_rag.py` pode coletar e adicionar conteúdo educacional automaticamente:

```bash
cd backend/scraping
python3 populate_rag.py --phase mvp
```

**O que ele faz:**
1. **API BNCC Cientificar** - Estrutura curricular
2. **Projeto Ágatha Edu** - Questões ENEM/vestibulares
3. **Nova Escola** - Planos de aula

**⚠️ Nota:** Isso faz scraping em tempo real, pode demorar.

---

### Opção 2: Importar Dados BNCC de Arquivo JSON

Se você já tem dados BNCC coletados em JSON:

```bash
cd backend/scraping
python3 -m importers.bncc_json_importer [caminho-do-arquivo.json] --add-to-rag
```

**Exemplo:**
```bash
python3 -m importers.bncc_json_importer data/bncc_data.json --add-to-rag
```

---

### Opção 3: Usar Script de Importação BNCC

```bash
cd backend/scraping
python3 import_bncc_data.py [arquivo.json] --add-to-rag
```

---

## 🔍 Verificar se Há Dados Educacionais Coletados

```bash
# Procurar arquivos JSON com dados educacionais
find backend/data -name "*.json" -type f
find . -name "*bncc*.json" -o -name "*educacional*.json"
```

---

## 📝 Próximos Passos

### 1. Verificar Dados Disponíveis

Primeiro, vamos verificar se há arquivos JSON com dados educacionais já coletados:

```bash
cd /Users/fernandafaria/Downloads/P1A
find . -name "*bncc*.json" -o -name "*educacional*.json" -o -name "*bncc*.json"
```

### 2. Se Não Houver Dados Coletados

Você pode:

**A) Coletar dados agora:**
```bash
cd backend/scraping
python3 populate_rag.py --phase mvp
```

**B) Usar API BNCC diretamente:**
```bash
cd backend/scraping
python3 -m scrapers.bncc_api
```

### 3. Se Houver Dados Coletados

Importar para o RAG:
```bash
cd backend/scraping
python3 -m importers.bncc_json_importer [arquivo.json] --add-to-rag
```

---

## 🚀 Executar Agora

Quer que eu:
1. **Verifique se há dados educacionais coletados?**
2. **Execute o pipeline para coletar dados educacionais?**
3. **Crie um script para popular com todos os dados disponíveis?**

---

## 📋 Checklist

- [x] Papers sobre neurodivergência adicionados (6 documentos)
- [ ] Dados BNCC adicionados
- [ ] Planos de aula (Nova Escola) adicionados
- [ ] Questões educacionais (Projeto Ágatha) adicionadas
- [ ] Outro conteúdo educacional

---

**Resumo:** Atualmente o RAG tem apenas papers sobre neurodivergência. Para adicionar conteúdo educacional, precisamos executar o pipeline de scraping ou importar dados já coletados.
