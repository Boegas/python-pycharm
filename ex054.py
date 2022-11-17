from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade <= 21:
       totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoa maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoa menores de idade'.format(totmenor))
