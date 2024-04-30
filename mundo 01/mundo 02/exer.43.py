# PROGRAMA QUE LER IMC
# PROGRAMAR INFORMAR STATUS DE ACORDO COM A TABELA
# 18,5 = ABAIXO DO PESO
# ENTRE 18.5 E 25 PESO IDEAL
# 25 A 30 SOBREPESO
# 30 A 40 OBESIDADE
# ACIMA DE 40 OBESIDADE MORBIDA



def calcular_imc(peso, altura):
    try:
        imc = peso/(altura*altura)
    finally:

        return imc

def status_imc(imc):

# ABAIXO DO PESO
    if imc < 18.5:
        status = 'Abaixo do peso'
# PESO IDEAL
    elif 18.5 <= imc < 25:
        status = 'Peso ideal'
# SOBREPESO
    elif 25 <= imc < 30:
        status = 'Sobrepeso'
# OBESIDADE
    elif 30 <= imc < 40:
        status = 'Obesidade'
# OBESIDADE MÓRBIDA
    else:
        status = 'Obesidade Mórbida'
    return status


# TENTANDO UTILIZAR O QUE APRENDI DE EXCESSOES
while True:
    try:
        peso = float(input('Digite seu peso: '))
        altura= float(input('Digite sua altura: '))

        break
    except ValueError:
        print('APENAS NUMERO E NO LUGAR DE VIRGULA(,), COLOQUE PONTO(.)')


# Calcular o IMC
imc = calcular_imc(peso, altura)

# Determinar o status do IMC
status = status_imc(imc)

print('De acordo com seu IMC, seu status é {}'.format(status))

