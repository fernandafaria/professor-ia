# Anki - Quick Start de Instalação

## ✅ Guia de Instalação Criado

Foi criado um guia completo de instalação do Anki e configuração para uso com MCP.

---

## 🚀 Início Rápido

### 1. Download do Anki

A página de download do Anki foi aberta no seu navegador.

Se não abriu, acesse: **https://apps.ankiweb.net/**

### 2. Instalar o Anki

1. **Baixe o Anki** para macOS
2. **Abra o arquivo `.dmg`** baixado
3. **Arraste o Anki** para a pasta **Applications**
4. **Abra o Anki** da pasta Applications

### 3. Instalar Plugin AnkiConnect

1. No Anki, vá em **Tools** > **Add-ons**
2. Clique em **Get Add-ons...**
3. Digite o código: **2055492159**
4. Clique em **OK**
5. **Reinicie o Anki** completamente (`Cmd + Q`)

### 4. Desabilitar App Nap (macOS)

Execute no Terminal:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

Depois reinicie o Anki novamente.

### 5. Verificar Instalação

Com o Anki rodando, teste a conexão:

```bash
curl http://localhost:8765
```

Se funcionar, você verá uma resposta do AnkiConnect.

---

## ⚠️ Importante: Servidor MCP Anki

### Requisito: Python 3.10+

O pacote `mcp-server-anki` requer **Python 3.10 ou superior**.

**Versão atual do Python:** 3.9.6

**Opções:**

1. **Atualizar Python para 3.10+** (recomendado)
2. **Usar Anki diretamente** sem servidor MCP (alternativa)

---

## 📝 Configuração MCP (Após Instalar Python 3.10+)

Quando tiver Python 3.10+ instalado:

### 1. Instalar Servidor MCP

```bash
pip3 install mcp-server-anki
```

### 2. Configurar no Cursor

Adicione ao arquivo `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    },
    "anki": {
      "command": "/caminho/para/python3.10+",
      "args": ["-m", "mcp_server_anki"],
      "env": {
        "ANKI_CONNECT_URL": "http://localhost:8765"
      }
    }
  }
}
```

### 3. Reiniciar o Cursor

Reinicie completamente o Cursor para aplicar as mudanças.

---

## 🎯 Alternativa: Usar Anki Diretamente (Python 3.9)

Se você não puder atualizar Python, use Anki diretamente via AnkiConnect:

### 1. Instalar requests

```bash
pip3 install requests
```

### 2. Usar no código Python

```python
import requests
import json

def add_note_to_anki(deck_name, front, back):
    """Adiciona um flashcard ao Anki"""
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
    
    response = requests.post(
        "http://localhost:8765",
        data=json.dumps(request_data)
    )
    return response.json()

# Exemplo de uso
result = add_note_to_anki(
    "Default",
    "Qual é a capital do Brasil?",
    "Brasília"
)
print(result)
```

---

## ✅ Checklist de Instalação

### Instalação do Anki
- [ ] Anki baixado
- [ ] Anki instalado (arrastado para Applications)
- [ ] Anki iniciado pela primeira vez

### Plugin AnkiConnect
- [ ] AnkiConnect instalado (código: 2055492159)
- [ ] Anki reiniciado após instalar plugin
- [ ] AnkiConnect verificado (aparece em Tools > Add-ons)

### Configuração macOS
- [ ] App Nap desabilitado (`defaults write net.ichi2.anki NSAppSleepDisabled -bool true`)
- [ ] Anki reiniciado após desabilitar App Nap

### Verificação
- [ ] AnkiConnect testado (`curl http://localhost:8765`)
- [ ] Porta 8765 verificada (`lsof -i :8765`)

### Servidor MCP (Opcional - requer Python 3.10+)
- [ ] Python 3.10+ instalado (se usar mcp-server-anki)
- [ ] `mcp-server-anki` instalado via pip (se usar Python 3.10+)
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado
- [ ] Servidor MCP conectado no Cursor

---

## 📚 Documentação Completa

- **Guia Completo:** `INSTALAR-ANKI-COMPLETO.md`
- **Guia MCP:** `INSTALAR-ANKI.md`
- **Documentação Geral:** `_docs/GUIA-MCP-SERVERS.md`

---

## 🎯 Próximos Passos

1. **Baixe e instale o Anki** (página já aberta no navegador)
2. **Instale o plugin AnkiConnect** (código: 2055492159)
3. **Desabilite App Nap** no Terminal
4. **Teste a conexão** com `curl http://localhost:8765`
5. **Configure o servidor MCP** (se tiver Python 3.10+)

---

**Status:** Guia de instalação criado - Página de download aberta  
**Última Atualização:** 2025-01-08
