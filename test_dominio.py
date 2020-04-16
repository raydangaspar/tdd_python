# alt + enter em cima da palavra em vermelho, mostra e coloca a biblioteca que falta importar
# ctrl+ shift + t em cima do nome da classe que se deseja fazer o teste unitário
from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):  # herda de TestCase

    # método setUp é herdado da classe TestCase
    # quando coloca self na frente do atributo, significa que é um atributo da classe
    # setUp método da classe unittest que já invoca o setup antes de todos os testes
    # serve para isolar o cenário comum de todos os testes
    # sempre cria um objeto novo a cada teste invocado
    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        # self.fail() # herdando de TestCase. Quando executar essa linha, o teste vai falhar

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
