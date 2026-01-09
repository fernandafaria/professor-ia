"""
Script de verificação rápida do setup para RAG.
Verifica se tudo está configurado corretamente antes de popular o RAG.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Carregar variáveis de ambiente do arquivo .env
env_path = Path(__file__).parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
# Também tentar carregar do backend/.env
backend_env = Path(__file__).parent.parent.parent / "backend" / ".env"
if backend_env.exists():
    load_dotenv(backend_env)

def check_environment():
    """Verifica variáveis de ambiente."""
    print("🔍 Verificando variáveis de ambiente...")
    
    checks = {
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),  # Supabase connection string
        "SECRET_KEY": os.getenv("SECRET_KEY"),
    }
    
    all_ok = True
    for key, value in checks.items():
        if value:
            print(f"  ✅ {key}: Configurada")
        else:
            print(f"  ⚠️  {key}: Não configurada")
            all_ok = False
    
    return all_ok

def check_dependencies():
    """Verifica dependências instaladas."""
    print("\n🔍 Verificando dependências...")
    
    dependencies = [
        ("firecrawl", "firecrawl-py"),  # firecrawl-py instala módulo firecrawl
        ("sqlalchemy", "sqlalchemy"),  # Para Supabase/PostgreSQL
        ("psycopg2", "psycopg2-binary"),  # Driver PostgreSQL
        ("sentence_transformers", "sentence-transformers"),
        ("langchain", "langchain"),
        ("bs4", "beautifulsoup4"),  # beautifulsoup4 instala módulo bs4
    ]
    
    all_ok = True
    for module_name, package_name in dependencies:
        try:
            __import__(module_name)
            print(f"  ✅ {package_name}: Instalado")
        except ImportError:
            print(f"  ❌ {package_name}: Não instalado")
            print(f"     Instale com: pip install {package_name}")
            all_ok = False
    
    return all_ok

def check_supabase():
    """Verifica se Supabase está acessível e tabela rag_documents existe."""
    print("\n🔍 Verificando Supabase...")
    
    try:
        from sqlalchemy import create_engine, text
        from app.config import settings
        
        # Tentar conectar ao banco
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as conn:
            # Verificar se tabela rag_documents existe
            result = conn.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'rag_documents'
                )
            """))
            table_exists = result.scalar()
            
            if table_exists:
                # Verificar se pgvector está instalado
                result = conn.execute(text("""
                    SELECT EXISTS (
                        SELECT FROM pg_extension 
                        WHERE extname = 'vector'
                    )
                """))
                pgvector_installed = result.scalar()
                
                if pgvector_installed:
                    # Contar documentos
                    result = conn.execute(text("SELECT COUNT(*) FROM rag_documents"))
                    count = result.scalar()
                    
                    print(f"  ✅ Supabase: Conectado")
                    print(f"  ✅ Tabela rag_documents: Existe")
                    print(f"  ✅ pgvector: Instalado")
                    print(f"  ✅ Documentos: {count}")
                    return True
                else:
                    print(f"  ⚠️  Supabase: Conectado, mas pgvector não está instalado")
                    print(f"     Instale com: CREATE EXTENSION vector;")
                    return False
            else:
                print(f"  ⚠️  Supabase: Conectado, mas tabela rag_documents não existe")
                print(f"     Crie a tabela usando a migration")
                return False
        
    except ImportError:
        print(f"  ⚠️  sqlalchemy não instalado")
        print(f"     Instale com: pip install sqlalchemy psycopg2-binary")
        return False
    except Exception as e:
        print(f"  ⚠️  Supabase: Não acessível")
        print(f"     Erro: {e}")
        print(f"     Verifique DATABASE_URL no .env")
        return False

def check_scraping_config():
    """Verifica configuração de scraping."""
    print("\n🔍 Verificando configuração de scraping...")
    
    config_path = Path(__file__).parent / "config" / "sources.yaml"
    
    if config_path.exists():
        print(f"  ✅ sources.yaml: Encontrado")
        
        # Verificar se tem fontes configuradas
        try:
            import yaml
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)
            
            sources_count = 0
            if config:
                if "curricular_sources" in config:
                    sources_count += len(config["curricular_sources"])
                if "question_sources" in config:
                    sources_count += len(config["question_sources"])
                if "olympiad_sources" in config:
                    sources_count += len(config["olympiad_sources"])
            
            print(f"  ✅ Fontes configuradas: {sources_count}")
            return True
        except Exception as e:
            print(f"  ❌ Erro ao ler sources.yaml: {e}")
            return False
    else:
        print(f"  ❌ sources.yaml: Não encontrado em {config_path}")
        return False

def main():
    """Executa todas as verificações."""
    print("=" * 60)
    print("VERIFICAÇÃO DE SETUP PARA RAG")
    print("=" * 60)
    
    results = {
        "environment": check_environment(),
        "dependencies": check_dependencies(),
        "supabase": check_supabase(),
        "scraping_config": check_scraping_config(),
    }
    
    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    
    all_ok = all(results.values())
    
    for check, result in results.items():
        status = "✅ OK" if result else "❌ FALHOU"
        print(f"{check.upper()}: {status}")
    
    if all_ok:
        print("\n🎉 Tudo configurado! Sistema RAG usando Supabase está pronto!")
        print("\n💡 Próximos passos:")
        print("   python -m backend.scraping.populate_rag --phase mvp")
        print("   python -m backend.scraping.import_bncc_data 'scraping/extract-data-2026-01-08 (1).json'")
        return 0
    else:
        print("\n⚠️  Algumas verificações falharam. Corrija os problemas acima.")
        if not results.get("supabase"):
            print("\n💡 Para configurar Supabase:")
            print("   1. Obtenha DATABASE_URL do Supabase Dashboard")
            print("   2. Adicione ao arquivo .env")
            print("   3. Execute CREATE EXTENSION vector; no Supabase (se necessário)")
        return 1

if __name__ == "__main__":
    exit(main())
