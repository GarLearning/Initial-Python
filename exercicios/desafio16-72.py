numex = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
count = 0
while True:
    num = int(input("Enter a number between 0 and 20: "))
    print(numex[num])
    res = (numex[num])
    count += 1
    stop = str(input("Do you want to continue: [yes/no]")).strip().lower()
    if stop != "yes" and stop != "no":
        print("Option not accept, try again! ")
        stop = str(input("Do you want to continue: [yes/no]")).strip().lower()
    if stop == "no":
        break
print(f"You typed {count} numbers.")
print(res)