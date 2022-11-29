print("--Factorial of the number--")
numb = int(input("Enter the number for yor factorial: "))
nu = numb
fac = 1
while nu != 0:
    print("{}".format(nu), end="")
    print(" x " if nu != 1 else " = ", end="")
    fac = fac * nu
    nu -= 1
print("{}".format(fac))
