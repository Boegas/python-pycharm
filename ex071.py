print('-='*15)
print('BANCO BOEGAS')
print('-='*15)
valor = int(input('Qual será o valor a ser sacado? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-='*15)
print('VOLTE SEMPRE AO BANCO BOEGAS')
print('-='*15)
