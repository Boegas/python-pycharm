print('{:=^40}'.format(' LEIA DOIS VALORES '))
n1 = int(input('Escolha o primeiro numero! '))
n2 = int(input('Escolha o segundo numero '))
opção = 0
print('Os numeros escolhidos foram {} e {}! '.format(n1, n2))
while opção != 5:
    print('''QUAL É A SUA OPÇÃO?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('>>>>>Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, (n1+n2)))
    elif opção == 2:
        print('O resultado da multiplicação ente {} x {} é {}'.format(n1, n2, (n1 * n2)))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} é {}'.format(n1, n2, maior ))
    elif opção == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Escolha o primeiro numero! '))
        n2 = int(input('Escolha o segundo numero '))
        print('Os numeros escolhidos foram {} e {}! '.format(n1, n2))
    elif opção == 5:
        print('Fim do programa! Volte sempre! ' )
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim de programa! volte sempre!')

