import unittest
from unittest.mock import patch

from src.main import menu


class TestSistema(unittest.TestCase):

    @patch("builtins.print")
    def test_menu_exibe_titulo(self, mock_print):
        menu()

        mock_print.assert_any_call("\n===== TECHFLOW SOLUTIONS =====")

    @patch("builtins.print")
    def test_menu_exibe_opcoes(self, mock_print):
        menu()

        mock_print.assert_any_call("1 - Cadastrar tarefa")
        mock_print.assert_any_call("5 - Sair")


if __name__ == "__main__":
    unittest.main()
