numeros = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um valor! '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    if resp in 'Nn':
        break
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par} ')
print(f'A lista de impares é {impar} ')