# Configuração do Hugging Face MCP

**Criado em:** 2025-01-08  
**Status:** Configuração Inicial

---

## 📋 Visão Geral

O Hugging Face MCP Server permite que agentes de IA acessem diretamente o Hugging Face Hub, incluindo:
- **Modelos** - Buscar e acessar modelos de ML
- **Datasets** - Acessar datasets para treinamento
- **Spaces** - Usar aplicações Gradio hospedadas
- **Ferramentas da Comunidade** - Integrar com ferramentas MCP-compatíveis

---

## 🚀 Configuração Rápida

### 1. Configuração Aplicada

O arquivo `.cursor/mcp.json` já foi configurado com:

```json
{
  "mcpServers": {
    "huggingface": {
      "url": "https://huggingface.co/mcp",
      "transport": "sse"
    }
  }
}
```

### 2. Autenticação no Hugging Face

**IMPORTANTE:** Você precisa autenticar no Hugging Face:

1. **Acesse:** https://huggingface.co/settings/mcp
   - A página foi aberta automaticamente no navegador
   - Se não abriu, acesse manualmente

2. **Faça login** na sua conta Hugging Face (ou crie uma se necessário)

3. **Selecione seu cliente:** Escolha "Cursor" na lista

4. **Copie a configuração** fornecida (se houver token específico)

5. **Autentique** conforme as instruções na página

### 3. Reiniciar o Cursor

**IMPORTANTE:** Reinicie completamente o Cursor para aplicar a configuração:

1. Feche completamente o Cursor (`Cmd + Q`)
2. Abra novamente o Cursor

### 4. Verificar Conexão

Após reiniciar:

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `huggingface` aparece na lista
4. O status deve mostrar "Connected" ou similar

---

## 🎯 Como Usar

Após autenticar e conectar, você pode usar comandos como:

### Buscar Modelos

```
"Busque modelos do Hugging Face para Qwen 3 Quantizations"
"Encontre modelos de tradução português-inglês"
"Mostre modelos de geração de imagens"
```

### Buscar Datasets

```
"Encontre datasets sobre séries temporais de clima"
"Busque datasets de NLP em português"
"Mostre datasets de classificação de imagens"
```

### Buscar Spaces

```
"Encontre um Space que pode transcrever arquivos de áudio"
"Busque Spaces para geração de imagens"
"Mostre Spaces de análise de sentimentos"
```

### Usar Ferramentas

```
"Crie uma imagem 1024x1024 de um gato no estilo Ghibli"
"Transcreva este áudio"
"Analise o sentimento deste texto"
```

---

## 🔐 Autenticação

### Opção 1: Via Interface do Hugging Face (Recomendado)

1. Acesse: https://huggingface.co/settings/mcp
2. Faça login na sua conta
3. Selecione "Cursor" como cliente
4. Siga as instruções de autenticação
5. O token será configurado automaticamente

### Opção 2: Token Manual (Avançado)

Se você precisar configurar um token manualmente:

1. Obtenha seu token Hugging Face:
   - Acesse: https://huggingface.co/settings/tokens
   - Crie um novo token ou use um existente

2. Adicione ao `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "huggingface": {
      "url": "https://huggingface.co/mcp",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer hf_seu_token_aqui"
      }
    }
  }
}
```

**⚠️ Nota:** Não commite tokens no código! Use variáveis de ambiente quando possível.

---

## 🛠️ Ferramentas da Comunidade

O Hugging Face MCP suporta ferramentas da comunidade (Gradio Spaces com MCP):

### Adicionar Ferramentas

1. Acesse: https://huggingface.co/settings/mcp
2. Navegue até a seção de ferramentas da comunidade
3. Explore Spaces disponíveis com suporte MCP
4. Adicione as ferramentas desejadas
5. Reinicie o Cursor para reconhecer as novas ferramentas

### Exemplos de Ferramentas

- Geração de imagens
- Transcrição de áudio
- Análise de sentimentos
- Tradução
- E muitas outras...

---

## 🔍 Troubleshooting

### Problema: Servidor não conecta

**Soluções:**
1. Verifique se você está autenticado no Hugging Face
2. Certifique-se de que a URL está correta: `https://huggingface.co/mcp`
3. Verifique se o transport está como `sse`
4. Reinicie o Cursor completamente
5. Verifique os logs do Cursor em **Features > MCP**

### Problema: Autenticação falha

**Soluções:**
1. Acesse https://huggingface.co/settings/mcp
2. Verifique se você está logado
3. Refaça o processo de autenticação
4. Verifique se o token está válido (se usando token manual)

### Problema: Ferramentas não aparecem

**Soluções:**
1. Certifique-se de que adicionou ferramentas em https://huggingface.co/settings/mcp
2. Reinicie o Cursor completamente
3. Verifique se as ferramentas estão ativas nas configurações do Hugging Face

---

## 📚 Recursos

- **Hugging Face MCP Settings:** https://huggingface.co/settings/mcp
- **Hugging Face MCP Documentation:** https://huggingface.co/docs/hub/en/hf-mcp-server
- **Hugging Face Tokens:** https://huggingface.co/settings/tokens
- **MCP Protocol:** https://modelcontextprotocol.io/
- **Cursor MCP Docs:** https://docs.cursor.com/context/mcp

---

## ✅ Checklist de Configuração

- [x] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Página de configuração do Hugging Face acessada
- [ ] Login realizado no Hugging Face
- [ ] Cliente "Cursor" selecionado
- [ ] Autenticação completada
- [ ] Cursor reiniciado completamente
- [ ] Servidor conectado verificado
- [ ] Teste de uso realizado

---

**Última Atualização:** 2025-01-08  
**Status:** Configuração aplicada - Aguardando autenticação
