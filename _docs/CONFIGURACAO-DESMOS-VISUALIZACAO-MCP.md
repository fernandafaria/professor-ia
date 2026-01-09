# Configuração do Desmos / Formula Visualization MCP

**Criado em:** 2025-01-08  
**Status:** Configuração Inicial

---

## 📋 Visão Geral

O Desmos MCP permite que agentes de IA criem visualizações interativas de gráficos matemáticos e fórmulas. Infelizmente, o pacote `@modelcontextprotocol/server-desmos` **não existe oficialmente no npm**.

**Alternativas disponíveis:**
1. **Plotly** (já instalado) - Visualização de gráficos e fórmulas
2. **Matplotlib** - Visualização matemática básica
3. **Uso direto de Plotly** - Sem servidor MCP, mas funcional

---

## 🎯 Situação Atual

### Pacote Desmos MCP

O pacote `@modelcontextprotocol/server-desmos` **não existe** no npm:
- ❌ `@modelcontextprotocol/server-desmos` - Não disponível
- ❌ `mcp-server-desmos` - Não disponível no PyPI

### Alternativas Disponíveis

1. **mcp-plots** - Requer Python 3.10+ (sistema tem 3.9.6)
   - ❌ Não compatível com Python 3.9

2. **Plotly** - ✅ Já instalado e funcionando
   - ✅ Compatível com Python 3.9
   - ✅ Pode ser usado diretamente no código

3. **Matplotlib** - Disponível
   - ✅ Compatível com Python 3.9
   - ✅ Pode ser usado diretamente no código

---

## 🚀 Solução Recomendada: Usar Plotly Diretamente

Como não há um servidor MCP oficial do Desmos disponível e o `mcp-plots` requer Python 3.10+, recomendamos usar **Plotly diretamente no código Python**.

### Configuração no Código Python

**Exemplo de uso do Plotly para visualização de fórmulas:**

```python
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import sympy

def plot_formula(formula_str, x_range=(-10, 10), points=1000):
    """
    Plota uma fórmula matemática usando Plotly
    
    Args:
        formula_str: String com a fórmula (ex: "x^2 + 5*x + 6")
        x_range: Tupla com (x_min, x_max)
        points: Número de pontos para plotar
    """
    x = sympy.Symbol('x')
    
    # Converte string para expressão SymPy
    expr = sympy.sympify(formula_str)
    
    # Cria array de valores x
    x_vals = np.linspace(x_range[0], x_range[1], points)
    
    # Calcula valores y usando lambdify
    f = sympy.lambdify(x, expr, 'numpy')
    y_vals = f(x_vals)
    
    # Cria gráfico Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=formula_str
    ))
    
    fig.update_layout(
        title=f'Gráfico de {formula_str}',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    
    return fig

# Exemplo de uso
fig = plot_formula("x**2 - 5*x + 6")
fig.show()  # Abre no navegador
fig.write_html("grafico.html")  # Salva como HTML
```

### Funções Utilitárias para Visualização

**Criar arquivo `visualization_utils.py`:**

```python
"""
Utilitários para visualização de fórmulas matemáticas
"""
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import sympy
from typing import Tuple, Optional

def plot_function(expression_str: str, 
                  x_range: Tuple[float, float] = (-10, 10),
                  points: int = 1000,
                  title: Optional[str] = None) -> go.Figure:
    """Plota uma função matemática"""
    x = sympy.Symbol('x')
    expr = sympy.sympify(expression_str)
    
    x_vals = np.linspace(x_range[0], x_range[1], points)
    f = sympy.lambdify(x, expr, 'numpy')
    y_vals = f(x_vals)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=expression_str
    ))
    
    fig.update_layout(
        title=title or f'Gráfico de {expression_str}',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    
    return fig

def plot_multiple_functions(expressions: list,
                            x_range: Tuple[float, float] = (-10, 10),
                            points: int = 1000) -> go.Figure:
    """Plota múltiplas funções no mesmo gráfico"""
    x = sympy.Symbol('x')
    fig = go.Figure()
    
    x_vals = np.linspace(x_range[0], x_range[1], points)
    
    for expr_str in expressions:
        expr = sympy.sympify(expr_str)
        f = sympy.lambdify(x, expr, 'numpy')
        y_vals = f(x_vals)
        
        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            name=expr_str
        ))
    
    fig.update_layout(
        title='Gráficos Comparativos',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white'
    )
    
    return fig

def plot_3d_surface(expression_str: str,
                    x_range: Tuple[float, float] = (-5, 5),
                    y_range: Tuple[float, float] = (-5, 5),
                    points: int = 50) -> go.Figure:
    """Plota uma superfície 3D"""
    x_sym, y_sym = sympy.symbols('x y')
    expr = sympy.sympify(expression_str)
    
    x_vals = np.linspace(x_range[0], x_range[1], points)
    y_vals = np.linspace(y_range[0], y_range[1], points)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    f = sympy.lambdify((x_sym, y_sym), expr, 'numpy')
    Z = f(X, Y)
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    fig.update_layout(
        title=f'Superfície 3D: {expression_str}',
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title='f(x,y)'
        )
    )
    
    return fig
```

---

## 📦 Alternativas de Pacotes MCP

### 1. mcp-plots (Não Compatível)

**Status:** Requer Python 3.10+ (sistema tem 3.9.6)

**Instalação (se atualizar Python):**
```bash
pip install mcp-plots
```

**Configuração:**
```json
{
  "mcpServers": {
    "mcp-plots": {
      "command": "python3",
      "args": ["-m", "mcp_plots"],
      "env": {}
    }
  }
}
```

### 2. plotting-mcp (GitHub)

**Status:** Disponível via GitHub

**Instalação:**
```bash
git clone https://github.com/StacklokLabs/plotting-mcp.git
cd plotting-mcp
pip install -r requirements.txt
```

**Nota:** Verificar se requer Python 3.10+

---

## 🎯 Recomendação Final

### Para Uso Imediato

**Use Plotly diretamente no código Python** (já instalado):

1. **Crie funções utilitárias** como as mostradas acima
2. **Use em scripts Python** para gerar visualizações
3. **Salve como HTML** ou exiba interativamente

### Para Uso via MCP (Futuro)

1. **Atualizar Python para 3.10+** (se possível)
2. **Instalar `mcp-plots`** quando compatível
3. **Configurar servidor MCP** quando disponível

---

## 📝 Exemplos de Uso

### Exemplo 1: Plotar Função Simples

```python
from visualization_utils import plot_function

# Plotar função quadrática
fig = plot_function("x**2 - 5*x + 6", x_range=(-2, 7))
fig.show()
```

### Exemplo 2: Comparar Múltiplas Funções

```python
from visualization_utils import plot_multiple_functions

# Comparar funções
fig = plot_multiple_functions(
    ["x**2", "x**3", "x**4"],
    x_range=(-3, 3)
)
fig.show()
```

### Exemplo 3: Superfície 3D

```python
from visualization_utils import plot_3d_surface

# Plotar superfície 3D
fig = plot_3d_surface("x**2 + y**2")
fig.show()
```

---

## 📚 Recursos

- **Plotly Documentation:** https://plotly.com/python/
- **Plotly API Reference:** https://plotly.com/python-api-reference/
- **SymPy Documentation:** https://www.sympy.org/
- **Matplotlib Documentation:** https://matplotlib.org/
- **mcp-plots PyPI:** https://pypi.org/project/mcp-plots/
- **Plotting MCP GitHub:** https://github.com/StacklokLabs/plotting-mcp

---

## ✅ Checklist de Configuração

- [x] Plotly instalado e funcionando
- [ ] Funções utilitárias criadas (`visualization_utils.py`)
- [ ] Exemplos de uso testados
- [ ] Documentação criada
- [ ] Python atualizado para 3.10+ (opcional, para `mcp-plots`)

---

**Última Atualização:** 2025-01-08  
**Status:** Solução alternativa implementada (Plotly direto)
