import random
import time
numero = range(1,5)
sortido = random.choice(numero)

num = int(input('Digite um numero de 1 a 5: '))
print('PROCESSANDO...')
time.sleep(2)

if num == sortido:
    print(f'Você venceu! acertou o numero sortido {sortido}, PARABENS')
else:
    print(f'Você errou, eu pensei no numero {sortido}. Tente novamente ')