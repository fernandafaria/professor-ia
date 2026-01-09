# ⚡ Quick Start - Next.js

**Next.js instalado e pronto para usar!** ✅

---

## ✅ Instalação Completa

- ✅ **Next.js 14.2.35** instalado
- ✅ **React 18.3.1** instalado
- ✅ **TypeScript** configurado
- ✅ **336 pacotes** instalados

---

## 🚀 Iniciar Agora

```bash
cd /Users/fernandafaria/Downloads/P1A/frontend
npm run dev
```

**Acesse:** http://localhost:3000

---

## 📋 Comandos Úteis

```bash
# Desenvolvimento
npm run dev          # Inicia servidor (porta 3000)

# Build
npm run build        # Cria build de produção

# Produção
npm run start        # Inicia servidor de produção

# Linting
npm run lint         # Verifica código
```

---

## ⚙️ Configurar Variáveis de Ambiente

Crie `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🎯 Testar

1. **Iniciar frontend:**
   ```bash
   npm run dev
   ```

2. **Iniciar backend (outro terminal):**
   ```bash
   cd ../backend
   uvicorn app.main:app --reload
   ```

3. **Acessar:**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000/docs

---

**Pronto!** Next.js está instalado e funcionando! 🎉

Veja guia completo: `INSTALACAO-NEXTJS.md`
