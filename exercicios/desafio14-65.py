bigger = lower = sum = num = count = average = 0
stop = "yes"
if stop == "yes" or stop == "no":
    #while stop == "yes":
    while stop in "yes":#correçao(do jeito de cima tb funciona), erro que deu quando interagi com numero, TypeError: argument of type 'int' is not iterable
        num = float(input("Enter a number: "))
        count += 1
        sum += num
        if count == 1:
            bigger = lower = num
        if num > bigger:
            bigger = num
        elif num < lower:
            lower = num
        if count != 1:
            stop = str(input("You wish continue: [yes, no]"))
            if stop != "yes" and stop != "no":
                print("This option not is accept.")
average = sum/count
print("Have been typed {} numbers, and the average is {}.".format(count, average))
print("The bigger was {}, and the lower was {}".format(bigger, lower))
