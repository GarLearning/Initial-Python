s=0
for n in range(1, 7):
    num = int(input("type a number: "))
    if num % 2 ==0:
        s+= num
print("the sum of the numbers pair is: {}".format(s))