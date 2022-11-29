lista = []
average = ["", 0, 0]
student = []
count = 0
while True:
    average[0] = str(input("Enter a name: ")).capitalize().strip()
    average[1] = float(input("Enter the first note: "))
    average[2] = float(input("Enter the second note: "))
    lista.append(average[:])
    average = ["", 0, 0]
    stop = ""
    while stop != "yes" and stop != "no":
        stop = str(input(f"Do you want continue [YES/NO]: ")).lower().strip()
    if stop == "no":
        break
average.clear()
for a in lista:
    result = (a[1] + a[2]) / 2
    average.append(result)
print(f"{'School Report':-^33}")
print(f"\n\033[1m{'Id':<5}{'Name':^15}{'average':>10}\033[m")
for i, n in enumerate(lista):
    print(f"{i:-<7}{n[0]:-<15}{average[count]:->10.2f}")
    student.append(f"Grade: {i:-<5}{n[0]:-<15}{lista[count][1]:->10.2f}, {lista[count][2]:.2f}")
    count += 1
individual_s = int(input("\nEnter a position of a student specific [999 for stop]: "))
while individual_s != 999:
    print(f"{student[individual_s]}")
    individual_s = int(input("\nEnter a position of a student specific [999 for stop]: "))
#str aceita inteiro, float
#pq a linha 24 da erro quando coloco {lista[count][1:2]:->10.2f}, (o problema esta depois do colchete":->10.2f", da algum conflito com os : sendo usado 2 vezes???)
