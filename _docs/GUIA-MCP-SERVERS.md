# Guia de Configuração de MCP Servers - Plataforma Educacional

**Criado em:** 2025-01-XX  
**Status:** Configuração Inicial

---

## 📋 Visão Geral

Este documento detalha como configurar todos os MCP servers necessários para a plataforma educacional, organizados por tiers de prioridade.

---

## 🎯 Tier 1 (Essencial)

### 1. Backend - Supabase

**Propósito:** Gerenciamento de perfis de alunos, progresso, autenticação e banco de dados de conteúdo (RAG).

**Configuração:**

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-supabase"],
      "env": {
        "SUPABASE_URL": "https://seu-projeto.supabase.co",
        "SUPABASE_KEY": "sua-chave-api",
        "SUPABASE_SERVICE_ROLE_KEY": "sua-service-role-key"
      }
    }
  }
}
```

**Instalação:**
```bash
npm install -g @modelcontextprotocol/server-supabase
```

**Variáveis de Ambiente Necessárias:**
- `SUPABASE_URL`: URL do seu projeto Supabase
- `SUPABASE_KEY`: Chave pública da API
- `SUPABASE_SERVICE_ROLE_KEY`: Chave de serviço (para operações administrativas)

**Recursos:**
- [Documentação Supabase MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/supabase)

---

### 2. Matemática - SymPy / Scientific Calculator

**Propósito:** Resolução de equações, cálculo simbólico e manipulação de expressões matemáticas usando SymPy, NumPy, SciPy e Pandas.

**Configuração:**

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "python3",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {}
    }
  }
}
```

**Instalação:**

1. Instale as dependências:
```bash
pip install sympy numpy scipy pandas
```

2. Instale o servidor MCP:
```bash
pip install mcp-scientific-calculator
```

Ou instale tudo de uma vez:
```bash
pip install -r requirements.txt
```

**Funcionalidades:**
- Resolução de equações simbólicas
- Cálculo diferencial e integral
- Simplificação de expressões
- Álgebra linear
- Cálculos numéricos avançados

**Recursos:**
- [SymPy Documentation](https://www.sympy.org/)
- [Scientific Calculator MCP PyPI](https://pypi.org/project/mcp-scientific-calculator/)
- [Documentação Completa - CONFIGURACAO-SYMPY-MCP.md](../_docs/CONFIGURACAO-SYMPY-MCP.md)

**Nota:** O pacote `mcp-server-sympy` não existe oficialmente no PyPI. Use `mcp-scientific-calculator` como alternativa recomendada.

---

### 3. Visualização - Desmos / Formula Visualization

**Propósito:** Plotagem interativa de gráficos e visualização de conceitos matemáticos abstratos.

**⚠️ Nota:** O pacote `@modelcontextprotocol/server-desmos` **não existe oficialmente** no npm. Use a **solução alternativa** abaixo.

**Solução Alternativa (Recomendada):**

Use **Plotly diretamente no código Python** (já instalado):

```python
from visualization_utils import plot_function, plot_multiple_functions, plot_3d_surface

# Plotar função simples
fig = plot_function("x**2 - 5*x + 6", x_range=(-1, 7))
fig.show()

# Comparar múltiplas funções
fig = plot_multiple_functions(["x**2", "x**3", "x**4"], x_range=(-3, 3))
fig.show()

# Superfície 3D
fig = plot_3d_surface("x**2 + y**2")
fig.show()
```

**Arquivos Disponíveis:**
- `visualization_utils.py` - Funções utilitárias para visualização
- `_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md` - Documentação completa
- Exemplos: `exemplo1_quadratica.html`, `exemplo2_multiplas.html`, `exemplo3_3d.html`

**Alternativa via MCP (Requer Python 3.10+):**

O pacote `mcp-plots` requer Python 3.10+, mas o sistema tem 3.9.6:

```bash
# Se atualizar Python para 3.10+
pip install mcp-plots
```

**Recursos:**
- [Plotly Documentation](https://plotly.com/python/)
- [SymPy Documentation](https://www.sympy.org/)
- [Documentação Completa - CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md](../_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md)
- [Quick Start - DESMOS-VISUALIZACAO-QUICK-START.md](../DESMOS-VISUALIZACAO-QUICK-START.md)

---

### 4. Aprendizagem - Anki

**Propósito:** Criação de flashcards personalizados para memorização e aprendizado via repetição espaçada.

**Configuração:**

```json
{
  "mcpServers": {
    "anki": {
      "command": "python",
      "args": ["-m", "mcp_server_anki"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**Instalação:**

1. Instale o Anki na sua máquina: [Anki Download](https://apps.ankiweb.net/)
2. Instale o plugin AnkiConnect no Anki
3. Instale o servidor MCP:
```bash
pip install mcp-server-anki anki-connect
```

**Nota:** O Anki precisa estar rodando com o plugin AnkiConnect ativo para funcionar.

**Recursos:**
- [AnkiConnect GitHub](https://github.com/FooSoft/anki-connect)
- [Anki Documentation](https://docs.ankiweb.net/)

---

### 5. Avaliação - Homework Grading

**Propósito:** Correção automática de exercícios, incluindo questões multimodais, fornecendo feedback instantâneo.

**Configuração:**

```json
{
  "mcpServers": {
    "homework-grading": {
      "command": "python",
      "args": ["-m", "mcp_server_homework_grading"],
      "env": {
        "OPENAI_API_KEY": "sua-chave-openai",
        "GRADING_MODEL": "gpt-4o"
      }
    }
  }
}
```

**Instalação:**
```bash
pip install mcp-server-homework-grading openai
```

**Variáveis de Ambiente:**
- `OPENAI_API_KEY`: Chave da API OpenAI para processamento de linguagem natural
- `GRADING_MODEL`: Modelo a ser usado (gpt-4o, gpt-4-turbo, etc.)

**Recursos:**
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

## 🚀 Tier 2 (Expansão)

### 6. Integração LMS - Moodle / Canvas LMS

**Propósito:** Conexão com sistemas de gerenciamento de aprendizado usados por escolas para sincronizar notas e tarefas.

**Configuração (Moodle):**

```json
{
  "mcpServers": {
    "moodle": {
      "command": "python",
      "args": ["-m", "mcp_server_moodle"],
      "env": {
        "MOODLE_URL": "https://sua-escola.moodle.com",
        "MOODLE_TOKEN": "seu-token-moodle"
      }
    }
  }
}
```

**Configuração (Canvas):**

```json
{
  "mcpServers": {
    "canvas": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-canvas"],
      "env": {
        "CANVAS_API_URL": "https://sua-escola.instructure.com",
        "CANVAS_API_TOKEN": "seu-token-canvas"
      }
    }
  }
}
```

**Instalação (Moodle):**
```bash
pip install mcp-server-moodle requests
```

**Instalação (Canvas):**
```bash
npm install -g @modelcontextprotocol/server-canvas
```

**Autenticação:**
- **Moodle:** Requer token de API gerado em: Site Administration > Security > Site policies > Web services
- **Canvas:** Requer token de API gerado em: Account > Settings > New Access Token

**Recursos:**
- [Moodle Web Services](https://docs.moodle.org/dev/Web_services)
- [Canvas API Documentation](https://canvas.instructure.com/doc/api/)

---

### 7. Ecossistema - Google MCP Servers

**Propósito:** Integração com Google Classroom, Drive e outras ferramentas do Google for Education.

**Configuração:**

```json
{
  "mcpServers": {
    "google-classroom": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-classroom"],
      "env": {
        "GOOGLE_CLIENT_ID": "seu-client-id",
        "GOOGLE_CLIENT_SECRET": "seu-client-secret",
        "GOOGLE_REDIRECT_URI": "http://localhost:3000/oauth/callback"
      }
    },
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-drive"],
      "env": {
        "GOOGLE_CLIENT_ID": "seu-client-id",
        "GOOGLE_CLIENT_SECRET": "seu-client-secret",
        "GOOGLE_REDIRECT_URI": "http://localhost:3000/oauth/callback"
      }
    }
  }
}
```

**Instalação:**
```bash
npm install -g @modelcontextprotocol/server-google-classroom
npm install -g @modelcontextprotocol/server-google-drive
```

**Autenticação OAuth 2.0:**

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative as APIs: Google Classroom API, Google Drive API
4. Crie credenciais OAuth 2.0 (Desktop App ou Web Application)
5. Configure URLs de redirecionamento autorizadas
6. Use o Client ID e Client Secret nas variáveis de ambiente

**Recursos:**
- [Google Classroom API](https://developers.google.com/classroom)
- [Google Drive API](https://developers.google.com/drive)
- [Google OAuth 2.0 Setup](https://developers.google.com/identity/protocols/oauth2)

---

### 8. Automação - Zapier MCP Client

**Propósito:** Conexão com milhares de outros aplicativos (sistemas de pagamento, comunicação, etc.).

**Configuração:**

```json
{
  "mcpServers": {
    "zapier": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-zapier"],
      "env": {
        "ZAPIER_API_KEY": "sua-chave-zapier"
      }
    }
  }
}
```

**Instalação:**
```bash
npm install -g @modelcontextprotocol/server-zapier
```

**Autenticação:**
1. Acesse [Zapier Platform](https://zapier.com/app/developer)
2. Crie uma conta de desenvolvedor
3. Gere uma API Key nas configurações do desenvolvedor
4. Configure as integrações necessárias (Zaps)

**Recursos:**
- [Zapier Platform Documentation](https://platform.zapier.com/docs)
- [Zapier API Reference](https://zapier.com/help/api)

---

### 9. Multimídia - MiniMax

**Propósito:** Geração de conteúdo educacional em áudio (Text-to-Speech) e vídeo para diferentes estilos de aprendizado.

**Configuração:**

```json
{
  "mcpServers": {
    "minimax": {
      "command": "python",
      "args": ["-m", "mcp_server_minimax"],
      "env": {
        "MINIMAX_API_KEY": "sua-chave-minimax",
        "MINIMAX_GROUP_ID": "seu-group-id"
      }
    }
  }
}
```

**Instalação:**
```bash
pip install mcp-server-minimax minimax-python-sdk
```

**Autenticação:**
1. Acesse [MiniMax Platform](https://www.minimax.chat/)
2. Crie uma conta e obtenha API Key
3. Obtenha Group ID nas configurações do projeto

**Recursos:**
- [MiniMax API Documentation](https://www.minimax.chat/document/)

---

### 12. Design - Figma Make (Remote & Desktop MCP Server)

**Propósito:** Acesso e interação com arquivos de design do Figma, permitindo geração de código a partir de designs e extração de contexto de design (variáveis, componentes, etc.).

**Configuração (Remote Server - Recomendado):**

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

**Configuração (Desktop Server):**

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

**Instalação (Desktop Server):**

1. Instale o Figma Desktop App: [Figma Downloads](https://www.figma.com/downloads/)
2. Certifique-se de que o app está rodando
3. O servidor MCP será iniciado automaticamente

**Autenticação (Remote Server):**

1. Abra seu arquivo Figma Design ou Make no navegador
2. Mude para **Dev Mode**
3. No painel de inspeção à direita, clique em **"Set up an MCP client"**
4. Siga o fluxo de autenticação OAuth conforme solicitado

**Funcionalidades:**
- Geração de código a partir de frames selecionados
- Extração de contexto de design (variáveis, componentes)
- Recuperação de recursos de código de arquivos Figma Make
- Sincronização design-to-code

**Recursos:**
- [Figma MCP Server Documentation](https://developers.figma.com/docs/figma-mcp-server/)
- [Figma Remote MCP Setup](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Figma Desktop MCP Setup](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)
- [Documentação Completa - CONFIGURACAO-FIGMA-MAKE-MCP.md](../_docs/CONFIGURACAO-FIGMA-MAKE-MCP.md)

---

## ⚡ Tier 3 (Otimização)

### 13. Design - Figma Make (Desktop MCP Server)

**Nota:** Configuração alternativa do servidor desktop. Veja Tier 2 para servidor remoto (recomendado).

**Propósito:** Conexão local direta via app desktop do Figma.

**Configuração:**
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

**Recursos:**
- Veja documentação completa em: `_docs/CONFIGURACAO-FIGMA-MAKE-MCP.md`

---

### 14. Programação - E2B (Code Sandbox)

**Propósito:** Fornece um ambiente seguro para alunos executarem código, essencial para o ensino de programação.

**Configuração:**

```json
{
  "mcpServers": {
    "e2b": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-e2b"],
      "env": {
        "E2B_API_KEY": "sua-chave-e2b"
      }
    }
  }
}
```

**Instalação:**
```bash
npm install -g @modelcontextprotocol/server-e2b
```

**Autenticação:**
1. Acesse [E2B Platform](https://e2b.dev/)
2. Crie uma conta
3. Obtenha API Key no dashboard

**Recursos:**
- [E2B Documentation](https://docs.e2b.dev/)
- [E2B GitHub](https://github.com/e2b-dev/e2b)

---

### 15. Conteúdo - Firecrawl / Browserbase

**Propósito:** Web scraping para coletar conteúdo educacional relevante, questões de provas e artigos.

**Configuração (Firecrawl):**

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-firecrawl"],
      "env": {
        "FIRECRAWL_API_KEY": "sua-chave-firecrawl"
      }
    }
  }
}
```

**Configuração (Browserbase):**

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-browserbase"],
      "env": {
        "BROWSERBASE_API_KEY": "sua-chave-browserbase",
        "BROWSERBASE_PROJECT_ID": "seu-project-id"
      }
    }
  }
}
```

**Instalação (Firecrawl):**
```bash
npm install -g @modelcontextprotocol/server-firecrawl
```

**Instalação (Browserbase):**
```bash
npm install -g @modelcontextprotocol/server-browserbase
```

**Autenticação:**
- **Firecrawl:** Acesse [Firecrawl](https://firecrawl.dev/) e obtenha API Key
- **Browserbase:** Acesse [Browserbase](https://www.browserbase.com/) e obtenha API Key e Project ID

**Recursos:**
- [Firecrawl Documentation](https://docs.firecrawl.dev/)
- [Browserbase Documentation](https://docs.browserbase.com/)

---

### 16. Pesquisa - Exa / AMiner

**Propósito:** Busca inteligente de informações e papers acadêmicos para embasar conteúdo educacional.

**Configuração (Exa):**

```json
{
  "mcpServers": {
    "exa": {
      "command": "python",
      "args": ["-m", "mcp_server_exa"],
      "env": {
        "EXA_API_KEY": "sua-chave-exa"
      }
    }
  }
}
```

**Configuração (AMiner):**

```json
{
  "mcpServers": {
    "aminer": {
      "command": "python",
      "args": ["-m", "mcp_server_aminer"],
      "env": {
        "AMINER_API_KEY": "sua-chave-aminer"
      }
    }
  }
}
```

**Instalação (Exa):**
```bash
pip install mcp-server-exa exa-py
```

**Instalação (AMiner):**
```bash
pip install mcp-server-aminer aminer-api
```

**Autenticação:**
- **Exa:** Acesse [Exa AI](https://exa.ai/) e obtenha API Key
- **AMiner:** Acesse [AMiner](https://www.aminer.org/) e obtenha API Key

**Recursos:**
- [Exa API Documentation](https://docs.exa.ai/)
- [AMiner API Documentation](https://www.aminer.org/api)

---

## 📝 Arquivos de Configuração

### Opção 1: Arquivo JSON (`.cursor/mcp.json`)

O arquivo `.cursor/mcp.json` já foi criado na raiz do projeto com todas as configurações. Este é o formato padrão para o Cursor.

### Opção 2: Configuração TypeScript (`mcp.config.ts`)

Para projetos que usam Nx ou TypeScript, use o arquivo `mcp.config.ts`:

```typescript
import { configureMcpServers } from './mcp.config';

// Configurar todos os servidores
const servers = configureMcpServers();

// Ou configurar por tier
import { tier1Servers } from './mcp.config';
```

### Opção 3: Usando Nx configureMcpServer

Para projetos Nx, você pode usar a função `nx.configureMcpServer` diretamente:

```typescript
import { configureMcpServer } from '@nx/mcp';

// Configurar servidor individual
configureMcpServer({
  name: 'supabase',
  command: 'npx',
  args: ['-y', '@modelcontextprotocol/server-supabase'],
  env: {
    SUPABASE_URL: process.env.SUPABASE_URL || '',
    SUPABASE_KEY: process.env.SUPABASE_KEY || '',
  },
});
```

No Cursor, execute o comando `nx.configureMcpServer` através da paleta de comandos (`Cmd/Ctrl + Shift + P`).

---

## 🔒 Segurança e Melhores Práticas

1. **Variáveis de Ambiente:**
   - Nunca commite chaves de API no código
   - Use arquivos `.env` ou variáveis de ambiente do sistema
   - Considere usar um gerenciador de secrets (AWS Secrets Manager, Azure Key Vault, etc.)

2. **Permissões:**
   - Configure permissões mínimas necessárias para cada API
   - Revise e rotacione chaves regularmente
   - Use service accounts quando possível

3. **Monitoramento:**
   - Configure logs para rastrear uso de APIs
   - Implemente rate limiting para evitar custos excessivos
   - Monitore quotas de API

4. **Testes:**
   - Teste cada servidor individualmente antes de integrar
   - Use ambientes de desenvolvimento/staging separados
   - Valide autenticação antes de deploy em produção

---

## 🚀 Próximos Passos

1. **Priorização:**
   - Comece com Tier 1 (essencial)
   - Teste cada servidor isoladamente
   - Documente casos de uso específicos

2. **Integração:**
   - Integre servidores gradualmente
   - Teste fluxos end-to-end
   - Monitore performance e custos

3. **Documentação:**
   - Documente casos de uso para cada servidor
   - Crie exemplos de código para a equipe
   - Mantenha este guia atualizado

---

## 📚 Recursos Adicionais

- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [Cursor MCP Documentation](https://docs.cursor.com/context/mcp)

---

**Última Atualização:** 2025-01-XX  
**Mantido por:** Time de Engenharia