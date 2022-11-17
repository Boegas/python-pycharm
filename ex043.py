peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('Seu imc esta em {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso! ')
elif 18.5 <= imc < 25:
    print('Você esta no PESO IDEAL! ')
elif  25 <= imc < 30:
    print('Você esta com SOBREPESO! ')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE! ')
elif imc > 40:
    print('Você esta com OBESIDADE MORBIDA. CUIDADO! ')