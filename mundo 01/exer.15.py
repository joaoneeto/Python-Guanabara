d = int(input('Quanto dias alugados: '))
km= float(input('Quantos km rodados: '))
t = (d * 60) + (km * 0.15)
print(f'o valor a pagar é R${t:.2f} por {d} alugado e {km:.2f}km rodados')