# 🎯 Anki - Guia Simples

## ✅ Status: Anki já está instalado!

O Anki está instalado em `/Applications/Anki.app`. Agora só precisa configurar.

---

## 🚀 3 Passos Simples

### 1️⃣ Abrir o Anki

```bash
open -a Anki
```

Ou abra manualmente: **Applications** > **Anki**

---

### 2️⃣ Instalar Plugin (1 minuto)

**No Anki:**

1. **Tools** > **Add-ons** (ou `Cmd + Shift + A`)
2. Clique em **Get Add-ons...**
3. Digite: **2055492159**
4. Clique **OK**
5. **Feche e abra o Anki novamente** (`Cmd + Q`)

**Pronto!** O plugin está instalado.

---

### 3️⃣ Desabilitar App Nap (1 comando)

Execute no Terminal:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

Depois **reinicie o Anki** novamente.

---

## ✅ Testar se Funcionou

Com o Anki rodando, execute:

```bash
curl http://localhost:8765
```

**Se aparecer algo = Funcionou! ✅**

---

## 🎯 Pronto!

Agora você pode usar o Anki. O servidor MCP é opcional (requer Python 3.10+).

---

## 💡 Dica: Usar Anki Diretamente (Mais Simples)

Se não quiser configurar MCP, use Anki diretamente no código Python:

```python
import requests
import json

# Adicionar flashcard
def criar_flashcard(pergunta, resposta):
    dados = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Default",
                "modelName": "Basic",
                "fields": {"Front": pergunta, "Back": resposta}
            }
        }
    }
    requests.post("http://localhost:8765", json=dados)

# Usar
criar_flashcard("O que é Python?", "Linguagem de programação")
```

**Instalar biblioteca:**
```bash
pip3 install requests
```

---

**Fim!** É só isso. 🎉
