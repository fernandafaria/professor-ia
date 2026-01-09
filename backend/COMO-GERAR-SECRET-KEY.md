# 🔐 Como Gerar SECRET_KEY para Railway

Guia rápido para gerar uma chave secreta segura para autenticação JWT.

---

## 🚀 Método 1: Usando Python (Recomendado)

### **No Terminal:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Exemplo de saída:**
```
xK9jP2mL8nQ5rT7wV4yZ6bC1dE3fG5hI7jK9lM1nO3pQ5rS7tU9vW1xY3zA5bC7dE9fG
```

### **Copiar e usar:**

1. **Execute o comando** no terminal
2. **Copie a chave gerada** (todo o texto)
3. **Cole no Railway** como valor de `SECRET_KEY`

---

## 🚀 Método 2: Usando Python3 (se Python não funciona)

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🚀 Método 3: Gerar via Script Python

### **Criar arquivo temporário:**

```bash
# Criar arquivo
cat > gerar_secret_key.py << 'EOF'
import secrets

# Gerar chave segura de 32 bytes (base64 URL-safe)
secret_key = secrets.token_urlsafe(32)
print(f"SECRET_KEY={secret_key}")
EOF

# Executar
python gerar_secret_key.py

# Limpar (opcional)
rm gerar_secret_key.py
```

---

## 🔧 Método 4: Online (Alternativa)

Se não tiver Python instalado, você pode usar:

1. **Acesse:** https://www.uuidgenerator.net/
2. **Gere um UUID v4**
3. **Ou use:** https://randomkeygen.com/
4. **Copie uma chave longa** (mínimo 32 caracteres)

**⚠️ Nota:** Não é tão seguro quanto usar Python `secrets`, mas funciona.

---

## 📝 Passo a Passo para Railway

### **1. Gerar a Chave:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### **2. Copiar a Chave Gerada:**

Exemplo:
```
xK9jP2mL8nQ5rT7wV4yZ6bC1dE3fG5hI7jK9lM1nO3pQ5rS7tU9vW1xY3zA5bC7dE9fG
```

### **3. Adicionar no Railway:**

1. **Acesse seu projeto no Railway**
2. **Clique no serviço do backend**
3. **Vá em "Variables"** (ou clique no serviço → "Variables")
4. **Clique em "New Variable"**
5. **Configure:**
   - **Name:** `SECRET_KEY`
   - **Value:** Cole a chave gerada (exemplo acima)
6. **Clique em "Add"**

### **4. Verificar:**

Após adicionar, você deve ver `SECRET_KEY` na lista de variáveis.

---

## ✅ Requisitos da SECRET_KEY

- **Mínimo 32 caracteres** (recomendado: 64+)
- **Aleatória** (não use palavras conhecidas)
- **Única** (não reutilize em outros projetos)
- **Secreta** (nunca compartilhe ou commite no Git)

---

## 🔒 Boas Práticas

### **✅ FAZER:**
- ✅ Gerar chave única para cada ambiente (dev, staging, produção)
- ✅ Guardar chave em local seguro (gerenciador de senhas)
- ✅ Usar variáveis de ambiente (Railway/Render)
- ✅ Rotacionar chaves periodicamente (se necessário)

### **❌ NÃO FAZER:**
- ❌ Commitar SECRET_KEY no Git
- ❌ Compartilhar chave publicamente
- ❌ Usar a mesma chave em múltiplos projetos
- ❌ Usar chaves previsíveis (ex: "minha-chave-123")

---

## 🧪 Testar se Funcionou

Após adicionar `SECRET_KEY` no Railway:

1. **Faça redeploy** (Railway faz automático ao adicionar variável)
2. **Teste login/registro** no frontend
3. **Verifique logs** no Railway (não deve ter erros de JWT)

---

## 💡 Dica: Gerar Múltiplas Chaves

Se precisar de várias chaves (dev, staging, produção):

```bash
# Gerar 3 chaves diferentes
for i in {1..3}; do
  echo "SECRET_KEY_$i:"
  python -c "import secrets; print(secrets.token_urlsafe(32))"
  echo ""
done
```

---

## 📚 Referências

- **Python secrets module:** https://docs.python.org/3/library/secrets.html
- **JWT Best Practices:** https://datatracker.ietf.org/doc/html/rfc8725
- **Railway Variables:** https://docs.railway.app/develop/variables

---

## ✅ Checklist

- [ ] Python instalado no computador
- [ ] Comando executado: `python -c "import secrets; print(secrets.token_urlsafe(32))"`
- [ ] Chave copiada (mínimo 32 caracteres)
- [ ] Chave adicionada no Railway como `SECRET_KEY`
- [ ] Variável salva no Railway
- [ ] Redeploy realizado (automático ou manual)

---

**Pronto!** Sua SECRET_KEY está configurada! 🎉

**Veja também:**
- `VARIAVEIS-AMBIENTE-PRODUCAO.md` - Outras variáveis necessárias
- `DEPLOY-RAPIDO.md` - Quick start do deploy
