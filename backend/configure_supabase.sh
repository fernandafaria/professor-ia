#!/bin/bash

# Script de configuração do Supabase para o projeto P1A

echo "🚀 Configuração do Supabase para P1A Backend"
echo ""

# Verificar se .env existe
if [ ! -f .env ]; then
    echo "📝 Criando arquivo .env a partir de env.example..."
    cp env.example .env
fi

echo "📋 Para configurar o Supabase, você precisa:"
echo ""
echo "1. Criar um projeto em: https://supabase.com"
echo "2. Obter a Connection String em: Settings → Database → Connection string"
echo "3. Editar o arquivo .env e atualizar DATABASE_URL"
echo ""
echo "📝 Formato da URL do Supabase:"
echo "   postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres"
echo ""
echo "💡 Dica: Use Connection Pooling para produção (recomendado)"
echo ""
read -p "Você já tem a Connection String do Supabase? (s/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "Cole a Connection String abaixo (ou pressione Enter para pular):"
    read -r SUPABASE_URL
    
    if [ ! -z "$SUPABASE_URL" ]; then
        # Atualizar DATABASE_URL no .env
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            sed -i '' "s|^DATABASE_URL=.*|DATABASE_URL=$SUPABASE_URL|" .env
        else
            # Linux
            sed -i "s|^DATABASE_URL=.*|DATABASE_URL=$SUPABASE_URL|" .env
        fi
        
        echo "✅ DATABASE_URL atualizado no arquivo .env"
        echo ""
        echo "📋 Próximos passos:"
        echo "   1. Execute: alembic upgrade head"
        echo "   2. Inicie o servidor: uvicorn app.main:app --reload"
    else
        echo "⚠️  URL não fornecida. Você pode editar o arquivo .env manualmente."
    fi
else
    echo "📖 Consulte o guia completo em: SETUP_SUPABASE.md"
fi

echo ""
echo "✅ Configuração concluída!"
