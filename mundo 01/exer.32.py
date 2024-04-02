import datetime
num = int(input('Digite o ano que gostaria de saber ou 0 (zero) para saber ano atual se é bissesto ou não: '))

anos = num % 4

agora = datetime.datetime.now()
data = agora.date()
ano = data.strftime("%Y")


if anos == 0 and num % 100 != 0 or num % 400 == 0:
    print('Este Ano é Bissesto!')

elif num == 0:
    atual = ano % 4 == 0 and num % 100 != 0 or num % 400 == 0
    print('O ano atual é Bissesto')
elif num == 0:
    atual = ano % 4 == 1 and num % 100 != 0 or num % 400 == 0
    print('O ano atual não é Bissesto')

else:
    print('Este ano NÃO é Bissesto!')














