# Quick Start - Configuração MCP Servers

**Início Rápido para Configurar MCP Servers**

---

## 📦 Instalação Rápida

### Pré-requisitos

- Node.js 18+ instalado
- Python 3.8+ instalado
- npm ou yarn
- pip

### Passo 1: Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```bash
# Tier 1 - Essencial
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-publica-api
SUPABASE_SERVICE_ROLE_KEY=sua-service-role-key
DESMOS_API_KEY=sua-chave-api-desmos
OPENAI_API_KEY=sua-chave-openai

# Tier 2 - Expansão
MOODLE_URL=https://sua-escola.moodle.com
MOODLE_TOKEN=seu-token-moodle
CANVAS_API_URL=https://sua-escola.instructure.com
CANVAS_API_TOKEN=seu-token-canvas
GOOGLE_CLIENT_ID=seu-google-client-id
GOOGLE_CLIENT_SECRET=seu-google-client-secret
ZAPIER_API_KEY=sua-chave-zapier
MINIMAX_API_KEY=sua-chave-minimax
MINIMAX_GROUP_ID=seu-group-id

# Tier 3 - Otimização
E2B_API_KEY=sua-chave-e2b
FIRECRAWL_API_KEY=sua-chave-firecrawl
BROWSERBASE_API_KEY=sua-chave-browserbase
BROWSERBASE_PROJECT_ID=seu-project-id
EXA_API_KEY=sua-chave-exa
AMINER_API_KEY=sua-chave-aminer
```

### Passo 2: Instalar Dependências

```bash
# Servidores Node.js
npm install -g @modelcontextprotocol/server-supabase
npm install -g @modelcontextprotocol/server-desmos
npm install -g @modelcontextprotocol/server-canvas
npm install -g @modelcontextprotocol/server-google-classroom
npm install -g @modelcontextprotocol/server-google-drive
npm install -g @modelcontextprotocol/server-zapier
npm install -g @modelcontextprotocol/server-e2b
npm install -g @modelcontextprotocol/server-firecrawl
npm install -g @modelcontextprotocol/server-browserbase

# Servidores Python
pip install mcp-server-sympy
pip install mcp-server-anki anki-connect
pip install mcp-server-homework-grading openai
pip install mcp-server-moodle requests
pip install mcp-server-minimax minimax-python-sdk
pip install mcp-server-exa exa-py
pip install mcp-server-aminer aminer-api
pip install plotly mcp-server-plotly  # Alternativa para visualização
```

### Passo 3: Configurar Cursor

1. Abra o Cursor
2. Vá em `Settings` > `MCP Servers` (ou `File` > `Settings` > `Tools` > `Gemini` > `MCP Servers`)
3. Importe o arquivo `mcp-config.json` ou cole o conteúdo manualmente
4. Certifique-se de que as variáveis de ambiente estão configuradas

### Passo 4: Testar Conexões

Para testar cada servidor individualmente, use:

```bash
# Teste Supabase
npx @modelcontextprotocol/server-supabase

# Teste Desmos
npx @modelcontextprotocol/server-desmos

# Teste SymPy
python -m mcp_server_sympy
```

---

## 🎯 Configuração por Tier

### Tier 1 (Começar Aqui)

1. **Supabase** - Backend essencial
2. **SymPy** - Matemática
3. **Desmos/Plotly** - Visualização
4. **Anki** - Flashcards (requer Anki instalado)
5. **Homework Grading** - Correção automática

### Tier 2 (Depois de Tier 1)

6. **Moodle/Canvas** - Integração LMS
7. **Google Classroom/Drive** - Ecossistema Google
8. **Zapier** - Automação
9. **MiniMax** - Multimídia

### Tier 3 (Otimização)

10. **E2B** - Code Sandbox
11. **Firecrawl/Browserbase** - Web Scraping
12. **Exa/AMiner** - Pesquisa Acadêmica

---

## ⚠️ Notas Importantes

- **Anki:** Requer instalação do Anki e plugin AnkiConnect rodando
- **Google APIs:** Requer configuração OAuth 2.0 no Google Cloud Console
- **Moodle/Canvas:** Requer tokens de API gerados nos respectivos sistemas
- **Variáveis de Ambiente:** Nunca commite o arquivo `.env` no git

---

## 🔧 Troubleshooting

### Erro: "Command not found"
- Verifique se os pacotes foram instalados globalmente
- Para Node.js: use `npm install -g` ou `npx`
- Para Python: use `pip install` e verifique se está no PATH

### Erro: "Authentication failed"
- Verifique se as variáveis de ambiente estão configuradas
- Confirme que as chaves de API estão corretas
- Verifique permissões e quotas das APIs

### Erro: "Connection refused"
- Verifique se os serviços necessários estão rodando (ex: Anki com AnkiConnect)
- Confirme URLs e endpoints estão corretos
- Verifique firewall e configurações de rede

---

## 📚 Próximos Passos

1. Consulte o [GUIA-MCP-SERVERS.md](./GUIA-MCP-SERVERS.md) para detalhes completos
2. Configure autenticação OAuth para Google APIs
3. Teste cada servidor individualmente
4. Integre gradualmente no seu projeto

---

**Última Atualização:** 2025-01-XX