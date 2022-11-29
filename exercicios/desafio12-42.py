print('lados do triangulo')
l1 = float(input('lado 1: '))
l2 = float(input('lado 2: '))
l3 = float(input('lado 3: '))
tri = l1< l2+l3 and l2< l1+l3 and l3< l1+l2
if l1 == l2 == l3 and tri:
    print('this triangulo is equilatero :)')
elif l1 == l2 or l1 == l3 or l2 == l3 and tri:
    print('este triangulo é isoceles')
elif l1 != l2 and l1 != l3 and l3 != l2 and tri:
    print('este triangulo é  escaleno')
else:
    print("estas medidas nao formam um triangulo")
