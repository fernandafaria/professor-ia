#!/usr/bin/env python3
"""
Script para verificar configuração do Supabase PostgreSQL.
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

def check_supabase():
    """Verifica se Supabase está configurado corretamente."""
    
    print("🔍 Verificando Supabase PostgreSQL...")
    print("=" * 50)
    
    # 1. Verificar DATABASE_URL
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        print("❌ DATABASE_URL não configurado")
        print("   Configure no arquivo .env:")
        print("   DATABASE_URL=postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres")
        return False
    
    if "supabase" not in database_url.lower():
        print("⚠️  DATABASE_URL não parece ser do Supabase")
        print(f"   URL atual: {database_url[:50]}...")
    
    print(f"✅ DATABASE_URL configurado")
    
    # 2. Testar conexão
    try:
        engine = create_engine(database_url, pool_pre_ping=True)
        with engine.connect() as conn:
            # Verificar versão PostgreSQL
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Conectado ao PostgreSQL")
            print(f"   Versão: {version.split(',')[0]}")
            
            # Verificar extensão pgvector
            result = conn.execute(text("SELECT * FROM pg_extension WHERE extname = 'vector'"))
            if result.fetchone():
                print("✅ Extensão pgvector instalada")
            else:
                print("❌ Extensão pgvector NÃO instalada")
                print("   Execute no SQL Editor do Supabase:")
                print("   CREATE EXTENSION IF NOT EXISTS vector;")
                return False
            
            # Verificar tabela rag_documents
            result = conn.execute(text("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_name = 'rag_documents'
                )
            """))
            if result.fetchone()[0]:
                print("✅ Tabela rag_documents existe")
                
                # Contar documentos
                result = conn.execute(text("SELECT COUNT(*) FROM rag_documents"))
                count = result.fetchone()[0]
                print(f"   Documentos: {count}")
                
                # Verificar estrutura
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'rag_documents'
                    ORDER BY ordinal_position
                """))
                columns = result.fetchall()
                print(f"   Colunas: {len(columns)}")
                for col_name, col_type in columns:
                    print(f"     - {col_name}: {col_type}")
            else:
                print("❌ Tabela rag_documents NÃO existe")
                print("   Execute o script: backend/setup_supabase_postgresql.sql")
                return False
            
            # Verificar índices
            result = conn.execute(text("""
                SELECT indexname 
                FROM pg_indexes 
                WHERE tablename = 'rag_documents'
            """))
            indexes = [row[0] for row in result.fetchall()]
            if indexes:
                print(f"✅ Índices criados: {len(indexes)}")
                for idx in indexes:
                    print(f"     - {idx}")
            else:
                print("⚠️  Nenhum índice encontrado")
            
            print("\n" + "=" * 50)
            print("✅ Supabase PostgreSQL configurado corretamente!")
            return True
            
    except OperationalError as e:
        print(f"❌ Erro de conexão: {e}")
        print("\n💡 Verifique:")
        print("   1. DATABASE_URL está correto no .env")
        print("   2. Senha do projeto Supabase está correta")
        print("   3. Projeto Supabase está ativo")
        return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    # Carregar variáveis de ambiente
    from dotenv import load_dotenv
    load_dotenv()
    
    success = check_supabase()
    sys.exit(0 if success else 1)
