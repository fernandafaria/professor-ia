# 🚀 Guia de Setup do ChromaDB

Guia rápido para iniciar e gerenciar o servidor ChromaDB para o sistema RAG da Plataforma Educacional P1A.

---

## 📋 Pré-requisitos

- Python 3.9+
- ChromaDB instalado: `pip3 install chromadb`

---

## 🚀 Iniciar ChromaDB

### Opção 1: Modo Interativo (Recomendado para desenvolvimento)

```bash
./iniciar_chromadb.sh
```

Este comando:
- ✅ Verifica se ChromaDB está instalado
- ✅ Verifica se já está rodando
- ✅ Inicia o servidor na porta 8000
- ✅ Mantém o terminal aberto (mostra logs em tempo real)

**Para parar:** Pressione `Ctrl+C`

### Opção 2: Modo Background (Recomendado para produção)

```bash
./iniciar_chromadb.sh --background
# ou
./iniciar_chromadb.sh -b
```

Este comando:
- ✅ Inicia ChromaDB em background
- ✅ Salva o PID em `chroma.pid`
- ✅ Salva logs em `chroma.log`
- ✅ Libera o terminal

**Para parar:** `./parar_chromadb.sh`

---

## 🔍 Verificar Status

```bash
./verificar_chromadb.sh
```

Mostra:
- ✅ Se o ChromaDB está rodando
- ✅ URL do servidor
- ✅ Collections disponíveis
- ✅ Status de conectividade

---

## 🛑 Parar ChromaDB

```bash
./parar_chromadb.sh
```

Este comando:
- ✅ Para o processo usando o PID salvo
- ✅ Limpa processos na porta 8000
- ✅ Remove arquivo de PID

---

## ⚙️ Configuração

As configurações são lidas do arquivo `.env`:

```env
CHROMA_HOST=localhost
CHROMA_PORT=8000
CHROMA_COLLECTION_NAME=educational_content
```

Ou você pode exportar antes de executar:

```bash
export CHROMA_HOST=localhost
export CHROMA_PORT=8000
./iniciar_chromadb.sh
```

---

## 📁 Estrutura de Arquivos

```
P1A/
├── iniciar_chromadb.sh      # Script para iniciar
├── parar_chromadb.sh         # Script para parar
├── verificar_chromadb.sh     # Script para verificar status
├── chroma_db/                # Diretório de dados (criado automaticamente)
├── chroma.pid                # PID do processo (se rodando em background)
└── chroma.log                # Logs (se rodando em background)
```

---

## 🔧 Troubleshooting

### ChromaDB não inicia

1. **Verificar se a porta está livre:**
   ```bash
   lsof -i :8000
   ```

2. **Verificar se ChromaDB está instalado:**
   ```bash
   pip3 list | grep chromadb
   ```

3. **Reinstalar ChromaDB:**
   ```bash
   pip3 install --upgrade chromadb
   ```

### Porta 8000 em uso

Se a porta 8000 estiver em uso, você pode:

1. **Mudar a porta no `.env`:**
   ```env
   CHROMA_PORT=8001
   ```

2. **Ou matar o processo que está usando a porta:**
   ```bash
   lsof -ti:8000 | xargs kill
   ```

### Ver logs em background

Se o ChromaDB está rodando em background:

```bash
tail -f chroma.log
```

---

## ✅ Verificar se está funcionando

Depois de iniciar, teste com:

```bash
curl http://localhost:8000/api/v1/heartbeat
```

Ou use o script de verificação:

```bash
./verificar_chromadb.sh
```

---

## 📚 Próximos Passos

Após iniciar o ChromaDB:

1. **Popular o RAG:**
   ```bash
   python -m backend.scraping.populate_rag --phase mvp
   ```

2. **Verificar setup completo:**
   ```bash
   python -m backend.scraping.check_setup
   ```

3. **Testar recuperação:**
   ```python
   from backend.app.core.rag.retriever import RAGRetriever
   
   retriever = RAGRetriever()
   results = retriever.retrieve("matemática básica", n_results=5)
   print(results)
   ```

---

## 🎯 Resumo de Comandos

```bash
# Iniciar (modo interativo)
./iniciar_chromadb.sh

# Iniciar (background)
./iniciar_chromadb.sh --background

# Verificar status
./verificar_chromadb.sh

# Parar
./parar_chromadb.sh

# Ver logs (se em background)
tail -f chroma.log
```

---

**Última atualização:** 2026-01-08
