# Como Verificar os Logs do Cursor para Diagnosticar o Erro

## 🔍 Passos para Verificar os Logs do Cursor

### 1. Abrir os Logs do Cursor

**No macOS:**

1. Abra o Cursor
2. Pressione `Cmd + Shift + P` para abrir a paleta de comandos
3. Digite: `Output: Focus on Output View`
4. Selecione a opção

**Ou via Menu:**

1. Vá em **View > Output** (ou `Cmd + Shift + U`)
2. No dropdown do painel de Output, selecione **"MCP Logs"** ou **"MCP"**

### 2. Verificar os Logs do Scientific Calculator

Nos logs, procure por:

- Mensagens relacionadas a `scientific-calculator`
- Erros relacionados a Python
- Mensagens de conexão MCP
- Qualquer traceback de erro Python

### 3. Verificar a Configuração do Cursor

**Via Interface:**

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `scientific-calculator` aparece na lista
4. Verifique o status (Connected, Error, etc.)
5. Clique no servidor para ver detalhes e logs

**Via Arquivo de Configuração:**

O arquivo de configuração está em:
```
/Users/fernandafaria/Downloads/P1A/.cursor/mcp.json
```

### 4. Copiar a Mensagem de Erro Específica

Quando encontrar o erro nos logs:

1. **Copie a mensagem de erro completa**
2. Inclua:
   - A mensagem de erro
   - O traceback (se houver)
   - Qualquer linha relacionada ao `scientific-calculator`

**Exemplo de formato para compartilhar:**

```
Erro: [data/hora]
Servidor: scientific-calculator
Mensagem: [mensagem de erro aqui]
Traceback: [traceback completo, se houver]
```

## 📋 Checklist de Verificação

- [ ] Logs do Cursor abertos (`Cmd + Shift + U`)
- [ ] Dropdown configurado para "MCP Logs" ou "MCP"
- [ ] Procurado por `scientific-calculator` nos logs
- [ ] Mensagem de erro identificada
- [ ] Erro copiado completo (incluindo traceback se houver)
- [ ] Configuração do Cursor verificada (Features > MCP)
- [ ] Status do servidor verificado

## 🔧 Erros Comuns e Possíveis Soluções

### Erro: "command not found"

**Causa:** Caminho do Python incorreto

**Solução:** Verifique se o caminho em `.cursor/mcp.json` está correto:
```json
"command": "/Library/Developer/CommandLineTools/usr/bin/python3"
```

### Erro: "ModuleNotFoundError"

**Causa:** Pacote não instalado ou Python incorreto

**Solução:**
```bash
/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install mcp-scientific-calculator
```

### Erro: "Permission denied"

**Causa:** Arquivo ou diretório sem permissão

**Solução:**
```bash
chmod +x mcp_calculator_wrapper.sh
```

### Erro: Timeout ou "Server not responding"

**Causa:** Servidor não está iniciando corretamente

**Solução:** Teste manualmente:
```bash
python3 test_mcp_server.py
```

## 📝 Informações para Compartilhar

Se o erro persistir, compartilhe:

1. **Mensagem de erro completa** dos logs do Cursor
2. **Conteúdo do arquivo** `.cursor/mcp.json`
3. **Saída do teste:**
   ```bash
   python3 test_mcp_server.py
   ```
4. **Versão do Cursor** (Help > About Cursor)
5. **Sistema Operacional** e versão

## 🎯 Próximos Passos Após Identificar o Erro

1. **Se o erro for de caminho:** Use o caminho correto em `.cursor/mcp.json`
2. **Se o erro for de módulo:** Reinstale o pacote com o Python correto
3. **Se o erro for de permissão:** Ajuste as permissões dos arquivos
4. **Se o erro for de protocolo:** Verifique a versão do protocolo MCP

---

**Última Atualização:** 2025-01-08
