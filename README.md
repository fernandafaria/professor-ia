# 🎓 Plataforma Educacional P1A - Professor IA

Plataforma educacional hiper-personalizada para estudantes brasileiros, utilizando **IA generativa** para criar professores virtuais personalizados que adaptam o ensino aos interesses e necessidades de cada aluno.

---

## 🎯 Visão do Projeto

A **Professor IA** é uma plataforma inovadora que permite aos estudantes criar seu próprio professor virtual personalizado. O sistema utiliza **RAG (Retrieval-Augmented Generation)** e **IA generativa** para contextualizar conteúdo curricular através dos interesses pessoais dos alunos (games, futebol, música, etc.).

### ✨ Diferenciais

- 🎮 **Gamificação**: Sistema de XP, níveis e badges
- 🧠 **IA Personalizada**: Professor virtual que aprende com o aluno
- 📚 **Todas as Matérias**: Matemática, Física, Química, Português, História, etc.
- ⚡ **Sessões Rápidas**: 8-15 minutos, perfeito para encaixar no dia a dia
- 🎯 **Hiper-personalização**: Adapta estilo de ensino à personalidade do aluno

### 🎨 Design

Landing page completa integrada do Figma com design moderno e responsivo.

---

## 🚀 Quick Start

### **Pré-requisitos**

- Python 3.10+
- Node.js 18+ (para frontend)
- PostgreSQL (ou Supabase)
- Conta no Supabase (recomendado)

### **Instalação Rápida**

```bash
# 1. Clone o repositório
git clone <repository-url>
cd P1A

# 2. Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure variáveis de ambiente
cp env.example .env
# Edite .env com suas credenciais

# 4. Frontend
cd ../frontend
npm install

# 5. Configure variáveis de ambiente
# Crie .env.local com:
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

### **Executar Localmente**

```bash
# Terminal 1: Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm run dev
```

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

---

## 📁 Estrutura do Projeto

```
P1A/
├── backend/              # Backend FastAPI (Python)
│   ├── app/             # Aplicação principal
│   │   ├── api/        # Endpoints da API
│   │   ├── models/     # Modelos de dados
│   │   ├── schemas/    # Schemas Pydantic
│   │   ├── core/       # Lógica de negócio (RAG, personalização)
│   │   └── services/   # Serviços (auth, LLM, database)
│   ├── scraping/       # Sistema de web scraping
│   └── requirements.txt
│
├── frontend/            # Frontend Next.js (TypeScript/React)
│   ├── app/            # Next.js App Router
│   ├── components/     # Componentes React
│   │   └── figma/     # Componentes do design Figma
│   └── lib/            # Utilitários (API client)
│
├── docs/               # Documentação
└── README.md           # Este arquivo
```

---

## 🛠️ Tecnologias

### **Backend**
- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM
- **Supabase** - Banco de dados PostgreSQL + pgvector
- **Anthropic Claude** - LLM para geração de conteúdo
- **LangChain** - Framework RAG
- **Sentence Transformers** - Embeddings

### **Frontend**
- **Next.js 14** - Framework React
- **TypeScript** - Tipagem estática
- **React** - Biblioteca UI
- **Design do Figma** - Componentes integrados

---

## 📚 Documentação

### **Setup e Configuração**
- **[DEPLOY-ONLINE.md](./DEPLOY-ONLINE.md)** - Como fazer deploy online
- **[DEPLOY-RAPIDO.md](./DEPLOY-RAPIDO.md)** - Quick start para deploy
- **[CHECKLIST-PRE-DEPLOY.md](./CHECKLIST-PRE-DEPLOY.md)** - Checklist antes de deploy

### **Design e Frontend**
- **[DESIGN-FIGMA-COMPLETO-INTEGRADO.md](./DESIGN-FIGMA-COMPLETO-INTEGRADO.md)** - Design do Figma integrado
- **[COMO-INTEGRAR-FIGMA-COM-BACKEND.md](./COMO-INTEGRAR-FIGMA-COM-BACKEND.md)** - Guia de integração
- **[GUIA-COMPLETO-ASSETS-FIGMA.md](./GUIA-COMPLETO-ASSETS-FIGMA.md)** - Como extrair assets

### **Backend e API**
- **[backend/CONFIGURAR-CHAT-RAG.md](./backend/CONFIGURAR-CHAT-RAG.md)** - Configuração RAG
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Arquitetura técnica

---

## 🌐 Deploy Online

### **Opção Recomendada: Vercel + Railway**

1. **Frontend no Vercel:**
   - Conecte repositório GitHub
   - Root Directory: `frontend`
   - Configure `NEXT_PUBLIC_API_URL`

2. **Backend no Railway:**
   - Conecte repositório GitHub
   - Root Directory: `backend`
   - Configure variáveis de ambiente

**Veja guia completo:** [DEPLOY-ONLINE.md](./DEPLOY-ONLINE.md)

---

## 🔐 Variáveis de Ambiente

### **Backend (.env)**
```env
DATABASE_URL=postgresql://...  # URL do Supabase
SECRET_KEY=sua-chave-secreta
ANTHROPIC_API_KEY=sk-ant-...
CORS_ORIGINS=http://localhost:3000,https://seu-frontend.vercel.app
```

### **Frontend (.env.local)**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000  # Ou URL do backend deployado
```

---

## 🎨 Design do Figma

O design completo da landing page foi integrado do Figma:

- ✅ Header com logo e login
- ✅ Hero section com CTA
- ✅ Seções de features
- ✅ CTA final
- ✅ Footer

**Componentes:** `frontend/components/figma/`

---

## 📝 Funcionalidades

### **MVP Implementado**
- ✅ Autenticação (registro/login)
- ✅ Perfil do professor
- ✅ Sistema de conversas
- ✅ Mensagens com IA
- ✅ Landing page completa

### **Em Desenvolvimento**
- 🔄 Sistema RAG completo
- 🔄 Gamificação (XP, níveis, badges)
- 🔄 Personalização avançada
- 🔄 Integração com múltiplas matérias

---

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob licença proprietária.

---

## 📞 Contato

Para dúvidas ou suporte, consulte a documentação em `docs/` ou abra uma issue.

---

**Última Atualização:** 2026-01-09  
**Versão:** 1.0.0
