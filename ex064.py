num = cont = soma = 0 #soma, cont e num é todos igual a 0, pode colocar na mesma linha
'''cont = 0
soma = 0'''
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        print('FIM')


print('Voce digitou {} números e a soma deles foi {}'.format(cont, soma))

