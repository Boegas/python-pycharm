n = s = d = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        d += 1
    if n == 999:
        break
print(f'Foram digitados {d} números e a  soma vale {s}')







'''n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n'''
'''print('A soma vale {}'.format(s))''' # posso trocar por
'''print(f'A soma vale {s}')'''