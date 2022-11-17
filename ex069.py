tot18 = homens = totM20 = 0
while True:
    print('-='*15)
    print('CADASTRE UMA PESSOA')
    print('-='*15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    continuar= ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados foram: {homens}')
print(f'Temos {totM20} mulheres com menos de 20 anos ')




