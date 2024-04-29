# PROGRAMA QUE DIGA QND IRA TER Q SE ALISTAR (18 ANOS)
# SE AINDA NAO FOR HORA DE SE ALISTAR DIGA QUANDO TEMPO FALTA
# SE JA PASSOU MOSTRE QUANTO TEMPO JA PASSOU

idade = int(input('Informe sua idade: '))


if idade < 18:
    print('Você ainda irá se alistar\n'
          'Ainda falta {} anos para seu alistamento'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar!')
else:
    print('Você já passou do tempo do alistamento\n'
          'Você ja passou {} anos do prazo'.format(idade - 18))






