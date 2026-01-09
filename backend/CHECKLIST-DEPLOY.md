# ✅ Checklist de Deploy do Backend

Checklist passo a passo para garantir que tudo está pronto para deploy.

---

## 📋 Pré-Deploy

### **Arquivos Necessários**

- [ ] `Procfile` existe na raiz do `backend/`
  ```bash
  # Conteúdo: web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

- [ ] `runtime.txt` existe na raiz do `backend/`
  ```bash
  # Conteúdo: python-3.11
  ```

- [ ] `requirements.txt` existe e está atualizado
  ```bash
  # Deve conter: fastapi, uvicorn[standard], sqlalchemy, etc.
  ```

- [ ] `backend/app/main.py` existe e está funcional
  ```bash
  # Teste localmente: uvicorn app.main:app --reload
  ```

---

## 🔐 Variáveis de Ambiente

### **Obrigatórias:**

- [ ] `DATABASE_URL` configurada (Supabase)
  ```bash
  # Formato: postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
  ```

- [ ] `SECRET_KEY` gerada e configurada
  ```bash
  # Gerar: python -c "import secrets; print(secrets.token_urlsafe(32))"
  # Mínimo 32 caracteres
  ```

- [ ] `CORS_ORIGINS` configurada com URL do frontend
  ```bash
  # Exemplo: https://seu-frontend.vercel.app,http://localhost:3000
  ```

### **Recomendadas:**

- [ ] `DEBUG=False` (produção)
- [ ] `LOG_LEVEL=INFO` (produção)
- [ ] `ANTHROPIC_API_KEY` (se usar Claude)
- [ ] `ANTHROPIC_MODEL` (padrão: claude-3-5-sonnet-20241022)

---

## 🚀 Deploy no Railway

### **Configuração:**

- [ ] Conta Railway criada (https://railway.app)
- [ ] Projeto criado no Railway
- [ ] Repositório GitHub conectado
- [ ] **Root Directory configurado como `backend`** ⚠️ **CRÍTICO!**
- [ ] Todas as variáveis de ambiente adicionadas
- [ ] Deploy iniciado

### **Verificação:**

- [ ] Build completou com sucesso (ver logs)
- [ ] Health check funciona: `/health`
- [ ] Root endpoint funciona: `/`
- [ ] Documentação Swagger acessível: `/docs`
- [ ] URL do backend obtida (ex: `https://seu-projeto.up.railway.app`)

---

## 🔗 Integração com Frontend

- [ ] URL do backend atualizada no Vercel (variável `NEXT_PUBLIC_API_URL`)
- [ ] Frontend fazendo redeploy com nova URL
- [ ] Teste de conexão: Frontend → Backend
- [ ] Teste de autenticação: Login/Registro funcionando
- [ ] Teste de API: Endpoints respondendo corretamente

---

## 🧪 Testes Finais

### **Backend:**

```bash
# Health check
curl https://sua-url.railway.app/health
# Esperado: {"status": "healthy", "version": "1.0.0"}

# Root
curl https://sua-url.railway.app/
# Esperado: {"name": "...", "version": "...", "status": "running"}

# Docs
# Acesse: https://sua-url.railway.app/docs
# Deve abrir interface Swagger
```

### **Frontend:**

- [ ] Landing page carrega
- [ ] Botão "Entrar" funciona
- [ ] Onboarding funciona (criar conta)
- [ ] Login funciona
- [ ] Dashboard carrega após login
- [ ] Dados do usuário aparecem corretamente

---

## 📝 Documentação

- [ ] URLs salvas (backend e frontend)
- [ ] Variáveis de ambiente documentadas
- [ ] Credenciais salvas em local seguro
- [ ] Logs monitorados (Railway Dashboard)

---

## 🔒 Segurança

- [ ] `SECRET_KEY` única e segura (não commitada no Git)
- [ ] `DEBUG=False` em produção
- [ ] `CORS_ORIGINS` limitado apenas às URLs necessárias
- [ ] `.env` não commitado no Git (verificar `.gitignore`)
- [ ] Credenciais não expostas publicamente

---

## 🎯 Próximos Passos (Pós-Deploy)

- [ ] Configurar domínio customizado (opcional)
- [ ] Configurar monitoramento/alerts
- [ ] Configurar backup do banco de dados (Supabase)
- [ ] Documentar processo de deploy para equipe
- [ ] Configurar CI/CD (se necessário)

---

## 🆘 Troubleshooting

### **Se build falhar:**

- [ ] Verificar logs do Railway
- [ ] Verificar se Root Directory está correto (`backend`)
- [ ] Verificar se `requirements.txt` está completo
- [ ] Verificar se Python 3.11 está especificado no `runtime.txt`

### **Se health check falhar:**

- [ ] Verificar se `DATABASE_URL` está correta
- [ ] Verificar se banco Supabase está acessível
- [ ] Verificar logs do Railway para erros

### **Se frontend não conectar:**

- [ ] Verificar `CORS_ORIGINS` inclui URL do frontend
- [ ] Verificar `NEXT_PUBLIC_API_URL` no Vercel
- [ ] Verificar se backend está rodando (health check)
- [ ] Verificar logs do backend para erros de CORS

---

## 📚 Guias de Referência

- **Guia Completo:** `DEPLOY-BACKEND.md`
- **Quick Start:** `DEPLOY-RAPIDO.md`
- **Variáveis de Ambiente:** `VARIAVEIS-AMBIENTE-PRODUCAO.md`
- **Deploy Frontend:** `../VERCEL-DEPLOY.md`

---

## ✅ Status Final

**Backend Deployado:** [ ] Sim [ ] Não

**URL do Backend:** `________________________________`

**Frontend Conectado:** [ ] Sim [ ] Não

**URL do Frontend:** `________________________________`

**Testes Passando:** [ ] Sim [ ] Não

**Data do Deploy:** `____/____/____`

---

**Pronto para produção!** 🎉
