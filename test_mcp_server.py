#!/usr/bin/env python3
"""
Script de teste para verificar se o MCP Scientific Calculator está funcionando
"""
import subprocess
import sys
import json

def test_mcp_server():
    """Testa o servidor MCP enviando uma requisição de inicialização"""
    
    print("Testando MCP Scientific Calculator Server...")
    print("-" * 50)
    
    # Requisição JSON-RPC 2.0 para inicializar o servidor
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    try:
        # Executa o servidor e envia a requisição
        process = subprocess.Popen(
            [sys.executable, "-m", "mcp_scientific_calculator"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Envia a requisição
        request_json = json.dumps(init_request) + "\n"
        stdout, stderr = process.communicate(input=request_json, timeout=5)
        
        print(f"Status: {process.returncode}")
        print(f"STDOUT: {stdout[:500] if stdout else '(vazio)'}")
        print(f"STDERR: {stderr[:500] if stderr else '(vazio)'}")
        
        if stdout:
            try:
                response = json.loads(stdout.strip())
                print(f"\n✅ Servidor respondeu com sucesso!")
                print(f"Resposta: {json.dumps(response, indent=2)[:500]}")
                return True
            except json.JSONDecodeError as e:
                print(f"\n⚠️ Resposta não é JSON válido: {e}")
                return False
        else:
            print("\n❌ Servidor não produziu saída")
            return False
            
    except subprocess.TimeoutExpired:
        process.kill()
        print("\n❌ Servidor não respondeu a tempo")
        return False
    except Exception as e:
        print(f"\n❌ Erro ao executar servidor: {e}")
        return False

if __name__ == "__main__":
    success = test_mcp_server()
    sys.exit(0 if success else 1)
