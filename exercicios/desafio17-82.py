lista = []
pair = []
odd = []
print(f"{'Numbers typed are pair or odd'}?\n{'[ENTER A NUMBER NEGATIVE FOR STOP]'}")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    lista.append(num)
    if num % 2 == 0:
        pair.append(num)
    else:
        odd.append(num)
count = 1
dot = len(lista)
print(f"\n\033[1;32m{'-'*50}\033[m")
print(f"The numbers typed are: ", end="")
for lista in lista:
    print(lista, end=", " if count < dot else ".")
    count += 1
dot = len(pair)
count = 1
print(f"\n\033[1;32m{'-'*50}\033[m")
print(f"The numbers pair typed are: ", end="")
for pair in pair:
    print(pair, end=", " if count < dot else ".")
    count += 1
dot = len(odd)
count = 1
print(f"\n\033[1;32m{'-'*50}\033[m")
print(f"The numbers odd typed are: ", end="")
for odd in odd:
    print(odd, end=", " if count < dot else ".")
    count += 1
print(f"\n\033[1;32m{'-'*50}\033[m\n")
