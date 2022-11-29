salario = float(input('digite seu salario: R$'))
if salario>1250:
    print('o seu novo salario e de R${:.2f}'.format(salario+salario*10//100))
else:
    print('o seu novo salario e de R${:.2f}'.format(salario+salario*15//100))
print('parabens nigga!')