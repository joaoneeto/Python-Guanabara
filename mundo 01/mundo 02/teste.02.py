#  CRIAR UMA CLASSE DE VEICULO
# ESSA CLASSE TEM QUE DEFINI NOME, VELOCIADDE MAXIMA E KM PERCORRIDO POR LITRO

class Veiculo: #class pai
    def __init__(self, nome, velocidade_max, km_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.km_litro = km_litro

    def capacidade_assentos(self, capacidade): #descrição adicionada para ajudar a class filha do onibus
        print(f'Capacidade de assentos: {capacidade}')
    def descricao(self): #descrição geral para veiculos
        print(f'Nome: {self.nome}')
        print(f'Velocidade maxima: {self.velocidade_max}')
        print(f'Km percorrido por litro: {self.km_litro}')


class Onibus(Veiculo): #class filha
    def capacidade_assentos(self, capacidade=70): #dando valor a class pai para acrescentar informação de assento
        return super().capacidade_assentos(capacidade=70)

modelo = Onibus('Onibus', 100, 5, )
modelo.descricao()
modelo.capacidade_assentos() #de acordo onde estiver esse objeto, é onde sera apresentado