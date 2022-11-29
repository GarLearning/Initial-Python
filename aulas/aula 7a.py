print("---Operações---")
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
pote = n1 ** n2
raiz = (n1+n2)**(1/2)
print('-Soma: {}. \n-Subtração: {}.'.format(soma, sub))
print('-Multiplicação: {}. \n-Divisão: {:.3f}.'.format(mult, div))
print('-Potência: {}.\n-Divisão inteira: {}.\n-Raiz quadrada da soma entre eles: {:.4}.'.format(pote, div_int, raiz))
#print((n1+n2), end='       ...         ')
#print(n1,  n2)
