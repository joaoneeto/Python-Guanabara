# o valor da casa
# salario da pessoa
# em quantos anos ira pagar
# o valor da prestação nao pode exceder 30% do salario

casa = float(input('Qual o valor da casa: R$ '))
salario = int(input('Qual valor do seu salário: R$ '))

trint = salario * 30 / 100

anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)


if prestacao <= trint:
    print('O emprestimo foi aprovado!')
else:
    print('Infelizmente o emprestimo não foi aprovado!')


