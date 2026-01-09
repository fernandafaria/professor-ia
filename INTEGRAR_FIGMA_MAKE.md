# 🎨 Como Adicionar Frontend do Figma Make

Este guia explica como adicionar o frontend criado no **Figma Make** ao projeto P1A.

---

## 📋 Pré-requisitos

- Node.js 18+ instalado
- NPM ou Yarn instalado
- Código gerado pelo Figma Make

---

## 🚀 Passo a Passo Rápido

### 1. Instalar Dependências do Frontend

```bash
cd /Users/fernandafaria/Downloads/P1A/frontend
npm install
```

### 2. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
```

Edite o `.env`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Adicionar Código do Figma Make

#### Opção A: Componente Individual

1. **Gere o código no Figma Make:**
   - Abra seu design no Figma
   - Use o plugin Figma Make
   - Selecione o componente/frame
   - Gere código React/Next.js

2. **Adicione ao projeto:**
   ```bash
   # Crie o arquivo do componente
   touch frontend/components/figma/MeuComponente.tsx
   ```

3. **Cole o código gerado** no arquivo criado

4. **Ajuste imports:**
   - Use `@/` para paths absolutos
   - Mova assets para `public/assets/`

#### Opção B: Página Completa

1. **Gere a página no Figma Make**

2. **Adicione em `app/`:**
   ```bash
   # Exemplo: página de landing
   mkdir -p frontend/app/landing
   touch frontend/app/landing/page.tsx
   ```

3. **Cole o código** e ajuste conforme necessário

### 4. Iniciar o Frontend

```bash
cd frontend
npm run dev
```

Acesse: http://localhost:3000

---

## 📁 Estrutura de Pastas

```
frontend/
├── components/
│   └── figma/              # 👈 Adicione componentes do Figma Make aqui
│       ├── Button.tsx
│       ├── Card.tsx
│       └── ...
├── app/                     # 👈 Ou adicione páginas completas aqui
│   ├── landing/
│   │   └── page.tsx
│   └── ...
├── public/
│   └── assets/             # 👈 Coloque imagens/ícones aqui
│       ├── images/
│       └── icons/
└── lib/
    └── api.ts              # Cliente para conectar com backend
```

---

## 🔧 Ajustes Necessários

### 1. Imports

**Antes (gerado pelo Figma):**
```tsx
import './styles.css';
import icon from './assets/icon.svg';
```

**Depois (ajustado):**
```tsx
import styles from './Component.module.css';
import icon from '/assets/icons/icon.svg';
```

### 2. Assets

Mova imagens/ícones para:
```
public/assets/images/
public/assets/icons/
```

E use paths absolutos:
```tsx
<img src="/assets/images/logo.png" alt="Logo" />
```

### 3. Conectar com Backend

Use o cliente API:
```tsx
import { api } from '@/lib/api';

// Exemplo: Login
const response = await api.login(email, password);
```

---

## 📚 Documentação Completa

Para instruções detalhadas, veja:
- **[frontend/GUIA_FIGMA_MAKE.md](./frontend/GUIA_FIGMA_MAKE.md)** - Guia completo de integração

---

## ✅ Checklist

- [ ] Dependências instaladas (`npm install`)
- [ ] `.env` configurado
- [ ] Código do Figma Make adicionado
- [ ] Imports ajustados
- [ ] Assets movidos para `public/assets/`
- [ ] Frontend rodando (`npm run dev`)
- [ ] Backend rodando (`uvicorn app.main:app --reload`)
- [ ] Testado localmente

---

## 🆘 Problemas Comuns

### Erro: "Module not found"
**Solução:** Ajuste imports para usar `@/` ou paths relativos corretos

### Imagens não aparecem
**Solução:** Use paths absolutos começando com `/` (ex: `/assets/images/logo.png`)

### Erro de conexão com backend
**Solução:** Verifique se o backend está rodando em `http://localhost:8000`

---

**Pronto!** Seu frontend do Figma Make está integrado! 🎉
