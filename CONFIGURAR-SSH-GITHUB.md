# 🔐 Configurar SSH para GitHub

Guia passo a passo para configurar SSH e fazer push sem precisar digitar senha/token toda vez.

---

## ✅ Passo 1: Verificar se já tem chave SSH

```bash
ls -al ~/.ssh
```

**Se você ver arquivos como:**
- `id_ed25519` e `id_ed25519.pub` ✅ (já tem chave)
- `id_rsa` e `id_rsa.pub` ✅ (já tem chave)

**Pule para Passo 3** (adicionar chave ao GitHub)

**Se não tiver nenhum desses arquivos**, continue no Passo 2.

---

## 🔑 Passo 2: Gerar Nova Chave SSH

```bash
# Gerar chave SSH (recomendado: ed25519)
ssh-keygen -t ed25519 -C "seu-email@example.com"

# Ou se seu sistema não suporta ed25519:
ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
```

**Quando pedir:**
1. **"Enter file in which to save the key"** → Pressione **Enter** (usa local padrão: `~/.ssh/id_ed25519`)
2. **"Enter passphrase"** → Digite uma senha (ou deixe vazio para não pedir senha)
3. **"Enter same passphrase again"** → Confirme a senha

**Resultado:**
- Chave privada: `~/.ssh/id_ed25519` (NUNCA compartilhe!)
- Chave pública: `~/.ssh/id_ed25519.pub` (esta você vai adicionar ao GitHub)

---

## 📋 Passo 3: Copiar Chave Pública

### **No Mac:**

```bash
# Copiar chave pública para clipboard
pbcopy < ~/.ssh/id_ed25519.pub

# Ou ver o conteúdo:
cat ~/.ssh/id_ed25519.pub
```

### **No Linux:**

```bash
# Copiar chave pública para clipboard (se tiver xclip)
xclip -sel clip < ~/.ssh/id_ed25519.pub

# Ou ver o conteúdo:
cat ~/.ssh/id_ed25519.pub
```

**A chave será algo como:**
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... seu-email@example.com
```

---

## 🔗 Passo 4: Adicionar Chave ao GitHub

1. **Acesse:** https://github.com/settings/keys
2. **Clique em:** "New SSH key"
3. **Preencha:**
   - **Title:** "MacBook" (ou nome que identifique seu computador)
   - **Key type:** Authentication Key
   - **Key:** Cole a chave pública que você copiou (começa com `ssh-ed25519` ou `ssh-rsa`)
4. **Clique em:** "Add SSH key"
5. **Confirme sua senha do GitHub** (se pedir)

---

## ✅ Passo 5: Testar Conexão SSH

```bash
# Testar conexão com GitHub
ssh -T git@github.com
```

**Primeira vez pode pedir:**
```
The authenticity of host 'github.com (...)' can't be established.
Are you sure you want to continue connecting (yes/no)?
```
Digite `yes` e pressione Enter.

**Se funcionar, você verá:**
```
Hi fernandafaria! You've successfully authenticated, but GitHub does not provide shell access.
```

✅ **Sucesso!** SSH está configurado!

---

## 🚀 Passo 6: Fazer Push com SSH

O remote já está configurado para SSH. Agora é só fazer push:

```bash
cd /Users/fernandafaria/Downloads/P1A

# Verificar remote (deve mostrar git@github.com)
git remote -v

# Fazer push
git push -u origin main
```

**Não vai pedir senha!** SSH usa a chave automaticamente. 🎉

---

## 🔄 Se já tinha chave SSH

Se você já tinha uma chave SSH mas não estava no GitHub:

1. **Copie a chave pública:**
   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   # Ou
   cat ~/.ssh/id_ed25519.pub
   ```

2. **Adicione ao GitHub:**
   - https://github.com/settings/keys
   - "New SSH key"
   - Cole a chave

3. **Teste:**
   ```bash
   ssh -T git@github.com
   ```

4. **Faça push:**
   ```bash
   git push -u origin main
   ```

---

## 🆘 Problemas Comuns

### ❌ "Permission denied (publickey)"

**Soluções:**

1. **Verificar se a chave está no GitHub:**
   - Acesse: https://github.com/settings/keys
   - Veja se sua chave está listada

2. **Verificar se está usando a chave correta:**
   ```bash
   # Ver qual chave está sendo usada
   ssh -vT git@github.com
   ```
   - Veja nos logs qual chave está tentando usar
   - Certifique-se de que essa chave está no GitHub

3. **Adicionar chave ao ssh-agent:**
   ```bash
   # Iniciar ssh-agent
   eval "$(ssh-agent -s)"
   
   # Adicionar chave
   ssh-add ~/.ssh/id_ed25519
   ```

### ❌ "Host key verification failed"

**Solução:**
```bash
# Remover GitHub das chaves conhecidas e tentar novamente
ssh-keygen -R github.com
ssh -T git@github.com
# Digite "yes" quando pedir
```

### ❌ "Could not resolve hostname github.com"

**Solução:**
- Verifique sua conexão com internet
- Tente: `ping github.com`

---

## 💡 Dicas

1. **Múltiplas chaves SSH:**
   - Você pode ter chaves diferentes para diferentes computadores
   - Cada uma com um "Title" diferente no GitHub

2. **Passphrase:**
   - Se você definiu uma passphrase, precisará digitá-la na primeira vez
   - Ou use `ssh-add` para adicionar ao keychain (Mac)

3. **Keychain (Mac):**
   ```bash
   # Adicionar chave ao keychain (não pede senha depois)
   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
   ```

---

## ✅ Checklist

- [ ] Chave SSH gerada (ou já existia)
- [ ] Chave pública copiada
- [ ] Chave adicionada ao GitHub
- [ ] Conexão SSH testada (`ssh -T git@github.com`)
- [ ] Remote configurado para SSH (`git@github.com:...`)
- [ ] Push realizado com sucesso

---

## 🎯 Após Configurar SSH

**Vantagens:**
- ✅ Não precisa digitar senha/token toda vez
- ✅ Mais seguro que HTTPS
- ✅ Push automático sem autenticação

**Próximos commits:**
```bash
git add .
git commit -m "sua mensagem"
git push  # Sem pedir senha!
```

---

**Pronto!** SSH configurado! Agora você pode fazer push sem autenticação toda vez! 🚀
