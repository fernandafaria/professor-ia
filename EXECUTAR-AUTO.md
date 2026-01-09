# 🚀 Executar Instalação Automática

## Script Automático Disponível

O script `instalar_pre_requisitos_auto.sh` instala todos os pré-requisitos automaticamente, sem perguntas.

## ⚡ Execução Rápida

```bash
cd /Users/fernandafaria/Downloads/P1A
./instalar_pre_requisitos_auto.sh
```

## 📋 O Que Será Instalado

1. **Homebrew** (se não estiver instalado)
2. **Python 3.10+** (se atual < 3.10)
3. **pnpm** (se não estiver instalado)
4. **PostgreSQL 15** (se não estiver instalado)
   - Inicia o serviço automaticamente
   - Cria o banco `p1a_db` automaticamente

## 🐘 PostgreSQL no Supabase (Recomendado)

**⚠️ IMPORTANTE:** O projeto usa **Supabase PostgreSQL** para o sistema RAG.

### Configurar Supabase:

1. **Criar projeto no Supabase:**
   - Acesse: https://supabase.com
   - Crie um novo projeto
   - Anote a senha do banco de dados

2. **Executar script SQL:**
   ```bash
   # No Supabase Dashboard → SQL Editor
   # Execute: backend/setup_supabase_postgresql.sql
   ```

3. **Configurar Connection String:**
   ```bash
   # Edite backend/.env
   DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
   ```

4. **Verificar configuração:**
   ```bash
   cd backend
   python3 verificar_supabase.py
   ```

**📖 Guia completo:** `backend/CONFIGURAR-SUPABASE-POSTGRESQL.md`

---

## ⚠️ Requisitos

- **Permissões de administrador** (para instalar Homebrew)
- **Conexão com internet**
- **Tempo:** 10-15 minutos
- **Conta Supabase** (para PostgreSQL)

## 🔍 Após Executar

1. **Recarregue o shell:**
   ```bash
   source ~/.zshrc
   ```

2. **Verifique a instalação:**
   ```bash
   ./verificar_pre_requisitos.sh
   ```

3. **Configure Supabase:**
   ```bash
   cd backend
   python3 verificar_supabase.py
   ```

## 📝 Notas

- O script **não faz perguntas** - instala tudo automaticamente
- Pode solicitar sua **senha de administrador** durante a instalação do Homebrew
- Se algum item já estiver instalado, o script **pula** automaticamente
- **PostgreSQL local é opcional** - o projeto usa Supabase

---

**Pronto para executar!** 🎯
