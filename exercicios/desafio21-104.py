def readint(num):
    num = input(num)
    if num.isnumeric() is True:
        return num
    else:
        while num.isnumeric() is False:
            print("\033[31mErro! this isn't integer. try again!\033[m")
            num = str(input("Enter a integer: "))
        return num


number = readint(f"Enter a integer: ")
print(f"The number typed is {number}")
