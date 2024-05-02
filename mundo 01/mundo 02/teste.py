class Somar_multiplicar:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def somar(self):
        return self.a + self.b;
    def multiplicar(self):
        return self.a * self.b;

class filha(Somar_multiplicar):
    def subtrair(self):
        return self.a - self.b;
    def dividir(self):
        return self.a / self.b;

n1 = int(input('Digite um valor:  '))
n2 = int(input('Digite outro valor: '))
valores = filha(n1 , n2)
print(f'A soma dos valores citados: {valores.somar()}\n'
      f'a multiplicação dos valores citados : {valores.multiplicar()}\n'
      f'a subtração dos valores citados: {valores.subtrair()}\n'
      f'a divisão dos valores citados : {valores.dividir():.2f}')