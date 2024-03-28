frase = str(input('Digite uma frase: ')).strip().upper()
quantidade = frase.count('A')
pri = frase.find('A')
ult = frase.rfind('A')
print(f'A letra A aparece {quantidade} vezes na frase.\n'
      f'A primeira letra A aparece na posição {pri + 1}\n'
      f'A ultima letra A apareceu na posição {ult + 1}')