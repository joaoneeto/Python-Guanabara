n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
fim = '\033[m'
azul = '\033[34m'
verm = '\033[31m'
print(f'A soma entre {verm}{n1}{fim} e {verm}{n2}{fim} vale: {azul}{s}{fim}')