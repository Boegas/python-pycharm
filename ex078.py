listanum = []
mai = 0
men = 0
for c in range(0, 5):
     listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
     if c == 0:
          mai = men = listanum[c]
     else:
          if listanum[c] > mai:
               mai = listanum[c]
          if listanum[c] < men:
               men = listanum[c]

print ('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor sorteado foi {mai} que esta na posição ', end='')
for i, v in enumerate(listanum): # i = indice  v = valor
     if v == mai:
          print(f'{i}...', end='')
print()
print(f'O menor numero sorteado foi {men} que esta na posição ', end='')

for i, v in enumerate(listanum):
     if v == men:
          print(f'{i}...', end='')
print()

'''from random import randint
n = [randint(1, 10) ,randint(1, 10) ,randint(1, 10) ,
     randint(1, 10) ,randint(1, 10)]
print(f'Os valores sorteados foram {n}')
print(f'O maior valor sorteado foi {max(listanum)} que esta na posição ', end='')

print(f'O menor numero sorteado foi {min(listanum)} que esta na posição ' end='')'''