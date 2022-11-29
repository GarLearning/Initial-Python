print('digite o numero e precione enter!!')
n1 = int(input('numero 1:'))
n2 = int(input('numero 2:'))
n3 = int(input('numero 3:'))
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('o menor numero é {} e o maior numero é {}'.format(menor, maior))