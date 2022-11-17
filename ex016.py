import math #pode fazer de outra maneira. linha 1 colocar from math import e linha 3 apagar o nome math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

'''pode fazer da uma maneira sem importar nada
num = float(input('Digite um valor: '))\
print('O valor digitado foi {} e a porção inteira é {}`.format(num, int(num)))'''