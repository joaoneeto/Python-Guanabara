distancia = float(input('Qual a distancia da sua viagem? km '))
curta = distancia * 0.50
longa = distancia * 0.45
if distancia <= 200:
    print(f'O valor total da sua viagem sera: R$ {curta:.2f} ')
else:
    print(f'O valor total da sua viagem sera: R$ {longa:.2f}')