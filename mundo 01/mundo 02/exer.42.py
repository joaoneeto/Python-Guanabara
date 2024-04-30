# REFAZER EXERCICIO 35 DOS TRIÂNGULOS E ACRESCENTAR OS TIPO DE TRIÂNGULOS



n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))


# SEGMENTOS PARA FORMAR TRIÂNGULO
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    pass
    # TRIÂNGULO EQUILÁTERO
    if n1 == n2 == n3:
        print('Os segmentos acima PODEM FORMAR um triângulo!\n'
              'De acordo com os segmentos acima, o Triângulo formado é EQUILÁTERO')

    # TRIANGULO ISÓSCELES
    elif n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2 :
        print('Os segmentos acima PODEM FORMAR um triângulo!\n'
              'De acordo com os segmentos acima, o Triângulo formado é ISÓSCELES')

    # TRIÂNGULO ESCALENO
    elif n1 != n2 != n3:
        print('Os segmentos acima PODEM FORMAR um triângulo!\n'
              'De acordo com os segmentos acima, o Triângulo formado é ESCALENO')

else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo!')

