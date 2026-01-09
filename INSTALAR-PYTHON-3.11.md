# 🐍 Instalação do Python 3.11+

Este guia vai instalar Python 3.11 via Homebrew no macOS.

---

## 📋 Pré-requisitos

- ✅ Homebrew instalado (`/opt/homebrew/bin/brew`)
- ✅ Versão atual: Python 3.9.6
- ✅ Versão alvo: Python 3.11+

---

## 🚀 Instalação

### Passo 1: Instalar Python 3.11

```bash
brew install python@3.11
```

### Passo 2: Verificar Instalação

```bash
# Verificar versão instalada
python3.11 --version

# Verificar localização
which python3.11
```

### Passo 3: Configurar como Padrão (Opcional)

Você pode usar Python 3.11 de duas formas:

**Opção A: Usar python3.11 explicitamente**
```bash
python3.11 --version
python3.11 -m pip install ...
```

**Opção B: Criar alias ou atualizar PATH**
```bash
# Adicionar ao ~/.zshrc ou ~/.bash_profile
echo 'alias python3="/opt/homebrew/bin/python3.11"' >> ~/.zshrc
source ~/.zshrc
```

**Opção C: Usar pyenv (recomendado para múltiplas versões)**
```bash
brew install pyenv
pyenv install 3.11.14
pyenv local 3.11.14  # Na pasta do projeto
```

---

## ✅ Verificação Pós-Instalação

Após instalar, execute:

```bash
# 1. Verificar versão
python3.11 --version
# Deve mostrar: Python 3.11.x

# 2. Verificar pip
python3.11 -m pip --version

# 3. Testar importação de módulos básicos
python3.11 -c "import sys; print(f'Python {sys.version}')"
```

---

## 🔧 Configurar para o Projeto P1A

### Opção 1: Usar python3.11 no projeto

Atualize scripts e comandos para usar `python3.11`:

```bash
cd backend
python3.11 -m pip install -r requirements.txt
python3.11 verificar_pre_requisitos_rag.py
```

### Opção 2: Criar virtual environment com Python 3.11

```bash
cd backend

# Criar venv com Python 3.11
python3.11 -m venv venv

# Ativar
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Opção 3: Usar pyenv no projeto

```bash
cd /Users/fernandafaria/Downloads/P1A

# Instalar pyenv se ainda não tiver
brew install pyenv

# Instalar Python 3.11
pyenv install 3.11.14

# Definir como versão local do projeto
pyenv local 3.11.14

# Verificar
python --version  # Deve mostrar 3.11.14
```

---

## 📝 Notas

- Python 3.9.6 continuará disponível como `python3` (sistema)
- Python 3.11 será `python3.11` após instalação
- Para usar como padrão, configure PATH ou use alias
- Recomendado: usar `venv` ou `pyenv` para isolar versões por projeto

---

## 🐛 Troubleshooting

### Problema: "command not found: python3.11"

**Solução:**
```bash
# Verificar se foi instalado
ls -la /opt/homebrew/bin/python3.11

# Se não existir, reinstalar
brew reinstall python@3.11
```

### Problema: "Permission denied"

**Solução:**
```bash
# Verificar permissões do Homebrew
sudo chown -R $(whoami) /opt/homebrew
```

### Problema: Quer remover Python 3.9

**Não recomendado** - Python do sistema não deve ser removido. Use Python 3.11 para o projeto.

---

## ✅ Próximos Passos

Após instalar Python 3.11:

1. ✅ Instalar dependências do projeto
2. ✅ Re-executar verificação de pré-requisitos
3. ✅ Configurar ANTHROPIC_API_KEY
4. ✅ Corrigir DATABASE_URL
