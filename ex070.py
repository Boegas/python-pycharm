compra = 0
mil = 0
menor = 0
cont = 0
barato = ''
print('-='*15)
print('LOJAS BOEGAS BARATÃO')
print('-='*15)
continuar = ' '
while True:
    produto = str(input('Nome do produto! '))
    preço = float(input('Preço:R$ '))
    cont += 1
    compra += preço
    mil = (preço >= 1000)+1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*8, 'FIM DE PROGRAMA', '-='*8)
print(f'O total de compra foi {compra:.2f}:R$')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}R$')



