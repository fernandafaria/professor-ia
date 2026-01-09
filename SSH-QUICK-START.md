# ⚡ SSH Quick Start - Configuração Rápida

Chave SSH gerada! Agora você precisa adicioná-la ao GitHub.

---

## ✅ O que foi feito

- ✅ Chave SSH gerada: `~/.ssh/id_ed25519`
- ✅ Chave pública copiada para clipboard
- ✅ Remote configurado para SSH: `git@github.com:fernandafaria/professor-ia.git`

---

## 🔗 Passo 1: Adicionar Chave ao GitHub

1. **Acesse:** https://github.com/settings/keys

2. **Clique em:** "New SSH key" (botão verde)

3. **Preencha:**
   - **Title:** `MacBook` (ou nome que identifique seu computador)
   - **Key type:** Authentication Key
   - **Key:** Cole a chave (já está no seu clipboard! Pressione Cmd+V)

4. **Clique em:** "Add SSH key"

5. **Confirme sua senha do GitHub** (se pedir)

---

## ✅ Passo 2: Testar Conexão

```bash
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

## 🚀 Passo 3: Fazer Push

```bash
cd /Users/fernandafaria/Downloads/P1A
git push -u origin main
```

**Não vai pedir senha!** SSH usa a chave automaticamente. 🎉

---

## 📋 Se a chave não estiver no clipboard

Execute para ver a chave:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copie todo o conteúdo (começa com `ssh-ed25519` e termina com seu email) e cole no GitHub.

---

## ✅ Checklist

- [ ] Chave SSH gerada ✅
- [ ] Chave adicionada ao GitHub (https://github.com/settings/keys)
- [ ] Conexão testada (`ssh -T git@github.com`)
- [ ] Push realizado (`git push -u origin main`)

---

**Pronto!** Após adicionar a chave ao GitHub, você pode fazer push! 🚀

Veja guia completo: `CONFIGURAR-SSH-GITHUB.md`
