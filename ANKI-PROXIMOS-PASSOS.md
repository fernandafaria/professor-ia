# ✅ Anki Instalado - Próximos Passos

## 📊 Status Atual

- ✅ **Anki instalado** em `/Applications/Anki.app`
- ⚠️ **Anki não está rodando** - Precisa ser aberto
- ❌ **AnkiConnect não está respondendo** - Plugin precisa ser instalado

---

## 🚀 Próximos Passos Imediatos

### 1. Abrir o Anki

**Opção A: Via Finder**
1. Abra o Finder
2. Vá para **Applications** (ou use `Cmd + Shift + A`)
3. Clique duas vezes no **Anki**

**Opção B: Via Spotlight**
1. Pressione `Cmd + Space` (Spotlight)
2. Digite "Anki"
3. Pressione Enter

**Opção C: Via Terminal**
```bash
open -a Anki
```

### 2. Instalar Plugin AnkiConnect

**No Anki, faça:**

1. Vá em **Tools** (Ferramentas) > **Add-ons** (Complementos)
   - Ou pressione `Cmd + Shift + A`

2. Clique em **Get Add-ons...** (Obter complementos)

3. No campo que aparece, digite exatamente: **2055492159**

4. Clique em **OK**

5. O AnkiConnect será baixado e instalado automaticamente

6. **IMPORTANTE:** Feche completamente o Anki (`Cmd + Q`) e abra novamente

### 3. Desabilitar App Nap (macOS)

Execute no Terminal:

```bash
cd /Users/fernandafaria/Downloads/P1A
./desabilitar_app_nap_anki.sh
```

Ou manualmente:

```bash
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
```

Depois **reinicie o Anki novamente**.

### 4. Verificar Instalação

Execute o script de verificação:

```bash
cd /Users/fernandafaria/Downloads/P1A
./verificar_anki.sh
```

Ou teste manualmente:

```bash
curl http://localhost:8765
```

**Se funcionar, você verá uma resposta do AnkiConnect!**

---

## 🎯 Comandos Úteis

### Abrir o Anki

```bash
open -a Anki
```

### Verificar se Anki está rodando

```bash
ps aux | grep -i anki | grep -v grep
```

### Testar AnkiConnect

```bash
curl http://localhost:8765
```

### Verificar porta 8765

```bash
lsof -i :8765
```

### Executar script de verificação completa

```bash
cd /Users/fernandafaria/Downloads/P1A
./verificar_anki.sh
```

---

## 📋 Checklist Rápido

- [ ] **Abra o Anki** (`open -a Anki`)
- [ ] **Instale o plugin AnkiConnect** (código: 2055492159)
- [ ] **Reinicie o Anki** completamente
- [ ] **Desabilite App Nap** (`./desabilitar_app_nap_anki.sh`)
- [ ] **Reinicie o Anki** novamente
- [ ] **Teste a conexão** (`./verificar_anki.sh`)

---

## ✅ Após Completar os Passos

Depois de instalar o AnkiConnect e verificar que está funcionando, você poderá:

1. **Usar Anki diretamente** via AnkiConnect (Python 3.9)
2. **Configurar servidor MCP** (se atualizar Python para 3.10+)

---

## 📚 Documentação

- **Guia Completo:** `INSTALAR-ANKI-COMPLETO.md`
- **Passo a Passo:** `INSTALAR-ANKI-PASSO-A-PASSO.md`
- **Quick Start:** `ANKI-INSTALACAO-QUICK-START.md`

---

**Status:** Anki instalado - Aguardando instalação do plugin AnkiConnect  
**Próximo Passo:** Abrir o Anki e instalar o plugin (código: 2055492159)
