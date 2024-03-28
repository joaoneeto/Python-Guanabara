num = str(input('Informe um numero: ')).strip()
print(f'Analisando o numero {num}...\n')
num = num[::-1]
print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(num[0], num[1], num[2], num[3]))
