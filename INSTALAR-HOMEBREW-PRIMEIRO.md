# 🍺 Instalar Homebrew Primeiro

## ⚠️ Importante

O script de instalação precisa do **Homebrew** para instalar Python 3.10+ e PostgreSQL.

## 🚀 Instalação do Homebrew

### Passo 1: Instalar Homebrew

**Execute no terminal:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**O que vai acontecer:**
- Vai solicitar sua senha de administrador
- Vai instalar o Homebrew
- Pode levar alguns minutos

### Passo 2: Configurar PATH

**Após instalar, adicione ao PATH:**

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

### Passo 3: Verificar Instalação

```bash
brew --version
```

**Deve mostrar algo como:** `Homebrew 4.x.x`

---

## ✅ Após Instalar Homebrew

Depois de instalar o Homebrew, você pode:

1. **Executar o script novamente:**
   ```bash
   cd /Users/fernandafaria/Downloads/P1A
   ./instalar_pre_requisitos.sh
   ```

2. **Ou instalar manualmente:**
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

## 📋 Status Atual

✅ **Já Instalado:**
- Node.js v24.12.0
- npm 11.6.2
- pnpm 10.27.0 ✅ (acabou de instalar!)
- Git 2.37.1

❌ **Precisa Homebrew para instalar:**
- Python 3.10+ (atual: 3.9.6)
- PostgreSQL 15

---

## 🔗 Links Úteis

- **Homebrew:** https://brew.sh
- **Documentação:** https://docs.brew.sh

---

**Próximo Passo:** Instale Homebrew e depois execute o script novamente!
