# PROGRAMA QUE LER IMC
# PROGRAMAR INFORMAR STATUS DE ACORDO COM A TABELA
# 18,5 = ABAIXO DO PESO
# ENTRE 18.5 E 25 PESO IDEAL
# 25 A 30 SOBREPESO
# 30 A 40 OBESIDADE
# ACIMA DE 40 OBESIDADE MORBIDA


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

# ABAIXO DO PESO
if imc < 18.5:
    print('Abaixo do peso')
# PESO IDEAL
elif 18.5 <= imc < 25:
    print('Peso ideal')
# SOBREPESO
elif 25 <= imc < 30:
    print('Sobrepeso')
# OBESIDADE
elif 30 <= imc < 40:
    print('Obesidade')
# OBESIDADE MÓRBIDA
else:
    print('Obesidade Mórbida')

















