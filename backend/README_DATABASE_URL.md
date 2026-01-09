# 🔗 Database URL - Instruções Rápidas

## ⚡ Resumo Ultra Simples

### O que você precisa:
1. **A senha do banco Supabase**
2. **Copiar o template abaixo e substituir a senha**

---

## 📋 Template (Copie e Cole)

### Para Aplicação (Recomendado):
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

### Para Migrations:
```env
DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@db.mzhgkbdnslnlpfciduru.supabase.co:5432/postgres
```

**Só substitua `SUA_SENHA` pela senha do banco!**

---

## 🔑 Como Obter a Senha

### Opção 1: Você já tem a senha
- Use a senha que você anotou ao criar o projeto
- Substitua `SUA_SENHA` no template acima

### Opção 2: Resetar a senha (se esqueceu)

1. **Acesse:** https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database

2. **Role até:** "Database password"

3. **Clique em:** "Reset database password"

4. **Copie a senha** que aparece (ela só aparece uma vez!)

5. **Use no template** acima

---

## 💻 Configurar

1. Edite o arquivo: `backend/.env`

2. Cole uma das URLs acima (substituindo `SUA_SENHA`)

3. Salve o arquivo

---

## ✅ Testar

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 obter_database_url.py
```

Ou teste a conexão:
```bash
python3 -c "from app.config import settings; print('DATABASE_URL configurada!' if settings.DATABASE_URL else '❌ Não configurada')"
```

---

## 🆘 Ainda com Dúvida?

Execute o script de ajuda:
```bash
cd /Users/fernandafaria/Downloads/P1A/backend
python3 obter_database_url.py
```

---

**Link direto para resetar senha:**  
https://app.supabase.com/project/mzhgkbdnslnlpfciduru/settings/database
