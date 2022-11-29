more = less = 0
namem = []
namel = []
lista = []
mapping = []

while True:
    name = str(input("Enter your name: "))
    weight = int(input("Enter your weight: "))
    lista.append(name), lista.append(weight)#Em lista acrecente nome
    mapping.append(lista[:])
    lista.clear()
    stop = str(input("You want continue? [Y/N]")).lower().strip()[0]
    while stop != "y" and stop != "n":
        stop = str(input("You want continue? [Y/N]")).lower().strip()[0]
    if stop == "n":
        break
print('-_-'*20)
print(f"Were registered {len(mapping)}")
if len(mapping) == 1:
    namem.append(mapping[0]), namel.append(mapping[0])
else:
    for c, w in enumerate(mapping):
        if c == 0:
            more = w[1]
            less = w[1]
            namem.append(w[0]), namel.append(w[0])
        elif w[1] >= more:
            if w[1] == more:
                namem.append(w[0])
            elif w[1] > more:
                namem.clear()
                namem.append(w[0])
            more = w[1]
        elif w[1] <= less:
            if w[1] == less:
                namel.append(w[0])
            elif w[1] < less:
                namel.clear()
                namel.append(w[0])
            less = w[1]
if len(mapping) == 1:
    print(f"Only one person registered {mapping[0][0]} than weighs {mapping[0][1]}")
else:
    print(f"The heaviest is ", end="")
    for namem in namem:
        print(namem, end=", ")
    print(f"than weigh {more}.")
    print(f"The lightest is ", end="")
    for namel in namel:
        print(namel, end=", ")
    print(f" than weigh {less}.")


#caralho borracha era so criar uma copia da main list depois de fazer as analizes do q é maior ou menor
#sem contar q era so fazer uma lista, e trbalhar com posições pares e impares, ou 0, 1  caso usasse o modo a cima
#olhar verção de guanabara ficou muito mais otimizado(print dos nomes das pessoas mais e menos pesadas)