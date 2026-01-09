# 🚀 Instalar Anki - Passo a Passo Completo

**Status Atual:** Anki não está instalado  
**Próximo Passo:** Download e instalação do Anki

---

## 📥 Passo 1: Download do Anki

A página de download foi aberta no seu navegador: **https://apps.ankiweb.net/**

### Se a página não abriu:

1. **Acesse manualmente:** https://apps.ankiweb.net/
2. **Clique em "Download"** para macOS
3. **Baixe a versão apropriada:**
   - Intel Mac: Versão Intel
   - Apple Silicon (M1/M2/M3): Versão Apple Silicon

---

## 📦 Passo 2: Instalar o Anki

### 2.1 Abrir o arquivo baixado

1. Encontre o arquivo `.dmg` baixado (geralmente na pasta Downloads)
2. Clique duas vezes no arquivo para abrir

### 2.2 Instalar no Applications

1. Uma janela será aberta mostrando o aplicativo Anki
2. **Arraste o ícone do Anki** para a pasta **Applications**
3. Aguarde a cópia ser concluída

### 2.3 Iniciar o Anki pela primeira vez

1. Abra a pasta **Applications** (ou use Spotlight: `Cmd + Space` e digite "Anki")
2. Clique duas vezes no **Anki** para iniciar
3. Na primeira vez, pode aparecer um aviso de segurança (normal no macOS)
4. Se aparecer o aviso: **Control + Click** no Anki > **Abrir** > **Abrir** novamente

---

## 🔌 Passo 3: Instalar Plugin AnkiConnect

### 3.1 Abrir Gerenciador de Add-ons

1. Com o Anki aberto, vá em **Tools** (Ferramentas) no menu superior
2. Clique em **Add-ons** (Complementos)
   - Ou pressione `Cmd + Shift + A`

### 3.2 Instalar AnkiConnect

1. No gerenciador de add-ons, clique em **Get Add-ons...** (Obter complementos)
2. No campo que aparece, digite exatamente: **2055492159**
3. Clique em **OK**
4. O AnkiConnect será baixado e instalado automaticamente

### 3.3 Reiniciar o Anki

**⚠️ IMPORTANTE:** Após instalar o plugin, você DEVE reiniciar o Anki:

1. Feche completamente o Anki (`Cmd + Q`)
2. Abra novamente o Anki
3. O AnkiConnect estará ativo

---

## 🛠️ Passo 4: Desabilitar App Nap (macOS)

O App Nap do macOS pode interferir no AnkiConnect quando o Anki está em background.

### 4.1 Executar comando

Abra o Terminal e execute:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

**Ou execute o script criado:**

```bash
cd /Users/fernandafaria/Downloads/P1A
./desabilitar_app_nap_anki.sh
```

### 4.2 Reiniciar o Anki novamente

1. Feche completamente o Anki (`Cmd + Q`)
2. Abra novamente o Anki

---

## ✅ Passo 5: Verificar Instalação

### 5.1 Verificar se AnkiConnect está instalado

1. No Anki, vá em **Tools** > **Add-ons**
2. Verifique se **AnkiConnect** aparece na lista com código **2055492159**
3. O status deve mostrar como instalado

### 5.2 Testar conexão AnkiConnect

**Certifique-se de que o Anki está rodando**, depois abra o Terminal e execute:

```bash
curl http://localhost:8765
```

**Resposta esperada:**
Se funcionar, você verá algo como:
```
AnkiConnect v.X.X.X
```

**Se não funcionar:**
- Certifique-se de que o Anki está rodando
- Verifique se o plugin está instalado
- Reinicie o Anki completamente

### 5.3 Verificar porta 8765

Para verificar se a porta está aberta:

```bash
lsof -i :8765
```

**Se funcionar, você verá algo como:**
```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
Anki     1234 user   42u  IPv4  ...      0t0  TCP localhost:8765 (LISTEN)
```

---

## 📦 Passo 6: Instalar Servidor MCP (Opcional)

⚠️ **Nota:** O servidor MCP Anki requer **Python 3.10 ou superior**.

**Versão atual do Python:** 3.9.6

### Opção A: Atualizar Python para 3.10+ (Recomendado)

Se você quiser usar o servidor MCP Anki, precisará atualizar o Python.

### Opção B: Usar Anki Diretamente (Alternativa)

Você pode usar Anki diretamente via AnkiConnect sem servidor MCP intermediário. Veja a seção abaixo.

---

## 🎯 Alternativa: Usar Anki Diretamente (Sem MCP)

Se você não puder atualizar Python agora, pode usar Anki diretamente via AnkiConnect:

### 1. Instalar biblioteca requests

```bash
pip3 install requests
```

### 2. Usar no código Python

Crie um arquivo `anki_helper.py`:

```python
import requests
import json

def add_note_to_anki(deck_name, front, back, tags=None):
    """
    Adiciona um flashcard ao Anki via AnkiConnect
    
    Args:
        deck_name: Nome do deck (ex: "Default")
        front: Frente do cartão (pergunta)
        back: Verso do cartão (resposta)
        tags: Lista de tags (opcional)
    
    Returns:
        Resposta do AnkiConnect
    """
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
                "tags": tags or []
            }
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:8765",
            data=json.dumps(request_data),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        raise Exception("Erro: Anki não está rodando ou AnkiConnect não está instalado")
    except Exception as e:
        raise Exception(f"Erro ao adicionar nota: {e}")

def get_decks():
    """Lista todos os decks disponíveis no Anki"""
    request_data = {
        "action": "deckNames",
        "version": 6
    }
    
    try:
        response = requests.post(
            "http://localhost:8765",
            data=json.dumps(request_data),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Erro ao listar decks: {e}")

def check_connection():
    """Verifica se o AnkiConnect está funcionando"""
    request_data = {
        "action": "version",
        "version": 6
    }
    
    try:
        response = requests.post(
            "http://localhost:8765",
            data=json.dumps(request_data),
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Exemplo de uso
if __name__ == "__main__":
    # Verificar conexão
    print("Verificando conexão com Anki...")
    version = check_connection()
    print(f"Versão do AnkiConnect: {version}")
    
    # Listar decks
    print("\nListando decks...")
    decks = get_decks()
    print(f"Decks disponíveis: {decks}")
    
    # Adicionar flashcard
    print("\nAdicionando flashcard...")
    result = add_note_to_anki(
        "Default",
        "Qual é a capital do Brasil?",
        "Brasília"
    )
    print(f"Resultado: {result}")
```

### 3. Usar o helper

```python
from anki_helper import add_note_to_anki, get_decks

# Listar decks
decks = get_decks()
print(f"Decks: {decks}")

# Adicionar flashcard
result = add_note_to_anki(
    "Default",
    "O que é Python?",
    "Python é uma linguagem de programação de alto nível"
)
print(result)
```

---

## ✅ Checklist de Instalação

### Instalação do Anki
- [ ] Anki baixado do site oficial
- [ ] Arquivo .dmg aberto
- [ ] Anki arrastado para Applications
- [ ] Anki iniciado pela primeira vez
- [ ] Anki funcionando normalmente

### Plugin AnkiConnect
- [ ] AnkiConnect instalado (código: 2055492159)
- [ ] Anki reiniciado após instalar plugin
- [ ] AnkiConnect verificado em Tools > Add-ons

### Configuração macOS
- [ ] App Nap desabilitado (comando executado)
- [ ] Anki reiniciado após desabilitar App Nap

### Verificação
- [ ] AnkiConnect testado (`curl http://localhost:8765`)
- [ ] Porta 8765 verificada (`lsof -i :8765`)
- [ ] Teste de conexão bem-sucedido

### Servidor MCP (Opcional - requer Python 3.10+)
- [ ] Python 3.10+ instalado
- [ ] `mcp-server-anki` instalado via pip
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado
- [ ] Servidor MCP conectado no Cursor

---

## 🎯 Próximos Passos Imediatos

1. **✅ Baixe o Anki** (página já aberta: https://apps.ankiweb.net/)
2. **Instale o Anki** (arraste para Applications)
3. **Abra o Anki** pela primeira vez
4. **Instale o plugin AnkiConnect** (código: 2055492159)
5. **Reinicie o Anki** completamente
6. **Desabilite App Nap** (execute `./desabilitar_app_nap_anki.sh`)
7. **Teste a conexão** (`curl http://localhost:8765`)

---

## 📚 Recursos e Documentação

- **Site Oficial Anki:** https://apps.ankiweb.net/
- **AnkiConnect GitHub:** https://github.com/FooSoft/anki-connect
- **AnkiConnect Plugin:** Código 2055492159
- **Documentação Completa:** `INSTALAR-ANKI-COMPLETO.md`
- **Quick Start:** `ANKI-INSTALACAO-QUICK-START.md`

---

## 🔧 Troubleshooting

### Anki não abre após instalação

**Solução macOS:**
1. **Control + Click** no Anki em Applications
2. Selecione **Abrir**
3. Clique em **Abrir** na mensagem de segurança
4. O Anki abrirá normalmente

### AnkiConnect não aparece nos add-ons

**Soluções:**
1. Verifique se digitou o código correto: **2055492159**
2. Reinicie o Anki completamente
3. Verifique sua conexão com a internet
4. Tente reinstalar o plugin

### AnkiConnect não responde

**Soluções:**
1. Certifique-se de que o Anki está rodando
2. Verifique se o plugin está instalado
3. Reinicie o Anki completamente
4. Desabilite App Nap: `defaults write net.ichi2.anki NSAppSleepDisabled -bool true`
5. Reinicie o Anki novamente

---

**Status:** Guia completo criado - Aguardando instalação do Anki  
**Última Atualização:** 2025-01-08
