#funciona com ou sem parenteses
#lanche = tuple()
lanche = ("Hamburger", "juice", "Pizza", "Pudding")
print(lanche[1], lanche[3], lanche[-2])
#[-2] de traz para frente
print(lanche[2:], "\n", lanche[:2], "\n",  lanche[-2:], "\n",   lanche[:-1], "\n", lanche[0:4:2],
      "\n", lanche[1:2:-1], "\n", lanche[4:0:-2], "\n", lanche[3:4:6])
print("-"*30)
#tuplas são imutaveis
#lanche[2] = "bread"
#print(lanche[2])
#comando n funciona pois n é possivel alterar o valor de uma tupla apois sua declaração inicial
for lunch in lanche:
    print(f"{lunch}")
print("END")
print("-"*30)
cont = 2
for cont in range(0, len(lanche)):
    print(cont, lanche[cont])
#n acontece nada se atribuido um valor no cont devido o cont em for ser só uma contagem para o for
print("- " * 15)
for p, c in enumerate(lanche, start=1):
    print(p, c)
#p == enumerate que está inumerando as posições da vaeriavel o c == lanche
#o start = 1 define onde começa a contagem
print(sorted(lanche))
print(lanche)
print("-"*30)
a = (1, 2)
b = (7, 8, 5, 2)
c = a + b
print(a + b)
print(b + a)
print(f"c tem {len(c)} termos")
print(f"o numero 2 aparece {c.count(2)} vezes.")
print(f"o numero 2 aparece pela primeira vez na posição {c.index(2)}")
#len conta quantos termos, cont conta quantas vezes um certo termo aparece, index mostra a primeira vez que um termo apareceu
print(f"o numero 2 contando apartir da posição 3(faz isso para que n escolha o da posição 1) = posição {c.index(2, 3)+1}")
#o len começa a contar do 1 e o index do 0
print("-"*30)
#as tuplas aceitam dados de forma de caracteres e numeros em uma mesma tupula
pessoa = ("Gabriel", 20, "M", 80)
print("\nnome:", pessoa[0], "\nidade:", pessoa[1], "\nsexo:", pessoa[2], "\npeso:", pessoa[3])
#del(pessoa)
print(pessoa)
#tupulas podem ser apagadas por inteiro com o comando del mais n pode-se apagar apenas 1 termo
#tupulas sao valores(numeros, texto, input,) gravados em uma variavel entre () e separados com virgulas