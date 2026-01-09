# 🚀 Quick Start - Instalação de Pré-requisitos

## ✅ Status Atual

| Ferramenta | Status | Versão |
|------------|--------|--------|
| ✅ Node.js | Instalado | v24.12.0 |
| ✅ npm | Instalado | 11.6.2 |
| ✅ Git | Instalado | 2.37.1 |
| ❌ Homebrew | **Precisa instalar** | - |
| ⚠️ Python | Instalado mas antigo | 3.9.6 (precisa 3.10+) |
| ❌ PostgreSQL | **Precisa instalar** | - |
| ❌ pnpm | **Precisa instalar** | - |
| ⚠️ Docker | Opcional | - |

---

## 🎯 Instalação Rápida (3 Passos)

### Passo 1: Instalar Homebrew

**Execute no terminal:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Após instalar, adicione ao PATH:**

```bash
# Para Mac Apple Silicon (M1/M2/M3)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

# Para Mac Intel
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/usr/local/bin/brew shellenv)"
```

---

### Passo 2: Instalar Tudo de Uma Vez

**Execute este comando (instala tudo necessário):**

```bash
# Instalar Python 3.10, PostgreSQL, pnpm
brew install python@3.10 postgresql@15
npm install -g pnpm

# Adicionar PostgreSQL ao PATH
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Iniciar PostgreSQL
brew services start postgresql@15

# Criar banco de dados
createdb p1a_db
```

---

### Passo 3: Verificar Instalação

**Execute o script de verificação:**

```bash
cd /Users/fernandafaria/Downloads/P1A
./verificar_pre_requisitos.sh
```

**Ou verifique manualmente:**

```bash
python3.10 --version  # Deve mostrar Python 3.10.x
node --version         # Deve mostrar v24.12.0
pnpm --version         # Deve mostrar versão do pnpm
psql --version         # Deve mostrar PostgreSQL 15.x
brew --version         # Deve mostrar Homebrew
```

---

## 📋 Comandos Individuais (Se Preferir)

### 1. Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Python 3.10+
```bash
brew install python@3.10
```

### 3. PostgreSQL 15
```bash
brew install postgresql@15
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
brew services start postgresql@15
createdb p1a_db
```

### 4. pnpm
```bash
npm install -g pnpm
```

### 5. Docker (Opcional)
```bash
brew install --cask docker
# Depois abra Docker Desktop manualmente
```

---

## 🔧 Configurar Git (Se Ainda Não Configurado)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

## 📚 Documentação Completa

Para instruções detalhadas e troubleshooting, consulte:
- **`INSTALAR-PRE-REQUISITOS.md`** - Guia completo passo a passo

---

## ✅ Checklist Final

Após instalar, verifique:

- [ ] Homebrew instalado e funcionando
- [ ] Python 3.10+ disponível (`python3.10 --version`)
- [ ] PostgreSQL 15 instalado e rodando (`psql --version`)
- [ ] Banco `p1a_db` criado (`psql -d p1a_db -c "SELECT 1;"`)
- [ ] pnpm instalado (`pnpm --version`)
- [ ] Git configurado (nome e email)
- [ ] Docker Desktop instalado e rodando (opcional)

---

**Próximo Passo:** Após instalar tudo, configure o ambiente Python:
```bash
cd backend
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

**Última Atualização:** 2025-01-08
