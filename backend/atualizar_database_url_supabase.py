#!/usr/bin/env python3
"""
Script para atualizar DATABASE_URL no .env com informações do Supabase.
Usa informações obtidas via MCP do Supabase.
"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

def update_database_url(password: str = None):
    """Atualiza DATABASE_URL no arquivo .env."""
    
    # Informações obtidas via MCP Supabase
    project_ref = "mzhgkbdnslnlpfciduru"
    project_url = "mzhgkbdnslnlpfciduru.supabase.co"
    
    # Carregar .env atual
    env_path = Path(".env")
    if not env_path.exists():
        print("❌ Arquivo .env não encontrado!")
        return False
    
    # Ler conteúdo atual
    with open(env_path, 'r') as f:
        content = f.read()
    
    # Construir nova URL
    if password:
        # Formato: postgresql://postgres.[PROJECT-REF]:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres
        new_url = f"postgresql://postgres.{project_ref}:{password}@db.{project_ref}.supabase.co:5432/postgres"
        
        # Atualizar ou adicionar DATABASE_URL
        if re.search(r'^DATABASE_URL=', content, re.MULTILINE):
            # Substituir existente
            content = re.sub(
                r'^DATABASE_URL=.*$',
                f'DATABASE_URL={new_url}',
                content,
                flags=re.MULTILINE
            )
            print(f"✅ DATABASE_URL atualizado")
        else:
            # Adicionar novo
            content += f"\nDATABASE_URL={new_url}\n"
            print(f"✅ DATABASE_URL adicionado")
        
        # Salvar
        with open(env_path, 'w') as f:
            f.write(content)
        
        print(f"\n📝 DATABASE_URL configurado:")
        print(f"   postgresql://postgres.{project_ref}:***@db.{project_ref}.supabase.co:5432/postgres")
        
        return True
    else:
        print("⚠️  Senha não fornecida")
        print("\n📋 Informações do projeto Supabase:")
        print(f"   Project Ref: {project_ref}")
        print(f"   Project URL: {project_url}")
        print(f"\n🔐 Para obter a senha do banco:")
        print(f"   1. Acesse: https://app.supabase.com/project/{project_ref}/settings/database")
        print(f"   2. Role até 'Connection string'")
        print(f"   3. Selecione 'URI' mode")
        print(f"   4. Copie a senha (parte após 'postgres.' e antes de '@')")
        print(f"\n💡 Ou use a Connection String completa:")
        print(f"   - Copie a Connection String (URI mode)")
        print(f"   - Cole aqui quando executar: python3 atualizar_database_url_supabase.py [SENHA]")
        print(f"\n📝 Formato esperado:")
        print(f"   postgresql://postgres.{project_ref}:[SENHA]@db.{project_ref}.supabase.co:5432/postgres")
        
        return False

def main():
    import sys
    
    print("🔧 Atualizar DATABASE_URL para Supabase")
    print("=" * 60)
    print()
    
    # Verificar se senha foi fornecida como argumento
    password = None
    if len(sys.argv) > 1:
        password = sys.argv[1]
        if password.startswith("postgresql://"):
            # Se forneceu URL completa, extrair senha
            match = re.search(r'postgres\.([^:]+):([^@]+)@', password)
            if match:
                password = match.group(2)
            else:
                print("❌ Formato de URL inválido")
                return 1
    
    # Tentar atualizar
    success = update_database_url(password)
    
    if success:
        print("\n✅ DATABASE_URL atualizado com sucesso!")
        print("\n🧪 Testar conexão:")
        print("   python3 verificar_supabase.py")
        return 0
    else:
        print("\n💡 Execute novamente com a senha:")
        print("   python3 atualizar_database_url_supabase.py [SENHA]")
        return 1

if __name__ == "__main__":
    sys.exit(main())
