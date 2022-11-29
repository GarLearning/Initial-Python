num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
option = 0
while option != 5:
    print("""Choice a option
    \033[34m[1]Sum
    \033[33m[2]Multiplication
    \033[32m[3]Highest value
    \033[35m[4]New numbers 
    \033[30m[5]Exit to program\033[m""")
    option = int(input("Enter a option: "))
    if option == 1:
        print("The option chosen was \033[34m[1]Sum.\n\033[1;34mThe result of operation is {}.\033[37m".format(num1 + num2))
    elif option == 2:
        print("The option chosen was \033[33m[2]Multiplication.\n\033[1;33mThe result of operation is {}.\033[37m".format(num1 * num2))
    elif option == 3:
        if num1 > num2:
            print("The option chosen was \033[32m[3]Highest value.\n\033[1;32mThe result of operation is {}.\033[37m".format(num1))
        elif num2 > num1:
            print("The option chosen was \033[32m[3]Highest value.\n\033[1;32mThe result of operation is {}.\033[37m".format(num1))
        elif num1 == num2:
            print("The option chosen was \033[32m[3]Highest value.\n\033[1;32mThe numbers are equals .\033[37m")
    elif option == 4:
        print("The option chosen was \033[1;35m[4]New numbers.\033[m")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    elif option !=5:
        print("\033[1;31mOption not accepted, try again.\033[m")
if option == 5:
    print("\033[30mYou chosen exit to program.\033[m")
