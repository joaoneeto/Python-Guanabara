from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que vc deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print(f'O ângulo de {a} tem o SENO de {seno:.2f}')
print(f'O ângulo de {a} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {a} tem a TANGENTE de {tan:.2f}')