km = float(input('Quantidade de km percorrido? '))
d = int(input('Quantidade de dias alugado? '))
diaria = 60*d
km = km*0.15
total = diaria+km
print(' Valor da diaria? {:.2f} R$,\n valor do km percorrido? {:.2f} R$,\n total do aluguel? {:.2f} R$'.format(diaria, km, total))