count = 0
lista = []
for n in range(0, 5):
    num = int(input("Enter a number: "))
    if n == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
for lista in lista:
    print(lista, end=", " if count != 4 else ".")
    count += 1