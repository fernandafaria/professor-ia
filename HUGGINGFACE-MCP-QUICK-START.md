# Hugging Face MCP - Quick Start

## ✅ Configuração Aplicada

O Hugging Face MCP foi configurado no `.cursor/mcp.json`:

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

---

## 🚀 Próximos Passos

### 1. Autenticar no Hugging Face

A página de configuração foi aberta no navegador: **https://huggingface.co/settings/mcp**

**Se não abriu, acesse manualmente:**
- URL: https://huggingface.co/settings/mcp

**No site:**
1. Faça login na sua conta Hugging Face (ou crie uma)
2. Selecione **"Cursor"** como cliente
3. Siga as instruções de autenticação
4. O token será configurado automaticamente

### 2. Reiniciar o Cursor

**IMPORTANTE:** Reinicie completamente o Cursor:

1. Feche completamente o Cursor (`Cmd + Q`)
2. Abra novamente o Cursor

### 3. Verificar Conexão

Após reiniciar:

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `huggingface` aparece na lista
4. Status deve mostrar "Connected"

---

## 🎯 Como Usar

Após conectar, você pode usar:

```
"Busque modelos do Hugging Face para tradução"
"Encontre datasets sobre séries temporais"
"Crie uma imagem de um gato no estilo Ghibli"
"Transcreva este áudio"
```

---

## 📚 Documentação

- **Configuração Completa:** `_docs/CONFIGURACAO-HUGGINGFACE-MCP.md`
- **Hugging Face MCP Settings:** https://huggingface.co/settings/mcp
- **Documentação Oficial:** https://huggingface.co/docs/hub/en/hf-mcp-server

---

**Status:** Configurado - Aguardando autenticação no Hugging Face
