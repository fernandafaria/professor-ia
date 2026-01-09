#!/usr/bin/env python3
"""
Script para ajudar a obter/configurar a Database URL do Supabase.
"""

import sys

# Informações do projeto (obtidas via MCP)
PROJECT_REF = "mzhgkbdnslnlpfciduru"
PROJECT_URL = "https://mzhgkbdnslnlpfciduru.supabase.co"

print("=" * 60)
print("🔗 Configuração da Database URL do Supabase")
print("=" * 60)
print()
print(f"📋 Seu projeto: {PROJECT_REF}")
print(f"🌐 URL: {PROJECT_URL}")
print()
print("=" * 60)
print("📝 PASSO A PASSO:")
print("=" * 60)
print()
print("1. Acesse o Supabase Dashboard:")
print(f"   👉 {PROJECT_URL.replace('.supabase.co', '.supabase.com')}")
print()
print("2. No menu lateral, clique em: ⚙️ Settings")
print()
print("3. Clique em: Database")
print()
print("4. Role até encontrar: 'Connection string'")
print()
print("5. Selecione a aba: 'Pooler' (recomendado)")
print()
print("6. Selecione: 'Transaction mode'")
print()
print("7. Copie a URL que aparece")
print()
print("=" * 60)
print("🔑 IMPORTANTE - A URL vem assim:")
print("=" * 60)
print()
print("postgresql://postgres.mzhgkbdnslnlpfciduru:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres")
print()
print("⚠️  Você precisa substituir [YOUR-PASSWORD] pela senha do banco!")
print()
print("=" * 60)
print("❓ Esqueceu a senha?")
print("=" * 60)
print()
print("1. No mesmo lugar (Settings → Database)")
print("2. Role até 'Database password'")
print("3. Clique em 'Reset database password'")
print("4. Anote a nova senha (ela só aparece uma vez!)")
print()
print("=" * 60)
print("💻 Depois de copiar, configure no .env:")
print("=" * 60)
print()
print("Edite: backend/.env")
print()
print("E adicione:")
print("DATABASE_URL=postgresql://postgres.mzhgkbdnslnlpfciduru:SUA_SENHA@aws-0-sa-east-1.pooler.supabase.com:5432/postgres")
print()
print("=" * 60)
print("✅ Testar conexão:")
print("=" * 60)
print()
print("python3 -c \"from app.config import settings; from sqlalchemy import create_engine, text; engine = create_engine(settings.DATABASE_URL); conn = engine.connect(); print('✅ OK!')\"")
print()
print("=" * 60)

# Tentar construir URL se senha for fornecida
if len(sys.argv) > 1:
    password = sys.argv[1]
    region = sys.argv[2] if len(sys.argv) > 2 else "sa-east-1"
    
    url_pooler = f"postgresql://postgres.{PROJECT_REF}:{password}@aws-0-{region}.pooler.supabase.com:5432/postgres"
    url_direct = f"postgresql://postgres.{PROJECT_REF}:{password}@db.{PROJECT_REF}.supabase.co:5432/postgres"
    
    print()
    print("=" * 60)
    print("🔗 URLs Geradas:")
    print("=" * 60)
    print()
    print("Para Aplicação (Pooler):")
    print(url_pooler)
    print()
    print("Para Migrations (Direct):")
    print(url_direct)
    print()
    print("=" * 60)
    print("💾 Copie uma das URLs acima para o arquivo .env")
    print("=" * 60)
