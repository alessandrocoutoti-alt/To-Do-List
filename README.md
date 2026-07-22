# 📝 Gerenciador de Tarefas (To-Do List)

Uma aplicação simples e prática de gerenciamento de tarefas desenvolvida em Python para linha de comando (CLI). O projeto permite que você organize seu dia a dia adicionando, visualizando, concluindo e removendo tarefas diretamente pelo terminal.

## 🚀 Como Funciona?

* O programa exibe um menu interativo com opções de gerenciamento.
* A cada ação, você pode adicionar novas tarefas à lista ou remover as existentes.
* As tarefas possuem um indicador visual de status: concluído (`✅`) ou pendente (`❌`).
* Todas as alterações são salvas automaticamente em um arquivo JSON local, garantindo que suas tarefas não sejam perdidas ao fechar o programa.

## 🛠️ Pré-requisitos

Para rodar o gerenciador de tarefas, você só precisa ter o Python 3 instalado em sua máquina.

## 📋 Exemplo de Uso

```text
--- Gerenciador de Tarefas ---
1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
Escolha uma opção: 1
Digite o título da tarefa: Estudar Python
Tarefa adicionada com sucesso!

--- Gerenciador de Tarefas ---
1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
Escolha uma opção: 2
1. [❌] Estudar Python
```

## 💻 Como Rodar o Projeto

1. Abra o terminal ou prompt de comando na pasta do projeto.
2. Execute o seguinte comando:
   ```bash
   python tarefas.py
   ```
Organize suas tarefas com facilidade!

## ⚙️ Tecnologias Utilizadas

* **Python 3**
* Biblioteca nativa `json` para persistência de dados.
* Tratamento de exceções com `try/except` para garantir que o programa não quebre caso você digite um número de tarefa inválido ou inexistente.

## 📚 O que Pratiquei

* Leitura e gravação de arquivos com o módulo `json` (persistência de dados)
* Loops (`while`) com condição de parada para o menu interativo
* Estruturas de dados (listas e dicionários) para organizar as tarefas
* Uso da função `enumerate()` para gerar índices dinâmicos na listagem
* Tratamento de exceções (`try/except`) para tratar entradas inválidas do usuário