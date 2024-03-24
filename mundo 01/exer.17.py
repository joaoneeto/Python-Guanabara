import math
caop= float(input('Comprimento do cateto oposto: '))
caad = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(caop, caad)
print(f'A hipotenusa vai medir {hip:.2f}')