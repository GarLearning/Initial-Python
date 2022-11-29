count = count1 = pair = 0
lista = []
for m in range(0, 9):
    lista.append(int(input(f"Enter a number for matrix: [{count}, {count1}]")))
    if count1 < 2:
        count1 += 1
    else:
        count += 1
        count1 = 0
print()
print(f"-_-_-The matrix is-_-_-")
print(f"[{lista[0]:^5}] [{lista[1]:^5}] [{lista[2]:^5}]")
print(f"[{lista[3]:^5}] [{lista[4]:^5}] [{lista[5]:^5}]")
print(f"[{lista[6]:^5}] [{lista[7]:^5}] [{lista[8]:^5}]")
print("-_-_-_-_-_-_-_-_-_-_-_-_-")
for p in lista:
    if p % 2 == 0:
        pair += p
if pair != 0:
    print(f"The sum of value pairs typed is: {pair}.")
else:
    print("Not found values pair.")
print(f"The sum of 3th column is: {lista[2]+lista[5]+lista[8]}.")
print(f"The bigger value of the line 2 is: {max(lista[3:6])}.")