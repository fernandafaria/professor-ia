# Configuração do Figma Make MCP

**Criado em:** 2025-01-08  
**Status:** Configuração Inicial

---

## 📋 Visão Geral

O Figma Make MCP permite que agentes de IA acessem e interajam com seus arquivos de design do Figma, fornecendo contexto essencial para geração de código. Esta integração aprimora os fluxos de trabalho permitindo:

- Geração de código a partir de frames selecionados
- Extração de contexto de design, incluindo variáveis e componentes
- Recuperação de recursos de código de arquivos Figma Make

---

## 🎯 Opções de Configuração

O Figma Make MCP oferece duas opções de servidor:

### 1. Remote MCP Server (Recomendado)

**Propósito:** Acessar arquivos de design via servidor hospedado pela Figma sem precisar do app desktop.

**Configuração no Cursor:**

No arquivo `.cursor/mcp.json` (ou configurações do Cursor), adicione:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    }
  }
}
```

**Configuração Manual no Cursor:**

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Clique em **Add MCP Server**
4. Configure:
   - **Name:** `figma-remote`
   - **Type:** `SSE` (Server-Sent Events)
   - **URL:** `https://mcp.figma.com/mcp`
5. Salve a configuração

**Autenticação:**

1. Abra seu arquivo Figma Design ou Make no navegador
2. Mude para **Dev Mode**
3. No painel de inspeção à direita, clique em **"Set up an MCP client"**
4. Siga o fluxo de autenticação OAuth conforme solicitado
5. Após autenticação bem-sucedida, o Cursor confirmará a conexão

**Recursos:**
- [Figma Remote MCP Server Documentation](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Figma Help Center - MCP Setup](https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server)

---

### 2. Desktop MCP Server

**Propósito:** Usar o app desktop do Figma para conexão local direta.

**Configuração no Cursor:**

```json
{
  "mcpServers": {
    "figma-desktop": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server"],
      "env": {
        "FIGMA_DESKTOP_PORT": "5555"
      }
    }
  }
}
```

**Instalação:**

1. Instale o app desktop do Figma: [Figma Desktop App](https://www.figma.com/downloads/)
2. Certifique-se de que o app está rodando
3. O servidor MCP será iniciado automaticamente

**Nota:** Requer que o Figma Desktop App esteja em execução.

**Recursos:**
- [Figma Desktop MCP Server Documentation](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)

---

## 🚀 Como Usar

### Após Configuração

Com o servidor MCP conectado, você pode:

1. **Gerar código de frames selecionados:**
   - Selecione um frame no Figma
   - Use comandos do Cursor para gerar código baseado no design

2. **Extrair contexto de design:**
   - Acesse variáveis e componentes do Figma
   - Use essas informações para alinhar código com design

3. **Recuperar recursos de código:**
   - Obtenha assets, estilos e especificações técnicas
   - Use em seu fluxo de desenvolvimento

### Exemplo de Uso

```
# No Cursor, você pode pedir:
"Gere código React para o frame selecionado no Figma"
"Extraia as variáveis de cor do design atual"
"Obtenha os estilos do componente Button do Figma"
```

---

## 🔒 Segurança e Considerações

⚠️ **Importante:** Esteja ciente de possíveis vulnerabilidades de segurança em integrações MCP de terceiros.

**Boas Práticas:**

1. **Versões Atualizadas:**
   - Sempre use as versões mais recentes de pacotes MCP relacionados
   - Mantenha o Figma Desktop App atualizado

2. **Autenticação:**
   - Use OAuth para autenticação (recomendado)
   - Não compartilhe tokens de acesso
   - Revise permissões regularmente

3. **Acesso a Arquivos:**
   - Apenas autorize acesso a arquivos necessários
   - Revise quais arquivos estão sendo acessados pelo MCP

4. **Monitoramento:**
   - Monitore atividades do MCP
   - Verifique logs regularmente

**Recursos de Segurança:**
- [Figma Security Documentation](https://www.figma.com/security/)
- Mantenha-se informado sobre atualizações de segurança

---

## 📝 Arquivos de Configuração

### Opção 1: Configuração JSON (.cursor/mcp.json)

O formato recomendado para Cursor:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "figma-desktop": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server"],
      "env": {
        "FIGMA_DESKTOP_PORT": "5555"
      }
    }
  }
}
```

### Opção 2: Configuração TypeScript (mcp.config.ts)

A configuração já foi adicionada ao arquivo `mcp.config.ts` do projeto:

- `figma-remote`: Servidor remoto (Tier 2)
- `figma-desktop`: Servidor desktop (Tier 3)

---

## 🔍 Troubleshooting

### Problema: Servidor remoto não conecta

**Soluções:**
1. Verifique se você está autenticado no Figma
2. Certifique-se de que o arquivo está em Dev Mode
3. Verifique se a URL está correta: `https://mcp.figma.com/mcp`
4. Verifique logs do Cursor para erros

### Problema: Servidor desktop não inicia

**Soluções:**
1. Certifique-se de que o Figma Desktop App está rodando
2. Verifique a porta (padrão: 5555)
3. Reinicie o app do Figma
4. Verifique se não há firewall bloqueando a conexão

### Problema: Autenticação falha

**Soluções:**
1. Limpe cookies/cache do navegador
2. Refaça o fluxo de autenticação OAuth
3. Verifique permissões na conta Figma
4. Certifique-se de que o Dev Mode está ativado

---

## 📚 Recursos Adicionais

- [Figma MCP Server Documentation](https://developers.figma.com/docs/figma-mcp-server/)
- [Figma Dev Mode](https://help.figma.com/hc/en-us/articles/360055204533-Dev-mode-in-Figma)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Cursor MCP Documentation](https://docs.cursor.com/context/mcp)
- [Figma API Documentation](https://www.figma.com/developers/api)

---

## 🎯 Próximos Passos

1. **Configurar servidor remoto** (recomendado para começar)
2. **Autenticar via Figma Dev Mode**
3. **Testar extração de código de um frame simples**
4. **Explorar variáveis e componentes**
5. **Integrar em fluxo de desenvolvimento**

---

**Última Atualização:** 2025-01-08  
**Mantido por:** Time de Engenharia
