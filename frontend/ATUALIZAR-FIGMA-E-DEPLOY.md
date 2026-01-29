# Atualizar landing do Figma e fazer deploy

## 1. Sincronizar o novo design do Figma com o código

Você refez a landing no Figma. Para eu (ou o Cursor) atualizar o frontend a partir do novo design:

**Opção A – Enviar o link do frame**
- No Figma, clique com o botão direito no frame da **Landing** (a página inteira).
- Escolha **"Copy link to selection"** (ou "Copiar link").
- O link deve ter o formato: `https://www.figma.com/design/kYaKQo5HILal0lD7HEcGcN/NomeDoArquivo?node-id=123-456`
- Envie esse link aqui; com o `node-id` dá para puxar o design e sugerir/gerar o código.

**Opção B – Exportar código do Figma**
- Use um plugin no Figma (ex.: Figma to Code, Anima, etc.) para gerar HTML/CSS ou React.
- Copie os componentes gerados para `frontend/components/figma/` e adapte para Next.js/React (imports, rotas, etc.).

**Componentes atuais da landing (para substituir/ajustar):**
- `Header.tsx`
- `HeroSection.tsx`
- `ProblemOpportunitySection.tsx`
- `ComoFuncionaSection.tsx`
- `WhySection.tsx`
- `EmBreveSection.tsx`
- `FinalCTA.tsx`
- `Footer.tsx`

A página que monta tudo é `app/page.tsx`.

---

## 2. Fazer o deploy

O **build** do frontend está passando (Tailwind foi ajustado para v3 para compatibilidade com o tema).

### Se o projeto já está conectado ao Vercel (GitHub)

1. Faça commit e push das alterações:
   ```bash
   git add .
   git commit -m "Landing atualizada, build corrigido"
   git push origin main
   ```
2. O Vercel faz o deploy automático. Confira em [vercel.com](https://vercel.com) no seu projeto.
3. No projeto Vercel, confira se o **Root Directory** está como `frontend` (e não a raiz do repositório).

### Se ainda não conectou ao Vercel

1. Acesse [vercel.com](https://vercel.com) e faça login.
2. **Add New Project** → importe o repositório do GitHub.
3. Em **Root Directory** escolha: `frontend`.
4. Em **Environment Variables** (se o frontend chamar uma API):  
   `NEXT_PUBLIC_API_URL` = URL do backend (ex.: `https://seu-backend.railway.app`).
5. Clique em **Deploy**. Os próximos deploys serão automáticos a cada push na branch conectada.

### Deploy manual pelo CLI

1. Instale e faça login no Vercel:
   ```bash
   npm i -g vercel
   vercel login
   ```
2. Na pasta do frontend:
   ```bash
   cd frontend
   vercel --prod
   ```
3. Siga as perguntas (projeto novo ou existente, etc.). No primeiro deploy pode ser preciso linkar o projeto ao time/conta.

---

## 3. O que foi ajustado no projeto

- **Tailwind:** O projeto usava Tailwind v4 com PostCSS antigo; o build quebrava. Foi rebaixado para **Tailwind v3** no frontend para o build passar com o `globals.css` e o tema atuais.
- **Build:** `npm run build` na pasta `frontend` está passando.

Se quiser migrar de volta para Tailwind v4 no futuro, será preciso:
- Usar `@tailwindcss/postcss` e `@import "tailwindcss"` no CSS.
- Ajustar o tema (variáveis como `border-border`) para o formato do Tailwind v4 ou definir em `@theme` no CSS.
