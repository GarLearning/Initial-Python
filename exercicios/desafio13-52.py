print("¨¨how know if it is a prime number¨¨")
div = 0
primo = int(input("type: "))
for n in range(1, primo+1):
    if primo % n == 0:
        print('\033[32m', end=' ')
        div += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(n), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(primo, div))
if div == 2:
        print("this number is prime.")
else:
        print("this number not's prime.")