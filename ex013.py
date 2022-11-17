s = float(input('Qual o salario de um funcionario? '))
a = (15/100)
ns = s + (s*a) #poderia trocar esses 2 linha por essa ns = s + (s * 15/100)
print('salario atual {:.2f}R$. Seu novo salario é {:.2f}R$. '.format(s,ns))