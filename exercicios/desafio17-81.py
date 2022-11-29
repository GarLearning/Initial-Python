cont = 0
lista = []
while True:
    num = int(input("Enter a number [ENTER 0 TO STOP]: "))
    if num == 0:
        break
    lista.append(num)
print(f"Were typed {len(lista)} terms.")
lista.sort(reverse=True)
dot = len(lista)
print("The terms typed in order reverse are ", end="")
for l in lista:
    print(f"{lista[cont]}", end=", " if cont+1 < dot else ".")
    cont += 1
if lista.count(5) != 0:
    print(f"\nThe number five was typed {lista.count(5)} times.")
else:
    print(f"\nThe number five not was typed.")
