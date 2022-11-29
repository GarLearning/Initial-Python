def area(length, width):
    print(f"The area equivalent the {length}x{width} = {a*b}².")


#program principal
while True:
    print(f"---calculation of area---")
    a = float(input("length (m): "))
    b = float(input("width (m): "))
    area(a, b)
    while True:
        stop = str(input("You want continue [Y/N]?")).lower().strip()[0]
        if stop in "yn":
            break
        else:
            print(f"Try again, this option {stop} not accept.")
    if stop in "n":
        break
print("<<<END PROGRAM>>>")
