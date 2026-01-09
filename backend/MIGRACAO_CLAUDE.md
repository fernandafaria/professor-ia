# ✅ Migração para Claude API (Anthropic)

## O que foi alterado

### 1. ✅ LLMService atualizado
- Substituído `AsyncOpenAI` por `AsyncAnthropic`
- Atualizado formato de mensagens (Claude usa system separado)
- Streaming atualizado para API do Claude
- Metadata de tokens ajustado (input_tokens + output_tokens)

### 2. ✅ Configurações atualizadas
- `ANTHROPIC_API_KEY` ao invés de `OPENAI_API_KEY`
- `ANTHROPIC_MODEL` configurável
- Modelo padrão: `claude-3-5-sonnet-20241022`

### 3. ✅ Requirements atualizado
- Adicionado `anthropic==0.34.2` (SDK oficial)
- Adicionado `langchain-anthropic==0.1.0` (opcional, para integração LangChain)
- `openai` mantido apenas para embeddings (opcional)

### 4. ✅ env.example atualizado
- Instruções para obter chave da Anthropic
- Modelos disponíveis documentados

## 📋 Próximos Passos

### 1. Instalar dependências

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
pip install anthropic==0.34.2
# ou
pip install -r requirements.txt
```

### 2. Obter API Key da Anthropic

1. Acesse: https://console.anthropic.com/
2. Faça login ou crie uma conta
3. Vá em **API Keys**
4. Crie uma nova chave
5. Copie a chave (formato: `sk-ant-...`)

### 3. Configurar .env

Edite `backend/.env`:

```env
ANTHROPIC_API_KEY=sk-ant-sua-chave-aqui
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

### 4. Testar

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
uvicorn app.main:app --reload --port 8000
```

Teste em: http://localhost:8000/docs

## 🎯 Modelos Disponíveis

### Claude 3.5 Sonnet (Recomendado)
- **Modelo:** `claude-3-5-sonnet-20241022`
- **Melhor custo-benefício**
- **Excelente para educação**
- **Suporte a português nativo**

### Claude 3 Opus
- **Modelo:** `claude-3-opus-20240229`
- **Melhor qualidade**
- **Mais caro**
- **Ideal para casos complexos**

### Claude 3 Haiku
- **Modelo:** `claude-3-haiku-20240307`
- **Mais rápido e barato**
- **Bom para respostas simples**

## 🔄 Diferenças da API

### OpenAI vs Claude

**OpenAI:**
```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
]
response = client.chat.completions.create(...)
```

**Claude:**
```python
system = "..."  # Separado
messages = [
    {"role": "user", "content": "..."}
]
response = client.messages.create(
    system=system,
    messages=messages,
    ...
)
```

### Streaming

**OpenAI:**
```python
stream = await client.chat.completions.create(..., stream=True)
async for chunk in stream:
    yield chunk.choices[0].delta.content
```

**Claude:**
```python
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        yield text
```

## ✅ Vantagens do Claude

1. **Melhor em português** - Treinado com mais dados em português
2. **Contexto maior** - Até 200k tokens de contexto
3. **Mais seguro** - Menos alucinações
4. **Melhor para educação** - Respostas mais didáticas
5. **Custo-benefício** - Claude 3.5 Sonnet é competitivo

## 📝 Notas

- O sistema RAG continua funcionando normalmente
- Embeddings podem usar sentence-transformers (local) ou OpenAI (opcional)
- Todos os endpoints permanecem iguais
- Apenas o backend LLM foi alterado

---

**Migração concluída!** 🎉
