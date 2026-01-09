# 🔗 Como Obter o Link Original do Figma

Você compartilhou um link do **Figma Make**, mas para extrair assets via MCP do Figma, precisamos do **link do arquivo original do Figma**.

---

## 🎯 Solução Rápida

### **Opção 1: Encontrar o Link Original no Figma Make**

1. **Na página do Figma Make que você compartilhou:**
   - Procure por um botão ou link que diz **"Abrir no Figma"** ou **"View in Figma"**
   - Ou procure por **"Source File"** ou **"Arquivo Original"**
   - Geralmente está no topo ou no menu lateral

2. **Clique nesse link** - ele vai abrir o arquivo original no Figma

3. **Copie o link do arquivo:**
   - Quando o arquivo abrir no Figma, copie a URL da barra de endereço
   - Formato: `https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]`

---

### **Opção 2: Acessar Diretamente no Figma**

1. **Abra o Figma** (navegador ou desktop app)

2. **Procure pelo arquivo "Frontend da Plataforma"**
   - Pode estar em "Recents" (Recentes) ou em alguma pasta

3. **Abra o arquivo**

4. **Selecione o frame/componente** que contém o design

5. **Copie o link:**
   - Menu: **Share** → **Copy link**
   - Ou copie da URL do navegador

---

### **Opção 3: Pedir ao Criador do Design**

Se o design foi criado por outra pessoa:

1. Peça para compartilhar o **link do arquivo do Figma** (não o protótipo ou Make)
2. Formato necessário: `https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]`

---

## 📋 Formato do Link Necessário

### ✅ **Link Correto (Arquivo Original):**
```
https://figma.com/design/abc123xyz/Frontend-da-Plataforma?node-id=1-2
```

### ❌ **Link do Figma Make (NÃO serve para MCP):**
```
https://www.figma.com/make/iHKJzezk69Uj3XbyeeWDy9/Frontend-da-Plataforma
```

---

## 🔍 Como Identificar se é o Link Correto

O link correto:
- ✅ Começa com `figma.com/design/`
- ✅ Tem um `fileKey` após `/design/`
- ✅ Pode ter `?node-id=` para um frame específico

O link do Make:
- ❌ Começa com `figma.com/make/`
- ❌ Tem um ID do Make, não o fileKey do arquivo

---

## 🚀 Após Obter o Link Original

Assim que tiver o link correto, compartilhe aqui e eu:

1. ✅ Extraio todos os assets automaticamente
2. ✅ Organizo na estrutura correta (`public/assets/`)
3. ✅ Atualizo os componentes para usar os assets
4. ✅ Otimizo imagens se necessário

**Basta colar o link original aqui!** 🎉

---

## 💡 Alternativa: Exportar Manualmente

Se não conseguir o link original, você pode:

1. **No Figma Make:**
   - Gere o código React/Next.js
   - O código gerado geralmente inclui referências aos assets

2. **No Figma Original:**
   - Exporte assets manualmente
   - Selecione imagens/ícones → Right-click → Export
   - Salve em `frontend/public/assets/`

3. **Atualize os componentes:**
   - Use os assets exportados
   - Atualize paths no código

---

## 🆘 Precisa de Ajuda?

Se não conseguir encontrar o link original:

1. **Descreva o problema** - onde está travado
2. **Compartilhe uma screenshot** - da página do Figma Make
3. **Verifique se tem acesso** - ao arquivo original no Figma

Posso ajudar a encontrar o link ou criar uma solução alternativa!

---

**Próximo Passo:** Compartilhe o link original do Figma aqui e eu extraio os assets automaticamente! 🚀
