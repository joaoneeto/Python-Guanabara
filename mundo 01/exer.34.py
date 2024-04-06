# AUMENTO DE 10 % PARA QUEM GANHA SALARIO ACIMA DE 1.250
# QUEM GANHAR MENOR QUE ISSO AUMENTO DE 15%

salario = float(input('Digite o valor do seu Salário: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print(f'Quem ganhava R${salario:.2f} passara a ganhar R${aumento:.2f}')


if salario > 1250:
    ganho = salario * 10 / 100
else:
    ganho = salario * 15 / 100
print(f'Você teve um aumento de R${ganho:.2f} a mais.')