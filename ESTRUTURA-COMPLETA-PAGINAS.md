# 📄 Estrutura Completa de Páginas do Projeto

Lista de todas as páginas necessárias baseado no backend e funcionalidades.

---

## 📋 Páginas Identificadas

### **1. Landing Page (Home)** ✅
- **Rota:** `/`
- **Status:** ✅ Implementada com design do Figma
- **Componentes:** Header, Hero, Como Funciona, Why, CTA, Footer

### **2. Login Page** ❓
- **Rota:** `/login`
- **Status:** ❓ Precisa criar/extrair do Figma
- **Funcionalidade:** Login de usuário
- **API:** `POST /api/v1/auth/login`

### **3. Onboarding Page** ✅
- **Rota:** `/onboarding`
- **Status:** ✅ Existe, mas pode precisar ajustar design do Figma
- **Funcionalidade:** Criar conta + configurar professor
- **API:** `POST /api/v1/auth/register`, `POST /api/v1/profile`

### **4. Dashboard Page** ✅
- **Rota:** `/dashboard`
- **Status:** ✅ Existe, mas precisa ajustar design do Figma
- **Funcionalidade:** Lista de conversas, estatísticas
- **API:** `GET /api/v1/auth/me`, `GET /api/v1/conversations`

### **5. Chat/Conversa Page** ❓
- **Rota:** `/conversations/[id]`
- **Status:** ❓ Precisa criar/extrair do Figma
- **Funcionalidade:** Interface de chat com professor IA
- **API:** `GET /api/v1/conversations/:id/messages`, `POST /api/v1/conversations/:id/messages`

### **6. Profile/Perfil Page** ❓
- **Rota:** `/profile`
- **Status:** ❓ Pode precisar criar
- **Funcionalidade:** Ver/editar perfil do usuário e professor
- **API:** `GET /api/v1/profile`, `PUT /api/v1/profile/:id`

---

## 🎯 Próximas Ações

Para extrair todas as páginas do Figma, preciso que você:

### **Opção 1: Me enviar os node-ids**

Para cada página no Figma, me envie:
- Nome da página
- node-id (ex: `2:3`, `3:4`, etc.)
- Ou URL completa com node-id

### **Opção 2: Listar as páginas**

Me diga quais páginas/frames você vê no painel esquerdo do Figma:
- Landing Page
- Login
- Dashboard
- Chat
- etc.

### **Opção 3: Deixar eu criar baseado na estrutura**

Posso criar páginas básicas baseado na estrutura esperada e você pode ajustar depois com os designs do Figma.

---

## 🚀 Vou Criar Páginas Base

Enquanto isso, posso criar páginas básicas funcionais que você pode ajustar depois com os designs do Figma:

1. **Login Page** - Página de login básica
2. **Chat Page** - Interface de chat básica
3. **Profile Page** - Página de perfil básica

**Prefere que eu:**
- A) Crie páginas básicas agora (você ajusta depois com Figma)
- B) Aguarde você me enviar os node-ids das páginas no Figma
- C) Tente explorar o Figma sozinho (pode demorar mais)

---

**Como prefere prosseguir?** 🚀
