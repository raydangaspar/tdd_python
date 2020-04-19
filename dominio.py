# primeira regra de negócio: um usuário não pode dar dois lances seguidos
# segunda regra de negócio: não posso dar um lance menor ou igual que o lance anterior
class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise ValueError('Não pode propor um lance com valor maior que  valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property  # para acessar o atributo privado
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira


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
        self.maior_lance = 0.0
        # colocar um valor muito alto, a ponto de qualquer lance ser menor que ele
        self.menor_lance = 0.0

    # reduz acoplamento
    def propoe(self, lance: Lance):  # diga, não pergunte
        # lances[-1].usuario pega o último lance da lista
        # if len(self.__lances) == 0 or self.lances[-1].usuario != lance.usuario:
        # self.__lances retorna true se tiver algum item dentro
        # um lance só pode ser aprovado se for maior que o lance anterior
        if self._lance_eh_valido(lance):  # jeito paythonico
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
            # self.__lances.add(lance)
        else:
            raise ValueError('Erro ao propor lance')

    @property  # para acessar o atributo privado
    def lances(self):
        # return self.__lances    # estamos devolvendo o mesmo endereço de memória da lista criada
        # vamos devolver uma cópia dessa lista
        return self.__lances[:]  # cópia rasa de lista

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._valor_maior_que_lance_anterior(lance))
