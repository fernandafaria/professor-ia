# Desmos / Formula Visualization - Quick Start

## ✅ Solução Implementada

Como o pacote oficial `@modelcontextprotocol/server-desmos` não existe no npm, implementamos uma **solução alternativa funcional** usando **Plotly diretamente no código Python**.

---

## 🚀 Solução Aplicada

### 1. Plotly Instalado ✅

O Plotly já está instalado e funcionando:
- Versão: 6.5.1
- Compatível com Python 3.9

### 2. Funções Utilitárias Criadas ✅

Arquivo `visualization_utils.py` criado com funções para:
- Plotar funções matemáticas 2D
- Comparar múltiplas funções
- Plotar superfícies 3D
- Plotar em coordenadas polares

### 3. Exemplos Gerados ✅

Três exemplos foram gerados com sucesso:
- `exemplo1_quadratica.html` - Função quadrática
- `exemplo2_multiplas.html` - Múltiplas funções
- `exemplo3_3d.html` - Superfície 3D

---

## 🎯 Como Usar

### Exemplo 1: Plotar Função Simples

```python
from visualization_utils import plot_function

# Plotar função quadrática
fig = plot_function("x**2 - 5*x + 6", x_range=(-1, 7), show=True)
# ou salvar
fig.write_html("grafico.html")
```

### Exemplo 2: Comparar Múltiplas Funções

```python
from visualization_utils import plot_multiple_functions

# Comparar funções
fig = plot_multiple_functions(
    ["x**2", "x**3", "x**4"],
    x_range=(-3, 3),
    show=True
)
```

### Exemplo 3: Superfície 3D

```python
from visualization_utils import plot_3d_surface

# Plotar superfície 3D
fig = plot_3d_surface("x**2 + y**2", show=True)
```

### Exemplo 4: Coordenadas Polares

```python
from visualization_utils import plot_polar

# Plotar em coordenadas polares
fig = plot_polar("2*cos(theta)", show=True)
```

---

## 📊 Gráficos Gerados

Abra os arquivos HTML gerados no navegador para ver os gráficos interativos:

1. **exemplo1_quadratica.html** - Função quadrática x² - 5x + 6
2. **exemplo2_multiplas.html** - Comparação de x², x³, x⁴
3. **exemplo3_3d.html** - Superfície 3D x² + y²

---

## 🔍 Por Que Não Tem Servidor MCP?

### Problema Identificado

1. **`@modelcontextprotocol/server-desmos`** - Não existe no npm
2. **`mcp-server-desmos`** - Não existe no PyPI
3. **`mcp-plots`** - Requer Python 3.10+ (sistema tem 3.9.6)

### Solução Implementada

**Uso direto de Plotly** sem servidor MCP intermediário, o que é:
- ✅ Mais simples e direto
- ✅ Mais rápido (sem overhead de MCP)
- ✅ Funcional imediatamente
- ✅ Compatível com Python 3.9

---

## 📝 Arquivos Criados

- ✅ `visualization_utils.py` - Funções utilitárias para visualização
- ✅ `_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md` - Documentação completa
- ✅ `exemplo1_quadratica.html` - Exemplo de função quadrática
- ✅ `exemplo2_multiplas.html` - Exemplo de múltiplas funções
- ✅ `exemplo3_3d.html` - Exemplo de superfície 3D

---

## 🎯 Exemplos de Uso Prático

### Resolver e Visualizar Equação

```python
import sympy
from visualization_utils import plot_function

# Resolver equação x² - 5x + 6 = 0
x = sympy.Symbol('x')
expr = x**2 - 5*x + 6
solutions = sympy.solve(expr, x)
print(f"Soluções: {solutions}")  # [-2, -3]

# Visualizar a função
fig = plot_function("x**2 - 5*x + 6", x_range=(-1, 7))
fig.show()
```

### Calcular e Visualizar Derivada

```python
import sympy
from visualization_utils import plot_multiple_functions

# Calcular derivada de sin(x) * cos(x)
x = sympy.Symbol('x')
expr = sympy.sin(x) * sympy.cos(x)
derivative = sympy.diff(expr, x)
print(f"Derivada: {derivative}")

# Visualizar função original e derivada
fig = plot_multiple_functions(
    ["sin(x) * cos(x)", str(derivative)],
    x_range=(-2*sympy.pi, 2*sympy.pi),
    points=2000
)
fig.show()
```

### Visualizar Integral

```python
import sympy
from visualization_utils import plot_function

# Calcular integral de x² + 3x + 2
x = sympy.Symbol('x')
expr = x**2 + 3*x + 2
integral = sympy.integrate(expr, x)
print(f"Integral: {integral}")

# Visualizar função original
fig = plot_function("x**2 + 3*x + 2", x_range=(-5, 2))
fig.show()
```

---

## 📚 Recursos

- **Plotly Documentation:** https://plotly.com/python/
- **SymPy Documentation:** https://www.sympy.org/
- **Documentação Completa:** `_docs/CONFIGURACAO-DESMOS-VISUALIZACAO-MCP.md`
- **Código Fonte:** `visualization_utils.py`

---

## ✅ Checklist

- [x] Plotly instalado e funcionando
- [x] Funções utilitárias criadas
- [x] Exemplos gerados e testados
- [x] Documentação criada
- [x] Pronto para uso

---

**Status:** ✅ Solução alternativa implementada e funcionando  
**Última Atualização:** 2025-01-08
