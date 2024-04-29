# UM PROGRAMA QUE LEIA DATA DE NASCIMENTO DE UMA PESSOA E MOSTRE A IDADE
# DE ACORDO COM A IDADE MOSTRA CATEGORIA QUE ELA REPRESENTA NA NATAÇÃO
# ATE 9 ANOS = MIRIM  ATE 14 = INFATIL ATE 19 = JUNIOR ATE 20 = SENIOR ACIMA MASTE
from datetime import datetime

ano = int(input('Digite o ano de nascimento: '))
mes = int(input('Digite mês de nascimento(apenas número): '))
dia = int(input('Digite o dia de nascimento: '))

nascimento = datetime(ano, mes, dia)

# ano atual
atual = datetime.today()

diferenca = atual - nascimento

# a idade ja convertida
anos = diferenca.days // 365



if anos <= 9:
    categoria = 'MIRIM'
elif anos <= 14:
    cagetoria = 'INFATIL'
elif anos <= 19:
    categoria = 'JUNIOR'
elif anos <= 20:
    categoria = 'SÉNIOR'
else:
    categoria = 'MASTER'
print('A categoria de acordo com data informada de {} anos é {}.'.format(anos,categoria))
























