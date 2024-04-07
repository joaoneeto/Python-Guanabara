a = input('Digite algo: ')

# CORES
fim = '\033[m'
azul = '\033[34m'
verm = '\033[31m'

print('O tipo primitivo desse valor é {}{}{} '.format(azul, type(a), fim))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())
