print("{:-^50}".format("Sequence of the Fibonacci"))
sequence = int(input("Amount of terms in the sequence of Fibonacci: "))
count = 0
count2 = 0
a = 0
b = 1
while count < sequence:
    if count == 0:
        print(a, end=", ")
    else:
        if count % 2 == 0:
            print("{}".format(a + b), end=", " if count < sequence - 1 else "")
            a = a + b
        else:
            print("{}".format(a + b), end=", " if count < sequence - 1 else "")
            b = a + b
    count += 1
    count2 += 1
    if count2 == 14:
        print("\n")
        count2 = 0
print("\n{:-^50}".format("END"))