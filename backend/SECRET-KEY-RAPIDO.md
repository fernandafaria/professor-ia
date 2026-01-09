# ⚡ Gerar SECRET_KEY em 30 Segundos

Guia super rápido para gerar e configurar SECRET_KEY no Railway.

---

## 🚀 Passo 1: Gerar a Chave

**No terminal, execute:**

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Ou se `python3` não funcionar:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Exemplo de saída:**
```
m1H5zIA_zin_SSZSaBdBtvqqQQzhkoC34qy0Q8DwLQU
```

**✅ Copie toda essa chave!**

---

## 🚀 Passo 2: Adicionar no Railway

### **Opção A: Via Dashboard**

1. **Acesse:** https://railway.app
2. **Entre no seu projeto**
3. **Clique no serviço do backend**
4. **Vá em "Variables"** (menu lateral ou aba)
5. **Clique em "+ New Variable"** ou **"Add Variable"**
6. **Preencha:**
   - **Key:** `SECRET_KEY`
   - **Value:** Cole a chave que você copiou
7. **Clique em "Add"** ou **"Save"**

### **Opção B: Via Railway CLI (se instalado)**

```bash
railway variables set SECRET_KEY="m1H5zIA_zin_SSZSaBdBtvqqQQzhkoC34qy0Q8DwLQU"
```

---

## ✅ Verificar

Após adicionar:

1. **Verifique se `SECRET_KEY` aparece na lista de variáveis**
2. **Railway faz redeploy automaticamente**
3. **Aguarde o deploy completar**

---

## 🧪 Testar

Após o deploy:

1. **Teste o endpoint de health:**
   ```bash
   curl https://sua-url.railway.app/health
   ```

2. **Teste registro/login no frontend:**
   - Deve funcionar sem erros de JWT

---

## 📋 Exemplo Completo

```bash
# 1. Gerar chave
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
# Saída: m1H5zIA_zin_SSZSaBdBtvqqQQzhkoC34qy0Q8DwLQU

# 2. Copiar chave gerada

# 3. No Railway:
#    - Variables → New Variable
#    - Key: SECRET_KEY
#    - Value: m1H5zIA_zin_SSZSaBdBtvqqQQzhkoC34qy0Q8DwLQU
#    - Add

# 4. Aguardar redeploy automático

# 5. Testar
curl https://sua-url.railway.app/health
```

---

## ⚠️ Importante

- **Mínimo 32 caracteres** (a chave gerada tem ~43, perfeito!)
- **Nunca compartilhe** a chave
- **Nunca commite** no Git
- **Use variáveis de ambiente** do Railway (não arquivo .env)

---

## 🆘 Problemas?

### **"python3: command not found"**

```bash
# Tente:
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Ou instale Python:
# macOS: brew install python3
# Linux: sudo apt install python3
```

### **"ModuleNotFoundError: No module named 'secrets'"**

Isso não deveria acontecer, `secrets` vem com Python 3.6+.

Se acontecer:
- Verifique versão: `python3 --version` (deve ser 3.6+)
- Reinstale Python

---

**Pronto em 30 segundos!** 🎉

**Veja guia completo:** `COMO-GERAR-SECRET-KEY.md`
