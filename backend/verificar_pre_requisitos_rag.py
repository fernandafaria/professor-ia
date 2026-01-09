#!/usr/bin/env python3
"""
Script completo para verificar pré-requisitos do Chat com RAG.
Verifica todas as dependências e configurações necessárias.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

def check_python_version() -> Tuple[bool, str]:
    """Verifica versão do Python."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        return True, f"✅ Python {version.major}.{version.minor}.{version.micro}"
    return False, f"❌ Python {version.major}.{version.minor}.{version.micro} (requer 3.10+)"

def check_env_file() -> Tuple[bool, str]:
    """Verifica se arquivo .env existe."""
    env_path = Path(".env")
    if env_path.exists():
        return True, "✅ Arquivo .env existe"
    return False, "❌ Arquivo .env não encontrado (copie de env.example)"

def check_env_variables() -> Dict[str, Tuple[bool, str]]:
    """Verifica variáveis de ambiente essenciais."""
    results = {}
    required_vars = {
        "DATABASE_URL": "URL do banco de dados Supabase",
        "ANTHROPIC_API_KEY": "Chave da API Anthropic (Claude)",
        "SECRET_KEY": "Chave secreta para JWT",
    }
    
    optional_vars = {
        "RAG_TABLE_NAME": "rag_documents",
        "EMBEDDING_DIMENSION": "384",
        "EMBEDDING_MODEL": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "ANTHROPIC_MODEL": "claude-3-5-sonnet-20241022",
    }
    
    # Verificar variáveis obrigatórias
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value:
            # Mascarar valores sensíveis
            if "KEY" in var or var == "SECRET_KEY":
                masked = value[:10] + "..." if len(value) > 10 else "***"
                results[var] = (True, f"✅ {var} configurado ({masked})")
            elif var == "DATABASE_URL":
                # Verificar se parece ser uma URL válida
                if "postgresql://" in value or "postgres://" in value:
                    results[var] = (True, f"✅ {var} configurado (formato válido)")
                else:
                    results[var] = (False, f"⚠️  {var} configurado mas formato pode estar incorreto")
            else:
                results[var] = (True, f"✅ {var} configurado")
        else:
            results[var] = (False, f"❌ {var} não configurado - {description}")
    
    # Verificar variáveis opcionais (com valores padrão)
    for var, default in optional_vars.items():
        value = os.getenv(var, default)
        if value == default:
            results[var] = (True, f"✅ {var} usando valor padrão: {default}")
        else:
            results[var] = (True, f"✅ {var} configurado: {value}")
    
    return results

def check_database_connection() -> Tuple[bool, str]:
    """Verifica conexão com banco de dados."""
    try:
        from sqlalchemy import create_engine, text
        database_url = os.getenv("DATABASE_URL")
        
        if not database_url:
            return False, "❌ DATABASE_URL não configurado"
        
        engine = create_engine(database_url, pool_pre_ping=True)
        with engine.connect() as conn:
            # Testar conexão
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
            return True, "✅ Conexão com banco de dados OK"
    except ImportError:
        return False, "❌ sqlalchemy não instalado (pip install sqlalchemy)"
    except Exception as e:
        return False, f"❌ Erro de conexão: {str(e)[:100]}"

def check_pgvector_extension() -> Tuple[bool, str]:
    """Verifica se extensão pgvector está instalada."""
    try:
        from sqlalchemy import create_engine, text
        database_url = os.getenv("DATABASE_URL")
        
        if not database_url:
            return False, "❌ DATABASE_URL não configurado"
        
        engine = create_engine(database_url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector'"))
            if result.fetchone():
                return True, "✅ Extensão pgvector instalada"
            else:
                return False, "❌ Extensão pgvector NÃO instalada (execute: CREATE EXTENSION vector;)"
    except Exception as e:
        return False, f"⚠️  Não foi possível verificar: {str(e)[:80]}"

def check_rag_table() -> Tuple[bool, str, int]:
    """Verifica se tabela rag_documents existe e tem documentos."""
    try:
        from sqlalchemy import create_engine, text
        database_url = os.getenv("DATABASE_URL")
        
        if not database_url:
            return False, "❌ DATABASE_URL não configurado", 0
        
        engine = create_engine(database_url)
        with engine.connect() as conn:
            # Verificar se tabela existe
            result = conn.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'rag_documents'
                )
            """))
            exists = result.fetchone()[0]
            
            if not exists:
                return False, "❌ Tabela rag_documents NÃO existe", 0
            
            # Contar documentos
            result = conn.execute(text("SELECT COUNT(*) FROM rag_documents"))
            count = result.fetchone()[0]
            
            if count == 0:
                return True, "⚠️  Tabela rag_documents existe mas está vazia", 0
            else:
                return True, f"✅ Tabela rag_documents existe com {count} documentos", count
    except Exception as e:
        return False, f"⚠️  Erro ao verificar tabela: {str(e)[:80]}", 0

def check_dependencies() -> Dict[str, Tuple[bool, str]]:
    """Verifica dependências Python."""
    results = {}
    required_packages = {
        "sqlalchemy": "SQLAlchemy",
        "anthropic": "Anthropic SDK",
        "sentence_transformers": "Sentence Transformers",
        "pydantic": "Pydantic",
        "fastapi": "FastAPI",
        "python-dotenv": "python-dotenv",
    }
    
    for package, name in required_packages.items():
        try:
            __import__(package.replace("-", "_"))
            results[package] = (True, f"✅ {name} instalado")
        except ImportError:
            results[package] = (False, f"❌ {name} não instalado (pip install {package})")
    
    return results

def check_anthropic_api() -> Tuple[bool, str]:
    """Verifica se chave da API Anthropic é válida (teste básico)."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        return False, "❌ ANTHROPIC_API_KEY não configurado"
    
    # Verificar formato básico
    if api_key.startswith("sk-ant-") and len(api_key) > 20:
        return True, "✅ ANTHROPIC_API_KEY formato válido"
    else:
        return False, "⚠️  ANTHROPIC_API_KEY formato pode estar incorreto (deve começar com 'sk-ant-')"

def check_embedding_model() -> Tuple[bool, str]:
    """Verifica se modelo de embedding pode ser carregado."""
    try:
        from sentence_transformers import SentenceTransformer
        model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        
        # Tentar carregar modelo (pode demorar na primeira vez)
        print("   ⏳ Carregando modelo de embedding (pode demorar)...")
        model = SentenceTransformer(model_name)
        
        # Testar encoding
        test_embedding = model.encode("teste")
        dimension = len(test_embedding)
        expected_dim = int(os.getenv("EMBEDDING_DIMENSION", "384"))
        
        if dimension == expected_dim:
            return True, f"✅ Modelo de embedding OK ({dimension} dimensões)"
        else:
            return False, f"⚠️  Dimensão do modelo ({dimension}) diferente da configurada ({expected_dim})"
    except ImportError:
        return False, "❌ sentence-transformers não instalado"
    except Exception as e:
        return False, f"⚠️  Erro ao carregar modelo: {str(e)[:80]}"

def main():
    """Executa todas as verificações."""
    print("🔍 Verificação de Pré-requisitos: Chat com RAG")
    print("=" * 60)
    print()
    
    # Carregar .env
    from dotenv import load_dotenv
    env_loaded = load_dotenv()
    if env_loaded:
        print("✅ Arquivo .env carregado\n")
    else:
        print("⚠️  Arquivo .env não encontrado (algumas verificações podem falhar)\n")
    
    all_checks_passed = True
    
    # 1. Python
    print("📦 Python:")
    passed, msg = check_python_version()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    print()
    
    # 2. Arquivo .env
    print("📄 Arquivo .env:")
    passed, msg = check_env_file()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    print()
    
    # 3. Variáveis de ambiente
    print("🔐 Variáveis de Ambiente:")
    env_results = check_env_variables()
    for var, (passed, msg) in env_results.items():
        print(f"   {msg}")
        if not passed and var in ["DATABASE_URL", "ANTHROPIC_API_KEY", "SECRET_KEY"]:
            all_checks_passed = False
    print()
    
    # 4. Dependências Python
    print("📚 Dependências Python:")
    dep_results = check_dependencies()
    for package, (passed, msg) in dep_results.items():
        print(f"   {msg}")
        if not passed:
            all_checks_passed = False
    print()
    
    # 5. Conexão com banco
    print("🗄️  Banco de Dados:")
    passed, msg = check_database_connection()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    print()
    
    # 6. Extensão pgvector (só se banco conectou)
    if "✅" in msg:
        passed, msg = check_pgvector_extension()
        print(f"   {msg}")
        if not passed:
            all_checks_passed = False
        print()
    
    # 7. Tabela RAG
    print("📚 Tabela RAG:")
    passed, msg, count = check_rag_table()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    elif count == 0:
        print("   💡 Dica: Popule a base RAG com: python scraping/populate_rag.py")
    print()
    
    # 8. API Anthropic
    print("🤖 API Anthropic:")
    passed, msg = check_anthropic_api()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    print()
    
    # 9. Modelo de Embedding
    print("🧮 Modelo de Embedding:")
    passed, msg = check_embedding_model()
    print(f"   {msg}")
    if not passed:
        all_checks_passed = False
    print()
    
    # Resumo final
    print("=" * 60)
    if all_checks_passed:
        print("✅ Todos os pré-requisitos estão configurados!")
        print("\n🎉 Você pode usar o chat com RAG agora!")
        print("\n📝 Próximos passos:")
        print("   1. Inicie o servidor: uvicorn app.main:app --reload")
        print("   2. Teste o chat via API ou frontend")
    else:
        print("⚠️  Alguns pré-requisitos precisam de atenção")
        print("\n📖 Consulte: backend/CONFIGURAR-CHAT-RAG.md")
        print("\n🔧 Ações necessárias:")
        
        # Listar problemas críticos
        if not env_results.get("DATABASE_URL", (True, ""))[0]:
            print("   - Configure DATABASE_URL no .env")
        if not env_results.get("ANTHROPIC_API_KEY", (True, ""))[0]:
            print("   - Configure ANTHROPIC_API_KEY no .env")
        if not env_results.get("SECRET_KEY", (True, ""))[0]:
            print("   - Configure SECRET_KEY no .env")
        
        for package, (passed, _) in dep_results.items():
            if not passed:
                print(f"   - Instale: pip install {package}")
    
    print()
    return 0 if all_checks_passed else 1

if __name__ == "__main__":
    sys.exit(main())
