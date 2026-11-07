import unittest
from unittest.mock import patch

from src.main import (
    menu,
    cadastrar_tarefa,
    consultar_tarefas,
    editar_tarefa,
    excluir_tarefa,
    filtrar_tarefas
)


class TestSistema(unittest.TestCase):

    def setUp(self):
        self.tarefas = []

    @patch("builtins.print")
    def test_menu_exibe_titulo(self, mock_print):
        menu()
        mock_print.assert_any_call("\n===== TECHFLOW SOLUTIONS =====")

    @patch("builtins.print")
    def test_menu_exibe_opcoes(self, mock_print):
        menu()
        mock_print.assert_any_call("1 - Cadastrar tarefa")
        mock_print.assert_any_call("5 - Filtrar tarefas por status")
        mock_print.assert_any_call("6 - Sair")

    @patch("src.main.salvar_tarefas")
    @patch("builtins.input", side_effect=["Estudar Python", "Alta"])
    def test_cadastrar_tarefa(self, mock_input, mock_salvar):
        cadastrar_tarefa(self.tarefas)

        self.assertEqual(len(self.tarefas), 1)
        self.assertEqual(self.tarefas[0]["titulo"], "Estudar Python")
        self.assertEqual(self.tarefas[0]["prioridade"], "Alta")
        self.assertEqual(self.tarefas[0]["status"], "A Fazer")
        mock_salvar.assert_called_once()

    @patch("builtins.print")
    def test_consultar_tarefas(self, mock_print):
        self.tarefas.append({
            "id": 1,
            "titulo": "Estudar Python",
            "prioridade": "Alta",
            "status": "A Fazer"
        })

        consultar_tarefas(self.tarefas)
        mock_print.assert_any_call("\n===== LISTA DE TAREFAS =====")

    @patch("src.main.salvar_tarefas")
    @patch(
        "builtins.input",
        side_effect=["1", "Estudar Java", "Média", "Em Progresso"]
    )
    def test_editar_tarefa(self, mock_input, mock_salvar):
        self.tarefas.append({
            "id": 1,
            "titulo": "Estudar Python",
            "prioridade": "Alta",
            "status": "A Fazer"
        })

        editar_tarefa(self.tarefas)

        self.assertEqual(self.tarefas[0]["titulo"], "Estudar Java")
        self.assertEqual(self.tarefas[0]["prioridade"], "Média")
        self.assertEqual(self.tarefas[0]["status"], "Em Progresso")
        mock_salvar.assert_called_once()

    @patch("src.main.salvar_tarefas")
    @patch("builtins.input", return_value="1")
    def test_excluir_tarefa(self, mock_input, mock_salvar):
        self.tarefas.append({
            "id": 1,
            "titulo": "Estudar Python",
            "prioridade": "Alta",
            "status": "A Fazer"
        })

        excluir_tarefa(self.tarefas)

        self.assertEqual(len(self.tarefas), 0)
        mock_salvar.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.input", return_value="1")
    def test_filtrar_tarefas(self, mock_input, mock_print):
        self.tarefas.append({
            "id": 1,
            "titulo": "Estudar Python",
            "prioridade": "Alta",
            "status": "A Fazer"
        })

        filtrar_tarefas(self.tarefas)

        mock_print.assert_any_call(
            "ID: 1 | Título: Estudar Python | "
            "Prioridade: Alta | Status: A Fazer"
        )


if __name__ == "__main__":
    unittest.main()
