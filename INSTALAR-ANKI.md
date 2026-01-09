# Instalação do Anki e Configuração MCP

**Criado em:** 2025-01-08  
**Status:** Guia de Instalação

---

## 📋 Visão Geral

O Anki é um aplicativo de flashcards para memorização e aprendizado via repetição espaçada. Para usar com MCP, precisamos instalar:

1. **Anki** - Aplicativo principal
2. **AnkiConnect** - Plugin que permite comunicação via API HTTP
3. **mcp-server-anki** - Servidor MCP para integração com Cursor

---

## 🚀 Passo 1: Instalar o Anki

### 1.1 Download do Anki para macOS

1. Acesse o site oficial: [https://apps.ankiweb.net/](https://apps.ankiweb.net/)
2. Clique em **Download for macOS**
3. Baixe a versão apropriada para seu Mac (Intel ou Apple Silicon)

### 1.2 Instalar o Anki

1. Abra o arquivo `.dmg` baixado
2. Arraste o aplicativo **Anki** para a pasta **Applications**
3. Abra a pasta **Applications**
4. Clique duas vezes no **Anki** para iniciar

### 1.3 Primeira Inicialização

Na primeira vez que abrir o Anki:
1. Você pode criar uma conta (opcional)
2. Ou usar offline (recomendado para começar)
3. Siga as instruções iniciais

---

## 🔌 Passo 2: Instalar o Plugin AnkiConnect

### 2.1 Abrir Gerenciador de Add-ons

1. No Anki, vá em **Tools** > **Add-ons** (ou pressione `Cmd + Shift + A`)
2. O gerenciador de add-ons será aberto

### 2.2 Instalar AnkiConnect

1. Clique em **Get Add-ons...**
2. No campo de código, digite: **2055492159**
3. Clique em **OK**
4. O AnkiConnect será baixado e instalado

### 2.3 Reiniciar o Anki

1. Feche completamente o Anki (`Cmd + Q`)
2. Abra novamente o Anki
3. O AnkiConnect estará ativo

### 2.4 Verificar Instalação

1. Vá em **Tools** > **Add-ons**
2. Verifique se **AnkiConnect** aparece na lista
3. O código deve ser **2055492159**

---

## ⚙️ Passo 3: Configurar AnkiConnect (Opcional)

### 3.1 Acessar Configurações

1. No Anki, vá em **Tools** > **Add-ons**
2. Selecione **AnkiConnect** na lista
3. Clique em **Config**

### 3.2 Configurações Padrão (Recomendadas)

Por padrão, o AnkiConnect funciona sem configuração adicional. As configurações padrão são:

```json
{
  "apiKey": null,
  "apiLogPath": null,
  "webBindAddress": "127.0.0.1",
  "webBindPort": 8765,
  "webCorsOriginList": [
    "http://localhost",
    "http://localhost:8765",
    "http://127.0.0.1",
    "http://127.0.0.1:8765"
  ]
}
```

**Nota:** Não é necessário alterar essas configurações a menos que você tenha necessidades específicas.

### 3.3 Salvar e Reiniciar

1. Clique em **OK** ou **Save**
2. Reinicie o Anki se necessário

---

## 🛠️ Passo 4: Desabilitar App Nap (macOS)

O App Nap do macOS pode interferir no funcionamento do AnkiConnect quando o Anki está em background.

### 4.1 Desabilitar App Nap

Abra o Terminal e execute:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

### 4.2 Reiniciar o Anki

1. Feche completamente o Anki (`Cmd + Q`)
2. Abra novamente o Anki

---

## 📦 Passo 5: Instalar Servidor MCP Anki

### 5.1 Instalar Pacote Python

Execute no terminal:

```bash
pip3 install mcp-server-anki
```

**Nota:** O pacote `anki-connect` mencionado na documentação é apenas o plugin do Anki, não um pacote Python separado.

### 5.2 Verificar Instalação

Teste se o servidor MCP está instalado:

```bash
python3 -m mcp_server_anki --help 2>&1 || echo "Verificando..."
```

---

## 🔧 Passo 6: Configurar no Cursor

### 6.1 Atualizar `.cursor/mcp.json`

Adicione a configuração do Anki ao arquivo `.cursor/mcp.json`:

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

### 6.2 Reiniciar o Cursor

**IMPORTANTE:** Reinicie completamente o Cursor após atualizar a configuração.

---

## ✅ Passo 7: Verificar Instalação

### 7.1 Verificar AnkiConnect

1. Certifique-se de que o **Anki está rodando**
2. Abra o navegador e acesse: `http://localhost:8765`
3. Você deve ver uma mensagem ou página do AnkiConnect

Ou teste via curl:

```bash
curl http://localhost:8765
```

### 7.2 Verificar Servidor MCP no Cursor

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `anki` aparece na lista
4. O status deve mostrar "Connected" ou similar

### 7.3 Testar Funcionalidade

No Cursor, você pode testar comandos como:

```
"Crie um flashcard com a pergunta: Qual é a capital do Brasil? e resposta: Brasília"
"Liste todos os flashcards"
"Mostre os decks disponíveis"
```

---

## 🔍 Troubleshooting

### Problema: AnkiConnect não responde

**Soluções:**
1. Certifique-se de que o Anki está **rodando** (verifique na Dock)
2. Verifique se o plugin está instalado: **Tools** > **Add-ons**
3. Reinicie o Anki completamente
4. Verifique o porto: `curl http://localhost:8765`

### Problema: Servidor MCP não conecta

**Soluções:**
1. Certifique-se de que o Anki está rodando
2. Verifique se o caminho do Python está correto no `.cursor/mcp.json`
3. Verifique se `mcp-server-anki` está instalado: `pip3 show mcp-server-anki`
4. Reinicie o Cursor completamente
5. Verifique os logs do Cursor em **Features > MCP**

### Problema: App Nap interferindo

**Solução:**
Execute o comando para desabilitar App Nap:
```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```
Depois reinicie o Anki.

### Problema: AnkiConnect não aparece na lista

**Soluções:**
1. Verifique se instalou o código correto: **2055492159**
2. Reinicie o Anki completamente
3. Reinstale o plugin se necessário

---

## 📚 Recursos

- **Anki Download:** https://apps.ankiweb.net/
- **AnkiConnect GitHub:** https://github.com/FooSoft/anki-connect
- **AnkiConnect Plugin:** Código 2055492159
- **Anki Documentation:** https://docs.ankiweb.net/
- **MCP Anki Server:** https://github.com/modelcontextprotocol/servers (buscar por anki)
- **Documentação Completa:** `_docs/GUIA-MCP-SERVERS.md`

---

## ✅ Checklist de Instalação

- [ ] Anki baixado e instalado
- [ ] Anki iniciado pela primeira vez
- [ ] AnkiConnect instalado (código 2055492159)
- [ ] Anki reiniciado após instalar plugin
- [ ] App Nap desabilitado (macOS)
- [ ] `mcp-server-anki` instalado via pip
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado
- [ ] AnkiConnect verificado (http://localhost:8765)
- [ ] Servidor MCP conectado no Cursor
- [ ] Teste de criação de flashcard realizado

---

**Última Atualização:** 2025-01-08  
**Status:** Guia de Instalação Completo
