print('-='*20)
print('Analisador de triangulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 == r3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO! ')
elif r1 == r2 and r1 == r3 and r2 == r3:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
elif r1 != r2 != r3 != r1:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo')