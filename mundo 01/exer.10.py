n = float(input('Converta reais em dolar: R$'))
d = float(input('Converta dolares em reais: US$'))
r = n / 4.99
do = 4.99 * d
print('Você tem {:.2f}US$ dolares de {:.2f}R$ reais'. format(r, n))
print('Você tem {:.2f}R$ reais de {:.2f}US$ dolares'.format(do, d))