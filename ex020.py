from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista= [n1, n2, n3, n4]  #uma lista tem que estar dentro de []]
shuffle(lista) #shuffle = embaralhar
print('A ordem de apresentação será ')
print(lista)