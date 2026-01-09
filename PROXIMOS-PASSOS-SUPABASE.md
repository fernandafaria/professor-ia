# 🚀 Próximos Passos - Configurar Supabase

**Status:** ✅ Migração 99% completa  
**Falta:** Apenas configurar o `DATABASE_URL` no `.env`

---

## ✅ O que já está pronto

1. ✅ **Código migrado** - Todos os arquivos atualizados para usar Supabase
2. ✅ **Tabela `rag_documents`** - Já existe no Supabase
3. ✅ **pgvector** - Extensão instalada e funcionando
4. ✅ **Configurações** - ChromaDB removido, Supabase configurado

---

## ⚡ Ação Rápida (5 minutos)

### 1. Obter Connection String do Supabase

👉 **Link direto:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database

**Passos:**
1. Clique no link acima
2. Role até **Connection string**
3. Selecione a aba **URI**
4. Clique no botão **Copy** ao lado da string
5. A string será algo como:
   ```
   postgresql://postgres.mzhgkbdnslnlpfciduru:[YOUR-PASSWORD]@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
   ```

### 2. Atualizar o .env

Edite o arquivo `.env` na raiz do projeto:

```bash
# Abra o arquivo
code .env
# ou
nano .env
```

**Substitua esta linha:**
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/p1a_education
```

**Pela connection string do Supabase:**
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA_AQUI@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**⚠️ Importante:**
- Substitua `[YOUR-PASSWORD]` ou `SUA_SENHA_AQUI` pela senha do banco
- Se você não lembra a senha, pode resetá-la no dashboard:
  - Settings → Database → Database password → Reset database password

### 3. Copiar para backend/.env

```bash
cp .env backend/.env
```

### 4. Verificar

```bash
cd /Users/fernandafaria/Downloads/P1A
PYTHONPATH=/Users/fernandafaria/Downloads/P1A/backend:$PYTHONPATH python3 backend/scraping/check_setup.py
```

**Resultado esperado:**
```
SUPABASE: ✅ OK
  ✅ Supabase: Conectado
  ✅ Tabela rag_documents: Existe
  ✅ pgvector: Instalado
  ✅ Documentos: 0
```

---

## 📚 Documentação Criada

### Guias Completos

1. **`CONFIGURAR-DATABASE-URL.md`** - Guia detalhado passo a passo
2. **`MIGRACAO-CHROMADB-TO-SUPABASE.md`** - Documentação completa da migração
3. **`RESUMO-MIGRACAO-SUPABASE.md`** - Resumo executivo

### Links Úteis

- **Supabase Dashboard:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru
- **Connection String:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database
- **Table Editor:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru/editor

---

## 🎯 Depois de Configurar

### 1. Popular o RAG

```bash
# Popular com fontes MVP
python -m backend.scraping.populate_rag --phase mvp

# Ou importar dados BNCC
python -m backend.scraping.import_bncc_data "scraping/extract-data-2026-01-08 (1).json"
```

### 2. Verificar Documentos no Supabase

1. Acesse: https://app.supabase.com/project/mzhgkbdnslnlpfciduru/editor
2. Clique na tabela `rag_documents`
3. Veja os documentos adicionados

### 3. Testar Busca RAG

```python
from app.core.rag.retriever_supabase import RAGRetriever
from app.services.database import get_db

# Obter sessão do banco
db = next(get_db())

# Criar retriever
retriever = RAGRetriever()

# Buscar documentos
results = retriever.retrieve(
    query="equações de segundo grau",
    db=db,
    n_results=5,
    filters={"subject": "matematica"}  # Opcional
)

print(f"Encontrados {len(results)} documentos")
for doc in results:
    print(f"- {doc.get('content', '')[:100]}...")

# Fechar sessão
db.close()
```

---

## ✅ Checklist Final

- [ ] Obtenho connection string do Supabase Dashboard
- [ ] Atualizo `DATABASE_URL` no `.env`
- [ ] Copio `.env` para `backend/.env`
- [ ] Executo `check_setup.py` e vejo "SUPABASE: ✅ OK"
- [ ] Popular RAG pela primeira vez
- [ ] Verificar documentos no Supabase Dashboard

---

## 🆘 Precisa de Ajuda?

### Problema: Não consigo acessar o dashboard

**Solução:** Verifique se você está logado na conta correta do Supabase

### Problema: Connection string não funciona

**Solução:** 
1. Verifique se copiou a string completa
2. Verifique se a senha está correta
3. Tente resetar a senha do banco no dashboard

### Problema: Erro de conexão

**Solução:** Consulte `CONFIGURAR-DATABASE-URL.md` → Seção "Problemas Comuns"

---

**Pronto! Depois de configurar o DATABASE_URL, você estará 100% pronto para usar o RAG com Supabase!** 🎉
