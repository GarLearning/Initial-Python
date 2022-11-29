import wwcoin
print("Operations with coins")
coin = float(input("Enter the value: $"))
wwcoin.line()
print("Choice a operation: "
      "\n[1] increase."
      "\n[2] decrease."
      "\n[3] double."
      "\n[4] half."
      "\n[5] Get out")
wwcoin.line()
while True:
    while True:
        option = str(input("Enter your choice: "))
        if option in "12345":
            break
    if option == "1":
        percent = int(input("How many percent of the value do you want increase? "))#n accept % after number
        result = wwcoin.increase(coin, percent)
        print(f"--More {percent}% in ${coin:.2f} is ${result:.2f}")
    elif option == "2":
        percent = int(input("How many percent of the value do you want decrease? "))#n accept % after number
        result = wwcoin.decrease(coin, percent)
        print(f"--Less {percent}% in ${coin:.2f} is ${result:.2f}")
    elif option == "3":
        result = wwcoin.double(coin)
        print(f"--The double of ${coin:.2f} is ${result:.2f}")
    elif option == "4":
        result = wwcoin.half(coin)
        print(f"--The half of ${coin:.2f} is ${result:.2f}")
    elif option == "5":
        while True:
            stop = str(input("Do you want enter other value [Y/N]? ")).lower()
            if stop in "ny":
                break
            else:
                print("\033[31mThis isn't accept. try again!\033[m")
        if stop == "n":
            break
        else:
            coin = float(input("Enter the value: "))
            wwcoin.line()
            print("Choice a operation: "
                  "\n[1] increase."
                  "\n[2] decrease."
                  "\n[3] double."
                  "\n[4] half."
                  "\n[5] Get out")
    wwcoin.line()
