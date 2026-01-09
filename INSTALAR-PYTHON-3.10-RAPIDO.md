# ⚡ Instalar Python 3.10+ - Rápido

## 🎯 Situação Atual

- **Python atual:** 3.9.6 (sistema)
- **Python necessário:** 3.10+
- **Homebrew:** Não instalado

---

## 🚀 Opção 1: Script Automatizado (Recomendado)

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_python_3.10.sh
```

**O que faz:**
1. Instala Homebrew (se necessário)
2. Instala Python 3.10+
3. Configura PATH
4. Oferece criar aliases

**Tempo:** 10-15 minutos (depende da conexão)

---

## 🚀 Opção 2: Manual (3 Passos)

### Passo 1: Instalar Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Depois configure o PATH:**

```bash
# Para Mac Apple Silicon (M1/M2/M3)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

# Para Mac Intel
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/usr/local/bin/brew shellenv)"
```

### Passo 2: Instalar Python 3.10

```bash
brew install python@3.10
```

### Passo 3: Verificar

```bash
python3.10 --version
```

---

## ✅ Após Instalar

### Usar Python 3.10

```bash
# Usar explicitamente
python3.10 --version

# Ou criar alias (opcional)
echo 'alias python3=/opt/homebrew/bin/python3.10' >> ~/.zshrc
source ~/.zshrc
python3 --version  # Agora será 3.10
```

### Criar Ambiente Virtual

```bash
cd backend
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔍 Verificar Instalação

```bash
# Verificar versão
python3.10 --version

# Verificar localização
which python3.10

# Verificar pip
pip3.10 --version
```

---

## ⚠️ Notas Importantes

1. **Python do sistema (3.9.6) permanece intacto**
   - Não será substituído
   - Python 3.10 será instalado separadamente

2. **Múltiplas versões podem coexistir:**
   - `python3` → 3.9.6 (sistema)
   - `python3.10` → 3.10.x (Homebrew)

3. **Use `python3.10` explicitamente** quando necessário para garantir a versão correta

---

## 📚 Documentação Completa

Veja: `ATUALIZAR-PYTHON-3.10.md`

---

**Próximo Passo:** Execute o script ou siga os passos manuais acima!
