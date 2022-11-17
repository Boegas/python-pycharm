from random import randint
from time import sleep
computador = randint(0, 9) # faz computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('Sera que voce consegue adivinhar qual foi? ')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos ... Tente mais uma vez;')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
'''jogador = int(input('Em que número eu pensei?')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador < computador:
    print('VOCÊ ERROU! O número que escolhi é {}'.format(maior))
elif jogador > computador:
    print('VOCÊ ERROU! O número que escolhi é {}'.format(menor))
else:
    print('PARABÉNS! Você conseguiu me vencer!')'''