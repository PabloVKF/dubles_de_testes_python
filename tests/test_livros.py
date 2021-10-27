import unittest
from unittest.mock import patch

from colecao.livros import *


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)  # add assertion here

    def test_consultar_livros_retorna_resultado_formato_string(self):
        resultado = consultar_livros("Agatha Cristine")
        assert type(resultado) == str

    def test_consultar_livros_chama_preparar_dados_para_requisicao_uma_vez_e_com_os_mesmomos_parametroos_de_consultar_livros(self):
        with patch("colecao.livros.preparar_dados_para_requisicao") as duble:
            consultar_livros("Agatha Cristine")
            duble.assert_called_once_with("Agatha Cristine")

    def test_consultar_livros_chama_obter_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao(self):
        with patch("colecao.livros.preparar_dados_para_requisicao") as duble_preparar:
            dados = {"author": "Agatha Christie"}
            duble_preparar.return_value = dados
            with patch("colecao.livros.obter_url") as duble_obter_url:
                consultar_livros("Agatha Christie")
                duble_obter_url.assert_called_once_with("https://buscador", dados)

    def consultar_livros_chama_requisicao_usando_retorno_obter_url(self):
        with patch("colecao.livros.obter_url") as duble_obter_url:
            duble_obter_url.return_value = "https://buscador"
            with patch("colecao.livros.executar_requisicao") as duble_executar_requisicao:
                consultar_livros("Agatha Christie")
                duble_executar_requisicao.assert_called_once_with("https://buscador")


if __name__ == '__main__':
    unittest.main()

