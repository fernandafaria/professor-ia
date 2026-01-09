# 🎨 Guia Completo: Extrair Assets do Figma Make

Guia passo a passo completo desde o login no Figma até ter os assets no seu projeto.

---

## 🚀 Passo a Passo Completo

### **Passo 1: Login no Figma** 🔑

1. **Na página do Figma Make que você compartilhou:**
   - Você verá uma tela de login/criação de conta

2. **Faça login ou crie conta:**
   - **Opção A:** "Continuar com o Google" (mais rápido)
   - **Opção B:** "Continuar com o e-mail" (digite seu email)

3. **Após login:** A página do Figma Make será carregada

---

### **Passo 2: Acessar o Arquivo Original no Figma**

#### **Método A: Via Botão no Figma Make**

1. **Na página do Figma Make:**
   - Procure por um botão ou link:
     - **"Open in Figma"** ou **"Abrir no Figma"**
     - **"View Source File"** ou **"Ver Arquivo Original"**
     - **"Edit in Figma"** ou **"Editar no Figma"**
   - Geralmente está no **topo da página** ou **menu lateral**

2. **Clique nesse botão/link**
   - Isso abrirá o arquivo original no Figma em uma nova aba

#### **Método B: Direto no Figma**

1. **Abra o Figma** (navegador: figma.com ou app desktop)

2. **Procure pelo arquivo:**
   - **"Frontend da Plataforma"**
   - **"Professor IA"**
   - Ou qualquer nome que você deu ao arquivo

3. **Abra o arquivo**

---

### **Passo 3: Identificar os Assets Necessários**

No arquivo do Figma, identifique o que você precisa exportar:

#### **Ícones/Logos (SVG recomendado):**
- ✅ Logo "Professor IA" 
- ✅ Ícone de estrela
- ✅ Ícones de métricas (se houver)
- ✅ Ícones do menu

#### **Imagens (PNG/JPG):**
- ✅ Background do Hero (se houver imagem, não gradiente CSS)
- ✅ Ilustrações
- ✅ Imagens de features/seções

---

### **Passo 4: Exportar Assets do Figma**

#### **Para Ícones/Logos (SVG - Recomendado):**

1. **Selecione o ícone/logo no Figma**
   - Clique uma vez para selecionar

2. **No painel direito, vá em "Export":**
   - Se não ver a seção Export, clique no ícone de exportação (⬇️)

3. **Adicione formato:**
   - Clique em **"+"** para adicionar formato
   - Escolha: **SVG** (melhor para ícones - vetorial, escalável)
   - Ou **PNG @2x** para alta resolução

4. **Export:**
   - Clique em **"Export [Nome do Ícone]"**
   - O arquivo será baixado automaticamente

5. **Repita para cada ícone/logo**

#### **Para Imagens (PNG/JPG):**

1. **Selecione a imagem/ilustração no Figma**

2. **Painel direito → "Export"**

3. **Adicione formato:**
   - **PNG @2x** (recomendado para imagens com transparência)
   - **JPG @2x** (para fotos - menor tamanho)
   - **PNG @3x** (ultra alta resolução, se necessário)

4. **Export:**
   - Clique em **"Export [Nome]"**
   - Arquivo será baixado

---

### **Passo 5: Organizar Assets no Projeto**

#### **Estrutura de Pastas (já criada):**

```
frontend/public/assets/
├── images/    ← Imagens aqui
└── icons/     ← Ícones/logos aqui
```

#### **Mover Arquivos Exportados:**

##### **Opção A: Via Terminal (Mac/Linux):**

```bash
# Navegar para a pasta do projeto
cd /Users/fernandafaria/Downloads/P1A

# Criar estrutura (se ainda não criou)
mkdir -p frontend/public/assets/images
mkdir -p frontend/public/assets/icons

# Mover assets exportados (ajuste os nomes conforme você exportou)
# Ícones/Logos → icons/
mv ~/Downloads/logo.svg frontend/public/assets/icons/
mv ~/Downloads/star-icon.svg frontend/public/assets/icons/

# Imagens → images/
mv ~/Downloads/hero-bg.png frontend/public/assets/images/
mv ~/Downloads/hero-background.png frontend/public/assets/images/

# Verificar se foram movidos corretamente
ls -la frontend/public/assets/icons/
ls -la frontend/public/assets/images/
```

##### **Opção B: Manual (Arrastar e Soltar):**

1. **Abra o Finder** (Mac) ou Explorador de Arquivos (Windows)
2. **Vá para:** `~/Downloads` (ou onde você salvou os arquivos)
3. **Selecione os assets exportados**
4. **Arraste para:**
   - Ícones/logos → `P1A/frontend/public/assets/icons/`
   - Imagens → `P1A/frontend/public/assets/images/`

##### **Opção C: Usar o Script Helper:**

```bash
cd /Users/fernandafaria/Downloads/P1A/frontend
./organize-assets.sh
```

O script mostrará as instruções de onde mover os arquivos.

---

### **Passo 6: Atualizar Componentes com Assets**

Os componentes já estão preparados com **TODOs** marcando onde adicionar assets!

#### **6.1. HeroCTA.tsx - Background Image (se houver):**

Se você exportou uma imagem de background:

```tsx
// frontend/components/figma/HeroCTA.tsx

// 1. Descomente o import:
import Image from 'next/image';

// 2. Descomente o componente Image dentro do return:
<Image
  src="/assets/images/hero-background.png"  // Ajuste o nome do arquivo
  alt="Hero Background"
  fill
  className="hero-background-image"
  priority
/>

// 3. Descomente o CSS do ::before no style jsx:
.hero-cta::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('/assets/images/hero-background.png');
  background-size: cover;
  background-position: center;
  opacity: 0.1;
  z-index: 0;
}
```

#### **6.2. Footer.tsx - Logo SVG (se exportou):**

Se você exportou o logo como SVG:

```tsx
// frontend/components/figma/Footer.tsx

// Substitua o SVG inline pelo asset exportado:
import Image from 'next/image';

// Dentro do componente, substitua o SVG por:
<Image
  src="/assets/icons/logo.svg"  // Ajuste o nome do arquivo
  alt="Professor IA"
  width={24}
  height={24}
  className="logo-img"
/>
```

#### **6.3. Header.tsx - Ícones (se houver):**

Se você exportou ícones para as métricas:

```tsx
// frontend/components/figma/Header.tsx

// Adicione imports:
import Image from 'next/image';

// Dentro de cada Metric, adicione:
<Image
  src="/assets/icons/metric-icon.svg"  // Ajuste conforme necessário
  alt={label}
  width={24}
  height={24}
/>
```

---

### **Passo 7: Testar no Navegador**

1. **Inicie o servidor:**

```bash
# Terminal 1: Backend
cd /Users/fernandafaria/Downloads/P1A/backend
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd /Users/fernandafaria/Downloads/P1A/frontend
npm run dev
```

2. **Acesse:**
   - http://localhost:3000

3. **Verifique:**
   - ✅ Assets aparecem corretamente
   - ✅ Sem erros no console (F12 → Console)
   - ✅ Imagens carregam sem problemas

4. **Se algo não aparecer:**
   - Verifique o path dos assets (devem começar com `/assets/`)
   - Verifique se os arquivos estão em `public/assets/`
   - Reinicie o servidor: `Ctrl+C` e `npm run dev` novamente

---

## 📋 Checklist Completo

### **Exportação:**
- [ ] Fiz login no Figma
- [ ] Acessei o arquivo original no Figma
- [ ] Identifiquei todos os assets necessários
- [ ] Exportei logo "Professor IA" (SVG)
- [ ] Exportei ícone de estrela (SVG, se houver)
- [ ] Exportei background do Hero (PNG, se houver imagem)
- [ ] Exportei outras imagens/ilustrações (se houver)

### **Organização:**
- [ ] Criei estrutura de pastas (`public/assets/images/` e `icons/`)
- [ ] Mudei ícones/logos para `public/assets/icons/`
- [ ] Mudei imagens para `public/assets/images/`
- [ ] Verifiquei que os arquivos estão nos lugares corretos

### **Atualização de Componentes:**
- [ ] Atualizei HeroCTA.tsx com background (se houver)
- [ ] Atualizei Footer.tsx com logo SVG (se exportou)
- [ ] Atualizei Header.tsx com ícones (se houver)
- [ ] Ajustei paths para `/assets/...`
- [ ] Testei no navegador (assets aparecem)
- [ ] Não há erros no console

---

## 🆘 Problemas Comuns e Soluções

### ❌ "Não consigo fazer login no Figma"

**Solução:**
- Use "Continuar com Google" (mais rápido)
- Ou crie conta com email: digite email → clique em "Continuar"
- Verifique seu email para confirmar conta (se necessário)

### ❌ "Não encontro o botão 'Open in Figma'"

**Soluções:**
- **Opção 1:** Procure no menu lateral (ícone de 3 linhas)
- **Opção 2:** Acesse diretamente o Figma e procure pelo arquivo
- **Opção 3:** Peça ao criador do design para compartilhar o link direto

### ❌ "Assets não aparecem no navegador"

**Soluções:**
1. **Verifique paths:**
   - Devem ser absolutos: `/assets/images/logo.png`
   - Não use relativos: `./assets/...` ou `../assets/...`

2. **Verifique localização:**
   ```bash
   # Verificar se arquivos estão corretos
   ls -la frontend/public/assets/icons/
   ls -la frontend/public/assets/images/
   ```

3. **Reinicie servidor:**
   ```bash
   # Ctrl+C para parar
   npm run dev  # Iniciar novamente
   ```

4. **Verifique console:**
   - F12 → Console
   - Veja se há erros 404 (arquivo não encontrado)
   - Ajuste paths conforme necessário

### ❌ "SVG não aparece"

**Soluções:**
- Verifique se o SVG é válido (abra no navegador)
- Use `<img>` em vez de `<Image>` do Next.js para SVG simples:
  ```tsx
  <img src="/assets/icons/logo.svg" alt="Logo" />
  ```
- Ou use `next/image` com `unoptimized={true}`:
  ```tsx
  <Image src="/assets/icons/logo.svg" unoptimized />
  ```

### ❌ "Imagem muito grande/pesada"

**Soluções:**
- Use ferramentas de compressão: [TinyPNG](https://tinypng.com/)
- Ou use `next/image` que otimiza automaticamente
- Considere usar `@2x` em vez de `@3x` se a imagem ficar muito pesada

---

## 💡 Dicas Finais

1. **SVG para Ícones:**
   - ✅ Melhor qualidade em qualquer tamanho
   - ✅ Menor tamanho de arquivo
   - ✅ Escalável sem perda

2. **PNG para Imagens:**
   - ✅ Use @2x para alta resolução
   - ✅ Comprima imagens para reduzir tamanho
   - ✅ Use Next.js Image component para otimização automática

3. **Nomes Descritivos:**
   - Use nomes claros: `logo.svg`, `hero-background.png`
   - Evite: `Untitled-1.png`, `image.png`

4. **Organização:**
   - Mantenha ícones em `icons/`
   - Mantenha imagens em `images/`
   - Evite misturar tipos

---

## ✅ Próximos Passos Após Exportar Assets

1. ✅ **Teste completo:** Verifique todas as páginas
2. ✅ **Otimize imagens:** Comprima se necessário
3. ✅ **Remove placeholders:** Remova componentes temporários
4. ✅ **Adicione mais assets:** Se houver mais designs para integrar

---

## 🎯 Resumo Rápido

1. **Login no Figma** → Acesse arquivo original
2. **Exporte assets** → SVG (ícones), PNG (imagens)
3. **Organize** → `public/assets/icons/` e `images/`
4. **Atualize componentes** → Descomente TODOs e ajuste paths
5. **Teste** → `npm run dev` e verifique no navegador

---

**Pronto!** Siga este guia passo a passo e você terá todos os assets extraídos e funcionando no seu projeto! 🎉

Se tiver dúvidas em qualquer passo, me avise que ajudo! 🚀

---

**Última atualização:** 2026-01-09
