# 🎨 Exemplo Prático: Usando Figma MCP no Cursor

Este guia mostra exemplos práticos de como usar o MCP do Figma diretamente no Cursor para extrair código do seu design.

---

## 🚀 Como Usar

### **Método 1: Extrair Código de um Frame Específico**

1. **Abra seu design no Figma**
2. **Selecione o frame/componente que quer extrair**
3. **Copie a URL do Figma** (deve incluir `node-id`):
   ```
   https://figma.com/design/abc123/MeuProjeto?node-id=1-2
   ```

4. **No Cursor, digite:**
   ```
   Extraia o código React/Next.js deste frame do Figma e crie o componente em components/figma/LoginForm.tsx:
   
   URL: https://figma.com/design/abc123/MeuProjeto?node-id=1-2
   ```

5. **O Cursor vai:**
   - ✅ Conectar com o Figma via MCP
   - ✅ Extrair o design
   - ✅ Gerar código React/TypeScript
   - ✅ Criar o arquivo no projeto
   - ✅ Ajustar imports e paths

---

### **Método 2: Usar o nodeId Direto**

Se você souber o `fileKey` e `nodeId`:

1. **No Cursor, digite:**
   ```
   Gere código React/Next.js do Figma:
   - fileKey: abc123
   - nodeId: 1:2
   - Nome do componente: Button
   ```

2. **O Cursor vai criar:** `components/figma/Button.tsx`

---

### **Método 3: Extrair Múltiplos Componentes**

```
Extraia todos os componentes principais deste design do Figma:
URL: https://figma.com/design/abc123/MeuProjeto

Componentes para extrair:
1. LoginForm (node-id: 1-2)
2. Button (node-id: 1-5)
3. Card (node-id: 1-10)

Salve em components/figma/ com nomes apropriados.
```

---

## 📝 Exemplos de Comandos para o Cursor

### **Exemplo 1: Criar Formulário de Login**

```
Extraia o código do frame de login do Figma e crie um componente React funcional que:
1. Conecta com o backend usando api.login() de lib/api.ts
2. Mostra mensagens de erro
3. Redireciona após login bem-sucedido

URL do Figma: [SUA_URL_AQUI]
Salvar como: components/figma/LoginForm.tsx
```

### **Exemplo 2: Criar Lista de Conversas**

```
Do design do Figma, extraia o componente de lista de conversas e crie:
- Componente React que busca dados do backend via api.getConversations()
- Mostra loading state
- Trata erros
- Permite clicar em uma conversa

URL: [SUA_URL_AQUI]
Salvar como: components/figma/ConversationList.tsx
```

### **Exemplo 3: Extrair Design Completo de Página**

```
Extraia todo o design da página de dashboard do Figma e crie:
- Página completa em app/dashboard/page.tsx
- Componentes separados em components/figma/
- Integração com backend onde necessário

URL: [SUA_URL_AQUI]
```

---

## 🔍 Como Encontrar o fileKey e nodeId

### **Na URL do Figma:**

URL completa:
```
https://figma.com/design/[FILE_KEY]/[NOME]?node-id=[NODE_ID]
```

Exemplo:
```
https://figma.com/design/abc123xyz/MeuProjeto?node-id=1-2
```

- **fileKey:** `abc123xyz`
- **nodeId:** `1-2` (pode ser `1:2` também)

### **No Figma Desktop App:**

1. Abra o Dev Mode (ícone no canto superior direito)
2. Selecione o frame/componente
3. Veja o `nodeId` no painel à direita
4. Veja o `fileKey` na URL do navegador ou no menu File → Copy link

---

## 🎯 Exemplo Completo: Do Figma ao Código Funcional

### **Passo 1: No Cursor**

```
Extraia o componente de botão do Figma e crie um componente React reutilizável:

fileKey: abc123
nodeId: 1:5
Nome: Button
Salvar em: components/figma/Button.tsx

O componente deve aceitar props:
- label: string
- onClick?: () => void
- variant?: 'primary' | 'secondary'
- disabled?: boolean
```

### **Passo 2: O Cursor Gera:**

```tsx
// components/figma/Button.tsx
'use client';

export interface ButtonProps {
  label: string;
  onClick?: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export default function Button({
  label,
  onClick,
  variant = 'primary',
  disabled = false
}: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
      disabled={disabled}
    >
      {label}
    </button>
  );
}
```

### **Passo 3: Usar no Projeto**

```tsx
// app/page.tsx
import Button from '@/components/figma/Button';

export default function Home() {
  return (
    <main>
      <Button 
        label="Clique Aqui" 
        variant="primary"
        onClick={() => console.log('Clicou!')}
      />
    </main>
  );
}
```

---

## 🛠️ Integração Automática com Backend

Você pode pedir para o Cursor já integrar com o backend:

```
Extraia o formulário de criação de perfil do Figma e:
1. Crie o componente em components/figma/CreateProfileForm.tsx
2. Integre com o backend usando api.createProfile() de lib/api.ts
3. Adicione validação de campos
4. Mostre mensagens de sucesso/erro
5. Redirecione após criação

URL: [SUA_URL_AQUI]
```

O Cursor vai gerar um componente completo e funcional! 🎉

---

## ✅ Checklist de Extração

Antes de pedir para o Cursor extrair:

- [ ] Tenho a URL do Figma com node-id
- [ ] O design está finalizado no Figma
- [ ] Sei qual componente/frame extrair
- [ ] Defini onde salvar o arquivo
- [ ] Sei quais props o componente precisa
- [ ] Sei se precisa integrar com backend

---

## 💡 Dicas

1. **Seja específico:** Quanto mais detalhes você der, melhor o resultado
2. **Peça integração direto:** Peça para já conectar com o backend na primeira extração
3. **Extraia por partes:** Componentes pequenos funcionam melhor
4. **Revise o código:** Sempre revise o código gerado antes de usar
5. **Teste imediatamente:** Teste o componente logo após gerar

---

## 🆘 Problemas Comuns

### ❌ "Não consegui conectar com o Figma"

**Solução:**
1. Verifique se o MCP do Figma está configurado no Cursor
2. Verifique se está autenticado no Figma
3. Verifique se a URL está correta

### ❌ "Código gerado não está funcionando"

**Solução:**
1. Revise os imports
2. Verifique se os assets foram copiados
3. Ajuste paths de imagens
4. Verifique se há erros no console

### ❌ "Falta integração com backend"

**Solução:**
- Peça explicitamente: "Integre este componente com o backend usando api..."

---

**Pronto!** Agora você pode usar o Figma MCP no Cursor para extrair código automaticamente! 🚀

Para mais detalhes, veja: [COMO-INTEGRAR-FIGMA-COM-BACKEND.md](./COMO-INTEGRAR-FIGMA-COM-BACKEND.md)
