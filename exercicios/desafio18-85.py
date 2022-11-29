lista = [[], []]
for n in range(0, 7):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"These numbers are pair {lista[0]}.")
print(f"These numbers are odd {lista[1]}.")
