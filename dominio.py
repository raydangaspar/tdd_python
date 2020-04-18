import sys


# primeira regra de negócio: um usuário não pode dar dois lances seguidos
# segunda regra de negócio: não posso dar um lance menor ou igual que o lance anterior
class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property  # para acessar o atributo privado
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        # self.__lances = set()
        # colocar um valor muito baixo, a ponto de qualquer lance ser maior que ele
        self.maior_lance = sys.float_info.min  # o menor valor float que há no sistema
        # colocar um valor muito alto, a ponto de qualquer lance ser menor que ele
        self.menor_lance = sys.float_info.max  # o maior valor float que o sistema pode ter

    # reduz acoplamento
    def propoe(self, lance: Lance):  # diga, não pergunte
        # lances[-1].usuario pega o último lance da lista
        # if len(self.__lances) == 0 or self.lances[-1].usuario != lance.usuario:
        # self.__lances retorna true se tiver algum item dentro
        # um lance só pode ser aprovado se for maior que o lance anterior
        if not self.__lances or self.lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:  # jeito paythonico
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)
            # self.__lances.add(lance)
        else:
            raise ValueError('Erro ao propor lance')

    @property  # para acessar o atributo privado
    def lances(self):
        # return self.__lances    # estamos devolvendo o mesmo endereço de memória da lista criada
        # vamos devolver uma cópia dessa lista
        return self.__lances[:]  # cópia rasa de lista
