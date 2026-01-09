# 📦 Extração de Assets do Figma - Passo a Passo

Guia rápido para extrair assets do seu design do Figma usando o MCP do Figma no Cursor.

---

## ⚡ Quick Start

### **Passo 1: Obter o Link Correto do Figma**

Você precisa do **link direto do arquivo do Figma**, não o protótipo compartilhado.

**Formato do link:**
```
https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]
```

**Exemplo:**
```
https://figma.com/design/abc123xyz/EdTechFront?node-id=1-2
```

### **Passo 2: Extrair fileKey e nodeId**

Do link acima:
- **fileKey:** `abc123xyz`
- **nodeId:** `1-2` (ou `1:2`)

### **Passo 3: No Cursor, Use Este Comando**

Cole no chat do Cursor:

```
Extraia todos os assets (imagens, ícones, logos) deste design do Figma e salve na estrutura correta:

fileKey: [COLE_SEU_FILE_KEY_AQUI]
nodeId: [COLE_SEU_NODE_ID_AQUI]

Organize assim:
- Imagens/Ilustrações → public/assets/images/
- Ícones/Logos → public/assets/icons/
- Fontes (se houver) → public/assets/fonts/

Depois atualize o componente HeroCTA.tsx para usar esses assets.
```

---

## 🔍 Como Encontrar o Link Correto

### **Opção A: Via Figma Desktop/Web**

1. Abra seu arquivo no Figma
2. Selecione o frame/componente que contém os assets
3. No menu superior: **Share** → **Copy link**
4. Ou veja a URL na barra de endereço

### **Opção B: Do Protótipo Compartilhado**

O link que você compartilhou (`react-growl-37040204.figma.site`) é um **protótipo compartilhado**, não o arquivo direto.

Para obter o arquivo:
1. Peça ao criador do design para compartilhar o **link do arquivo** (não o protótipo)
2. Ou acesse o arquivo original no Figma e copie o link de lá

---

## 📋 Checklist de Assets a Extrair

Baseado no design observado, você pode ter:

- [ ] **Logo "Professor IA"** → `public/assets/icons/logo.svg`
- [ ] **Ícone de estrela** → `public/assets/icons/star-icon.svg`
- [ ] **Background do Hero** (se houver imagem) → `public/assets/images/hero-bg.png`
- [ ] **Ilustrações** (se houver) → `public/assets/images/`
- [ ] **Ícones de métricas** → `public/assets/icons/`

---

## 🎯 Exemplo Completo de Comando

Se você tiver:
- fileKey: `react-growl-37040204`
- nodeId: `1:2`

No Cursor, digite:

```
Extraia todos os assets deste design do Figma:

fileKey: react-growl-37040204
nodeId: 1:2

Faça o seguinte:
1. Baixe todas as imagens e salve em frontend/public/assets/images/
2. Baixe todos os ícones/logos e salve em frontend/public/assets/icons/
3. Atualize o componente HeroCTA.tsx para usar os assets extraídos
4. Atualize o componente Header.tsx se houver ícones nas métricas
5. Atualize o componente Footer.tsx para usar o logo real

Organize os assets com nomes descritivos:
- hero-background.png (se houver)
- logo.svg
- star-icon.svg
- etc.
```

---

## 🛠️ Alternativa: Exportação Manual

Se o MCP não funcionar, você pode exportar manualmente:

### **1. No Figma:**

1. Selecione os assets (imagens, ícones, etc.)
2. No painel à direita, vá em **Export**
3. Escolha formato:
   - **SVG** para ícones/logos
   - **PNG** para imagens (com background)
   - **JPG** para fotos
4. Clique em **Export [Nome]**

### **2. Salvar no Projeto:**

```bash
# Mover para a estrutura correta
mv ~/Downloads/logo.svg frontend/public/assets/icons/
mv ~/Downloads/hero-bg.png frontend/public/assets/images/
```

### **3. Atualizar Componentes:**

```tsx
// Exemplo no HeroCTA.tsx
import Image from 'next/image';

<Image
  src="/assets/images/hero-bg.png"
  alt="Background"
  fill
  className="hero-background"
/>
```

---

## ✅ Verificação

Após extrair, verifique:

```bash
# Listar assets extraídos
ls -la frontend/public/assets/images/
ls -la frontend/public/assets/icons/
```

Os arquivos devem aparecer aqui. Se não, verifique:
- Permissões de escrita
- Caminho correto
- Se os assets foram exportados do Figma

---

## 🆘 Problemas Comuns

### ❌ "Erro ao acessar Figma"

**Causa:** Link incorreto ou não autenticado

**Solução:**
1. Verifique se o link é do arquivo do Figma (não protótipo)
2. Certifique-se de estar autenticado no Figma Desktop
3. Verifique configuração do MCP no Cursor

### ❌ "Assets não foram baixados"

**Causa:** nodeId incorreto ou sem permissões

**Solução:**
1. Verifique se o nodeId aponta para um frame/componente com assets
2. Tente usar `0:1` (página raiz) primeiro
3. Verifique permissões da pasta `public/assets/`

### ❌ "Imagens não aparecem no navegador"

**Causa:** Path incorreto no código

**Solução:**
- Use paths absolutos: `/assets/images/logo.png`
- Não use paths relativos: `./assets/...`
- Verifique se o arquivo está em `public/assets/`

---

## 📚 Documentação Relacionada

- **[COMO-EXTRAIR-ASSETS-FIGMA.md](./COMO-EXTRAIR-ASSETS-FIGMA.md)** - Guia completo
- **[COMO-INTEGRAR-FIGMA-COM-BACKEND.md](./COMO-INTEGRAR-FIGMA-COM-BACKEND.md)** - Integração geral

---

## 💡 Dica Final

Se você compartilhar o **link direto do arquivo do Figma** aqui no chat, eu posso:

1. ✅ Extrair todos os assets automaticamente
2. ✅ Organizar na estrutura correta
3. ✅ Atualizar todos os componentes para usar os assets
4. ✅ Otimizar imagens (se necessário)

**Basta compartilhar o link!** 🚀

---

**Última atualização:** 2026-01-09
