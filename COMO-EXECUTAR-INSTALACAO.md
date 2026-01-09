# 🚀 Como Executar a Instalação de Pré-requisitos

## 📋 Opções Disponíveis

Você tem **3 opções** para instalar os pré-requisitos:

---

## Opção 1: Script Interativo (Recomendado) ⭐

**Melhor para:** Primeira vez, quer controle sobre o que instalar

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_pre_requisitos.sh
```

**O que faz:**
- ✅ Pergunta antes de instalar cada item
- ✅ Mostra status de cada instalação
- ✅ Permite pular itens opcionais
- ✅ Mostra resumo final

**Tempo estimado:** 10-15 minutos (dependendo da conexão)

---

## Opção 2: Script Automático (Não-Interativo)

**Melhor para:** Quer instalar tudo de uma vez sem perguntas

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_pre_requisitos_auto.sh
```

**O que faz:**
- ✅ Instala tudo automaticamente
- ✅ Não faz perguntas
- ✅ Mais rápido

**Tempo estimado:** 10-15 minutos

**⚠️ Nota:** Pode solicitar senha de administrador durante a instalação do Homebrew.

---

## Opção 3: Instalação Manual Passo a Passo

**Melhor para:** Prefere controle total, quer entender cada passo

Siga o guia: **`QUICK-START-PRE-REQUISITOS.md`**

Ou o guia completo: **`INSTALAR-PRE-REQUISITOS.md`**

---

## 🔍 Verificar Instalação

Após instalar, verifique tudo:

```bash
cd /Users/fernandafaria/Downloads/P1A
./verificar_pre_requisitos.sh
```

---

## 📝 O Que Será Instalado

### Essenciais:
- ✅ **Homebrew** - Gerenciador de pacotes
- ✅ **Python 3.10+** - Linguagem de programação
- ✅ **PostgreSQL 15** - Banco de dados
- ✅ **pnpm** - Gerenciador de pacotes Node.js

### Já Instalados:
- ✅ Node.js v24.12.0
- ✅ npm 11.6.2
- ✅ Git 2.37.1

### Opcionais:
- ⚠️ Docker Desktop - Para containers (opcional)

---

## ⚠️ Requisitos

- **macOS** (este script é para macOS)
- **Permissões de administrador** (para instalar Homebrew)
- **Conexão com internet** (para baixar pacotes)

---

## 🐛 Troubleshooting

### Erro: "Permission denied"
```bash
chmod +x instalar_pre_requisitos.sh
```

### Erro: "Homebrew installation failed"
- Verifique se tem permissões de administrador
- Execute manualmente: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

### Erro: "Command not found" após instalação
```bash
source ~/.zshrc
# ou reinicie o terminal
```

---

## ✅ Após Instalar

1. **Reinicie o terminal** ou execute:
   ```bash
   source ~/.zshrc
   ```

2. **Configure Git** (se ainda não configurado):
   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu@email.com"
   ```

3. **Verifique tudo:**
   ```bash
   ./verificar_pre_requisitos.sh
   ```

4. **Configure ambiente Python:**
   ```bash
   cd backend
   python3.10 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

**Última Atualização:** 2025-01-08
