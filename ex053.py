frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa poir palavras
junto = ''.join(palavras)#substitui o espaço pelo que esta dentro do ''
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo! ')
else:
    print('a frase digitada não é um palíndromo! ')