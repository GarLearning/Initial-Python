print('digite os lados do triangulo')
a = int(input('digite o lado a:'))
b = int(input('digite o lado b:'))
c = int(input('digite o lado c:'))
if a< b+c and b< a+c and c< b+a:
    print('\033[1;35mÉ possivel formar um triandulo!!\033[m')
else:
    print('\033[4;31m nao sera possivel formar um triangulo!!\033[m')
