import wwcoin

print("Operations with coins")
coin = float(input("Enter the value: R$"))
wwcoin.line()
print("Choice a operation: "
      "\n[1] increase."
      "\n[2] decrease."
      "\n[3] double."
      "\n[4] half."
      "\n[5] Get out.")
wwcoin.line()
while True:
    while True:
        option = str(input("Enter your choice: "))
        if option in "12345":
            break
    if option == "1":
        percent = int(input("How many percent of the value do you want increase? "))#n accept % after number
        result = wwcoin.increase(coin, percent)
        print(f"--More {wwcoin.percent(percent)} in {wwcoin.coin(coin)} is {wwcoin.coin(result)}")
    elif option == "2":
        percent = int(input("How many percent of the value do you want decrease? "))#n accept % after number
        result = wwcoin.decrease(coin, percent)
        print(f"--Less {wwcoin.percent(percent)} in {wwcoin.coin(coin)} is {wwcoin.coin(result)}")
    elif option == "3":
        result = wwcoin.double(coin)
        print(f"--The double of {wwcoin.coin(coin)} is {wwcoin.coin(result)}")
    elif option == "4":
        result = wwcoin.half(coin)
        print(f"--The half of {wwcoin.coin(coin)} is {wwcoin.coin(result)}")
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
            int(coin)
            wwcoin.line()
            print("Choice a operation: "
                  "\n[1] increase."
                  "\n[2] decrease."
                  "\n[3] double."
                  "\n[4] half."
                  "\n[5] Get out")
    wwcoin.line()
