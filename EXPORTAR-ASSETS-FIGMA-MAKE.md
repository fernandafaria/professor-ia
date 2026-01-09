# 📦 Como Exportar Assets do Figma Make

Guia passo a passo para exportar assets do seu design no Figma Make e adicionar ao projeto.

---

## 🎯 Método Recomendado: Exportar do Arquivo Original

O Figma Make é uma ferramenta para gerar código, mas para extrair assets (imagens, ícones), você precisa acessar o **arquivo original no Figma**.

---

## 📋 Passo a Passo Completo

### **Passo 1: Acessar o Arquivo Original**

#### **Opção A: Via Figma Make**

1. **Na página do Figma Make que você compartilhou:**
   - Procure por um botão **"Open in Figma"** ou **"Abrir no Figma"**
   - Ou um link **"View Source File"**
   - Geralmente está no topo da página ou no menu

2. **Clique nesse link** - ele abrirá o arquivo original no Figma

#### **Opção B: Direto no Figma**

1. **Abra o Figma** (navegador ou desktop app)
2. **Procure pelo arquivo "Frontend da Plataforma"** ou **"Professor IA"**
3. **Abra o arquivo**

---

### **Passo 2: Identificar os Assets**

No arquivo do Figma, identifique os assets que você precisa:

#### **Ícones/Logos:**
- Logo "Professor IA"
- Ícone de estrela
- Ícones de métricas (se houver)
- Menu icons

#### **Imagens:**
- Background do Hero (se houver imagem)
- Ilustrações
- Imagens de features

---

### **Passo 3: Exportar Assets**

#### **Para Ícones (SVG recomendado):**

1. **Selecione o ícone/logo no Figma**
2. **No painel direito, vá em "Export"**
3. **Clique em "+" para adicionar formato**
4. **Escolha:**
   - **SVG** (melhor para ícones/logos - vetorial)
   - Ou **PNG** com 2x/3x para alta resolução
5. **Clique em "Export [Nome]"**
6. **Salve o arquivo**

#### **Para Imagens (PNG/JPG):**

1. **Selecione a imagem/ilustração**
2. **No painel direito → "Export"**
3. **Adicione formato:**
   - **PNG** (para imagens com transparência)
   - **JPG** (para fotos - menor tamanho)
4. **Escolha resolução:**
   - 1x (padrão)
   - 2x (alta resolução)
   - 3x (ultra alta resolução)
5. **Export e salve**

---

### **Passo 4: Organizar Assets no Projeto**

Salve os arquivos exportados na estrutura correta:

```
frontend/public/assets/
├── images/              # Imagens e ilustrações
│   ├── hero-background.png (se houver)
│   └── ...
└── icons/               # Ícones e logos
    ├── logo.svg
    ├── star-icon.svg
    └── ...
```

#### **Comandos úteis:**

```bash
# Mover assets exportados para a estrutura correta
# (ajuste os caminhos conforme onde você salvou os arquivos)

# Ícones
mv ~/Downloads/logo.svg frontend/public/assets/icons/
mv ~/Downloads/star-icon.svg frontend/public/assets/icons/

# Imagens
mv ~/Downloads/hero-bg.png frontend/public/assets/images/
```

---

### **Passo 5: Atualizar Componentes**

Após adicionar os assets, os componentes já estão preparados para usá-los!

#### **Exemplo: Header.tsx**

```tsx
// Já preparado - basta adicionar o path do logo se tiver
<img src="/assets/icons/logo.svg" alt="Logo" />
```

#### **Exemplo: HeroCTA.tsx**

```tsx
// Já tem TODOs marcando onde adicionar assets
// Basta descomentar e ajustar paths:

import Image from 'next/image';

<Image
  src="/assets/images/hero-background.png"
  alt="Background"
  fill
  className="hero-background"
/>
```

#### **Exemplo: Footer.tsx**

```tsx
// Já tem um SVG inline do ícone de estrela
// Você pode substituir por um asset se preferir:

<img src="/assets/icons/star-icon.svg" alt="Star" />
```

---

## 🚀 Script Rápido para Organizar Assets

Criei um script para ajudar a organizar assets:

```bash
#!/bin/bash
# organize-assets.sh

echo "📦 Organizando assets do Figma..."

# Criar estrutura de pastas
mkdir -p frontend/public/assets/images
mkdir -p frontend/public/assets/icons

echo "✅ Estrutura criada!"
echo ""
echo "📋 Próximos passos:"
echo "1. Exporte assets do Figma"
echo "2. Salve em Downloads (ou pasta de sua preferência)"
echo "3. Execute:"
echo ""
echo "   # Mover para estrutura correta"
echo "   mv ~/Downloads/logo.svg frontend/public/assets/icons/"
echo "   mv ~/Downloads/hero-bg.png frontend/public/assets/images/"
echo ""
echo "4. Atualize componentes (já preparados com TODOs)"
```

---

## 📝 Checklist de Assets

Baseado no design observado, você precisa exportar:

### **Ícones/Logos:**
- [ ] Logo "Professor IA" → `public/assets/icons/logo.svg`
- [ ] Ícone de estrela (se houver) → `public/assets/icons/star-icon.svg`
- [ ] Ícones de métricas (se houver) → `public/assets/icons/`

### **Imagens:**
- [ ] Background do Hero (se for imagem, não gradiente) → `public/assets/images/hero-background.png`
- [ ] Ilustrações (se houver) → `public/assets/images/`
- [ ] Imagens de features/seções → `public/assets/images/`

---

## 🎨 Atualizar Componentes Após Exportar

### **1. Header.tsx**

Se você exportou o logo:

```tsx
// Adicione antes do return:
import Image from 'next/image';

// Dentro do componente, substitua o texto "Professor IA" por:
<Image
  src="/assets/icons/logo.svg"
  alt="Professor IA"
  width={120}
  height={40}
/>
```

### **2. HeroCTA.tsx**

Se você exportou background:

```tsx
// Descomente e ajuste:
import Image from 'next/image';

// Dentro do .hero-cta:
<Image
  src="/assets/images/hero-background.png"
  alt="Background"
  fill
  className="hero-background"
  priority
/>
```

### **3. Footer.tsx**

Se você exportou logo/ícone:

```tsx
// Substitua o SVG inline por:
<img 
  src="/assets/icons/logo.svg" 
  alt="Professor IA" 
  className="logo-img"
/>
```

---

## 💡 Dicas

1. **Formato SVG para ícones:**
   - Melhor qualidade em qualquer tamanho
   - Menor tamanho de arquivo
   - Escalável sem perda de qualidade

2. **PNG para imagens complexas:**
   - Use 2x ou 3x para alta resolução
   - Comprima imagens para reduzir tamanho

3. **Otimização:**
   - Use ferramentas como [TinyPNG](https://tinypng.com/) para comprimir imagens
   - Ou Next.js Image component que otimiza automaticamente

---

## 🆘 Problemas Comuns

### ❌ "Não consigo acessar o arquivo original"

**Solução:**
- Peça ao criador do design para compartilhar o link do arquivo original
- Ou exporte manualmente do protótipo compartilhado (pode ter qualidade reduzida)

### ❌ "Assets não aparecem no navegador"

**Solução:**
- Verifique se estão em `public/assets/`
- Use paths absolutos: `/assets/images/logo.png`
- Reinicie o servidor Next.js: `npm run dev`

### ❌ "SVG não aparece"

**Solução:**
- Verifique se o SVG é válido
- Tente usar `<img>` ao invés de `<Image>` do Next.js para SVG
- Ou use `next/image` com `unoptimized={true}`

---

## ✅ Checklist Final

- [ ] Acessei o arquivo original no Figma
- [ ] Identifiquei todos os assets necessários
- [ ] Exportei assets (SVG para ícones, PNG para imagens)
- [ ] Organizei na estrutura `public/assets/`
- [ ] Atualizei componentes com paths corretos
- [ ] Testei no navegador (assets aparecem)
- [ ] Otimizei imagens (opcional, mas recomendado)

---

## 🎯 Próximos Passos

1. **Exporte os assets** seguindo este guia
2. **Organize na estrutura** `public/assets/`
3. **Atualize os componentes** (já estão preparados!)
4. **Teste no navegador** - `npm run dev`

---

**Precisa de ajuda?** Compartilhe o link do arquivo original do Figma e eu extraio os assets automaticamente via MCP! 🚀

---

**Última atualização:** 2026-01-09
