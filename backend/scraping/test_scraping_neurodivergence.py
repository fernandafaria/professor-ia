"""
Script de teste rápido para scraping de papers sobre neurodivergências.
"""

import sys
from pathlib import Path

# Adicionar ao path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from backend.scraping.scrapers.academic import PubMedScraper, SciELOScraper
    from backend.scraping.scrape_neurodivergence_papers import NeurodivergencePaperScraper
    
    print("✅ Imports bem-sucedidos!")
    
    # Teste rápido: buscar 3 papers sobre TDAH
    print("\n🔍 Testando busca no PubMed...")
    pubmed = PubMedScraper()
    papers = pubmed.search_papers("ADHD education", max_results=3)
    
    print(f"✅ Encontrados {len(papers)} papers")
    if papers:
        print(f"\nPrimeiro paper:")
        print(f"  Título: {papers[0].get('title', 'N/A')[:80]}...")
        print(f"  Autores: {', '.join(papers[0].get('authors', [])[:3])}")
        print(f"  Abstract: {papers[0].get('abstract', 'N/A')[:150]}...")
    
    print("\n✅ Teste concluído com sucesso!")
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("\nVerifique se as dependências estão instaladas:")
    print("  pip install requests beautifulsoup4")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro durante teste: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
