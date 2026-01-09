# SymPy MCP - Quick Start

## ✅ Configuração Completa

O SymPy MCP foi configurado com sucesso usando o **Scientific Calculator MCP**!

---

## 🚀 Configuração Rápida

### 1. Instalar Dependências

Execute no terminal:

```bash
# Instale as bibliotecas científicas e o servidor MCP
pip3 install sympy numpy scipy pandas mcp-scientific-calculator
```

Ou instale todas as dependências do projeto:

```bash
pip3 install -r requirements.txt
```

### 2. Configuração Aplicada

O arquivo `.cursor/mcp.json` já foi configurado:

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

### 3. Reiniciar o Cursor

**IMPORTANTE:** Reinicie completamente o Cursor para aplicar a configuração!

1. Feche completamente o Cursor
2. Abra novamente o Cursor

### 4. Verificar Conexão

1. Abra as configurações do Cursor (`Cmd/Ctrl + ,`)
2. Navegue até **Features > MCP**
3. Verifique se `scientific-calculator` aparece na lista
4. Status deve mostrar "Connected" ou similar

---

## 🎯 Como Usar

Após reiniciar o Cursor, você pode usar o SymPy MCP para cálculos matemáticos:

### Exemplos de Uso

**Resolução de Equações:**
```
"Resolva a equação quadrática x^2 - 5x + 6 = 0"
"Encontre as raízes de x^3 - 6x^2 + 11x - 6 = 0"
```

**Cálculo Diferencial:**
```
"Calcule a derivada de sin(x) * cos(x)"
"Encontre a derivada segunda de x^4 + 3x^2 - 2x"
```

**Cálculo Integral:**
```
"Calcule a integral de x^2 + 3x + 2"
"Encontre a integral definida de e^x de 0 a 1"
```

**Simplificação:**
```
"Simplifique (x+1)^2 - (x-1)^2"
"Expandir (a+b)^3"
```

**Álgebra Linear:**
```
"Calcule o determinante da matriz [[1,2],[3,4]]"
"Encontre os autovalores da matriz [[2,1],[1,2]]"
```

---

## 🔍 Verificação da Instalação

### Verificar se está instalado corretamente:

```bash
# Verificar Python
python3 --version

# Verificar SymPy
python3 -c "import sympy; print('SymPy:', sympy.__version__)"

# Verificar Scientific Calculator MCP
python3 -m mcp_scientific_calculator --help
```

Todos os comandos devem executar sem erros.

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
pip3 install sympy numpy scipy pandas
```

### Problema: Servidor não conecta no Cursor

**Soluções:**
1. Certifique-se de ter reiniciado o Cursor completamente
2. Verifique se Python 3.10+ está instalado: `python3 --version`
3. Verifique se todas as dependências estão instaladas
4. Verifique a sintaxe do JSON em `.cursor/mcp.json`
5. Verifique os logs do Cursor para erros

### Problema: Caminho do Python incorreto

Se o `python3` não estiver no PATH, use o caminho completo:

```bash
which python3
```

Atualize `.cursor/mcp.json` com o caminho completo se necessário.

---

## 📚 Documentação

Para mais detalhes, consulte:
- **Documentação Completa:** `_docs/CONFIGURACAO-SYMPY-MCP.md`
- **Guia Geral MCP:** `_docs/GUIA-MCP-SERVERS.md`
- **SymPy Documentation:** https://www.sympy.org/
- **Scientific Calculator MCP:** https://pypi.org/project/mcp-scientific-calculator/

---

## ✅ Checklist de Configuração

- [ ] Python 3.10+ instalado
- [ ] Dependências instaladas (`pip3 install -r requirements.txt`)
- [ ] Configuração adicionada ao `.cursor/mcp.json`
- [ ] Cursor reiniciado completamente
- [ ] Servidor conectado verificado
- [ ] Teste de uso realizado

---

**Última Atualização:** 2025-01-08
