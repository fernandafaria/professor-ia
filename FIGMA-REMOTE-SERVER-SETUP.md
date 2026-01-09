# Figma Remote Server MCP - Setup Completo

## ✅ Configuração Aplicada

O Remote Server do Figma Make MCP foi configurado com sucesso!

**Arquivo configurado:** `.cursor/mcp.json`

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

---

## 🔐 Passos para Autenticação

### 1. Reinicie o Cursor

Para que a configuração seja aplicada, você precisa reiniciar o Cursor:
- Feche completamente o Cursor
- Abra novamente o Cursor

### 2. Abra seu arquivo Figma

1. Acesse [Figma](https://www.figma.com/) no navegador
2. Abra seu arquivo Design ou Make que deseja usar com o MCP

### 3. Ative o Dev Mode

1. No Figma, clique no botão **"Dev Mode"** no topo da interface
2. Isso habilitará o painel de inspeção à direita

### 4. Configure o MCP Client

1. No painel de inspeção à direita (quando estiver em Dev Mode)
2. Procure e clique em **"Set up an MCP client"** ou **"Configure MCP"**
3. Isso iniciará o fluxo de autenticação OAuth

### 5. Complete a Autenticação OAuth

1. Você será redirecionado para uma página de autenticação do Figma
2. Faça login na sua conta Figma (se necessário)
3. Autorize o acesso do Cursor aos seus arquivos Figma
4. Após autorizar, você será redirecionado de volta

### 6. Verifique a Conexão

1. No Cursor, verifique se o servidor `figma-remote` está conectado
2. Você pode verificar nas configurações do Cursor: **Settings > Features > MCP**
3. O status deve mostrar como "Connected" ou similar

---

## 🎯 Como Usar

Após autenticar, você pode usar o Figma MCP para:

### 1. Gerar código de frames selecionados

```
No Cursor, você pode pedir:
"Gere código React para o frame selecionado no Figma"
"Crie componentes Vue baseados no design atual"
```

### 2. Extrair variáveis e componentes

```
"Extraia as variáveis de cor do design Figma"
"Liste todos os componentes do arquivo Figma"
"Mostre as medidas e espaçamentos do frame selecionado"
```

### 3. Obter recursos de código

```
"Obtenha os tokens de design do Figma"
"Exporte os ícones como SVG"
"Gere o código CSS das variáveis de design"
```

---

## 🔍 Troubleshooting

### Problema: Servidor não conecta

**Soluções:**
1. Verifique se reiniciou o Cursor após configurar
2. Verifique se o arquivo `.cursor/mcp.json` está correto
3. Verifique se o URL está correto: `https://mcp.figma.com/mcp`
4. Verifique se o transport está como `sse`

### Problema: Autenticação falha

**Soluções:**
1. Certifique-se de estar em **Dev Mode** no Figma
2. Limpe cookies/cache do navegador
3. Tente fazer logout e login novamente no Figma
4. Verifique se você tem permissões para acessar o arquivo Figma

### Problema: Não aparece "Set up an MCP client"

**Soluções:**
1. Certifique-se de que está em **Dev Mode** (não apenas Design Mode)
2. Verifique se você está usando a versão mais recente do Figma
3. Atualize o navegador para a versão mais recente
4. Tente fechar e abrir o arquivo Figma novamente

### Problema: Cursor não reconhece o servidor

**Soluções:**
1. Verifique a sintaxe do JSON em `.cursor/mcp.json`
2. Certifique-se de que não há vírgulas extras ou erros de sintaxe
3. Reinicie o Cursor completamente
4. Verifique se está usando uma versão do Cursor que suporta MCP SSE

---

## 📚 Recursos

- **Documentação Figma MCP:** https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- **Figma Help Center:** https://help.figma.com/hc/en-us/articles/35281350665623-Figma-MCP-collection-How-to-set-up-the-Figma-remote-MCP-server
- **Cursor MCP Docs:** https://docs.cursor.com/context/mcp
- **Documentação Completa do Projeto:** `_docs/CONFIGURACAO-FIGMA-MAKE-MCP.md`

---

## ✅ Checklist de Configuração

- [x] Arquivo `.cursor/mcp.json` configurado
- [ ] Cursor reiniciado
- [ ] Arquivo Figma aberto no navegador
- [ ] Dev Mode ativado no Figma
- [ ] "Set up an MCP client" clicado
- [ ] Autenticação OAuth completa
- [ ] Conexão verificada no Cursor
- [ ] Teste de uso realizado

---

**Última Atualização:** 2025-01-08
