# 📦 Instalação de Pré-requisitos - macOS

## Status Atual

✅ **Já Instalado:**
- Node.js v24.12.0
- npm 11.6.2
- Git 2.37.1

⚠️ **Precisa Instalar/Atualizar:**
- Homebrew (gerenciador de pacotes)
- Python 3.10+ (atual: 3.9.6)
- PostgreSQL 15+
- Docker Desktop (opcional)
- pnpm

---

## 🚀 Instalação Passo a Passo

### 1. Instalar Homebrew

**Execute no terminal:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Após instalar, adicione ao PATH:**

```bash
# Para Mac com chip Apple Silicon (M1/M2/M3)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

# Para Mac Intel
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/usr/local/bin/brew shellenv)"
```

**Verificar instalação:**
```bash
brew --version
```

---

### 2. Atualizar Python para 3.10+

```bash
brew install python@3.10
```

**Verificar instalação:**
```bash
python3.10 --version
```

**Nota:** Você pode usar `python3.10` diretamente ou criar um alias:
```bash
alias python3=/opt/homebrew/bin/python3.10  # Apple Silicon
# ou
alias python3=/usr/local/bin/python3.10      # Intel
```

---

### 3. Instalar PostgreSQL 15

```bash
brew install postgresql@15
```

**Adicionar ao PATH:**
```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Iniciar serviço:**
```bash
brew services start postgresql@15
```

**Criar banco de dados:**
```bash
createdb p1a_db
```

**Verificar:**
```bash
psql --version
psql -d p1a_db -c "SELECT version();"
```

---

### 4. Instalar pnpm

```bash
npm install -g pnpm
```

**Verificar:**
```bash
pnpm --version
```

---

### 5. Instalar Docker Desktop (Opcional, mas Recomendado)

**Opção 1: Via Homebrew (mais rápido)**
```bash
brew install --cask docker
```

**Opção 2: Download Manual**
1. Acesse: https://www.docker.com/products/docker-desktop/
2. Baixe Docker Desktop para Mac
3. Instale o arquivo `.dmg`
4. Arraste Docker para Applications
5. Abra Docker Desktop e siga o assistente

**Após instalar, inicie Docker Desktop e verifique:**
```bash
docker --version
docker ps
```

---

### 6. Configurar Git (se ainda não configurado)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

**Verificar:**
```bash
git config --global user.name
git config --global user.email
```

---

## ✅ Verificação Final

Execute este comando para verificar todas as instalações:

```bash
echo "=== Verificação de Pré-requisitos ===" && \
echo "Python:" && python3 --version && \
echo "Python 3.10:" && python3.10 --version 2>/dev/null || echo "Não instalado" && \
echo "Node.js:" && node --version && \
echo "npm:" && npm --version && \
echo "pnpm:" && pnpm --version && \
echo "Git:" && git --version && \
echo "PostgreSQL:" && psql --version && \
echo "Docker:" && docker --version && \
echo "Homebrew:" && brew --version
```

---

## 🔧 Troubleshooting

### Homebrew não encontrado após instalação

```bash
# Recarregar shell
source ~/.zshrc

# Ou adicionar manualmente ao PATH
export PATH="/opt/homebrew/bin:$PATH"  # Apple Silicon
# ou
export PATH="/usr/local/bin:$PATH"     # Intel
```

### PostgreSQL não inicia

```bash
# Verificar status
brew services list

# Iniciar manualmente
brew services start postgresql@15

# Verificar logs
tail -f ~/Library/Logs/Homebrew/postgresql@15.log
```

### Python 3.10 não encontrado

```bash
# Verificar onde foi instalado
which python3.10

# Criar symlink (se necessário)
ln -s /opt/homebrew/bin/python3.10 /usr/local/bin/python3.10
```

### Docker não funciona

1. Certifique-se que Docker Desktop está rodando
2. Verifique se está no grupo docker:
   ```bash
   groups
   ```
3. Reinicie o terminal após instalar Docker

---

## 📝 Próximos Passos

Após instalar todos os pré-requisitos:

1. **Reinicie o terminal** ou execute:
   ```bash
   source ~/.zshrc
   ```

2. **Configure o ambiente Python:**
   ```bash
   cd backend
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Configure variáveis de ambiente:**
   - Crie `backend/.env` com suas credenciais

4. **Inicie os serviços:**
   - PostgreSQL: `brew services start postgresql@15`
   - Docker: Abra Docker Desktop

---

## 🎯 Script Automatizado

Se preferir, você pode executar o script automatizado (requer senha de admin):

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_pre_requisitos.sh
```

**Nota:** O script pode solicitar sua senha de administrador durante a instalação.

---

**Última Atualização:** 2025-01-08
