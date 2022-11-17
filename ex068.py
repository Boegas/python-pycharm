from random import randint
V = 0
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':  #Enquanto tipo nao for PI
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-='*15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            V += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            V += 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {V} vezes. ')




