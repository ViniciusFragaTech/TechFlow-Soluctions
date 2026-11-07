# =====================================
# TechFlow Solutions
# Sistema de Gerenciamento de Tarefas
# =====================================

def menu():
    print("\n===== TECHFLOW SOLUTIONS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Consultar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")


def iniciar_sistema():
    while True:
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Cadastro de tarefas selecionado!")

        elif opcao == "2":
            print("Consulta de tarefas selecionada!")

        elif opcao == "3":
            print("Edição de tarefas selecionada!")

        elif opcao == "4":
            print("Exclusão de tarefas selecionada!")

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
