-- =====================================================
-- Setup PostgreSQL no Supabase para RAG
-- =====================================================
-- Execute este script no SQL Editor do Supabase
-- =====================================================

-- 1. Instalar extensão pgvector (se ainda não estiver instalada)
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Criar tabela rag_documents para armazenar documentos do RAG
CREATE TABLE IF NOT EXISTS rag_documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding vector(384),  -- Dimensão padrão do modelo multilingual-MiniLM
    metadata JSONB DEFAULT '{}'::jsonb,
    source VARCHAR(255),
    subject VARCHAR(100),
    grade VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 3. Criar índice para busca vetorial (HNSW - mais rápido para busca)
CREATE INDEX IF NOT EXISTS rag_documents_embedding_idx 
ON rag_documents 
USING hnsw (embedding vector_cosine_ops);

-- 4. Criar índices adicionais para filtros comuns
CREATE INDEX IF NOT EXISTS rag_documents_source_idx ON rag_documents(source);
CREATE INDEX IF NOT EXISTS rag_documents_subject_idx ON rag_documents(subject);
CREATE INDEX IF NOT EXISTS rag_documents_grade_idx ON rag_documents(grade);
CREATE INDEX IF NOT EXISTS rag_documents_metadata_idx ON rag_documents USING GIN (metadata);

-- 5. Criar função para atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 6. Criar trigger para atualizar updated_at
DROP TRIGGER IF EXISTS update_rag_documents_updated_at ON rag_documents;
CREATE TRIGGER update_rag_documents_updated_at
    BEFORE UPDATE ON rag_documents
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- 7. Comentários para documentação
COMMENT ON TABLE rag_documents IS 'Armazena documentos para o sistema RAG com embeddings vetoriais';
COMMENT ON COLUMN rag_documents.embedding IS 'Embedding vetorial gerado pelo modelo sentence-transformers';
COMMENT ON COLUMN rag_documents.metadata IS 'Metadados adicionais em formato JSONB';
COMMENT ON COLUMN rag_documents.source IS 'Fonte do documento (ex: neurodivergence_papers, bncc, etc)';

-- =====================================================
-- Verificações
-- =====================================================

-- Verificar se a extensão foi instalada
SELECT * FROM pg_extension WHERE extname = 'vector';

-- Verificar estrutura da tabela
SELECT 
    column_name, 
    data_type, 
    is_nullable
FROM information_schema.columns 
WHERE table_name = 'rag_documents'
ORDER BY ordinal_position;

-- Verificar índices
SELECT 
    indexname, 
    indexdef 
FROM pg_indexes 
WHERE tablename = 'rag_documents';

-- =====================================================
-- Teste de inserção (opcional)
-- =====================================================

-- Exemplo de inserção de teste (descomente para testar)
/*
INSERT INTO rag_documents (content, embedding, metadata, source, subject, grade)
VALUES (
    'Este é um documento de teste para verificar o funcionamento do RAG.',
    '[0.1, 0.2, 0.3]'::vector(384),  -- Embedding de exemplo (substitua por embedding real)
    '{"test": true}'::jsonb,
    'test',
    'teste',
    'teste'
);
*/

-- =====================================================
-- Limpeza (se necessário recriar tudo)
-- =====================================================

-- ATENÇÃO: Descomente apenas se quiser recriar tudo do zero
/*
DROP TABLE IF EXISTS rag_documents CASCADE;
DROP FUNCTION IF EXISTS update_updated_at_column() CASCADE;
-- Depois execute novamente os comandos acima
*/
