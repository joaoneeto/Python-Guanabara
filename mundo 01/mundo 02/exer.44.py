# Condição de pagamento
# a vista 10% de desconto

valor = float(input('Digite um valor total da sua comprar: '))
print('Digite sua opção de pagamento abaixo: \n'
      '(1) A vista no dinheiro \n'
      '(2) A vista no cartão \n'
      '(3) parcelado de 2x no cartão \n'
      '(4) parcelado em 3x ou mais')


opcao = int(input('Qual sua escolha: '))


if opcao == 1:
    total = valor - (valor * 0.10)
    desconto = valor * 0.10
    print('o total fica {} com um desconto de {:.2f}'.format(total, desconto))

elif opcao == 2:
    total = valor - (valor * 0.05)
    desconto = valor * 0.05
    print('o total fica {} com um desconto de {:.2f}'.format(total, desconto))

elif opcao == 3:
    print('Não ocorre desconto, valor integral de {:.2f}'.format(valor))

elif opcao == 4:
    juros = valor * 20 / 100
    total = valor + juros
    print('o total fica {} com juros de {:.2f}'.format(total, juros))



