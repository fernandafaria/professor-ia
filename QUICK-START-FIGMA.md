# ⚡ Quick Start: Figma → Frontend → Backend

Guia rápido para conectar seu design do Figma com o backend.

---

## 🚀 Em 5 Minutos

### **1. Obter Código do Figma (Escolha um método)**

#### **Opção A: Via Cursor MCP (Mais Rápido)** ⭐

No chat do Cursor:
```
Extraia este componente do Figma e crie em components/figma/MeuComponente.tsx:
URL: [COLE_SUA_URL_DO_FIGMA_AQUI]
```

#### **Opção B: Manual**

1. Abra Figma → Plugins → Figma Make
2. Selecione o frame
3. Gere código React/TypeScript
4. Copie e cole em `components/figma/`

---

### **2. Conectar com Backend**

No componente gerado, adicione:

```tsx
import { api } from '@/lib/api';

// Exemplo: Login
const handleSubmit = async () => {
  const response = await api.login(email, password);
  localStorage.setItem('token', response.access_token);
};
```

---

### **3. Rodar Tudo**

```bash
# Terminal 1: Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm install  # primeira vez apenas
npm run dev
```

---

### **4. Testar**

1. Abra: http://localhost:3000
2. Teste seu componente
3. Verifique se conecta com: http://localhost:8000

---

## ✅ Checklist Rápido

- [ ] Componente criado em `components/figma/`
- [ ] Imports ajustados (`@/lib/api`)
- [ ] Backend rodando (porta 8000)
- [ ] Frontend rodando (porta 3000)
- [ ] Testado no navegador

---

## 📚 Documentação Completa

- **[COMO-INTEGRAR-FIGMA-COM-BACKEND.md](./COMO-INTEGRAR-FIGMA-COM-BACKEND.md)** - Guia completo
- **[EXEMPLO-USO-FIGMA-MCP.md](./EXEMPLO-USO-FIGMA-MCP.md)** - Exemplos práticos

---

**Pronto!** 🎉
