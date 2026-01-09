# 🐍 Instalação do Python 3.11+ - Método Alternativo

Como o Homebrew está demorando para compilar dependências no macOS 12, vamos usar o **instalador oficial do Python.org**, que é pré-compilado e muito mais rápido.

---

## 🚀 Método 1: Instalador Oficial (Recomendado - Mais Rápido)

### Passo 1: Baixar Python 3.11

1. **Acesse:** https://www.python.org/downloads/release/python-31114/
2. **Baixe:** "macOS 64-bit universal2 installer" (arquivo `.pkg`)
   - Ou link direto: https://www.python.org/ftp/python/3.11.14/python-3.11.14-macos11.pkg

### Passo 2: Instalar

1. Abra o arquivo `.pkg` baixado
2. Siga o assistente de instalação
3. **Importante:** Marque "Add Python to PATH" se a opção aparecer

### Passo 3: Verificar Instalação

```bash
# Verificar versão
python3.11 --version
# Deve mostrar: Python 3.11.14

# Verificar localização
which python3.11
# Geralmente: /usr/local/bin/python3.11 ou /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
```

---

## 🔧 Método 2: Continuar Instalação Homebrew (Se Preferir)

Se quiser continuar com Homebrew, você pode:

### Opção A: Aguardar Compilação

A instalação do `openssl@3` pode demorar 10-30 minutos. Você pode:

1. **Deixar rodando em background:**
   ```bash
   brew install python@3.11 &
   ```

2. **Ou executar novamente:**
   ```bash
   brew install python@3.11
   ```
   (Deixe rodar até completar - pode demorar)

### Opção B: Usar Versão Pré-compilada (Se Disponível)

```bash
# Tentar instalar sem compilar
brew install --force-bottle python@3.11
```

---

## ✅ Após Instalação (Qualquer Método)

### 1. Verificar Instalação

```bash
python3.11 --version
python3.11 -m pip --version
```

### 2. Configurar para o Projeto

**Opção A: Usar python3.11 diretamente**

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Instalar dependências com Python 3.11
python3.11 -m pip install -r requirements.txt

# Executar scripts com Python 3.11
python3.11 verificar_pre_requisitos_rag.py
```

**Opção B: Criar Virtual Environment**

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Criar venv com Python 3.11
python3.11 -m venv venv

# Ativar
source venv/bin/activate

# Verificar versão no venv
python --version  # Deve mostrar 3.11.x

# Instalar dependências
pip install -r requirements.txt
```

**Opção C: Criar Alias (Opcional)**

Adicione ao `~/.zshrc`:

```bash
echo 'alias python3="/usr/local/bin/python3.11"' >> ~/.zshrc
source ~/.zshrc

# Agora python3 apontará para 3.11
python3 --version
```

---

## 🧪 Testar Instalação

```bash
# 1. Verificar versão
python3.11 --version

# 2. Testar importações básicas
python3.11 -c "import sys; print(f'Python {sys.version}')"

# 3. Instalar pacote de teste
python3.11 -m pip install requests
python3.11 -c "import requests; print('✅ requests instalado')"
```

---

## 📝 Notas Importantes

1. **Python 3.9.6 continuará disponível** como `python3` (sistema)
2. **Python 3.11 será** `python3.11` após instalação
3. **Recomendado:** Usar `venv` para isolar dependências do projeto
4. **Para produção:** Use sempre `python3.11` explicitamente ou configure `venv`

---

## 🐛 Troubleshooting

### Problema: "command not found: python3.11"

**Solução:**
```bash
# Verificar se foi instalado
ls -la /usr/local/bin/python3.11
ls -la /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11

# Se não encontrar, reinstalar ou verificar PATH
echo $PATH
```

### Problema: "pip não encontrado"

**Solução:**
```bash
# Instalar pip
python3.11 -m ensurepip --upgrade
python3.11 -m pip --version
```

### Problema: Quer usar como padrão

**Solução:**
```bash
# Adicionar ao PATH no ~/.zshrc
export PATH="/usr/local/bin:$PATH"
# ou
export PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:$PATH"
```

---

## ✅ Próximos Passos Após Instalação

1. ✅ Instalar dependências do projeto
2. ✅ Re-executar verificação de pré-requisitos
3. ✅ Configurar ANTHROPIC_API_KEY
4. ✅ Corrigir DATABASE_URL

---

## 🎯 Recomendação

**Para macOS 12 (Monterey):** Use o **instalador oficial do Python.org** (Método 1) - é mais rápido e confiável.

**Link direto:** https://www.python.org/ftp/python/3.11.14/python-3.11.14-macos11.pkg

Após instalar, execute:
```bash
python3.11 --version
cd /Users/fernandafaria/Downloads/P1A/backend
python3.11 -m pip install -r requirements.txt
```
