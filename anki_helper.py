"""
Helper simples para usar Anki diretamente via AnkiConnect
Sem necessidade de servidor MCP intermediário
"""
import requests
import json


def criar_flashcard(pergunta, resposta, deck="Default"):
    """
    Cria um flashcard no Anki
    
    Args:
        pergunta: Texto da frente do cartão
        resposta: Texto do verso do cartão
        deck: Nome do deck (padrão: "Default")
    
    Returns:
        Resultado da operação
    """
    dados = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck,
                "modelName": "Basic",
                "fields": {
                    "Front": pergunta,
                    "Back": resposta
                },
                "tags": []
            }
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:8765",
            json=dados,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"erro": "Anki não está rodando ou AnkiConnect não está instalado"}
    except Exception as e:
        return {"erro": str(e)}


def listar_decks():
    """Lista todos os decks disponíveis"""
    dados = {"action": "deckNames", "version": 6}
    
    try:
        response = requests.post("http://localhost:8765", json=dados, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"erro": str(e)}


def verificar_conexao():
    """Verifica se o AnkiConnect está funcionando"""
    dados = {"action": "version", "version": 6}
    
    try:
        response = requests.post("http://localhost:8765", json=dados, timeout=5)
        response.raise_for_status()
        return {"ok": True, "versao": response.json()}
    except Exception as e:
        return {"ok": False, "erro": str(e)}


# Exemplo de uso
if __name__ == "__main__":
    print("🔍 Verificando conexão com Anki...")
    status = verificar_conexao()
    
    if status.get("ok"):
        print(f"✅ Conectado! Versão: {status.get('versao')}")
        
        print("\n📚 Decks disponíveis:")
        decks = listar_decks()
        print(f"   {decks}")
        
        print("\n📝 Criando flashcard de exemplo...")
        resultado = criar_flashcard(
            "O que é Python?",
            "Python é uma linguagem de programação de alto nível"
        )
        print(f"   Resultado: {resultado}")
    else:
        print(f"❌ Erro: {status.get('erro')}")
        print("\n💡 Certifique-se de que:")
        print("   1. Anki está rodando")
        print("   2. Plugin AnkiConnect está instalado (código: 2055492159)")
        print("   3. Anki foi reiniciado após instalar o plugin")
