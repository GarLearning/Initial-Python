sum = num = count = 0
while True:
    num = int(input("Enter a number: [999 for STOP] "))
    if num == 999:
        break
    sum += num
    count += 1
print(f"Was typed {count} and the sum between them is {sum}.")
