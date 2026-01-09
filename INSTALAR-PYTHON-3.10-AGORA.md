# ⚡ Instalar Python 3.10+ Agora

## 🎯 Método Mais Rápido

### Opção 1: Download Direto (Recomendado) ⭐

**Tempo:** ~5 minutos

1. **Acesse:** https://www.python.org/downloads/
2. **Clique em:** "Download Python 3.x.x" (versão mais recente)
3. **Instale:** Execute o arquivo `.pkg` baixado
4. **Verifique:**
   ```bash
   python3.10 --version
   ```

**Pronto!** ✅

---

### Opção 2: Via Homebrew (Se já tiver instalado)

```bash
brew install python@3.10
python3.10 --version
```

---

## ✅ Após Instalar

### Criar Ambiente Virtual

```bash
cd /Users/fernandafaria/Downloads/P1A/backend

# Criar venv com Python 3.10
python3.10 -m venv venv

# Ativar
source venv/bin/activate

# Verificar
python --version
```

### Instalar Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔍 Verificar Instalação

```bash
# Verificar Python 3.10
python3.10 --version

# Verificar caminho
which python3.10

# Verificar no venv
source venv/bin/activate
python --version
```

---

**Próximo Passo:** Após instalar, execute os scripts de scraping novamente com Python 3.10!
