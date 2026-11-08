
# =====================================
# TechFlow Solutions
# Sistema de Gerenciamento de Tarefas
# =====================================

import json
from pathlib import Path

# Salva o arquivo tarefas.json na pasta principal do projeto
ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "tarefas.json"


def carregar_tarefas():
    """Carrega as tarefas armazenadas no arquivo JSON."""

    if not ARQUIVO_DADOS.exists():
        return []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)

        if isinstance(tarefas, list):
            return tarefas

        print("Aviso: formato dos dados inválido. Iniciando lista vazia.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Aviso: não foi possível carregar os dados.")
        return []


def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""

    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

    except OSError:
        print("Erro ao salvar as tarefas!")


def menu():
    print("\n===== TECHFLOW SOLUTIONS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Consultar tarefas")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Filtrar tarefas por status")
    print("6 - Sair")


def cadastrar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()

    if not titulo:
        print("O título não pode ficar vazio!")
        return

    prioridade = input(
        "Prioridade (Baixa, Média ou Alta): "
    ).strip().capitalize()

    if prioridade not in ["Baixa", "Média", "Alta"]:
        print("Prioridade inválida!")
        return

    novo_id = max(
        [tarefa["id"] for tarefa in tarefas],
        default=0
    ) + 1

    tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "prioridade": prioridade,
        "status": "A Fazer"
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa cadastrada com sucesso!")


def consultar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        print(
            f"ID: {tarefa['id']} | "
            f"Título: {tarefa['titulo']} | "
            f"Prioridade: {tarefa['prioridade']} | "
            f"Status: {tarefa['status']}"
        )


def filtrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== FILTRAR TAREFAS =====")
    print("1 - A Fazer")
    print("2 - Em Progresso")
    print("3 - Concluída")

    opcao = input("Escolha o status: ")

    status_opcoes = {
        "1": "A Fazer",
        "2": "Em Progresso",
        "3": "Concluída"
    }

    if opcao not in status_opcoes:
        print("Opção inválida!")
        return

    status_escolhido = status_opcoes[opcao]

    encontradas = [
        tarefa for tarefa in tarefas
        if tarefa["status"] == status_escolhido
    ]

    if not encontradas:
        print("Nenhuma tarefa encontrada com esse status.")
        return

    print("\n===== RESULTADO DO FILTRO =====")

    for tarefa in encontradas:
        print(
            f"ID: {tarefa['id']} | "
            f"Título: {tarefa['titulo']} | "
            f"Prioridade: {tarefa['prioridade']} | "
            f"Status: {tarefa['status']}"
        )


def editar_tarefa(tarefas):
    consultar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        id_tarefa = int(
            input("Digite o ID da tarefa que deseja editar: ")
        )
    except ValueError:
        print("Digite um ID numérico válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:

            novo_titulo = input("Novo título: ").strip()

            nova_prioridade = input(
                "Nova prioridade (Baixa, Média ou Alta): "
            ).strip().capitalize()

            novo_status = input(
                "Novo status (A Fazer, Em Progresso ou Concluída): "
            ).strip().title()

            if not novo_titulo:
                print("O título não pode ficar vazio!")
                return

            if nova_prioridade not in ["Baixa", "Média", "Alta"]:
                print("Prioridade inválida!")
                return

            if novo_status not in [
                "A Fazer",
                "Em Progresso",
                "Concluída"
            ]:
                print("Status inválido!")
                return

            tarefa["titulo"] = novo_titulo
            tarefa["prioridade"] = nova_prioridade
            tarefa["status"] = novo_status

            salvar_tarefas(tarefas)

            print("Tarefa atualizada com sucesso!")
            return

    print("Tarefa não encontrada!")


def excluir_tarefa(tarefas):
    consultar_tarefas(tarefas)

    if not tarefas:
        return

    try:
        id_tarefa = int(
            input("Digite o ID da tarefa que deseja excluir: ")
        )
    except ValueError:
        print("Digite um ID numérico válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)

            print("Tarefa excluída com sucesso!")
            return

    print("Tarefa não encontrada!")


def iniciar_sistema():
    tarefas = carregar_tarefas()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            consultar_tarefas(tarefas)

        elif opcao == "3":
            editar_tarefa(tarefas)

        elif opcao == "4":
            excluir_tarefa(tarefas)

        elif opcao == "5":
            filtrar_tarefas(tarefas)

        elif opcao == "6":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()
