# Solução para Erro do Scientific Calculator MCP

## ✅ Diagnóstico

O servidor **está funcionando corretamente**! O teste confirmou que ele responde adequadamente ao protocolo MCP.

O problema está na **configuração do Cursor**, não no servidor.

## 🔍 Possíveis Causas do Erro no Cursor

### 1. Caminho do Python incorreto
O Cursor pode não estar encontrando o `python3` no PATH.

### 2. Versão do protocolo MCP
O Cursor pode estar usando uma versão específica do protocolo MCP que precisa ser respeitada.

### 3. Formato de configuração
A configuração pode precisar de ajustes específicos para o Cursor.

## 🚀 Soluções

### Solução 1: Usar caminho absoluto do Python

Atualize o `.cursor/mcp.json` para usar o caminho absoluto do Python:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "scientific-calculator": {
      "command": "/usr/bin/python3",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {}
    }
  }
}
```

**Para encontrar o caminho correto do Python:**
```bash
which python3
```

### Solução 2: Usar script wrapper

Crie um script wrapper para garantir que o servidor inicie corretamente:

1. Crie o arquivo `mcp_calculator_wrapper.sh`:

```bash
#!/bin/bash
exec /usr/bin/python3 -m mcp_scientific_calculator "$@"
```

2. Torne-o executável:

```bash
chmod +x mcp_calculator_wrapper.sh
```

3. Atualize o `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "/caminho/absoluto/para/P1A/mcp_calculator_wrapper.sh",
      "args": [],
      "env": {}
    }
  }
}
```

### Solução 3: Verificar logs do Cursor

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique os logs de erro para o servidor `scientific-calculator`
4. Os logs devem mostrar o erro específico

### Solução 4: Reinstalar o pacote

Se o problema persistir, tente reinstalar o pacote:

```bash
pip3 uninstall mcp-scientific-calculator
pip3 install mcp-scientific-calculator
```

### Solução 5: Verificar versão do Cursor

Certifique-se de que está usando uma versão atualizada do Cursor que suporta MCP STDIO servers.

## 🔍 Verificação da Configuração

Execute o teste do servidor para confirmar que está funcionando:

```bash
python3 test_mcp_server.py
```

Se o teste passar (✅), o servidor está funcionando e o problema está na configuração do Cursor.

## 📝 Configuração Recomendada

Após encontrar o caminho correto do Python, use esta configuração no `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "scientific-calculator": {
      "command": "/usr/bin/python3",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

**Nota:** Adicione `PYTHONUNBUFFERED=1` ao `env` para garantir que a saída seja não-bufferizada, o que pode ajudar com problemas de comunicação via STDIO.

## 🎯 Próximos Passos

1. **Identifique o erro específico** nos logs do Cursor
2. **Use o caminho absoluto** do Python no `.cursor/mcp.json`
3. **Adicione `PYTHONUNBUFFERED=1`** ao ambiente
4. **Reinicie completamente o Cursor**
5. **Verifique a conexão** nas configurações do Cursor

## 📚 Recursos

- **Documentação MCP:** https://modelcontextprotocol.io/
- **Cursor MCP Docs:** https://docs.cursor.com/context/mcp
- **Teste do Servidor:** `python3 test_mcp_server.py`
- **Documentação Completa:** `_docs/CONFIGURACAO-SYMPY-MCP.md`

---

**Última Atualização:** 2025-01-08
