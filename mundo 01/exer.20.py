from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo: ')
n3 = input('Terceiro: ')
n4 = input('Quarto: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem da aprensentação sera assim: \n {lista}')

# eu utilizei o sample para sorteia e deu certo e botei q era igual a k=4 a lista porem o guanabara usou assim como esta
# agr o programa e fica mais bonito e facil interpretar entao deixei
# assim(usei o sample pq lê no pyton e entendi melhor e vi q daria pro oq eu queria