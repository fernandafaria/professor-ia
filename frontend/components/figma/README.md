# Componentes do Figma

Esta pasta contém componentes React gerados a partir de designs do Figma.

## Estrutura

```
components/figma/
├── README.md                    # Este arquivo
├── Button.tsx                   # Componentes individuais
├── Button.module.css
├── LoginForm.tsx
├── LoginForm.module.css
└── ...
```

## Como Adicionar um Novo Componente

1. **Extraia o código do Figma** (via Cursor MCP, Figma Make ou manual)
2. **Crie o arquivo** neste diretório: `MeuComponente.tsx`
3. **Crie o CSS** (se necessário): `MeuComponente.module.css`
4. **Ajuste imports** para usar `@/` (paths absolutos)
5. **Integre com backend** usando `api` de `@/lib/api`

## Exemplo de Uso

```tsx
// Em uma página
import LoginForm from '@/components/figma/LoginForm';

export default function LoginPage() {
  return <LoginForm />;
}
```

## Documentação

- Ver [COMO-INTEGRAR-FIGMA-COM-BACKEND.md](../../../COMO-INTEGRAR-FIGMA-COM-BACKEND.md)
- Ver [EXEMPLO-USO-FIGMA-MCP.md](../../../EXEMPLO-USO-FIGMA-MCP.md)
