nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em lhe conhecer!\n'
      f'Seu primeiro nome é {nome[0].title()}\n'
      f'Seu ultimo nome é {nome[-1].title()}')
