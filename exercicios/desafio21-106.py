def int_help(command):
    from time import sleep
    while True:
        operation = input(f"\033[1m{command}\033[m")
        if operation == "quit":
            break
        else:
            sleep(0.5)
            print(f"\033[1;31;40mloading", end="")
            for dot in range(0, 3):
                print(".", end="")
                sleep(1)
            print("\n", end="")
            print("\033[30;46m")
            print(f"\033[46m{help(operation)}")
            print("\033[m", end="")


int_help(str("\033[1mFunction or Library >\033[m "))

