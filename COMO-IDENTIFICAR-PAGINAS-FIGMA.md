# 🔍 Como Identificar Todas as Páginas no Figma

Guia para encontrar e extrair todas as páginas do design do Figma.

**Design:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled

---

## 📋 Método Rápido

### **Passo 1: Abrir o Figma**

1. **Acesse:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
2. **Veja o painel esquerdo** (Layers/Frames)

### **Passo 2: Identificar Páginas/Frames**

No painel esquerdo, você verá:
- **Páginas** (Pages) - diferentes telas/páginas
- **Frames** - frames dentro de cada página

**Páginas comuns:**
- Landing Page / Home
- Login
- Signup / Registro
- Onboarding
- Dashboard
- Chat / Conversa
- Perfil
- Configurações

### **Passo 3: Obter node-id de Cada Página**

Para cada página/frame:

1. **Selecione a página/frame** no Figma
2. **Veja a URL** na barra de endereço
3. **Copie o node-id** (ex: `node-id=2-3` → converta para `2:3`)

**Exemplo:**
```
URL: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=2-3
node-id: 2:3
```

---

## 🎯 Páginas Esperadas

Baseado no projeto, essas são as páginas que provavelmente existem:

### **1. Landing Page (Home)**
- ✅ **Status:** Já extraída e implementada
- **node-id:** `1:2` (já usado)

### **2. Login Page**
- ❓ **Status:** Precisa extrair
- **O que ter:**
  - Formulário de login (email, senha)
  - Link "Esqueceu a senha?"
  - Link para criar conta
  - Botão "Entrar"

### **3. Dashboard / Home Logado**
- ❓ **Status:** Existe código, mas precisa verificar design do Figma
- **O que ter:**
  - Lista de conversas
  - Estatísticas/XP
  - Botão "Nova Conversa"
  - Navegação

### **4. Chat / Conversa Page**
- ❓ **Status:** Precisa criar
- **O que ter:**
  - Interface de chat
  - Input para mensagem (texto, foto, áudio)
  - Histórico de mensagens
  - Botões de ação (enviar, anexar)

### **5. Onboarding**
- ❓ **Status:** Existe código, mas precisa verificar design do Figma
- **O que ter:**
  - Multi-step form
  - Passo 1: Criar conta
  - Passo 2: Configurar professor

### **6. Perfil / Configurações**
- ❓ **Status:** Pode existir no Figma
- **O que ter:**
  - Informações do usuário
  - Configurações do professor IA
  - Estatísticas

---

## 🚀 Como Me Enviar as Páginas

### **Opção 1: Lista de URLs (Mais Fácil)**

Me envie as URLs de cada página:

```
Landing Page: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=1-2
Login: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=X-Y
Dashboard: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=X-Y
Chat: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=X-Y
...
```

### **Opção 2: Lista de node-ids**

Me envie os node-ids:

```
Landing Page: 1:2
Login: X:Y
Dashboard: X:Y
Chat: X:Y
Onboarding: X:Y
```

### **Opção 3: Descrever Páginas**

Me diga quais páginas você vê no Figma:
- Nome da página
- O que tem nela (breve descrição)

---

## 📝 Checklist de Páginas

**Me informe quais existem:**

- [x] Landing Page ✅ (já extraída)
- [ ] Login Page
- [ ] Signup/Registro Page
- [ ] Onboarding Page
- [ ] Dashboard Page
- [ ] Chat/Conversa Page
- [ ] Perfil Page
- [ ] Configurações Page
- [ ] Outras: _______________

---

## 🎯 Próximos Passos

**Após você me enviar as páginas:**

1. **Vou extrair cada página** usando Figma MCP
2. **Criar componentes/páginas** correspondentes
3. **Atualizar design** das páginas existentes (dashboard, onboarding)
4. **Criar páginas faltantes** (login, chat, etc.)

---

**Me envie as URLs ou node-ids das páginas do Figma!** 🚀

**Ou me diga quais páginas você vê no painel esquerdo do Figma!**
