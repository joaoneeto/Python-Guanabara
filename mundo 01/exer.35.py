# formula: A SOMA DE DOIS LADOS É SEMPRE MENOR QUE O TERCEIRO LADO
# formula:
# a + b > c
# b + c > a
# a + c > b

n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo!')


