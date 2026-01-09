# Frontend - P1A

Frontend da plataforma educacional P1A, construído com Next.js e TypeScript.

## 🚀 Início Rápido

### 1. Instalar Dependências

```bash
cd frontend
npm install
```

### 2. Configurar Variáveis de Ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Edite o `.env` e configure:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Iniciar Servidor de Desenvolvimento

```bash
npm run dev
```

O frontend estará disponível em: http://localhost:3000

## 📁 Estrutura do Projeto

```
frontend/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Layout principal
│   ├── page.tsx           # Página inicial
│   └── ...
├── components/             # Componentes React
│   ├── figma/            # Componentes gerados pelo Figma Make
│   └── ...
├── lib/                   # Utilitários e configurações
│   ├── api.ts            # Cliente API para backend
│   └── ...
├── public/                # Arquivos estáticos
└── styles/               # Estilos globais
```

## 🎨 Integração com Figma Make

Veja o guia completo em: [GUIA_FIGMA_MAKE.md](./GUIA_FIGMA_MAKE.md)

### Resumo Rápido

1. **Gerar código no Figma Make:**
   - Abra seu design no Figma
   - Use o Figma Make para gerar código React/Next.js
   - Copie o código gerado

2. **Adicionar ao projeto:**
   - Coloque componentes em `components/figma/`
   - Coloque páginas em `app/` (se necessário)
   - Ajuste imports e paths conforme necessário

3. **Conectar com Backend:**
   - Use o cliente API em `lib/api.ts`
   - Configure endpoints conforme necessário

## 🔌 Conectando com o Backend

O frontend está configurado para se conectar ao backend FastAPI em `http://localhost:8000`.

### Exemplo de Uso da API

```typescript
import { api } from '@/lib/api';

// Exemplo: Login
const response = await api.post('/auth/login', {
  email: 'user@example.com',
  password: 'password'
});
```

## 📚 Documentação

- [Guia de Integração Figma Make](./GUIA_FIGMA_MAKE.md)
- [Estrutura de Componentes](./docs/COMPONENTES.md)
- [API Client](./docs/API.md)
