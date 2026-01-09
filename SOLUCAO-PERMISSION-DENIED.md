# 🔧 Solução: "zsh: permission denied"

## ⚠️ Erro Comum

Se você recebeu o erro `zsh: permission denied` ao tentar executar um script, significa que o arquivo não tem permissão de execução.

## ✅ Solução Rápida

### Opção 1: Dar Permissão de Execução

```bash
cd /Users/fernandafaria/Downloads/P1A
chmod +x nome_do_script.sh
```

**Exemplo:**
```bash
chmod +x instalar_pre_requisitos.sh
chmod +x instalar_pre_requisitos_auto.sh
chmod +x verificar_pre_requisitos.sh
```

### Opção 2: Dar Permissão a Todos os Scripts

```bash
cd /Users/fernandafaria/Downloads/P1A
chmod +x *.sh
```

### Opção 3: Executar com Bash Explicitamente

```bash
bash instalar_pre_requisitos.sh
# ou
zsh instalar_pre_requisitos.sh
```

---

## 🔍 Verificar Permissões

Para ver as permissões atuais:

```bash
ls -la *.sh
```

**Permissões corretas devem mostrar:**
```
-rwxr-xr-x  ... instalar_pre_requisitos.sh
```

O `x` significa que o arquivo tem permissão de execução.

---

## 📋 Scripts no Projeto

Todos os scripts devem ter permissão de execução:

- ✅ `instalar_pre_requisitos.sh`
- ✅ `instalar_pre_requisitos_auto.sh`
- ✅ `verificar_pre_requisitos.sh`
- ✅ `abrir_terminal_instalar_homebrew.sh`

---

## 🚀 Após Corrigir Permissões

Agora você pode executar normalmente:

```bash
./instalar_pre_requisitos.sh
# ou
./instalar_pre_requisitos_auto.sh
```

---

## 💡 Dica

Se você criar novos scripts `.sh`, sempre dê permissão de execução:

```bash
chmod +x novo_script.sh
```

---

**Problema resolvido!** ✅
