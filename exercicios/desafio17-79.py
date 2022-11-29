count = 0
stop = "y"
num = []
result = []
while True:
    num.append(int(input("Enter a number: ")))
    if num.index(num[count]) == count:
        result.append(num[count])
    count += 1
    stop = str(input("You want continue: [yes/no]")).strip().lower()[0]
    while stop != "y" and stop != "n":
        print("This option not accept. try again!!!")
        stop = str(input("You want continue: [yes/no]")).strip().lower()[0]
    if stop == "n":
        break
result.sort()
print("The numbers typed are: ")
for result in result:
    print(result, end=" => ")
print("...")


#ele uso"if num not in result"