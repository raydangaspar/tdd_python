# alt + enter em cima da palavra em vermelhor, mostra e coloca a biblioteca que falta importar
# ctrl+ shift + t em cima do nome da classe que se deseja fazer o teste unitário
from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):  # herda de TestCase
    def test_avalia(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)
        # leilao.lances.append(lance_do_yuri)
        # self.fail() # herdando de TestCase. Quando executar essa linha, o teste vai falhar

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        # método para trabalhar com teste
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
