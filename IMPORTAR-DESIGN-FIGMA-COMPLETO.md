# 🎨 Importar Design Completo do Figma

Guia completo para extrair e importar o design do Figma para o frontend Next.js.

**Design:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=1-2

---

## 📋 Pré-requisitos

- [x] Link do Figma (já temos)
- [x] Acesso ao arquivo Figma
- [x] Figma MCP configurado (opcional, mas recomendado)
- [x] Componentes React básicos criados

---

## 🚀 Método 1: Extrair via Figma MCP (Automático)

### **Passo 1: Obter fileKey e nodeId**

Do link do Figma:
```
https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=1-2
```

- **fileKey:** `kYaKQo5HILal0lD7HEcGcN`
- **nodeId:** `1:2` (converter de `1-2` para `1:2`)

### **Passo 2: Extrair Design Context**

Use o Figma MCP para extrair:
- Código React/Next.js
- Assets (SVG, imagens)
- Estilos (cores, tipografia, espaçamentos)
- Layout e estrutura

**Já foi feito!** ✅ Componentes criados baseados no design.

---

## 🎯 Método 2: Extrair Assets Manualmente (Recomendado)

Se o Figma MCP não funcionar, extraia assets manualmente:

### **Passo 1: Extrair SVG e Ícones**

1. **No Figma:**
   - Selecione o ícone/elemento
   - Clique com botão direito → **"Copy/Paste as"** → **"Copy as SVG"**
   - Ou: **Export** → **SVG**

2. **Salvar no projeto:**
   ```bash
   # Criar diretório para assets
   mkdir -p frontend/public/icons
   mkdir -p frontend/public/images
   ```

3. **Copiar SVG:**
   - Cole o SVG em arquivo: `frontend/public/icons/logo.svg`
   - Ou use inline no componente React

### **Passo 2: Extrair Cores**

1. **No Figma:**
   - Vá em **"Inspect"** (painel direito)
   - Veja as cores usadas
   - Ou vá em **"Design"** → **"Color Styles"**

2. **Cores identificadas no design:**
   - **Roxo:** `#7C3AED`, `#5B21B6` (gradientes)
   - **Laranja:** `#FF6B35`, `#FF5722` (botões primários)
   - **Amarelo:** `#FFC107` (tags)
   - **Branco:** `#FFFFFF` (textos e backgrounds)
   - **Cinza:** `#666`, `#999` (textos secundários)

**✅ Já aplicadas nos componentes!**

### **Passo 3: Extrair Tipografia**

1. **No Figma:**
   - Selecione texto
   - Veja font-family, font-size, font-weight, line-height
   - Ou vá em **"Design"** → **"Text Styles"**

2. **Tipografia do design:**
   - **Títulos:** Bold (700), tamanhos grandes (3-4rem)
   - **Textos:** Regular (400), tamanho médio (1rem-1.125rem)
   - **Labels:** Semibold (600), tamanho pequeno (0.875rem)
   - **Font:** Sans-serif (provavelmente Inter ou similar)

**✅ Já aplicadas nos componentes!**

---

## 📦 Método 3: Usar Figma Plugin (Figma to Code)

### **Opção A: Figma to React**

1. **No Figma:**
   - Instale plugin: **"Figma to React"** ou **"Figma to Code"**
   - Selecione o frame/componente
   - Execute o plugin
   - Copie o código gerado

2. **Integrar no projeto:**
   - Adapte o código para Next.js
   - Use styled-jsx ou CSS Modules
   - Mantenha estrutura de componentes

### **Opção B: Figma Dev Mode**

1. **No Figma:**
   - Ative **Dev Mode** (toggle no canto superior)
   - Veja especificações CSS
   - Copie valores (padding, margin, colors, etc.)
   - Exporte assets

2. **Aplicar no código:**
   - Use valores exatos do Figma
   - Mantenha consistência de espaçamentos
   - Respeite breakpoints (mobile/desktop)

---

## ✅ Status Atual da Importação

### **Já Implementado:**

- [x] Header com logo "mano, traduz!" e botão Entrar
- [x] Hero Section com tag amarela, título e botões
- [x] Seção "Tradução em 3 passos" (Como Funciona)
- [x] Seção "Por que você vai amar estudar aqui?" (4 benefícios)
- [x] Final CTA "Pronto pra entender de verdade?"
- [x] Footer com logo, links e newsletter

### **Precisa Ajustar:**

- [ ] Cores exatas do Figma (verificar no Inspect)
- [ ] Tipografia exata (font-family, weights)
- [ ] Assets (ícones SVG, imagens)
- [ ] Espaçamentos exatos (padding, margin, gaps)
- [ ] Breakpoints responsivos exatos

---

## 🔍 Verificar Diferenças com Design Original

### **Passo 1: Comparar Visualmente**

1. **Abra o Figma:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
2. **Execute localmente:**
   ```bash
   cd frontend
   npm run dev
   ```
3. **Compare lado a lado:**
   - Cores
   - Tipografia
   - Espaçamentos
   - Layout
   - Assets (ícones, imagens)

### **Passo 2: Ajustar Diferenças**

Se encontrar diferenças:

1. **Cores:**
   - Use Figma Inspect para obter valores exatos
   - Atualize nos componentes (styled-jsx)

2. **Tipografia:**
   - Verifique font-family no Figma
   - Adicione font no projeto (Google Fonts ou local)

3. **Espaçamentos:**
   - Use valores exatos do Figma (pixels)
   - Mantenha proporção em rem

4. **Assets:**
   - Exporte SVG do Figma
   - Adicione em `frontend/public/icons/`
   - Importe nos componentes

---

## 📝 Próximos Passos

### **1. Extrair Assets Específicos**

Se precisar de assets específicos:

1. **Logo "mano, traduz!":**
   - Exportar como SVG
   - Salvar: `frontend/public/icons/logo.svg`
   - Usar em Header e Footer

2. **Ícones:**
   - Estrela (XP)
   - Raio (Pontos)
   - Troféu (Resultados)
   - Chat bubble (Passo 1)
   - Lightning (Passo 2)
   - Trophy (Passo 3)

3. **Imagens (se houver):**
   - Hero image
   - Illustrations
   - Backgrounds

### **2. Adicionar Fontes**

1. **Verificar font-family no Figma:**
   - Provavelmente: Inter, Poppins, ou similar

2. **Adicionar no Next.js:**
   ```typescript
   // app/layout.tsx
   import { Inter } from 'next/font/google';
   
   const inter = Inter({ subsets: ['latin'] });
   ```

3. **Aplicar globalmente:**
   ```typescript
   <body className={inter.className}>
   ```

### **3. Refinar Estilos**

1. **Ajustar cores exatas:**
   - Use valores HEX/RGB do Figma Inspect
   - Atualize variáveis CSS se necessário

2. **Ajustar espaçamentos:**
   - Use valores em pixels do Figma
   - Converta para rem mantendo proporção

3. **Ajustar breakpoints:**
   - Verifique breakpoints no Figma (mobile, tablet, desktop)
   - Ajuste media queries nos componentes

---

## 🎨 Checklist de Importação

- [x] Componentes principais criados
- [x] Estrutura básica implementada
- [x] Cores principais aplicadas
- [x] Layout responsivo básico
- [ ] Cores exatas do Figma (verificar)
- [ ] Tipografia exata (font-family, weights)
- [ ] Assets extraídos (SVG, imagens)
- [ ] Espaçamentos exatos (padding, margin)
- [ ] Breakpoints exatos (mobile/desktop)
- [ ] Animações/transições (se houver)
- [ ] Interatividade (hover, active states)

---

## 🔧 Ferramentas Úteis

### **Extensão do Browser:**

- **Figma CSS Copy:** Copia estilos CSS do Figma
- **Figma to React:** Converte designs em código React

### **Plugins do Figma:**

- **Figma to Code:** Gera código HTML/CSS/React
- **Export Kit:** Exporta assets organizados
- **Style Guide:** Cria guia de estilo

### **Online:**

- **Figma Dev Mode:** Especificações técnicas
- **Figma Export:** Exporta assets em lote

---

## 📚 Referências

- **Figma Dev Mode:** https://help.figma.com/hc/en-us/articles/360055204534
- **Figma to Code:** https://www.figma.com/community/plugin
- **Next.js Fonts:** https://nextjs.org/docs/app/building-your-application/optimizing/fonts

---

## ✅ Status Atual

**Componentes criados baseados no design do Figma!** ✅

**Próximos passos:**
1. Extrair assets específicos (SVG, imagens)
2. Refinar cores e tipografia exatas
3. Ajustar espaçamentos e breakpoints
4. Adicionar animações (se houver)

**Veja componentes em:** `frontend/components/figma/`

---

**Design importado e componentes criados!** 🎨

**Quer ajustar algo específico ou extrair assets adicionais?**
