n = int(input('Digite um numero! '))
resultado = n % 2
if resultado == 0:
    print('O numero {} é par!'.format(n))
else:
    print('O numero {} é impar!'.format(n))