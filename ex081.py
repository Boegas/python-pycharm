numeros = list()
nd = 0
num5 = 0

while True:
    num = int(input('Digite um valor: '))
    if num == 5:
        num5+= 1
    numeros.append(num)
    print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    nd += 1
    if resp in 'Nn':
        break
print(f'Você digitou {nd} elementos')
numeros.sort(reverse = True)
print(f'Os valores em ordens decrescentes são {numeros}')
if num5 > 0:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')







