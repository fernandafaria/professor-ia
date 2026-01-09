"""
Script de validação do ambiente de desenvolvimento.
"""

import sys
import os
from pathlib import Path

# Adicionar backend ao path
backend_path = Path(__file__).parent.parent
sys.path.insert(0, str(backend_path))


def check_python_version():
    """Verifica versão do Python."""
    print("🐍 Verificando Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"  ❌ Python {version.major}.{version.minor} detectado. Requer Python 3.10+")
        return False
    print(f"  ✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Verifica dependências principais."""
    print("\n📦 Verificando dependências...")
    required = [
        "fastapi",
        "chromadb",
        "sentence_transformers",
        "sqlalchemy",
        "pydantic",
        "requests",
        "beautifulsoup4",
    ]
    
    missing = []
    for dep in required:
        try:
            __import__(dep.replace("-", "_"))
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} não instalado")
            missing.append(dep)
    
    if missing:
        print(f"\n  ⚠️  Instale as dependências faltantes:")
        print(f"     pip install {' '.join(missing)}")
        return False
    
    return True


def check_env_file():
    """Verifica se arquivo .env existe."""
    print("\n🔐 Verificando configuração...")
    env_file = backend_path / ".env"
    
    if not env_file.exists():
        print(f"  ⚠️  Arquivo .env não encontrado em {env_file}")
        print(f"     Copie .env.example para .env e configure")
        return False
    
    print(f"  ✅ Arquivo .env encontrado")
    
    # Verificar variáveis críticas
    from dotenv import load_dotenv
    load_dotenv(env_file)
    
    critical_vars = [
        "DATABASE_URL",
        "SECRET_KEY",
        "CHROMA_HOST",
        "CHROMA_PORT",
    ]
    
    missing_vars = []
    for var in critical_vars:
        value = os.getenv(var)
        if not value:
            print(f"  ⚠️  {var} não configurado")
            missing_vars.append(var)
        else:
            # Mascarar valores sensíveis
            if "KEY" in var or "SECRET" in var:
                display_value = value[:4] + "..." if len(value) > 4 else "***"
            else:
                display_value = value
            print(f"  ✅ {var} = {display_value}")
    
    if missing_vars:
        print(f"\n  ⚠️  Configure as variáveis faltantes no .env")
        return False
    
    return True


def check_chromadb():
    """Verifica conexão com ChromaDB."""
    print("\n🔍 Verificando ChromaDB...")
    try:
        from app.config import settings
        import chromadb
        from chromadb.config import Settings as ChromaSettings
        
        client = chromadb.Client(
            ChromaSettings(
                chroma_api_impl="rest",
                chroma_server_host=settings.CHROMA_HOST,
                chroma_server_http_port=settings.CHROMA_PORT,
            )
        )
        
        # Tentar listar collections
        collections = client.list_collections()
        print(f"  ✅ ChromaDB conectado em {settings.CHROMA_HOST}:{settings.CHROMA_PORT}")
        print(f"  ✅ {len(collections)} collections encontradas")
        return True
    except Exception as e:
        print(f"  ❌ Erro ao conectar ChromaDB: {e}")
        print(f"     Certifique-se de que ChromaDB está rodando:")
        print(f"     chroma run --path ./chroma_db --port {settings.CHROMA_PORT if 'settings' in locals() else 8000}")
        return False


def check_database():
    """Verifica conexão com PostgreSQL."""
    print("\n🗄️  Verificando PostgreSQL...")
    try:
        from app.config import settings
        from sqlalchemy import create_engine, text
        
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
        
        print(f"  ✅ PostgreSQL conectado")
        return True
    except Exception as e:
        print(f"  ⚠️  Erro ao conectar PostgreSQL: {e}")
        print(f"     Verifique DATABASE_URL no .env")
        return False


def check_redis():
    """Verifica conexão com Redis (opcional)."""
    print("\n🔴 Verificando Redis (opcional)...")
    try:
        from app.config import settings
        import redis
        
        r = redis.from_url(settings.REDIS_URL)
        r.ping()
        print(f"  ✅ Redis conectado")
        return True
    except Exception as e:
        print(f"  ⚠️  Redis não disponível: {e}")
        print(f"     Redis é opcional (necessário apenas para Celery)")
        return True  # Não é crítico


def check_scraping_data():
    """Verifica se arquivo de dados BNCC existe."""
    print("\n📚 Verificando dados BNCC...")
    data_file = backend_path.parent / "scraping" / "extract-data-2026-01-08 (1).json"
    
    if data_file.exists():
        import json
        with open(data_file) as f:
            data = json.load(f)
        total = sum(len(v) for v in data.values())
        print(f"  ✅ Arquivo encontrado: {total} itens BNCC")
        return True
    else:
        print(f"  ⚠️  Arquivo não encontrado: {data_file}")
        print(f"     Não é crítico - pode fazer scraping novo")
        return True  # Não é crítico


def main():
    """Executa todas as validações."""
    print("=" * 60)
    print("🔍 Validação do Ambiente - Plataforma P1A")
    print("=" * 60)
    
    checks = [
        ("Python", check_python_version),
        ("Dependências", check_dependencies),
        ("Configuração", check_env_file),
        ("ChromaDB", check_chromadb),
        ("PostgreSQL", check_database),
        ("Redis", check_redis),
        ("Dados BNCC", check_scraping_data),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n  ❌ Erro ao verificar {name}: {e}")
            results.append((name, False))
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 Resumo")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    print(f"\n{passed}/{total} verificações passaram")
    
    if passed == total:
        print("\n🎉 Ambiente configurado corretamente!")
        return 0
    else:
        print("\n⚠️  Algumas verificações falharam. Corrija antes de continuar.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
