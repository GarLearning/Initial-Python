#-------------listas-------------
lanche = ["juice", "pizza", "pudding", "hamburger"]
lanche[3] = "popsicle"
print(lanche)#substitui o valor
#listas funcionam da mesma forma que tupulas, porem sao mutaveis
#substituição, adção de elementos
lanche.append("cook")#add o valor ao final da lista
print(lanche)
#esse comando adiciona um elemento a lista
lanche.insert(0, "hot dog")
#adiciona um elemento na posição desejad, nesse caso 0
print(lanche)
lanche.pop()#remove o ultimo elemento de uma lista
del lanche[3] #or lanche.pop(3), esse metodo elimina o ultimo elemento normalmente(testa se n declarando ele elimina o ultimo)
print(lanche)
lanche.remove("juice")#interessante pois usa o valor(juice) e n o indice do juice(0), ele elimina a 1º ocorrencia do juice caso tivece mais so eliminaria o 1º.
print(lanche)
lanche.clear()#esse comando limpa tudo dentro de lanche
print(lanche)
# ao remover algo que não existe da erro, mais da para conferir se o elemento exist:
if "pizza1" in lanche:
    lanche.remove("pizza1")
else:
    print("term not found")
print(lanche)
# nesse exemplo a lista é disposta em valores ordenado no range a seguir
valores = list(range(4, 11))
# assim ele fica fora da ordem
valores = [8, 5, 4, 1, 6, 5]
# agora ordena os valores em ordem crescente
valores.sort()
# e agora de forma decrescente
valores.sort(reverse=True)
#quantos elementos == 7
len(valores)
#existem 2 opições para criação de uma lista
    #1 - valores = []
    #2 - valores = list()
"""count = count2 = 0
value = list()
#value = []
#value.append(1)
#value.append(3)
#value.append(5)
for count1 in range(0, 5):
    value.append(int(input("Enter the number: ")))
for p, v in enumerate(value):
    count += 1
    print(f"The {v} is in the position {p+1}, the position")
"""
a = [2, 3, 5, 6]
b = a
b[2] = 4
print(f"list {a}")
print(f"list {b}")
# em python ao alterar um parametro em uma lista da qual recebeu outra(list b q recebeu a), o parametro é alterado em ambas pois a linguagem faz uma
#ligação entre as duas listas substituindo nas 2 o que teoricamente foi alterado so em uma
print(f"{'-'*20}")
b = a[:]
b[2] = 8
print(f"list {a}")
print(f"list {b}")
#porem se fizer com q b receba todos os itens de a ([:]- fatiamento pega do 1 ate o ultimo), ele cria uma copia e ñ uma ligação entre as 2 listas
#obs:. a ficou alterado por isso vale 4 a posição 29
for a in a:
    print(a)
