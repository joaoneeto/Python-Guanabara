# Programa que leia 3 valores e me de o menor e o maior entre eles

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

# Achar o maior valor

if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior valor digitado foi {n2}')
else:
    print(f'O maior valor digitado foi {n3}')

# Achar o menor valor

if n1 < n2 and n1 < n3:
    print(f'E o menor valor digitado foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'E o menor valor digitado foi {n2}')
else:
    print(f'E o menor valor digitado foi {n3}')