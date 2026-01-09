# Solução para Erro do MCP Scientific Calculator

## 🔍 Problema Identificado

O erro mostra que o Cursor está recebendo respostas JSON-RPC 2.0 **inválidas** do servidor `mcp-scientific-calculator`:

```
"expected": "string", received null - para campo "id"
"expected": "string", received undefined - para campo "method"
Unrecognized key: "error"
```

Este é um **problema de compatibilidade** entre o pacote `mcp-scientific-calculator` e o protocolo MCP que o Cursor espera.

## ✅ Solução Temporária Aplicada

O servidor `scientific-calculator` foi **desabilitado temporariamente** no `.cursor/mcp.json` para evitar erros.

**Configuração atual:**

```json
{
  "mcpServers": {
    "figma-remote": {
      "url": "https://mcp.figma.com/mcp",
      "transport": "sse"
    }
  }
}
```

## 🎯 Soluções Alternativas

### Opção 1: Usar Servidor MCP Alternativo para Matemática

O pacote `mcp-scientific-calculator` parece ter problemas de compatibilidade. Considere usar uma alternativa:

**1. Instalar um servidor MCP de matemática alternativo:**

```bash
# Verificar se há alternativas disponíveis
pip3 search mcp math
pip3 search mcp calculator
```

**2. Usar biblioteca SymPy diretamente via código Python:**

Em vez de usar um servidor MCP, você pode usar SymPy diretamente no código Python do projeto:

```python
import sympy

# Exemplos de uso
x = sympy.Symbol('x')
expr = x**2 + 5*x + 6
result = sympy.solve(expr, x)
print(result)  # [-3, -2]
```

### Opção 2: Aguardar Correção do Pacote

O problema está no pacote `mcp-scientific-calculator` versão 1.0.1. Você pode:

1. **Aguardar uma atualização** do pacote que corrija o problema
2. **Reportar o bug** no repositório do pacote: https://github.com/thinkitpossible/CalcMCP

### Opção 3: Usar o Wrapper Fix (Experimento)

Criei um wrapper (`mcp_calculator_fixed.py`) que tenta corrigir o problema, mas pode não funcionar completamente devido ao problema estar no próprio servidor.

Se quiser tentar:

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "/Library/Developer/CommandLineTools/usr/bin/python3",
      "args": ["/Users/fernandafaria/Downloads/P1A/mcp_calculator_fixed.py"],
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

**Nota:** Este wrapper é experimental e pode não resolver completamente o problema.

## 🔄 Desabilitar e Reabilitar no Cursor

Se você quiser tentar reabilitar o servidor no futuro:

1. **Desabilitar no Cursor:**
   - Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
   - Navegue até **Features > MCP**
   - Remova ou desabilite `scientific-calculator`

2. **Reabilitar (após correção):**
   - Aguarde uma atualização do pacote
   - Ou use uma alternativa quando disponível

## 📚 Alternativas para Matemática Simbólica

### Usar SymPy Diretamente no Código

Você pode usar SymPy diretamente no seu código Python sem precisar de um servidor MCP:

**Exemplo de uso:**

```python
import sympy

# Resolver equação
x = sympy.Symbol('x')
expr = x**2 - 5*x + 6
solutions = sympy.solve(expr, x)
print(f"Soluções: {solutions}")

# Calcular derivada
expr = sympy.sin(x) * sympy.cos(x)
derivative = sympy.diff(expr, x)
print(f"Derivada: {derivative}")

# Simplificar
expr = (x + 1)**2 - (x - 1)**2
simplified = sympy.simplify(expr)
print(f"Simplificado: {simplified}")
```

**Criar funções auxiliares:**

```python
# math_utils.py
import sympy

def solve_equation(equation_str, variable='x'):
    """Resolve uma equação simbólica"""
    x = sympy.Symbol(variable)
    expr = sympy.sympify(equation_str)
    return sympy.solve(expr, x)

def calculate_derivative(expression_str, variable='x', order=1):
    """Calcula a derivada de uma expressão"""
    x = sympy.Symbol(variable)
    expr = sympy.sympify(expression_str)
    return sympy.diff(expr, x, order)

def simplify_expression(expression_str):
    """Simplifica uma expressão"""
    expr = sympy.sympify(expression_str)
    return sympy.simplify(expr)
```

## 🎯 Próximos Passos

1. ✅ **Servidor desabilitado** para evitar erros
2. ⏳ **Aguardar atualização** do pacote `mcp-scientific-calculator`
3. 💡 **Usar SymPy diretamente** no código quando necessário
4. 📝 **Reportar bug** no repositório do pacote

## 📋 Checklist

- [x] Problema identificado (incompatibilidade de protocolo)
- [x] Servidor desabilitado temporariamente
- [ ] Alternativa implementada (SymPy direto)
- [ ] Bug reportado no repositório do pacote
- [ ] Atualização do pacote aguardada

## 📚 Recursos

- **Repositório do Pacote:** https://github.com/thinkitpossible/CalcMCP
- **SymPy Documentation:** https://www.sympy.org/
- **MCP Protocol:** https://modelcontextprotocol.io/
- **Cursor Issues:** https://github.com/cursor/cursor/issues

---

**Status:** Servidor desabilitado - Aguardando correção do pacote ou alternativa  
**Última Atualização:** 2025-01-08
