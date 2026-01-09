# 🐍 Atualizar Python para 3.10+ - Guia Simples

## ⚠️ Situação Atual

- **Python atual:** 3.9.6
- **Python necessário:** 3.10+
- **Homebrew:** Não instalado

---

## 🚀 Opção Mais Rápida: Download Direto

### Passo 1: Baixar Python 3.10+

1. **Acesse:** https://www.python.org/downloads/
2. **Baixe:** Python 3.10.x ou superior (versão mais recente)
3. **Instale:** Execute o arquivo `.pkg` baixado
4. **Siga o assistente de instalação**

### Passo 2: Verificar Instalação

Abra um novo terminal e execute:

```bash
python3.10 --version
```

**Deve mostrar:** `Python 3.10.x`

### Passo 3: Usar Python 3.10

```bash
# Usar diretamente
python3.10 script.py

# Ou criar alias (opcional)
echo 'alias python3=/usr/local/bin/python3.10' >> ~/.zshrc
source ~/.zshrc
```

---

## 🔧 Após Instalar Python 3.10+

### 1. Criar Ambiente Virtual

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Remover venv antigo (se existir)
rm -rf venv

# Criar novo com Python 3.10
python3.10 -m venv venv

# Ativar
source venv/bin/activate

# Verificar versão
python --version
# Deve mostrar: Python 3.10.x
```

### 2. Instalar Dependências

```bash
# Ativar venv (se não estiver ativo)
source venv/bin/activate

# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt
```

---

## ✅ Verificar Tudo

```bash
# Versão do Python
python3.10 --version

# Caminho do Python 3.10
which python3.10

# Versão no ambiente virtual
source venv/bin/activate
python --version
```

---

## 📋 Checklist

- [ ] Python 3.10+ baixado e instalado
- [ ] `python3.10 --version` funciona
- [ ] Ambiente virtual criado com Python 3.10
- [ ] Dependências instaladas
- [ ] Scripts testados

---

## 🎯 Alternativa: Via Homebrew

Se preferir usar Homebrew (mais fácil para gerenciar versões):

1. **Instalar Homebrew:**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Configurar PATH:**
   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

3. **Instalar Python 3.10:**
   ```bash
   brew install python@3.10
   ```

4. **Verificar:**
   ```bash
   python3.10 --version
   ```

---

**Recomendação:** Use o download direto do Python.org se quiser algo rápido e simples.

---

**Última Atualização:** 2025-01-08
