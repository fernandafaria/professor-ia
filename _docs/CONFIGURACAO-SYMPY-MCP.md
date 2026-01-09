# Configuração do SymPy MCP

**Criado em:** 2025-01-08  
**Status:** Configuração Inicial

---

## 📋 Visão Geral

O SymPy MCP permite que agentes de IA realizem cálculos matemáticos simbólicos, resolução de equações e manipulação de expressões matemáticas usando a biblioteca SymPy.

**Capacidades:**
- Resolução de equações simbólicas
- Cálculo simbólico e numérico
- Manipulação de expressões matemáticas
- Álgebra linear
- Cálculo diferencial e integral
- Simplificação de expressões

---

## 🎯 Opções de Configuração

Existem duas opções principais para usar SymPy via MCP:

### 1. Scientific Calculator MCP (Recomendado)

**Propósito:** Servidor MCP que usa SymPy e outras bibliotecas científicas para cálculos avançados.

**Instalação:**

```bash
# Instale as dependências
pip install sympy numpy scipy pandas

# Instale o pacote MCP
pip install mcp-scientific-calculator
```

**Configuração no Cursor (`.cursor/mcp.json`):**

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "python",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {}
    }
  }
}
```

**Alternativa (usando comando direto):**

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "mcp-calculator",
      "args": [],
      "env": {}
    }
  }
}
```

**Recursos:**
- [mcp-scientific-calculator PyPI](https://pypi.org/project/mcp-scientific-calculator/)
- Suporta SymPy, NumPy, SciPy e Pandas

---

### 2. SymPy MCP via GitHub Repository

**Propósito:** Repositório GitHub que implementa um servidor MCP específico para SymPy usando `uv`.

**Pré-requisitos:**

1. Instale `uv` (gerenciador de pacotes Python moderno):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Após instalação, reinicie o terminal.

2. Clone o repositório:
   ```bash
   git clone https://github.com/sdiehl/sympy-mcp.git
   cd sympy-mcp
   ```

3. Configure o ambiente:
   ```bash
   uv init
   uv venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   uv sync
   ```

**Configuração no Cursor (`.cursor/mcp.json`):**

Após instalar, configure o caminho absoluto para o servidor:

```json
{
  "mcpServers": {
    "sympy-mcp": {
      "command": "uv",
      "args": ["run", "mcp", "run", "server.py"],
      "cwd": "/caminho/absoluto/para/sympy-mcp",
      "env": {}
    }
  }
}
```

**Alternativa (usando Python diretamente):**

Se você já configurou o ambiente virtual:

```json
{
  "mcpServers": {
    "sympy-mcp": {
      "command": "/caminho/absoluto/para/sympy-mcp/.venv/bin/python",
      "args": ["server.py"],
      "cwd": "/caminho/absoluto/para/sympy-mcp",
      "env": {}
    }
  }
}
```

**Recursos:**
- [sympy-mcp GitHub](https://github.com/sdiehl/sympy-mcp)
- Repositório oficial do desenvolvedor

---

## 🚀 Configuração Recomendada (Scientific Calculator)

Para começar rapidamente, recomendamos usar o `mcp-scientific-calculator`:

### Passo 1: Instalar Dependências

```bash
# Certifique-se de que Python 3.10+ está instalado
python3 --version

# Instale as bibliotecas científicas
pip3 install sympy numpy scipy pandas

# Instale o servidor MCP
pip3 install mcp-scientific-calculator
```

### Passo 2: Configurar no Cursor

Adicione ao arquivo `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "python3",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {}
    }
  }
}
```

### Passo 3: Reiniciar o Cursor

Reinicie completamente o Cursor para aplicar a configuração.

### Passo 4: Testar

Teste a configuração com comandos como:

```
"Resolva a equação x^2 + 5x + 6 = 0"
"Calcule a derivada de x^3 + 2x^2 + x"
"Simplifique a expressão (x+1)^2 - (x-1)^2"
```

---

## 🔍 Verificação da Instalação

### Verificar se SymPy está instalado

```bash
python3 -c "import sympy; print(sympy.__version__)"
```

### Verificar se mcp-scientific-calculator está instalado

```bash
python3 -m mcp_scientific_calculator --help
# ou
pip3 show mcp-scientific-calculator
```

### Verificar configuração do Cursor

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `scientific-calculator` aparece na lista
4. Verifique o status (deve mostrar "Connected" ou similar)

---

## 📝 Atualização do requirements.txt

O arquivo `requirements.txt` do projeto já inclui `mcp-server-sympy`, mas como este pacote não existe oficialmente, recomendamos atualizar para:

```txt
# Tier 1 - Essencial (Matemática)
sympy
numpy
scipy
pandas
mcp-scientific-calculator
```

Para instalar todas as dependências:

```bash
pip3 install -r requirements.txt
```

---

## 🎯 Como Usar

### Exemplos de Uso

Após configurar, você pode usar o SymPy MCP para:

**1. Resolver equações:**

```
"Resolva a equação quadrática x^2 - 5x + 6 = 0"
"Encontre as raízes de x^3 - 6x^2 + 11x - 6 = 0"
```

**2. Cálculo diferencial:**

```
"Calcule a derivada de sin(x) * cos(x)"
"Encontre a derivada segunda de x^4 + 3x^2 - 2x"
```

**3. Cálculo integral:**

```
"Calcule a integral de x^2 + 3x + 2"
"Encontre a integral definida de e^x de 0 a 1"
```

**4. Simplificação:**

```
"Simplifique (x+1)^2 - (x-1)^2"
"Expandir (a+b)^3"
```

**5. Álgebra linear:**

```
"Calcule o determinante da matriz [[1,2],[3,4]]"
"Encontre os autovalores da matriz [[2,1],[1,2]]"
```

---

## 🔍 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'mcp_scientific_calculator'"

**Solução:**
```bash
pip3 install mcp-scientific-calculator
```

### Problema: "ModuleNotFoundError: No module named 'sympy'"

**Solução:**
```bash
pip3 install sympy
```

### Problema: Servidor não inicia

**Soluções:**
1. Verifique se Python 3.10+ está instalado:
   ```bash
   python3 --version
   ```

2. Verifique se todas as dependências estão instaladas:
   ```bash
   pip3 install sympy numpy scipy pandas mcp-scientific-calculator
   ```

3. Verifique se o caminho do Python está correto em `.cursor/mcp.json`
4. Reinicie o Cursor completamente

### Problema: Comandos matemáticos não funcionam

**Soluções:**
1. Verifique se o servidor está conectado no Cursor
2. Certifique-se de que está usando comandos em formato que o servidor entende
3. Verifique os logs do Cursor para erros

### Problema: Caminho do Python incorreto

**Solução:**
Encontre o caminho correto do Python:
```bash
which python3
```

Atualize `.cursor/mcp.json` com o caminho completo, se necessário:
```json
{
  "mcpServers": {
    "scientific-calculator": {
      "command": "/usr/bin/python3",
      "args": ["-m", "mcp_scientific_calculator"],
      "env": {}
    }
  }
}
```

---

## 📚 Recursos Adicionais

- **SymPy Documentation:** https://www.sympy.org/
- **Scientific Calculator MCP:** https://pypi.org/project/mcp-scientific-calculator/
- **sympy-mcp GitHub:** https://github.com/sdiehl/sympy-mcp
- **Model Context Protocol:** https://modelcontextprotocol.io/
- **Cursor MCP Docs:** https://docs.cursor.com/context/mcp

---

## ✅ Checklist de Configuração

- [ ] Python 3.10+ instalado
- [ ] SymPy instalado (`pip3 install sympy`)
- [ ] Bibliotecas científicas instaladas (`numpy`, `scipy`, `pandas`)
- [ ] `mcp-scientific-calculator` instalado
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado
- [ ] Servidor conectado verificado
- [ ] Teste de uso realizado

---

**Última Atualização:** 2025-01-08  
**Mantido por:** Time de Engenharia
