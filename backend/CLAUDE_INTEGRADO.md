# ✅ Claude API Integrado

## Status: Migração Completa

A integração com Claude API (Anthropic) foi concluída com sucesso!

## 🔄 O que mudou

### Antes (OpenAI)
- SDK: `openai`
- Modelo: `gpt-4-turbo-preview`
- Variável: `OPENAI_API_KEY`

### Agora (Claude)
- SDK: `anthropic`
- Modelo: `claude-3-5-sonnet-20241022`
- Variável: `ANTHROPIC_API_KEY`

## 📋 Arquivos Modificados

1. ✅ `app/services/llm_service.py` - Migrado para Claude API
2. ✅ `app/config.py` - Configurações atualizadas
3. ✅ `requirements.txt` - Adicionado `anthropic==0.34.2`
4. ✅ `env.example` - Instruções atualizadas

## 🚀 Como Usar

### 1. Instalar dependência

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
pip install anthropic==0.34.2
```

### 2. Obter API Key

1. Acesse: https://console.anthropic.com/
2. Crie uma conta ou faça login
3. Vá em **API Keys**
4. Crie uma nova chave
5. Copie (formato: `sk-ant-...`)

### 3. Configurar .env

```env
ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

### 4. Testar

```bash
uvicorn app.main:app --reload --port 8000
```

Acesse: http://localhost:8000/docs

## 🎯 Modelos Disponíveis

| Modelo | Uso | Custo |
|--------|-----|-------|
| `claude-3-5-sonnet-20241022` | **Recomendado** - Melhor custo-benefício | Médio |
| `claude-3-opus-20240229` | Melhor qualidade | Alto |
| `claude-3-haiku-20240307` | Mais rápido e barato | Baixo |

## ✨ Vantagens do Claude

1. **Melhor em Português** - Treinado com mais dados em português brasileiro
2. **Contexto Maior** - Até 200k tokens de contexto
3. **Mais Seguro** - Menos alucinações e respostas mais precisas
4. **Ideal para Educação** - Respostas mais didáticas e explicativas
5. **Custo-Benefício** - Claude 3.5 Sonnet é competitivo

## 🔧 Funcionalidades Mantidas

- ✅ Chat com streaming
- ✅ Sistema RAG integrado
- ✅ Personalização por perfil
- ✅ Histórico de conversas
- ✅ Metadata de tokens e latência

## 📝 Notas Técnicas

### Diferenças na API

**OpenAI:**
```python
messages = [{"role": "system", ...}, {"role": "user", ...}]
response = await client.chat.completions.create(...)
```

**Claude:**
```python
system = "..."  # Separado
messages = [{"role": "user", ...}]
response = await client.messages.create(
    system=system,
    messages=messages,
    ...
)
```

### Streaming

O streaming funciona de forma similar, mas usa `async with` e `stream.text_stream`:

```python
async with client.messages.stream(...) as stream:
    async for text in stream.text_stream:
        yield text
```

## ⚠️ Importante

- **Embeddings**: Ainda pode usar OpenAI para embeddings (opcional) ou sentence-transformers (local)
- **Compatibilidade**: Todos os endpoints permanecem iguais
- **RAG**: Sistema RAG continua funcionando normalmente

---

**Integração concluída!** 🎉

Para mais detalhes, veja: `MIGRACAO_CLAUDE.md`
