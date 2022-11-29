maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("say the {}ª weight: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
#    if peso>peso:
#        maior = peso
#    elif peso<peso:
#        menor = peso
print("The bigger weight is {} Kg. \nThe smaller weight is {} Kg.".format(maior, menor))
