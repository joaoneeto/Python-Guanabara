import random
numero = range(1,5)
sortido = random.choice(numero)

num = int(input('Digite um numero de 1 a 5: '))

if num == sortido:
    print('Você venceu! acertou o numero sortido, PARABENS')
else:
    print('Você errou, tente novamente!')