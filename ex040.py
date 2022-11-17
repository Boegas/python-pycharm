n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
média = (n1+n2)/2
print('A média do aluno foi {:.2f}!'.format(média))
if média >= 7.0:
    print('O aluno está APROVADO. ')
elif média < 7.0 and média >= 5.0:
    print('O aluno ficou em RECUPERAÇÃO. ')
else:
    print('O aluno está REPROVADO')