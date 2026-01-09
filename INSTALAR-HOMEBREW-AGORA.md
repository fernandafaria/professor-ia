# 🍺 Instalar Homebrew Agora

## ⚠️ Necessário

O script precisa do **Homebrew** instalado primeiro. A instalação do Homebrew requer **permissões de administrador** e precisa ser feita manualmente.

## 🚀 Passo a Passo

### 1. Abra o Terminal

Abra o Terminal do macOS (Applications > Utilities > Terminal)

### 2. Execute o Comando de Instalação

**Cole e execute este comando:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. Siga as Instruções

- O script vai solicitar sua **senha de administrador**
- Digite sua senha e pressione Enter
- A instalação pode levar alguns minutos
- Aguarde até ver a mensagem de sucesso

### 4. Configure o PATH

**Após a instalação, execute um destes comandos:**

**Para Mac Apple Silicon (M1/M2/M3):**
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Para Mac Intel:**
```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/usr/local/bin/brew shellenv)"
```

### 5. Verifique a Instalação

```bash
brew --version
```

**Deve mostrar:** `Homebrew 4.x.x` ou similar

---

## ✅ Após Instalar Homebrew

Depois de instalar o Homebrew, você pode:

### Opção A: Executar o Script Automático Novamente

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_pre_requisitos_auto.sh
```

Agora o script vai instalar:
- ✅ Python 3.10+
- ✅ PostgreSQL 15
- ✅ E configurar tudo automaticamente

### Opção B: Instalar Manualmente

```bash
# Python 3.10+
brew install python@3.10

# PostgreSQL 15
brew install postgresql@15
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
brew services start postgresql@15
createdb p1a_db
```

---

## 🔍 Verificar Tudo

Após instalar, execute:

```bash
cd /Users/fernandafaria/Downloads/P1A
./verificar_pre_requisitos.sh
```

---

## 📝 Notas

- A instalação do Homebrew **pode levar 5-10 minutos**
- Você precisará da sua **senha de administrador**
- O Homebrew instala ferramentas em `/opt/homebrew` (Apple Silicon) ou `/usr/local` (Intel)

---

**Próximo Passo:** Instale o Homebrew e depois execute o script novamente! 🚀
