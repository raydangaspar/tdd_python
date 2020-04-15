import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property  # para acessar o atributo privado
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property  # para acessar o atributo privado
    def lances(self):
        return self.__lances


class Avaliador:

    def __init__(self):
        # colocar um valor muito baixo, a ponto de qualquer lance ser maior que ele
        self.maior_lance = sys.float_info.min  # o menor valor float que há no sistema
        # colocar um valor muito alto, a ponto de qualquer lance ser menor que ele
        self.menor_lance = sys.float_info.max  # o maior valor float que o sistema pode ter

    def avalia(self, leilao: Leilao):  # annotation, para termos uma ideia do que esperar do parâmetro
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
