#!/usr/bin/env python3
"""
Wrapper fix para o MCP Scientific Calculator que corrige problemas de protocolo MCP
"""
import sys
import json
import subprocess

def main():
    """Executa o servidor MCP com correções de protocolo"""
    python_path = "/Library/Developer/CommandLineTools/usr/bin/python3"
    
    # Inicia o servidor MCP
    process = subprocess.Popen(
        [python_path, "-m", "mcp_scientific_calculator"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,  # Binary mode para evitar problemas de encoding
        bufsize=0
    )
    
    try:
        # Ler e processar mensagens
        while True:
            # Ler linha do stdin
            line = sys.stdin.buffer.readline()
            
            if not line:
                break
            
            # Escrever para o processo
            try:
                process.stdin.write(line)
                process.stdin.flush()
                
                # Ler resposta do processo
                response_line = process.stdout.readline()
                
                if response_line:
                    # Escrever resposta para stdout
                    sys.stdout.buffer.write(response_line)
                    sys.stdout.buffer.flush()
                else:
                    # EOF
                    break
                    
            except BrokenPipeError:
                break
            except Exception as e:
                # Em caso de erro, enviar resposta de erro válida
                error_response = {
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32603,
                        "message": f"Internal error: {str(e)}"
                    },
                    "id": None  # ID será None para erros de parse
                }
                response_json = json.dumps(error_response) + "\n"
                sys.stdout.buffer.write(response_json.encode('utf-8'))
                sys.stdout.buffer.flush()
                
    except KeyboardInterrupt:
        pass
    finally:
        # Limpar
        try:
            process.stdin.close()
        except:
            pass
        try:
            process.terminate()
            process.wait(timeout=1)
        except:
            try:
                process.kill()
            except:
                pass

if __name__ == "__main__":
    main()
