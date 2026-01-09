# 🔗 Como Conectar ao GitHub

Guia passo a passo para conectar seu repositório local ao GitHub e fazer push do primeiro commit.

---

## 🚀 Opção 1: Criar Repositório Novo no GitHub

### **Passo 1: Criar Repositório no GitHub**

1. **Acesse:** https://github.com
2. **Faça login** (ou crie conta se não tiver)
3. **Clique no "+"** (canto superior direito) → **"New repository"**
4. **Preencha:**
   - **Repository name:** `P1A` (ou `professor-ia`, `p1a-platform`, etc.)
   - **Description:** "Plataforma Educacional - Professor IA"
   - **Visibility:** 
     - ✅ **Public** (visível para todos)
     - ✅ **Private** (apenas você)
   - **NÃO marque:**
     - ❌ "Add a README file" (você já tem)
     - ❌ "Add .gitignore" (você já tem)
     - ❌ "Choose a license" (opcional)
5. **Clique em "Create repository"**

### **Passo 2: Conectar Repositório Local**

**GitHub vai mostrar instruções. Execute no terminal:**

```bash
cd /Users/fernandafaria/Downloads/P1A

# Adicionar remote do GitHub
git remote add origin https://github.com/SEU-USUARIO/P1A.git

# Verificar se foi adicionado
git remote -v

# Fazer push do commit inicial
git branch -M main
git push -u origin main
```

**Substitua `SEU-USUARIO` pelo seu username do GitHub!**

---

## 🔄 Opção 2: Usar SSH (Recomendado)

### **Passo 1: Gerar Chave SSH (se ainda não tiver)**

```bash
# Verificar se já tem chave SSH
ls -al ~/.ssh

# Se não tiver, gerar nova chave
ssh-keygen -t ed25519 -C "seu-email@example.com"

# Pressione Enter para aceitar local padrão
# Digite uma senha (ou deixe vazio)
```

### **Passo 2: Adicionar Chave SSH ao GitHub**

```bash
# Copiar chave pública
cat ~/.ssh/id_ed25519.pub
# Ou no Mac:
pbcopy < ~/.ssh/id_ed25519.pub
```

1. **No GitHub:**
   - Settings → SSH and GPG keys
   - "New SSH key"
   - **Title:** "MacBook" (ou nome que preferir)
   - **Key:** Cole a chave copiada
   - "Add SSH key"

### **Passo 3: Conectar com SSH**

```bash
cd /Users/fernandafaria/Downloads/P1A

# Adicionar remote com SSH
git remote add origin git@github.com:SEU-USUARIO/P1A.git

# Fazer push
git push -u origin main
```

---

## ✅ Verificar se Funcionou

1. **Acesse seu repositório no GitHub:**
   - `https://github.com/SEU-USUARIO/P1A`

2. **Verifique:**
   - ✅ Todos os arquivos aparecem
   - ✅ README.md está visível
   - ✅ Commit inicial aparece no histórico

---

## 🆘 Problemas Comuns

### ❌ "remote origin already exists"

**Solução:**
```bash
# Verificar remotes existentes
git remote -v

# Remover e adicionar novamente
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/P1A.git
```

### ❌ "Permission denied (publickey)"

**Solução:**
- Use HTTPS em vez de SSH:
  ```bash
  git remote set-url origin https://github.com/SEU-USUARIO/P1A.git
  ```
- Ou configure SSH (veja Opção 2 acima)

### ❌ "Authentication failed"

**Solução:**
- GitHub não aceita mais senha via HTTPS
- Use **Personal Access Token**:
  1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. "Generate new token"
  3. Marque: `repo` (acesso completo)
  4. Copie o token
  5. Use o token como senha ao fazer push

### ❌ "Repository not found"

**Solução:**
- Verifique se o nome do repositório está correto
- Verifique se você tem permissão de escrita
- Certifique-se de que o repositório existe no GitHub

---

## 📋 Checklist

- [ ] Repositório criado no GitHub
- [ ] Remote adicionado (`git remote add origin`)
- [ ] Push realizado (`git push -u origin main`)
- [ ] Arquivos aparecem no GitHub
- [ ] README.md visível

---

## 🎯 Próximos Passos

Após conectar ao GitHub:

1. **Configurar Deploy Automático:**
   - Vercel/Railway podem fazer deploy automático
   - Veja: `DEPLOY-ONLINE.md`

2. **Criar Branches:**
   ```bash
   git checkout -b develop
   git push -u origin develop
   ```

3. **Configurar GitHub Actions (Opcional):**
   - CI/CD automático
   - Testes automáticos

---

**Pronto!** Seu código está no GitHub! 🎉

---

**Última atualização:** 2026-01-09
