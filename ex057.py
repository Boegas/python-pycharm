sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

