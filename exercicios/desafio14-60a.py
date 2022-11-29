#limitando numeros do resultado e fatiando o farorial
print("\033[30m         --Factorial of the number--")
numb = int(input("Enter the number for your factorial: "))
fac = 1
cout = 0
print("\033[1;32mThe {}! = ".format(numb), end="")
if numb < 10:
    for numb in range(numb, 0, -1):
        print("{}".format(numb), end="")
        print(" x " if numb > 1 else " = ", end="")
        fac *= numb
        numb -= 1
elif numb > 10:
    for numb in range(numb, 0, -1)[:5]:
        cout += 1
        print("{}".format(numb), end="")
        print(" x " if cout != 6 else " ... ", end="")
        print(" ... " if cout == 5 else "", end="")
        fac *= numb
        numb -= 1
#    print(" x ", end="")
    for n in range(5, 0, -1):
        print(n, end="")
        print(" x " if n > 1 else " = ", end="")
print("\033[31m{:5}".format(fac))
#o fatiamento do .format do ultimo print n funciona
#reduz o valor do cout para 5 na linha 17 e tira a linha 18 para tirar o x que vem depois do 5 numero