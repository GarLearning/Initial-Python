"""bigger = lower = sum = num = count = 0
bigger = 20
lower = 10
sum = 10
print(lower, sum, bigger, num)
avarage = (sum + lower) / 5
print(avarage)"""
"""num = count = 60
if count == 60:
    while True:
        if num > 50:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                break
                print("haha")
    print(f"{num+10}")
print("fim")"""
"""while True:
    sex = str(input("sexo: "))
    if sex != "male" and sex != "female":
        print(sex)
    else:
        print("errado")


if value > 1000:
    thousand = value // 1000
    resto = value % 1000
    value = resto
    print(thousand)
if value > 100:
    hundred = value // 100
    resto = value % 100
    value = resto
    print(hundred)
if value > 10:
    decimal = value // 10
    resto = value % 10
    value = resto
    print(decimal)
if value > 0:
    casa = value // 1
    print(casa)
print("- " * 20 )"""
"""player = "eo"
while "eo" in player:
   player = str(input("EVEN OR ODD: [E/O]")).lower().strip()[0]"""


def compareTriplets(a, b):
   ali = 0
   bob = 0
   for m in range(0, 3):
      if a[m] > b[m]:
         ali += 1
      if a[m] < b[m]:
         bob += 1
   return list(ali, bob)

num1 = 1, 2, 3
num2= 1, 5, 2
i = compareTriplets(num1, num2)
print(i)