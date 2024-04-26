# CRIAR UM PROGRAMA QUE LEIA NOME ECOMPLETO DE UMA PESSOA E MOSTRE|:
# NOME COM TODAS LETRAS MAIUSCULA E MINUSCULA
# QUANTAS LETRAS TEM SEM CONTAR OS ESPAÇOS
# E MOSTRE SO O 1 NOME E QUANTAS LETRAS TEM


nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...\n')

print(f'Seu nome em maiúsculo é {nome.upper()} \n'
      f'Seu nome em minúsculo é {nome.lower()}')
nome = nome.split()
nome1 = nome[0]
nome = len(''.join(nome))
print(f'Seu nome tem ao todo {nome} letras \n')
print(f'Seu primeiro nome é {nome1} e ela tem {len(nome1)} letras')



# COMO PROFESSOR GUANABARA FEZ NA MINHA 15 LINHA

# print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

# ___________________________________________________________________________
# COMO PROFESSOR GUANABARA FEZ NA MINHA 16 LINHA COM 2 OPÇÕES DE SER FEITA

# 1-OPÇÃO
# print(seu primeiro nome tem {} letras'.format(nome.find(' ')))

# 2-OPÇÃO
# separa = nome.split()
# print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))