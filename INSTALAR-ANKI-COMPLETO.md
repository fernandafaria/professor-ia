# Instalação Completa do Anki e Configuração MCP

**Criado em:** 2025-01-08  
**Status:** Guia de Instalação

---

## 📋 Visão Geral

Este guia cobre a instalação completa do Anki e configuração para uso com MCP no Cursor.

---

## 🚀 Passo 1: Instalar o Anki (Aplicativo)

### 1.1 Download do Anki para macOS

1. **Acesse o site oficial:** [https://apps.ankiweb.net/](https://apps.ankiweb.net/)
2. **Clique em "Download"** para macOS
3. **Baixe a versão apropriada:**
   - Intel Mac: Versão Intel
   - Apple Silicon (M1/M2/M3): Versão Apple Silicon

### 1.2 Instalar o Anki

1. Abra o arquivo `.dmg` baixado
2. Arraste o aplicativo **Anki** para a pasta **Applications**
3. Abra a pasta **Applications** (ou Spotlight)
4. Clique duas vezes no **Anki** para iniciar

### 1.3 Primeira Inicialização

1. Na primeira vez, o Anki pode pedir para criar uma conta (opcional)
2. Você pode usar offline se preferir
3. Siga as instruções iniciais de configuração

---

## 🔌 Passo 2: Instalar o Plugin AnkiConnect

### 2.1 Abrir Gerenciador de Add-ons

1. No Anki, vá em **Tools** > **Add-ons**
   - Ou pressione `Cmd + Shift + A`

### 2.2 Instalar AnkiConnect

1. No gerenciador de add-ons, clique em **Get Add-ons...**
2. No campo "Code:", digite: **2055492159**
3. Clique em **OK**
4. O AnkiConnect será baixado e instalado automaticamente

### 2.3 Reiniciar o Anki

**IMPORTANTE:** Após instalar o plugin, você **DEVE** reiniciar o Anki:

1. Feche completamente o Anki (`Cmd + Q` no Mac)
2. Abra novamente o Anki
3. O AnkiConnect estará ativo

### 2.4 Verificar Instalação

1. Vá em **Tools** > **Add-ons** novamente
2. Verifique se **AnkiConnect** aparece na lista com código **2055492159**
3. O status deve mostrar como instalado

---

## 🛠️ Passo 3: Desabilitar App Nap (Importante para macOS)

O App Nap do macOS pode interferir no AnkiConnect quando o Anki está em background.

### 3.1 Desabilitar App Nap

Abra o Terminal e execute:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

### 3.2 Reiniciar o Anki

1. Feche completamente o Anki (`Cmd + Q`)
2. Abra novamente o Anki
3. As mudanças estarão aplicadas

---

## ✅ Passo 4: Verificar AnkiConnect

### 4.1 Testar Conexão

**Certifique-se de que o Anki está rodando**, depois teste a conexão:

**Via Terminal:**
```bash
curl http://localhost:8765
```

**Ou via Navegador:**
1. Abra o navegador
2. Acesse: `http://localhost:8765`
3. Você deve ver uma resposta ou página do AnkiConnect

**Resposta esperada:**
Se funcionar, você verá uma mensagem ou página indicando que o AnkiConnect está rodando.

### 4.2 Verificar Porta

Se não funcionar, verifique se a porta está correta:

```bash
lsof -i :8765
```

Se o Anki estiver rodando com AnkiConnect, você deve ver algo como:

```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
Anki     1234 user   42u  IPv4  ...      0t0  TCP localhost:8765 (LISTEN)
```

---

## 📦 Passo 5: Instalar Servidor MCP Anki

### 5.1 Requisito: Python 3.10+

⚠️ **IMPORTANTE:** O pacote `mcp-server-anki` requer **Python 3.10 ou superior**.

**Verifique sua versão do Python:**
```bash
python3 --version
```

Se você tiver Python 3.9 ou inferior, você tem duas opções:

**Opção A: Atualizar Python** (Recomendado para funcionalidade completa)
**Opção B: Usar Anki diretamente** (sem servidor MCP intermediário)

### 5.2 Instalar Servidor MCP (Python 3.10+)

Se você tiver Python 3.10+, instale o servidor MCP:

```bash
pip3 install mcp-server-anki
```

**Alternativa usando uvx (se disponível):**

```bash
# Instalar uv (gerenciador de pacotes Python moderno)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Usar uvx para executar o servidor MCP
uvx mcp-server-anki
```

### 5.3 Verificar Instalação

```bash
python3 -m mcp_server_anki --help 2>&1 || echo "Verificando..."
```

---

## 🔧 Passo 6: Configurar no Cursor

### 6.1 Opção A: Usando Python Diretamente

Se você instalou `mcp-server-anki` via pip:

Atualize o arquivo `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "anki": {
      "command": "/Library/Developer/CommandLineTools/usr/bin/python3",
      "args": ["-m", "mcp_server_anki"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

**Nota:** Substitua o caminho do Python se necessário. Encontre com: `which python3`

### 6.2 Opção B: Usando uvx

Se você instalou `uv` e quer usar `uvx`:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "anki": {
      "command": "uvx",
      "args": ["mcp-server-anki"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

### 6.3 Reiniciar o Cursor

**IMPORTANTE:** Após atualizar a configuração:

1. Feche completamente o Cursor (`Cmd + Q`)
2. Abra novamente o Cursor
3. O servidor MCP será iniciado

---

## 🎯 Passo 7: Verificar Configuração no Cursor

### 7.1 Verificar Servidor MCP

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `anki` aparece na lista
4. O status deve mostrar "Connected" ou similar

### 7.2 Verificar Logs

Se houver problemas:

1. Nas configurações do Cursor, vá em **Features > MCP**
2. Clique em `anki` para ver os logs
3. Verifique se há mensagens de erro

### 7.3 Testar Funcionalidade

No Cursor, você pode testar comandos como:

```
"Crie um flashcard com a pergunta: Qual é a capital do Brasil? e resposta: Brasília"
"Liste todos os decks disponíveis no Anki"
"Mostre os flashcards do deck 'Default'"
"Crie um flashcard sobre Python com pergunta e resposta"
```

---

## 🔍 Troubleshooting

### Problema: AnkiConnect não responde

**Soluções:**

1. **Certifique-se de que o Anki está rodando:**
   ```bash
   # Verificar se Anki está rodando
   ps aux | grep -i anki
   ```

2. **Verifique se o plugin está instalado:**
   - No Anki: **Tools** > **Add-ons**
   - Verifique se **AnkiConnect** (2055492159) está na lista

3. **Reinicie o Anki completamente:**
   ```bash
   # No Mac
   killall Anki
   # Depois abra novamente o Anki
   ```

4. **Teste a conexão:**
   ```bash
   curl http://localhost:8765
   ```

5. **Verifique a porta:**
   ```bash
   lsof -i :8765
   ```

### Problema: mcp-server-anki requer Python 3.10+

**Soluções:**

**Opção 1: Atualizar Python** (Recomendado)
- Instale Python 3.10+ via Homebrew ou pyenv
- Use a versão atualizada para instalar o servidor MCP

**Opção 2: Usar Anki diretamente** (Temporário)
- Use a biblioteca `anki-connect` diretamente no código Python
- Não é necessário servidor MCP intermediário

### Problema: Servidor MCP não conecta no Cursor

**Soluções:**

1. **Certifique-se de que o Anki está rodando** (verifique na Dock)

2. **Verifique o caminho do Python:**
   ```bash
   which python3
   ```
   Atualize o `.cursor/mcp.json` com o caminho correto.

3. **Verifique se `mcp-server-anki` está instalado:**
   ```bash
   pip3 show mcp-server-anki
   ```

4. **Verifique a versão do Python:**
   ```bash
   python3 --version
   ```
   Deve ser 3.10+ para usar `mcp-server-anki`.

5. **Reinicie o Cursor completamente**

6. **Verifique os logs do Cursor** em **Features > MCP**

### Problema: App Nap interferindo

**Solução:**
Execute o comando para desabilitar App Nap:
```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```
Depois reinicie o Anki.

---

## 🎯 Alternativa: Usar Anki Diretamente (Sem MCP)

Se você não puder usar Python 3.10+ ou prefere uma solução mais simples, pode usar o AnkiConnect diretamente no código Python:

```python
import requests
import json

def add_note_to_anki(deck_name, front, back):
    """Adiciona um flashcard ao Anki via AnkiConnect"""
    
    # Requisição para AnkiConnect
    request_data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "tags": []
            }
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:8765",
            data=json.dumps(request_data)
        )
        return response.json()
    except Exception as e:
        print(f"Erro ao conectar com Anki: {e}")
        return None

# Exemplo de uso
result = add_note_to_anki(
    "Default",
    "Qual é a capital do Brasil?",
    "Brasília"
)
print(result)
```

**Instalação:**
```bash
pip3 install requests
```

---

## 📚 Recursos

- **Anki Download:** https://apps.ankiweb.net/
- **AnkiConnect GitHub:** https://github.com/FooSoft/anki-connect
- **AnkiConnect Plugin:** Código 2055492159
- **Anki Documentation:** https://docs.ankiweb.net/
- **AnkiConnect API Documentation:** https://github.com/FooSoft/anki-connect#api-documentation
- **mcp-server-anki PyPI:** https://pypi.org/project/mcp-server-anki/
- **MCP Protocol:** https://modelcontextprotocol.io/
- **Documentação Completa:** `_docs/GUIA-MCP-SERVERS.md`

---

## ✅ Checklist de Instalação

- [ ] Anki baixado e instalado
- [ ] Anki iniciado pela primeira vez
- [ ] AnkiConnect instalado (código 2055492159)
- [ ] Anki reiniciado após instalar plugin
- [ ] App Nap desabilitado (macOS)
- [ ] AnkiConnect verificado (curl http://localhost:8765)
- [ ] Python 3.10+ instalado (se usar mcp-server-anki)
- [ ] `mcp-server-anki` instalado via pip (se usar Python 3.10+)
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado
- [ ] Servidor MCP conectado no Cursor
- [ ] Teste de criação de flashcard realizado

---

**Última Atualização:** 2025-01-08  
**Status:** Guia de Instalação Completo
