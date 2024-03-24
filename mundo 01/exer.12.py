p = float(input('Preço do produto: R$ '))
d = float(input('Porcentagem de desconto ; %'))
v = p - (p * d / 100)
print(f'O produto do valor R${p} com desconto de {d:.0f}% fica: R${v:.2f}')
l = p * d / 100
print(f'\nVocê teve uma economia de: R${l:.2f}')