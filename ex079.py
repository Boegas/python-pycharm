numeros = list()
while True:
    num = int(input('Digite um numero : '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
numeros.sort() #deixar os numeros em ordens
print(f'Voce digitou os valores {numeros}')


