from datetime import date
nascimento = int(input('Qual o ano que voce nasceu? '))
ano = date.today().year
idade = ano-nascimento
falta = 18-idade
alistamento = falta+ano
passou = idade-18
foi = ano-passou
imediatamente = idade==18
print('A sua idade é de {} anos'.format(idade))
if idade < 18:
    print('Quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, ano ))
    print('Ainda faltam {} anos para o alistamento!'.format(falta))
    print('Seu alistamento será em {}!'.format(alistamento))
elif idade > 18:
    print('Quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, ano))
    print('Você ja deveria ter se alistado há {} anos!'.format(passou))
    print('Seu alistamento foi em {}!'.format(foi))
else:
    print('Quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, ano))
    print('Você tem que se alistar IMEDIATAMENTE! ')
