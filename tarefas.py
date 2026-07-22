import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

tarefas = carregar_tarefas()  


def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{indice}. [{status}] {tarefa['titulo']}")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Número inválido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{removida['titulo']}' removida.")
    except (ValueError, IndexError):
        print("Número inválido.")

def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()