# 🎨 Extrair Assets do Figma - Agora

Guia rápido para extrair assets (SVG, cores, tipografia) do design do Figma.

**Design:** https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled?node-id=1-2

---

## ⚡ Extração Rápida (5 minutos)

### **Passo 1: Abrir Figma Dev Mode**

1. **No Figma:**
   - Abra o design: https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/Untitled
   - Clique no toggle **"Dev Mode"** (canto superior direito)
   - Isso mostra especificações técnicas de cada elemento

### **Passo 2: Extrair Cores**

1. **No Dev Mode:**
   - Selecione qualquer elemento roxo
   - Veja o código de cor (HEX/RGB)
   - Anote os valores

2. **Cores para extrair:**
   - **Roxo primário:** (do header/hero)
   - **Roxo secundário:** (do footer)
   - **Laranja:** (botões primários)
   - **Amarelo:** (tag amarela)
   - **Branco:** (textos)
   - **Cinza:** (textos secundários)

### **Passo 3: Extrair SVG/Ícones**

1. **Ícone do logo (D):**
   - Selecione o círculo com "D"
   - Botão direito → **"Copy/Paste as"** → **"Copy as SVG"**
   - Ou: Selecionar → **Export** → **SVG**

2. **Ícones dos badges:**
   - Estrela (XP)
   - Raio (Pontos)
   - Troféu (Resultados)

3. **Ícones dos passos:**
   - Chat bubble (Passo 1)
   - Lightning (Passo 2)
   - Trophy (Passo 3)

### **Passo 4: Extrair Tipografia**

1. **No Dev Mode:**
   - Selecione um texto grande (título)
   - Veja especificações:
     - **Font-family:** (ex: Inter, Poppins)
     - **Font-size:** (ex: 64px, 48px)
     - **Font-weight:** (ex: 700, 600)
     - **Line-height:** (ex: 1.1, 1.2)

2. **Anotar:**
   - Títulos principais
   - Títulos de seção
   - Texto corpo
   - Labels/captions

---

## 📦 Salvar Assets no Projeto

### **Estrutura de Diretórios:**

```bash
cd frontend
mkdir -p public/icons
mkdir -p public/images
mkdir -p public/fonts
```

### **Arquivos para Criar:**

1. **Ícones SVG:**
   - `public/icons/logo.svg` (logo D)
   - `public/icons/star.svg` (estrela XP)
   - `public/icons/lightning.svg` (raio)
   - `public/icons/trophy.svg` (troféu)

2. **Variáveis de Cores:**
   - Criar `frontend/styles/colors.ts` ou
   - Usar diretamente nos componentes (já feito)

---

## 🔧 Método Manual: Passo a Passo

### **1. Extrair Logo "D"**

**No Figma:**
1. Selecione o círculo branco com "D" preto/roxo
2. Botão direito → **"Copy/Paste as"** → **"Copy as SVG"**
3. Cole aqui ou salve em arquivo

**Salvar:**
```bash
# Criar arquivo
touch frontend/public/icons/logo-d.svg
# Colar SVG copiado do Figma
```

### **2. Extrair Cores Exatas**

**No Figma Dev Mode:**
1. Selecione elemento roxo do header
2. Veja código de cor (ex: `#7C3AED`)
3. Verifique se há gradiente
4. Anote todos os valores

**Aplicar:**
- Atualizar nos componentes
- Ou criar variáveis CSS

### **3. Extrair Espaçamentos**

**No Figma Dev Mode:**
1. Selecione elemento
2. Veja **Padding** e **Margin**
3. Anote valores em pixels
4. Converta para rem (dividir por 16)

**Exemplo:**
- Figma: `padding: 32px` → CSS: `padding: 2rem`
- Figma: `gap: 24px` → CSS: `gap: 1.5rem`

---

## ✅ Checklist de Extração

- [ ] Logo "D" extraído (SVG)
- [ ] Ícones extraídos (estrela, raio, troféu)
- [ ] Cores exatas anotadas (roxo, laranja, amarelo)
- [ ] Tipografia verificada (font-family, sizes, weights)
- [ ] Espaçamentos anotados (padding, margin, gaps)
- [ ] Breakpoints identificados (mobile, tablet, desktop)
- [ ] Assets salvos em `public/icons/` ou `public/images/`

---

## 🚀 Próximos Passos

Após extrair assets:

1. **Salvar SVG no projeto:**
   ```bash
   # Criar diretório
   mkdir -p frontend/public/icons
   
   # Salvar SVGs extraídos
   # logo-d.svg
   # star.svg
   # lightning.svg
   # trophy.svg
   ```

2. **Atualizar componentes:**
   - Importar SVG nos componentes
   - Ou usar inline (já feito com SVGs inline)

3. **Refinar cores e espaçamentos:**
   - Usar valores exatos do Figma
   - Atualizar componentes

---

## 📝 Nota

**Componentes já foram criados** baseados na descrição do design do Figma! ✅

**O que falta:**
- Assets específicos (SVG, imagens) - se necessário
- Ajustes finos de cores/espaçamentos - se necessário
- Tipografia exata - se necessário

**O design já está implementado!** Quer ajustar algo específico?

---

**Pronto para extrair assets específicos quando necessário!** 🎨
