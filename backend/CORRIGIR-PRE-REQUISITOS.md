# 🔧 Correção de Pré-requisitos - Chat com RAG

Baseado na verificação executada, aqui estão os problemas encontrados e como corrigi-los:

---

## ✅ O que já está OK

- ✅ Arquivo `.env` existe
- ✅ `DATABASE_URL` configurado
- ✅ `SECRET_KEY` configurado
- ✅ SQLAlchemy instalado
- ✅ Sentence Transformers instalado
- ✅ FastAPI instalado
- ✅ Modelo de embedding funcionando (384 dimensões)

---

## ❌ Problemas Encontrados

### 1. Python 3.9.6 (requer 3.10+)

**Status:** ⚠️ Versão atual: 3.9.6

**Solução:**

```bash
# Verificar versões disponíveis
python3 --version

# Se tiver Homebrew, instalar Python 3.10+
brew install python@3.10

# Ou usar pyenv
pyenv install 3.10.12
pyenv local 3.10.12

# Verificar
python3 --version  # Deve mostrar 3.10.x ou superior
```

**Nota:** Se não puder atualizar agora, o sistema pode funcionar com 3.9, mas algumas funcionalidades podem não estar disponíveis.

---

### 2. ANTHROPIC_API_KEY não configurado

**Status:** ❌ Chave da API não encontrada no `.env`

**Solução:**

1. **Obter chave da API:**
   - Acesse: https://console.anthropic.com/
   - Faça login ou crie uma conta
   - Vá em "API Keys"
   - Clique em "Create Key"
   - Copie a chave (formato: `sk-ant-...`)

2. **Adicionar ao `.env`:**
   ```bash
   cd backend
   # Edite o arquivo .env e adicione:
   ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
   ```

3. **Verificar:**
   ```bash
   python3 verificar_pre_requisitos_rag.py
   ```

---

### 3. Pacotes Python faltando

**Status:** ❌ `anthropic` e `python-dotenv` não instalados

**Solução:**

```bash
cd backend

# Instalar pacotes faltantes
pip3 install anthropic python-dotenv

# Ou instalar todas as dependências
pip3 install -r requirements.txt
```

**Verificar instalação:**
```bash
python3 -c "import anthropic; import dotenv; print('✅ Pacotes instalados')"
```

---

### 4. Problema de Conexão com Banco

**Status:** ⚠️ Tentando conectar em `localhost` ao invés do Supabase

**Possíveis causas:**

1. **DATABASE_URL pode estar apontando para localhost**
2. **Formato da URL pode estar incorreto**

**Solução:**

1. **Verificar DATABASE_URL no `.env`:**
   ```bash
   cd backend
   # Verifique se a URL está no formato correto:
   # postgresql://postgres.[PROJECT-REF]:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
   ```

2. **Obter URL correta do Supabase:**
   - Acesse: https://app.supabase.com/
   - Selecione seu projeto
   - Vá em **Settings → Database**
   - Copie a **Connection String** (modo URI)
   - Substitua `[YOUR-PASSWORD]` pela senha do seu banco

3. **Testar conexão:**
   ```bash
   python3 verificar_supabase.py
   ```

4. **Se ainda não funcionar, verificar:**
   - Senha do banco está correta?
   - Projeto Supabase está ativo?
   - Firewall/network não está bloqueando?

---

## 🚀 Passos Rápidos para Corrigir Tudo

Execute na ordem:

```bash
# 1. Ir para o diretório backend
cd /Users/fernandafaria/Downloads/P1A/backend

# 2. Instalar dependências faltantes
pip3 install anthropic python-dotenv

# 3. Verificar se .env tem ANTHROPIC_API_KEY
# (Edite manualmente se necessário)

# 4. Verificar DATABASE_URL
python3 verificar_supabase.py

# 5. Executar verificação completa novamente
python3 verificar_pre_requisitos_rag.py
```

---

## 📋 Checklist de Correção

Marque conforme corrigir:

- [ ] Python atualizado para 3.10+ (ou verificado que 3.9 funciona)
- [ ] `anthropic` instalado (`pip3 install anthropic`)
- [ ] `python-dotenv` instalado (`pip3 install python-dotenv`)
- [ ] `ANTHROPIC_API_KEY` adicionado ao `.env`
- [ ] `DATABASE_URL` verificado e corrigido se necessário
- [ ] Conexão com banco testada (`python3 verificar_supabase.py`)
- [ ] Verificação completa executada (`python3 verificar_pre_requisitos_rag.py`)

---

## 🧪 Testar Após Correções

Após corrigir os problemas, execute:

```bash
cd backend
python3 verificar_pre_requisitos_rag.py
```

Você deve ver:
```
✅ Todos os pré-requisitos estão configurados!
🎉 Você pode usar o chat com RAG agora!
```

---

## 📚 Próximos Passos

Depois que todos os pré-requisitos estiverem OK:

1. **Popular base RAG** (se ainda não tiver conteúdo):
   ```bash
   cd backend/scraping
   python3 populate_rag.py --phase mvp
   ```

2. **Iniciar servidor:**
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

3. **Testar chat:**
   - Via API: Use Postman ou curl
   - Via Frontend: Acesse a interface web

---

## 💡 Dicas

- **ANTHROPIC_API_KEY:** Se não tiver conta, crie em https://console.anthropic.com/ (pode ter créditos gratuitos)
- **DATABASE_URL:** Certifique-se de usar a URL do Supabase, não localhost
- **Python 3.9:** Pode funcionar, mas 3.10+ é recomendado para todas as funcionalidades

---

**Precisa de ajuda?** Consulte `CONFIGURAR-CHAT-RAG.md` para guia completo.
