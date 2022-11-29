count = 0
value = (int(input("Enter a value: ")), int(input("Enter a value: ")),
         int(input("Enter a value: ")), int(input("Enter a value: ")))
print(f"The value 9 appeared {value.count(9)} times.")
if 3 in value[0:4]:
    print(f"The value 3 was typed for first time in the position {value.index(3) + 1}.")
else:
    print("It was't found the number 3.")
for value in value:
    if value % 2 == 0:
        print(end=", " if count != 0 else "")
        print(value, end="")
        count += 1
print(".")