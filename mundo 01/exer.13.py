s = float(input('Qual salário do funcionário: R$'))
p = float(input('Qual a porcentagem de aumento: %'))
r = s + ( s * p / 100)
a =  s * p / 100
print(f' O valor atual do seu salário é de R${s:.2f} e passará a ser R${r:.2f}\n com um aumento de R${a:.2f}')