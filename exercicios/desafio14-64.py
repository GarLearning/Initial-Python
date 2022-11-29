count = sum = num = 0
while num != 999:
    num = int(input("Enter a number: [999 for stop]"))
    if num != 999:
        sum += num
        count += 1
print("Have been added {} numbers, and the sum of the numbers typed has been {}".format(count, sum))