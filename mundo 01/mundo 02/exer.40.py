# PROGRAMA QUE LEIA DUAS NOTAS DE 1 ALUNO CALCULANDO SUA MEDIA
# MENOR QUE 5 REPORVADO ENTRE 5 E 6.9 RECUPERAÇÃO E MAIOR Q 7 APROVADO



nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = nota1 + nota2 / 2

if media >= 7:
    print('Você atingiu a média, está APROVADO')

elif media >= 5:
    print('Você ainda nao alcançou a média, mas podera ter uma nova chance, esá de RECUPERAÇÃO')

else:
    print('Você nao atingiu a média, está REPROVADO')









