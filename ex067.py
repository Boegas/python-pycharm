print('Quer ver a tabuada de qual valor? ')
print('--'*15)
while True:
    n = int(input('escolha um numero '))
    if n < 0:
        print('--' * 15)
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        print('--' * 15)
        break
    for c in range(1, 11 ):
        print(f' {n} * {c:2} = {n*c}')
    print('--' * 15)




