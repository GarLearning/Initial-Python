"""def factorial(number_factorial, show):
    print("¨" * 40)
    decreasing = number_factorial
    operation_factorial = number_factorial
    if show == "yes":
        print(f"The factorial of {number_factorial}! is: ", end="")
    else:
        print(f"The factorial of {number_factorial}! is: ", end="")
    while decreasing > 0:
        if show == "yes":
            print(f"{decreasing}", end="." if decreasing > 1 else " = ")
        operation_factorial += decreasing
        decreasing -= 1
    print(operation_factorial)


number = int(input(f"Enter a value of the factorial: "))
operation = str(input("You want see the operation? [yes/no] "))
factorial(number, operation)
"""


def factorial(number_factorial, show=False):
    print("¨" * 40)
    decreasing = number_factorial
    operation_factorial = number_factorial
    if show:
        print(f"The factorial of {number_factorial}! is: ", end="")
    else:
        print(f"The factorial of {number_factorial}! is: ", end="")
    while decreasing > 0:
        if show is True:
            print(f"{decreasing}", end="." if decreasing > 1 else " = ")
        decreasing -= 1
        if decreasing != 0:
            operation_factorial *= decreasing
    print(operation_factorial)
#duas formas de trabalhar com valores logcos: n declarando no if pq ja usa a declaração feita anteriomente e declarando


factorial(5, show=True)
