for c in range(1, 5):
    print(c)
print("fim")
for c in range(5, 1, -1):
    print(c)
print("fim")
for c in range(0, 10, 2):
    print(c)
print('fim')
#for c in range(0, 21):
#    print("oi {}".format(c%2==0))
#print("fim")
n = int(input('digite um numero:'))
for c in range(0, n+1):
   s = c%2
   if s == 0:
        print('par{}'.format(c))
print('fim')
d = 0
for c in range(1, 3):
    n = int(input("digite um d:  "))
    d +=n #d = d + n
print(d)
print('fim')

inicio = int(input('digite inicio'))
fim = int(input('digite fim'))
passo = int(input("digite o passo "))
for c in range(inicio, fim, passo):
    print(c)
