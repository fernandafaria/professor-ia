# 🎨 Como Integrar Frontend do Figma com o Backend

Este guia explica passo a passo como trazer seu design do Figma para o frontend Next.js e conectá-lo com o backend FastAPI.

---

## 📋 Pré-requisitos

- ✅ Design criado no Figma
- ✅ Backend FastAPI rodando (porta 8000)
- ✅ Frontend Next.js configurado
- ✅ Cursor com acesso ao MCP do Figma (opcional, mas recomendado)

---

## 🚀 Passo a Passo Completo

### **Etapa 1: Obter o Código do Figma**

Você tem **3 opções** para obter o código do seu design:

#### **Opção A: Usar o MCP do Figma no Cursor (Recomendado)** ⭐

O Cursor já tem integração com Figma via MCP! Siga estes passos:

1. **No Cursor, abra o chat**
2. **Compartilhe a URL do seu design do Figma:**
   ```
   https://figma.com/design/[SEU_FILE_KEY]/[NOME_DO_ARQUIVO]?node-id=[NODE_ID]
   ```
   
3. **Peça para extrair o código:**
   ```
   Extraia o código React/Next.js deste frame do Figma: [URL]
   ```

4. **O Cursor vai gerar o componente automaticamente!** 🎉

#### **Opção B: Usar o Plugin Figma Make**

1. Abra seu design no Figma
2. Vá em **Plugins** → **Figma Make**
3. Selecione o frame/componente
4. Configure:
   - Framework: **React/Next.js**
   - Language: **TypeScript**
   - Style: **CSS Modules** (ou Tailwind)
5. Clique em **"Generate Code"**
6. Copie o código gerado

#### **Opção C: Exportar Manualmente**

1. Selecione o frame no Figma
2. Use **Dev Mode** para ver propriedades CSS
3. Recrie os componentes manualmente no código

---

### **Etapa 2: Adicionar o Componente ao Frontend**

#### **2.1. Criar a Estrutura de Pastas**

```bash
cd /Users/fernandafaria/Downloads/P1A/frontend

# Criar pasta para componentes do Figma
mkdir -p components/figma
mkdir -p public/assets/images
mkdir -p public/assets/icons
```

#### **2.2. Criar o Componente**

**Exemplo:** Vamos criar um componente `LoginForm` gerado do Figma:

```bash
touch components/figma/LoginForm.tsx
```

Cole o código gerado do Figma. Exemplo:

```tsx
// components/figma/LoginForm.tsx
'use client';

import { useState } from 'react';
import { api } from '@/lib/api';

export default function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // Conectar com o backend
      const response = await api.login(email, password);
      
      // Salvar token
      localStorage.setItem('token', response.access_token);
      
      // Redirecionar para dashboard
      window.location.href = '/dashboard';
    } catch (err: any) {
      setError(err.message || 'Erro ao fazer login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="login-form">
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="password">Senha</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      {error && <div className="error-message">{error}</div>}

      <button type="submit" disabled={loading}>
        {loading ? 'Entrando...' : 'Entrar'}
      </button>
    </form>
  );
}
```

#### **2.3. Ajustar Imports e Assets**

**Imports:** Use paths absolutos com `@/`:

```tsx
// ✅ Correto
import { api } from '@/lib/api';
import Image from 'next/image';
import logo from '/assets/images/logo.png';

// ❌ Evite paths relativos longos
import { api } from '../../../lib/api';
```

**Imagens:** Coloque em `public/assets/` e use paths absolutos:

```tsx
// ✅ Correto
<img src="/assets/images/hero-bg.png" alt="Hero" />

// ❌ Evite
<img src="./assets/hero-bg.png" />
```

---

### **Etapa 3: Criar Estilos (CSS)**

Você pode usar **CSS Modules** ou **Tailwind**. Exemplo com CSS Modules:

```css
/* components/figma/LoginForm.module.css */
.loginForm {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
}

.formGroup {
  margin-bottom: 1.5rem;
}

.formGroup label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.formGroup input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.errorMessage {
  color: red;
  margin-bottom: 1rem;
}

button {
  width: 100%;
  padding: 0.75rem;
  background: #0070f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

Depois importe no componente:

```tsx
import styles from './LoginForm.module.css';
// ... use styles.loginForm, etc.
```

---

### **Etapa 4: Integrar com o Backend**

#### **4.1. Usar o Cliente API**

O projeto já tem um cliente API em `lib/api.ts`. Use assim:

```tsx
import { api } from '@/lib/api';

// Login
const response = await api.login(email, password);

// Criar perfil
const profile = await api.createProfile({
  name: 'João',
  role: 'teacher'
});

// Obter conversas
const conversations = await api.getConversations();

// Enviar mensagem
await api.sendMessage(conversationId, 'Olá!');
```

#### **4.2. Exemplo Completo: Componente com Dados do Backend**

```tsx
// components/figma/ConversationList.tsx
'use client';

import { useEffect, useState } from 'react';
import { api } from '@/lib/api';

interface Conversation {
  id: string;
  title: string;
  created_at: string;
}

export default function ConversationList() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadConversations();
  }, []);

  const loadConversations = async () => {
    try {
      const data = await api.getConversations();
      setConversations(data);
    } catch (err: any) {
      setError(err.message || 'Erro ao carregar conversas');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Carregando...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="conversation-list">
      <h2>Minhas Conversas</h2>
      {conversations.map((conv) => (
        <div key={conv.id} className="conversation-item">
          <h3>{conv.title}</h3>
          <p>{new Date(conv.created_at).toLocaleDateString()}</p>
        </div>
      ))}
    </div>
  );
}
```

---

### **Etapa 5: Usar na Página**

#### **5.1. Criar uma Página**

```tsx
// app/login/page.tsx
import LoginForm from '@/components/figma/LoginForm';

export default function LoginPage() {
  return (
    <main>
      <h1>Login</h1>
      <LoginForm />
    </main>
  );
}
```

#### **5.2. Ou Atualizar a Página Principal**

```tsx
// app/page.tsx
import LoginForm from '@/components/figma/LoginForm';
import ConversationList from '@/components/figma/ConversationList';

export default function Home() {
  return (
    <main>
      <LoginForm />
      <ConversationList />
    </main>
  );
}
```

---

### **Etapa 6: Configurar Variáveis de Ambiente**

Certifique-se de que o frontend está configurado para conectar com o backend:

```bash
# frontend/.env.local (crie se não existir)
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

### **Etapa 7: Testar**

#### **7.1. Iniciar o Backend**

```bash
cd /Users/fernandafaria/Downloads/P1A/backend
uvicorn app.main:app --reload
```

Verifique: http://localhost:8000/docs

#### **7.2. Iniciar o Frontend**

```bash
cd /Users/fernandafaria/Downloads/P1A/frontend
npm install  # se ainda não instalou
npm run dev
```

Acesse: http://localhost:3000

#### **7.3. Testar a Integração**

1. Abra o navegador em http://localhost:3000
2. Teste o login (ou qualquer ação que conecta com o backend)
3. Abra o Console do Navegador (F12) para ver erros
4. Verifique se as requisições estão sendo feitas no Network tab

---

## 📁 Estrutura Final Recomendada

```
frontend/
├── components/
│   └── figma/                    # Componentes do Figma
│       ├── LoginForm.tsx
│       ├── LoginForm.module.css
│       ├── ConversationList.tsx
│       └── ...
├── app/
│   ├── page.tsx                  # Página principal
│   ├── login/
│   │   └── page.tsx              # Página de login
│   ├── dashboard/
│   │   └── page.tsx              # Dashboard
│   └── layout.tsx
├── public/
│   └── assets/                   # Assets do Figma
│       ├── images/
│       └── icons/
├── lib/
│   └── api.ts                    # Cliente API (já existe)
└── .env.local                    # Configurações
```

---

## 🔗 Endpoints do Backend Disponíveis

Baseado no `main.py`, você pode usar:

### Autenticação
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/auth/register` - Registro
- `GET /api/v1/auth/me` - Usuário atual

### Perfil
- `GET /api/v1/profile` - Listar perfis
- `POST /api/v1/profile` - Criar perfil
- `PUT /api/v1/profile/{id}` - Atualizar perfil

### Conversas
- `GET /api/v1/conversations` - Listar conversas
- `POST /api/v1/conversations` - Criar conversa
- `GET /api/v1/conversations/{id}` - Obter conversa

### Mensagens
- `POST /api/v1/conversations/{id}/messages` - Enviar mensagem
- `GET /api/v1/conversations/{id}/messages` - Listar mensagens

---

## ✅ Checklist de Integração

- [ ] Código do Figma obtido (via MCP, Figma Make ou manual)
- [ ] Componente criado em `components/figma/`
- [ ] Estilos criados (CSS Modules ou Tailwind)
- [ ] Assets movidos para `public/assets/`
- [ ] Imports ajustados (usar `@/`)
- [ ] Integração com backend usando `api` de `lib/api.ts`
- [ ] Variáveis de ambiente configuradas (`.env.local`)
- [ ] Página criada/atualizada para usar o componente
- [ ] Backend rodando (porta 8000)
- [ ] Frontend rodando (porta 3000)
- [ ] Testado no navegador
- [ ] Console sem erros

---

## 🆘 Problemas Comuns e Soluções

### ❌ Erro: "Cannot connect to backend"

**Solução:**
1. Verifique se o backend está rodando: `curl http://localhost:8000/health`
2. Verifique o `.env.local`: `NEXT_PUBLIC_API_URL=http://localhost:8000`
3. Verifique CORS no backend (já configurado, mas confirme)

### ❌ Erro: "Module not found"

**Solução:**
```bash
# Reinstalar dependências
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### ❌ Imagens não aparecem

**Solução:**
- Use paths absolutos: `/assets/images/logo.png`
- Coloque imagens em `public/assets/`
- Reinicie o servidor Next.js

### ❌ Erro de autenticação (401)

**Solução:**
- Verifique se o token está sendo salvo: `localStorage.getItem('token')`
- Verifique se o token está sendo enviado no header
- Faça login novamente

---

## 💡 Dicas Finais

1. **Use o MCP do Figma no Cursor** para extrair código automaticamente
2. **Teste componente por componente** antes de integrar tudo
3. **Mantenha o design consistente** - use um sistema de design
4. **Trate erros** - sempre mostre feedback ao usuário
5. **Teste em diferentes tamanhos** de tela (responsivo)

---

## 🎯 Próximos Passos

1. ✅ Integrar mais componentes do Figma
2. ✅ Adicionar tratamento de erros global
3. ✅ Implementar loading states
4. ✅ Adicionar testes
5. ✅ Otimizar performance (lazy loading, code splitting)

---

**Pronto!** Agora você sabe como trazer qualquer design do Figma para o frontend e conectá-lo com o backend! 🎉

Se tiver dúvidas, pergunte no chat do Cursor ou consulte a documentação:
- [Guia Figma Make](./frontend/GUIA_FIGMA_MAKE.md)
- [Documentação Next.js](https://nextjs.org/docs)
- [Documentação FastAPI](https://fastapi.tiangolo.com/)
