# 🐍 Atualizar Python para 3.10+

## 📊 Status Atual

- **Python atual:** 3.9.6
- **Python necessário:** 3.10+
- **Homebrew:** Verificando...

---

## 🚀 Instalação

### Passo 1: Verificar Homebrew

```bash
brew --version
```

Se não estiver instalado, instale primeiro:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Passo 2: Instalar Python 3.10+

```bash
brew install python@3.10
```

### Passo 3: Verificar Instalação

```bash
python3.10 --version
```

Deve mostrar: `Python 3.10.x`

### Passo 4: Configurar PATH (Opcional)

Para usar `python3` apontando para 3.10:

```bash
# Para Mac Apple Silicon (M1/M2/M3)
echo 'alias python3=/opt/homebrew/bin/python3.10' >> ~/.zshrc
echo 'alias pip3=/opt/homebrew/bin/pip3.10' >> ~/.zshrc

# Para Mac Intel
echo 'alias python3=/usr/local/bin/python3.10' >> ~/.zshrc
echo 'alias pip3=/usr/local/bin/pip3.10' >> ~/.zshrc

# Recarregar
source ~/.zshrc
```

---

## ✅ Após Instalar

1. **Verificar versão:**
   ```bash
   python3.10 --version
   ```

2. **Criar ambiente virtual com Python 3.10:**
   ```bash
   cd backend
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🔧 Troubleshooting

### Python 3.10 não encontrado após instalar

```bash
# Verificar onde foi instalado
which python3.10

# Se não estiver no PATH, adicionar:
export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"  # Apple Silicon
# ou
export PATH="/usr/local/opt/python@3.10/bin:$PATH"     # Intel
```

### Múltiplas versões do Python

Você pode ter várias versões instaladas:
- `python3` → 3.9.6 (sistema)
- `python3.10` → 3.10.x (Homebrew)

Use `python3.10` explicitamente quando necessário.

---

**Última Atualização:** 2025-01-08
