# 🔍 Como Ver Todas as Telas no Figma

Guia para identificar e listar todas as páginas/telas no arquivo Figma.

**Arquivo Original:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled

---

## 🎯 Método 1: No Arquivo Figma (Recomendado)

### **Passo 1: Abrir o Arquivo**

1. **Acesse:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
2. **Veja o painel esquerdo** (Layers)

### **Passo 2: Identificar Páginas/Frames**

**No painel esquerdo, você verá:**

1. **Pages (Páginas)** - Se houver múltiplas páginas:
   - Page 1
   - Page 2
   - etc.

2. **Frames** - Frames dentro de cada página:
   - Frame "Landing"
   - Frame "Login"
   - Frame "Dashboard"
   - Frame "Chat"
   - etc.

### **Passo 3: Obter node-id de Cada Frame**

**Para cada frame:**

1. **Clique no frame** no painel esquerdo
2. **Veja a URL** na barra de endereço
3. **Copie o node-id:**

**Exemplo:**
- URL: `https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=2-3`
- node-id: `2:3` (converta `2-3` para `2:3`)

---

## 🎯 Método 2: Usar Dev Mode

1. **No Figma:**
   - Ative **Dev Mode** (toggle no canto superior direito)
   - Veja todos os frames com especificações
   - Cada frame representa uma tela/página

2. **Anote:**
   - Nome de cada frame
   - node-id de cada frame

---

## 🎯 Método 3: No Protótipo (Figma Site)

**No protótipo:** https://react-growl-37040204.figma.site/

1. **Pressione `Ctrl+K` (ou `⌘K` no Mac)**
   - Abre menu para ver todas as telas
   - Ou clique em "ver todas as telas"

2. **Anote:**
   - Lista de todas as telas disponíveis

---

## 📋 Checklist: Páginas Provavelmente Existentes

**Me informe quais dessas páginas existem no Figma:**

- [ ] **Landing Page** (Home) - node-id: `1:2` ✅
- [ ] **Login** - Precisa node-id
- [ ] **Registro/Signup** - Precisa node-id
- [ ] **Onboarding** - Precisa node-id
- [ ] **Dashboard** - Precisa node-id
- [ ] **Chat/Conversa** - Precisa node-id
- [ ] **Perfil** - Precisa node-id
- [ ] **Configurações** - Precisa node-id
- [ ] **FAQ** - Precisa node-id
- [ ] **Outras:** _______________

---

## 📝 Formato para Me Enviar

**Envie assim:**

```
Landing Page: 1:2 ✅
Login: 2:3
Dashboard: 3:4
Chat: 4:5
Onboarding: 5:6
...
```

**Ou:**

```
Vi essas páginas no Figma:
- Landing Page (node-id: 1:2)
- Login (node-id: 2:3)
- Dashboard (node-id: 3:4)
- Chat (node-id: 4:5)
...
```

---

## 🚀 Após Me Enviar os node-ids

**Eu vou:**

1. ✅ Extrair cada página com Figma MCP
2. ✅ Criar/atualizar componentes Next.js
3. ✅ Aplicar design exato
4. ✅ Integrar com backend
5. ✅ Garantir consistência visual

---

## 💡 Alternativa: Você Lista as Páginas

**Se não souber os node-ids:**

1. **Liste todas as páginas que você vê no Figma:**
   - Landing Page
   - Login
   - Dashboard
   - etc.

2. **Eu vou:**
   - Tentar encontrar automaticamente
   - Ou criar páginas básicas que você ajusta depois

---

**Me envie os node-ids ou lista de páginas do Figma!** 🚀
