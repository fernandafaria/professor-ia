# 🎨 Guia de Integração - Figma Make

Este guia explica como adicionar e integrar código gerado pelo **Figma Make** ao frontend do projeto P1A.

---

## 📋 O que é Figma Make?

O **Figma Make** é uma ferramenta que gera código React/Next.js diretamente a partir de designs do Figma. Ele permite:

- ✅ Gerar componentes React funcionais
- ✅ Preservar estilos e layout
- ✅ Exportar assets automaticamente
- ✅ Gerar código TypeScript

---

## 🚀 Passo a Passo

### 1. Gerar Código no Figma Make

#### Opção A: Via Figma Desktop/Web

1. **Abra seu design no Figma**
   - Certifique-se de que o design está completo e organizado
   - Use frames nomeados para facilitar a exportação

2. **Acesse o Figma Make**
   - No Figma, vá em **Plugins** → **Figma Make**
   - Ou acesse: https://www.figma.com/community/plugin/figma-make

3. **Selecione o Frame/Componente**
   - Selecione o frame ou componente que deseja exportar
   - Configure as opções:
     - **Framework:** React/Next.js
     - **Language:** TypeScript
     - **Style:** CSS Modules ou Tailwind (conforme preferência)

4. **Gere o Código**
   - Clique em **"Generate Code"**
   - O código será gerado e exibido

5. **Copie o Código**
   - Copie o código React/TypeScript gerado
   - Copie também os assets (imagens, ícones) se houver

---

### 2. Adicionar ao Projeto

#### Estrutura de Pastas Recomendada

```
frontend/
├── components/
│   ├── figma/              # Componentes gerados pelo Figma Make
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   └── ...
│   └── ...
├── app/
│   ├── (pages)/           # Páginas que usam componentes do Figma
│   │   ├── landing/
│   │   │   └── page.tsx
│   │   └── ...
│   └── ...
└── public/
    └── assets/             # Assets exportados do Figma
        ├── images/
        └── icons/
```

#### Passo 1: Criar o Componente

1. **Crie o arquivo do componente:**
   ```bash
   # Exemplo: criar um componente Button
   touch frontend/components/figma/Button.tsx
   ```

2. **Cole o código gerado pelo Figma Make:**
   ```tsx
   // frontend/components/figma/Button.tsx
   import React from 'react';
   import styles from './Button.module.css'; // ou use Tailwind
   
   export interface ButtonProps {
     label: string;
     onClick?: () => void;
     variant?: 'primary' | 'secondary';
   }
   
   export const Button: React.FC<ButtonProps> = ({
     label,
     onClick,
     variant = 'primary'
   }) => {
     return (
       <button
         className={styles.button}
         onClick={onClick}
         data-variant={variant}
       >
         {label}
       </button>
     );
   };
   ```

#### Passo 2: Ajustar Imports e Paths

O código gerado pelo Figma Make pode ter imports que precisam ser ajustados:

**Antes (gerado pelo Figma):**
```tsx
import './Button.css';
import icon from './assets/icon.svg';
```

**Depois (ajustado para o projeto):**
```tsx
import styles from './Button.module.css';
import icon from '@/public/assets/icons/icon.svg';
```

**Dicas:**
- Use `@/` para imports absolutos (configurado no `tsconfig.json`)
- Mova assets para `public/assets/`
- Ajuste paths de imagens para `/assets/...`

#### Passo 3: Adicionar Assets

1. **Copie assets do Figma:**
   - Imagens → `public/assets/images/`
   - Ícones → `public/assets/icons/`
   - Fontes → `public/assets/fonts/` (se necessário)

2. **Atualize referências no código:**
   ```tsx
   // Antes
   <img src="./assets/logo.png" />
   
   // Depois
   <img src="/assets/images/logo.png" alt="Logo" />
   ```

---

### 3. Integrar com o Backend

#### Conectar Componentes com API

1. **Use o cliente API:**
   ```tsx
   // components/figma/LoginForm.tsx
   import { api } from '@/lib/api';
   import { useState } from 'react';
   
   export const LoginForm = () => {
     const [email, setEmail] = useState('');
     const [password, setPassword] = useState('');
     
     const handleSubmit = async (e: React.FormEvent) => {
       e.preventDefault();
       
       try {
         const response = await api.post('/auth/login', {
           email,
           password
         });
         
         // Salvar token, redirecionar, etc.
         localStorage.setItem('token', response.data.access_token);
         window.location.href = '/dashboard';
       } catch (error) {
         console.error('Erro no login:', error);
       }
     };
     
     return (
       <form onSubmit={handleSubmit}>
         {/* Campos do formulário gerados pelo Figma Make */}
       </form>
     );
   };
   ```

2. **Adicionar Estado e Lógica:**
   - Use React Hooks (`useState`, `useEffect`)
   - Integre com o backend via `lib/api.ts`
   - Adicione validação e tratamento de erros

---

### 4. Usar em Páginas

#### Exemplo: Página de Landing

```tsx
// app/(pages)/landing/page.tsx
import { Button } from '@/components/figma/Button';
import { Hero } from '@/components/figma/Hero';
import { Features } from '@/components/figma/Features';

export default function LandingPage() {
  return (
    <main>
      <Hero />
      <Features />
      <Button 
        label="Começar Agora"
        onClick={() => window.location.href = '/onboarding'}
      />
    </main>
  );
}
```

---

## 🔧 Ajustes Comuns Necessários

### 1. Estilos (CSS)

**Opção A: CSS Modules (Recomendado)**
```tsx
// Button.module.css
.button {
  padding: 12px 24px;
  border-radius: 8px;
  /* ... */
}
```

**Opção B: Tailwind CSS**
```tsx
// Se usar Tailwind
<button className="px-6 py-3 rounded-lg bg-blue-500">
  {label}
</button>
```

### 2. TypeScript Types

Adicione tipos para props:
```tsx
export interface ComponentProps {
  title: string;
  description?: string;
  onClick?: () => void;
}
```

### 3. Responsividade

Ajuste breakpoints se necessário:
```tsx
// Use media queries ou Tailwind
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  {/* ... */}
</div>
```

### 4. Acessibilidade

Adicione atributos ARIA:
```tsx
<button
  aria-label="Fechar modal"
  aria-expanded={isOpen}
  onClick={handleClose}
>
  Fechar
</button>
```

---

## 📦 Estrutura Completa de Exemplo

```
frontend/
├── components/
│   └── figma/
│       ├── Button.tsx              # Componente gerado
│       ├── Button.module.css       # Estilos
│       ├── Card.tsx
│       ├── Card.module.css
│       ├── LoginForm.tsx            # Componente com lógica
│       └── ...
├── app/
│   ├── (pages)/
│   │   ├── landing/
│   │   │   └── page.tsx            # Usa componentes do Figma
│   │   └── dashboard/
│   │       └── page.tsx
│   └── layout.tsx
├── public/
│   └── assets/
│       ├── images/
│       │   └── hero-bg.png
│       └── icons/
│           └── logo.svg
└── lib/
    └── api.ts                      # Cliente API
```

---

## 🎯 Checklist de Integração

- [ ] Código gerado pelo Figma Make copiado
- [ ] Componente criado em `components/figma/`
- [ ] Imports ajustados (usar `@/` para paths absolutos)
- [ ] Assets movidos para `public/assets/`
- [ ] Estilos configurados (CSS Modules ou Tailwind)
- [ ] TypeScript types adicionados
- [ ] Integração com backend (se necessário)
- [ ] Testado localmente (`npm run dev`)
- [ ] Responsividade verificada
- [ ] Acessibilidade verificada

---

## 🆘 Troubleshooting

### Erro: "Module not found"

**Solução:** Ajuste os imports para usar paths absolutos:
```tsx
// ❌ Errado
import './styles.css';

// ✅ Correto
import styles from './Component.module.css';
```

### Imagens não aparecem

**Solução:** Use paths absolutos começando com `/`:
```tsx
// ❌ Errado
<img src="./assets/logo.png" />

// ✅ Correto
<img src="/assets/images/logo.png" alt="Logo" />
```

### Estilos não aplicam

**Solução:** Verifique se está usando CSS Modules corretamente:
```tsx
// ✅ CSS Modules
import styles from './Component.module.css';
<div className={styles.container} />
```

### TypeScript errors

**Solução:** Adicione tipos para props:
```tsx
export interface Props {
  // defina suas props aqui
}
```

---

## 📚 Recursos Adicionais

- [Documentação Figma Make](https://www.figma.com/community/plugin/figma-make)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

---

## 💡 Dicas

1. **Organize por Feature:** Agrupe componentes relacionados em pastas
2. **Reutilize:** Extraia componentes comuns para `components/common/`
3. **Mantenha Consistência:** Use um sistema de design (ex: Tailwind, CSS Modules)
4. **Teste Responsivo:** Sempre teste em diferentes tamanhos de tela
5. **Performance:** Otimize imagens e use lazy loading quando possível

---

**Pronto!** Agora você pode adicionar qualquer design do Figma Make ao projeto! 🎉
