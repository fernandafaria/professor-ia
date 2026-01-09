# 🎨 Extrair Todas as Páginas do Figma

Guia para extrair e implementar todas as páginas do design do Figma, não apenas a landing page.

**Design:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled

---

## 📋 Páginas Identificadas no Projeto

### **Páginas Existentes:**

1. ✅ **Landing Page** (`/`) - Já implementada
2. ✅ **Onboarding** (`/onboarding`) - Criar conta + perfil professor
3. ✅ **Dashboard** (`/dashboard`) - Página principal após login
4. ❓ **Login** (`/login`) - Precisa criar
5. ❓ **Conversas** (`/conversations/[id]`) - Precisa criar
6. ❓ Outras páginas no Figma?

---

## 🔍 Como Identificar Todas as Páginas no Figma

### **Método 1: Explorar Manualmente no Figma**

1. **Abra o Figma:**
   - https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled

2. **Veja todas as páginas/frames:**
   - Procure por diferentes frames/páginas no painel esquerdo
   - Cada frame geralmente representa uma página
   - Anote os nomes e node-ids

3. **Páginas comuns em apps educacionais:**
   - Landing Page
   - Login / Signup
   - Onboarding
   - Dashboard
   - Chat/Conversas
   - Perfil
   - Configurações
   - Ajuda/FAQ

### **Método 2: Usar Figma MCP**

Vou tentar extrair a estrutura completa usando o Figma MCP.

---

## 📝 Páginas para Extrair

### **1. Landing Page (Home)**
- ✅ **Status:** Já implementada
- **Componentes:** Header, Hero, Como Funciona, Why, CTA, Footer

### **2. Login Page**
- ❓ **Status:** Precisa criar
- **O que ter:**
  - Formulário de login (email, senha)
  - Link para criar conta
  - Opções sociais (se houver no Figma)

### **3. Signup/Registro Page**
- ❓ **Status:** Pode estar no onboarding ou separada
- **O que ter:**
  - Formulário de registro
  - Validações

### **4. Onboarding Page**
- ✅ **Status:** Já existe, mas pode precisar ajustar design
- **O que ter:**
  - Multi-step form
  - Criar conta + perfil professor

### **5. Dashboard Page**
- ✅ **Status:** Já existe, mas pode precisar ajustar design
- **O que ter:**
  - Lista de conversas
  - Estatísticas/XP
  - Navegação

### **6. Chat/Conversa Page**
- ❓ **Status:** Precisa criar
- **O que ter:**
  - Interface de chat
  - Input de mensagem
  - Histórico de mensagens
  - Opções de upload (foto, áudio, texto)

### **7. Perfil Page**
- ❓ **Status:** Precisa criar
- **O que ter:**
  - Informações do usuário
  - Configurações do professor IA
  - Estatísticas

### **8. Outras Páginas**
- Configurações
- Ajuda/FAQ
- Comunidade
- Sobre

---

## 🚀 Como Extrair Cada Página

Para cada página no Figma:

1. **Identificar o node-id:**
   - Selecione o frame da página no Figma
   - Copie o node-id da URL (ex: `node-id=2-3` → `2:3`)

2. **Extrair com Figma MCP:**
   ```typescript
   // Usar get_design_context com node-id específico
   ```

3. **Criar componente Next.js:**
   - Criar página em `app/[nome-da-pagina]/page.tsx`
   - Ou componente em `components/figma/[Nome]Page.tsx`

4. **Integrar com backend:**
   - Conectar com API (login, chat, etc.)

---

## 📋 Checklist de Páginas

**Me informe quais páginas existem no Figma:**

- [ ] Landing Page ✅ (já implementada)
- [ ] Login Page
- [ ] Signup/Registro Page
- [ ] Onboarding Page ✅ (existe, precisa verificar design)
- [ ] Dashboard Page ✅ (existe, precisa verificar design)
- [ ] Chat/Conversa Page
- [ ] Perfil Page
- [ ] Configurações Page
- [ ] Outras: _______________

---

## 🎯 Próximos Passos

1. **Você me informa quais páginas existem no Figma** (ou compartilha os node-ids)
2. **Eu extraio cada página** usando Figma MCP
3. **Crio os componentes/páginas** correspondentes
4. **Integro com backend** se necessário

---

**Me envie:**
- Lista de páginas no Figma
- Ou node-ids de cada página
- Ou me diga para explorar o Figma e identificar todas

**Pronto para extrair todas as páginas!** 🚀
