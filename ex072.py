cont = ('zero', 'um', 'dois', 'tres', 'Quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenone', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'N':
            break

    print('Tente novamente. ', end='')
print(f'Você digitou o numero {cont[num]}')





