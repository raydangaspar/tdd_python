# alt + enter em cima da palavra em vermelho, mostra e coloca a biblioteca que falta importar
# ctrl+ shift + t em cima do nome da classe que se deseja fazer o teste unitário
from unittest import TestCase
from dominio import Usuario, Lance, Leilao
from excecoes import LanceInvalido


class TestLeilao(TestCase):  # herda de TestCase

    # método setUp é herdado da classe TestCase
    # quando coloca self na frente do atributo, significa que é um atributo da classe
    # setUp método da classe unittest que já invoca o setup antes de todos os testes
    # serve para isolar o cenário comum de todos os testes
    # sempre cria um objeto novo a cada teste invocado
    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_descrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri', 500.0)
        vini = Usuario('Vini', 500.0)

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilão não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    # se o último usuário for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o último usuário for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui_200 = Lance(self.gui, 200.0)

        # uma forma de tratar a exceção
        # try:
        #     self.leilao.propoe(self.lance_do_gui)
        #     self.leilao.propoe(lance_do_gui_200)
        #     # se executou as linhas de cima, deveria ter dado excessão
        #     self.fail(msg='Não lançou exceção')
        # # dado a exceção e não executado as linhas de cima, faço a verificação abaixo.
        # except ValueError:
        #     quantidade_de_lances_recebidos = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances_recebidos)

        # outra forma de tratar exceção usando método do testcase
        # espera um erro
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui_200)
