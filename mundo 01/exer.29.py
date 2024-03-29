import math
velo = float(input('Digite a velocidade que você percorreu: km ')).__floor__()
valor = (velo - 80) * 7

if velo > 80:
    print('Você ultrapassou o limite permitido'
          f'\nDe acordo com o valor da multa de R$7,00 por km acima do limite a multa fica: R${valor:.2f}')
else:
    print('Você esta de acordo com limite permitido pela via, está isento de multa.\nContinue assim!')