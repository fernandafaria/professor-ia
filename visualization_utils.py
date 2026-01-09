"""
Utilitários para visualização de fórmulas matemáticas usando Plotly e SymPy
"""
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import sympy
from typing import Tuple, Optional, List
import base64
from io import BytesIO


def plot_function(expression_str: str, 
                  x_range: Tuple[float, float] = (-10, 10),
                  points: int = 1000,
                  title: Optional[str] = None,
                  show: bool = False,
                  save_path: Optional[str] = None) -> go.Figure:
    """
    Plota uma função matemática usando Plotly
    
    Args:
        expression_str: String com a fórmula (ex: "x**2 + 5*x + 6")
        x_range: Tupla com (x_min, x_max)
        points: Número de pontos para plotar
        title: Título do gráfico (opcional)
        show: Se True, exibe o gráfico no navegador
        save_path: Caminho para salvar o gráfico como HTML (opcional)
    
    Returns:
        go.Figure: Figura do Plotly
    """
    x = sympy.Symbol('x')
    
    # Converte string para expressão SymPy
    try:
        expr = sympy.sympify(expression_str)
    except Exception as e:
        raise ValueError(f"Erro ao processar expressão: {e}")
    
    # Cria array de valores x
    x_vals = np.linspace(x_range[0], x_range[1], points)
    
    # Calcula valores y usando lambdify
    try:
        f = sympy.lambdify(x, expr, 'numpy')
        y_vals = f(x_vals)
    except Exception as e:
        raise ValueError(f"Erro ao calcular valores: {e}")
    
    # Cria gráfico Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=expression_str,
        line=dict(width=2)
    ))
    
    fig.update_layout(
        title=title or f'Gráfico de {expression_str}',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white',
        hovermode='x unified'
    )
    
    if show:
        fig.show()
    
    if save_path:
        fig.write_html(save_path)
    
    return fig


def plot_multiple_functions(expressions: List[str],
                            x_range: Tuple[float, float] = (-10, 10),
                            points: int = 1000,
                            title: Optional[str] = None,
                            show: bool = False,
                            save_path: Optional[str] = None) -> go.Figure:
    """
    Plota múltiplas funções no mesmo gráfico
    
    Args:
        expressions: Lista de strings com fórmulas
        x_range: Tupla com (x_min, x_max)
        points: Número de pontos para plotar
        title: Título do gráfico (opcional)
        show: Se True, exibe o gráfico no navegador
        save_path: Caminho para salvar o gráfico como HTML (opcional)
    
    Returns:
        go.Figure: Figura do Plotly
    """
    x = sympy.Symbol('x')
    fig = go.Figure()
    
    x_vals = np.linspace(x_range[0], x_range[1], points)
    
    colors = px.colors.qualitative.Plotly
    
    for i, expr_str in enumerate(expressions):
        try:
            expr = sympy.sympify(expr_str)
            f = sympy.lambdify(x, expr, 'numpy')
            y_vals = f(x_vals)
            
            fig.add_trace(go.Scatter(
                x=x_vals,
                y=y_vals,
                mode='lines',
                name=expr_str,
                line=dict(width=2, color=colors[i % len(colors)])
            ))
        except Exception as e:
            print(f"Aviso: Não foi possível plotar {expr_str}: {e}")
            continue
    
    fig.update_layout(
        title=title or 'Gráficos Comparativos',
        xaxis_title='x',
        yaxis_title='f(x)',
        template='plotly_white',
        hovermode='x unified'
    )
    
    if show:
        fig.show()
    
    if save_path:
        fig.write_html(save_path)
    
    return fig


def plot_3d_surface(expression_str: str,
                    x_range: Tuple[float, float] = (-5, 5),
                    y_range: Tuple[float, float] = (-5, 5),
                    points: int = 50,
                    title: Optional[str] = None,
                    show: bool = False,
                    save_path: Optional[str] = None) -> go.Figure:
    """
    Plota uma superfície 3D
    
    Args:
        expression_str: String com a fórmula 3D (ex: "x**2 + y**2")
        x_range: Tupla com (x_min, x_max)
        y_range: Tupla com (y_min, y_max)
        points: Número de pontos por eixo
        title: Título do gráfico (opcional)
        show: Se True, exibe o gráfico no navegador
        save_path: Caminho para salvar o gráfico como HTML (opcional)
    
    Returns:
        go.Figure: Figura do Plotly
    """
    x_sym, y_sym = sympy.symbols('x y')
    
    try:
        expr = sympy.sympify(expression_str)
    except Exception as e:
        raise ValueError(f"Erro ao processar expressão: {e}")
    
    x_vals = np.linspace(x_range[0], x_range[1], points)
    y_vals = np.linspace(y_range[0], y_range[1], points)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    try:
        f = sympy.lambdify((x_sym, y_sym), expr, 'numpy')
        Z = f(X, Y)
    except Exception as e:
        raise ValueError(f"Erro ao calcular valores: {e}")
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
    fig.update_layout(
        title=title or f'Superfície 3D: {expression_str}',
        scene=dict(
            xaxis_title='x',
            yaxis_title='y',
            zaxis_title='f(x,y)'
        ),
        width=800,
        height=600
    )
    
    if show:
        fig.show()
    
    if save_path:
        fig.write_html(save_path)
    
    return fig


def plot_polar(expression_str: str,
               theta_range: Tuple[float, float] = (0, 2*np.pi),
               points: int = 1000,
               title: Optional[str] = None,
               show: bool = False,
               save_path: Optional[str] = None) -> go.Figure:
    """
    Plota função em coordenadas polares
    
    Args:
        expression_str: String com a fórmula polar (ex: "2*cos(theta)")
        theta_range: Tupla com (theta_min, theta_max) em radianos
        points: Número de pontos para plotar
        title: Título do gráfico (opcional)
        show: Se True, exibe o gráfico no navegador
        save_path: Caminho para salvar o gráfico como HTML (opcional)
    
    Returns:
        go.Figure: Figura do Plotly
    """
    theta = sympy.Symbol('theta')
    
    try:
        expr = sympy.sympify(expression_str)
    except Exception as e:
        raise ValueError(f"Erro ao processar expressão: {e}")
    
    theta_vals = np.linspace(theta_range[0], theta_range[1], points)
    
    try:
        f = sympy.lambdify(theta, expr, 'numpy')
        r_vals = f(theta_vals)
    except Exception as e:
        raise ValueError(f"Erro ao calcular valores: {e}")
    
    # Converte para coordenadas cartesianas
    x_vals = r_vals * np.cos(theta_vals)
    y_vals = r_vals * np.sin(theta_vals)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=expression_str,
        line=dict(width=2)
    ))
    
    fig.update_layout(
        title=title or f'Gráfico Polar: {expression_str}',
        xaxis_title='x',
        yaxis_title='y',
        template='plotly_white',
        hovermode='closest'
    )
    
    if show:
        fig.show()
    
    if save_path:
        fig.write_html(save_path)
    
    return fig


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Função simples
    print("Plotando x^2 - 5x + 6...")
    fig1 = plot_function("x**2 - 5*x + 6", x_range=(-1, 7), show=False)
    fig1.write_html("exemplo1_quadratica.html")
    print("Gráfico salvo em exemplo1_quadratica.html")
    
    # Exemplo 2: Múltiplas funções
    print("\nPlotando múltiplas funções...")
    fig2 = plot_multiple_functions(
        ["x**2", "x**3", "x**4"],
        x_range=(-3, 3),
        show=False
    )
    fig2.write_html("exemplo2_multiplas.html")
    print("Gráfico salvo em exemplo2_multiplas.html")
    
    # Exemplo 3: Superfície 3D
    print("\nPlotando superfície 3D...")
    fig3 = plot_3d_surface("x**2 + y**2", show=False)
    fig3.write_html("exemplo3_3d.html")
    print("Gráfico salvo em exemplo3_3d.html")
    
    print("\n✅ Todos os exemplos gerados com sucesso!")
