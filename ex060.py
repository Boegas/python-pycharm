'''n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n, end=''))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''  #pode ser assim. mais pode ser mais facil

from math import factorial
n = int(input('Digite um numero para calcular seu factorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))