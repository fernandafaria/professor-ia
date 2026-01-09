# ⚡ Passo a Passo Rápido: Extrair Assets do Figma

Guia ultra rápido para extrair assets e adicionar ao projeto **agora mesmo**.

---

## 🚀 Quick Start (5 Minutos)

### **1. Login no Figma** 🔑

1. **Acesse:** https://www.figma.com/make/iHKJzezk69Uj3XbyeeWDy9/Frontend-da-Plataforma
2. **Faça login:**
   - Clique em **"Continuar com o Google"** (ou email)
   - Complete o login

---

### **2. Abrir Arquivo Original** 📂

**Na página do Figma Make, procure por:**
- Botão **"Open in Figma"** ou **"Abrir no Figma"**
- Link **"View Source File"** ou **"Ver Arquivo Original"**
- Geralmente no **topo** ou **menu lateral**

**Ou:**
- Acesse diretamente o Figma (figma.com)
- Procure pelo arquivo **"Frontend da Plataforma"** ou **"Professor IA"**
- Abra o arquivo

---

### **3. Exportar Assets** 📦

#### **Para Logo/Ícones (SVG):**

1. **Selecione** o logo/ícone no Figma
2. **Painel direito** → **Export**
3. **Clique em "+"** → Escolha **SVG**
4. **Clique em "Export"** → Arquivo será baixado

#### **Para Imagens (PNG):**

1. **Selecione** a imagem no Figma
2. **Painel direito** → **Export**
3. **Clique em "+"** → Escolha **PNG @2x**
4. **Clique em "Export"** → Arquivo será baixado

---

### **4. Organizar Assets** 📁

**Mover arquivos exportados para o projeto:**

```bash
# Abra o terminal e execute:

cd /Users/fernandafaria/Downloads/P1A

# Criar pastas (se ainda não criou)
mkdir -p frontend/public/assets/images
mkdir -p frontend/public/assets/icons

# Mover assets exportados (ajuste nomes conforme você exportou)
# Ícones/logos → icons/
mv ~/Downloads/logo.svg frontend/public/assets/icons/
mv ~/Downloads/star-icon.svg frontend/public/assets/icons/

# Imagens → images/
mv ~/Downloads/hero-bg.png frontend/public/assets/images/
```

**Ou arraste manualmente no Finder:**
- Ícones → `P1A/frontend/public/assets/icons/`
- Imagens → `P1A/frontend/public/assets/images/`

---

### **5. Atualizar Componentes** ✏️

Os componentes já estão prontos! Basta descomentar os TODOs:

#### **HeroCTA.tsx - Se houver background:**

```tsx
// 1. Descomente o import:
import Image from 'next/image';

// 2. Descomente dentro do return:
<Image
  src="/assets/images/hero-background.png"  // Ajuste nome do arquivo
  alt="Background"
  fill
  priority
/>
```

#### **Footer.tsx - Se exportou logo:**

```tsx
// Substitua o SVG inline por:
import Image from 'next/image';

<Image
  src="/assets/icons/logo.svg"  // Ajuste nome do arquivo
  alt="Professor IA"
  width={24}
  height={24}
/>
```

---

### **6. Testar** ✅

```bash
# Terminal 1: Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm run dev
```

**Acesse:** http://localhost:3000

**Verifique:**
- ✅ Assets aparecem corretamente
- ✅ Sem erros no console (F12 → Console)

---

## 📋 Checklist Rápido

- [ ] Login no Figma ✅
- [ ] Abrir arquivo original no Figma ✅
- [ ] Exportar logo/ícones (SVG) ✅
- [ ] Exportar imagens (PNG @2x) ✅
- [ ] Mover para `public/assets/` ✅
- [ ] Atualizar componentes (descomentar TODOs) ✅
- [ ] Testar no navegador ✅

---

## 🆘 Problemas Rápidos

### ❌ "Assets não aparecem"

**Solução:**
```bash
# Verificar se arquivos estão corretos
ls -la frontend/public/assets/icons/
ls -la frontend/public/assets/images/

# Reiniciar servidor
# Ctrl+C para parar
npm run dev  # Iniciar novamente
```

### ❌ "Erro 404 - arquivo não encontrado"

**Solução:**
- Verifique o path: deve ser `/assets/icons/logo.svg` (não `./assets/...`)
- Verifique se o arquivo está em `public/assets/`

---

## 📚 Guias Completos

Para mais detalhes, veja:
- **Guia Completo:** `GUIA-COMPLETO-ASSETS-FIGMA.md`
- **Exportação Detalhada:** `EXPORTAR-ASSETS-FIGMA-MAKE.md`

---

**Pronto!** Siga esses 6 passos e você terá os assets funcionando em 5 minutos! 🚀
