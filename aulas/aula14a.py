'''for c in range (1, 10):
    print(c)
print("fim")'''
"""c = 1
while c < 10:
    print(c)
    c += 1
print("fim")"""
"""for n in range (1, 5):
    print(n)
print("fim")"""
"""n = 1
while n != 0:
    n = int(input("digite um valor: "))
print("fim")"""
"""r = "s"
while r == "s":
    n = int(input("digite um valor: "))
    r = str(input("quer continuar? [s/n] ")).lower()
print("fim")"""
n = 1
par = impar = 0
while n != 0:
    n = int(input("digite um valor: "))
#poderia colocar nessa linha um: if n != 0 para n prescisar colocar em baixo
    if n % 2 == 0 and n != 0:
        par += 1
    elif n != 0:
        impar += 1
print("Houve {} numeros pares e {} numeros impares.".format(par, impar))
print("acabou")
