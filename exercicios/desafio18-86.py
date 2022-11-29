count = count1 = 0
lista = []
for m in range(0, 9):
    matrix = int(input(f"Enter a number for the matrix [{count}, {count1}]: "))
    if count1 < 2:
        count1 += 1
    if count1 == 3:
        count += 1
        count1 = 0
    lista.append(matrix)
print()
print(f"-_-_-The matrix is-_-_-")
print(f"[{lista[0]:^5}] [{lista[1]:^5}] [{lista[2]:^5}]")
print(f"[{lista[3]:^5}] [{lista[4]:^5}] [{lista[5]:^5}]")
print(f"[{lista[6]:^5}] [{lista[7]:^5}] [{lista[8]:^5}]")
# 00 01 02
# 10 11 12
# 20 21 22

"""matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]#os 00000 sao colocados para tirar a necessidade do append
for l in range(0, 3):
    for m in range(0, 3):
        matrix[l][m] = (int(input(f"Enter a number [{l}, {m}]")))
print("-" * 30)
for l in range(0, 3):
    for m in range(0, 3):
        print(f"[{matrix[l][m]:^5}]")
    print()"""