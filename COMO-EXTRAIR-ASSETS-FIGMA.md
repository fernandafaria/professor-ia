# 🎨 Como Extrair Assets do Figma via MCP

Este guia explica como extrair imagens, ícones e outros assets do Figma usando o MCP do Figma.

---

## 📋 Pré-requisitos

1. **Link direto do arquivo do Figma** (não protótipo compartilhado)
   - Formato: `https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]`
   - Exemplo: `https://figma.com/design/abc123/MeuProjeto?node-id=1-2`

2. **Figma Desktop App instalado** ou acesso via browser com Dev Mode

---

## 🔍 Como Obter o fileKey e nodeId

### **Método 1: Do Link do Figma**

1. Abra seu design no Figma (navegador ou desktop)
2. Copie o link do arquivo (não o protótipo compartilhado)
3. O link terá o formato:
   ```
   https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]
   ```
4. Extraia:
   - **fileKey**: Parte entre `/design/` e `/` (ex: `abc123`)
   - **nodeId**: Parte depois de `node-id=` (ex: `1-2` ou `1:2`)

### **Método 2: Via Figma Desktop**

1. Abra o arquivo no Figma Desktop
2. Selecione o frame/componente que contém os assets
3. Veja o `nodeId` no painel à direita (Dev Mode)
4. O `fileKey` está na URL ou no menu File → Copy link

---

## 🚀 Extrair Assets via Cursor (Usando MCP)

### **Passo 1: Usar o Chat do Cursor**

No chat do Cursor, digite:

```
Extraia todos os assets (imagens, ícones, logos) deste design do Figma e salve em public/assets/:

fileKey: [SEU_FILE_KEY]
nodeId: [SEU_NODE_ID]

Salve as imagens em:
- public/assets/images/ (para imagens/ilustrações)
- public/assets/icons/ (para ícones/logos)
```

### **Passo 2: O Cursor vai:**

1. ✅ Conectar com o Figma via MCP
2. ✅ Extrair imagens e assets do design
3. ✅ Baixar e salvar em `public/assets/`
4. ✅ Gerar referências no código

---

## 📝 Exemplo Completo

### **1. No Figma, obtenha:**
- fileKey: `abc123xyz`
- nodeId: `1:2`

### **2. No Cursor, digite:**

```
Extraia o design e todos os assets do Figma:

fileKey: abc123xyz
nodeId: 1:2

Inclua:
- Todas as imagens (salvar em public/assets/images/)
- Todos os ícones (salvar em public/assets/icons/)
- Logo (se houver, em public/assets/icons/)

Também gere o componente React correspondente em components/figma/HeroCTA.tsx usando os assets extraídos.
```

### **3. Resultado:**

O Cursor vai:
- ✅ Baixar todas as imagens do design
- ✅ Salvar em `public/assets/images/`
- ✅ Salvar ícones em `public/assets/icons/`
- ✅ Criar componente React com referências corretas aos assets
- ✅ Atualizar imports e paths

---

## 🎯 Assets Comuns a Extrair

### **Imagens**
- Backgrounds
- Ilustrações
- Fotos de hero/banner
- Cards com imagens

### **Ícones**
- Logo da marca
- Ícones de UI (setas, check, etc.)
- Favicons
- Ícones de social media

### **Elementos Gráficos**
- Decorações
- Patterns
- Bordas personalizadas

---

## 📁 Estrutura de Assets Após Extração

```
public/
└── assets/
    ├── images/
    │   ├── hero-background.png
    │   ├── illustration-1.png
    │   └── ...
    └── icons/
        ├── logo.svg
        ├── star-icon.svg
        └── ...
```

---

## 💡 Usar Assets no Código

Após extrair, use assim:

```tsx
import Image from 'next/image';

export default function HeroCTA() {
  return (
    <section className="hero-cta">
      <Image
        src="/assets/images/hero-background.png"
        alt="Background"
        fill
        className="hero-background"
      />
      <img 
        src="/assets/icons/logo.svg" 
        alt="Logo" 
        className="logo"
      />
    </section>
  );
}
```

---

## 🆘 Problemas Comuns

### ❌ "Não consegui acessar o Figma"

**Solução:**
1. Verifique se o MCP do Figma está configurado
2. Verifique se está autenticado no Figma
3. Use o link direto do design (não protótipo)

### ❌ "fileKey não encontrado"

**Solução:**
- Certifique-se de usar o link do arquivo do Figma, não o protótipo
- O link deve ter o formato: `figma.com/design/[FILE_KEY]/...`

### ❌ "Assets não foram baixados"

**Solução:**
- Verifique permissões de escrita na pasta `public/assets/`
- Certifique-se de que o nodeId aponta para um frame/componente que contém assets

---

## 📚 Alternativa: Exportar Manualmente do Figma

Se o MCP não funcionar, você pode:

1. **No Figma:**
   - Selecione os assets
   - Clique com botão direito → Export
   - Escolha formato (PNG, SVG, etc.)
   - Baixe manualmente

2. **Salvar no projeto:**
   - Mova para `public/assets/images/` ou `public/assets/icons/`
   - Atualize referências no código

---

## ✅ Checklist

- [ ] Tenho o link direto do design do Figma
- [ ] Extraí o fileKey e nodeId
- [ ] Configurei o MCP do Figma no Cursor
- [ ] Assets foram extraídos e salvos
- [ ] Componentes foram atualizados com referências aos assets
- [ ] Testei no navegador (assets aparecem corretamente)

---

**Precisa de ajuda?** Compartilhe o link direto do seu design do Figma e eu extraio os assets para você!
