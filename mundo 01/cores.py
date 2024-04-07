# SISTEMA DE CORES

print('\033[4;97;45mOlá, Mundo!\033[m')

# PODEMOS SIMPLIFICAR AS CORES FAZENDO UMA LISTA

cores = {'fim':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'pretoebranco':'\033[7;97m'}
py = 'PYTHON'
print('Teste de cores para aumentar vocabulario no programa {}{}{}!!'.format(cores['pretoebranco'], py, cores['fim']))
