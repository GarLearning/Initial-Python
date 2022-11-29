import wwcoin
import wwcoin109

print("Operations with coins")
coin = float(input("Enter the value: R$"))
wwcoin109.line()
print("Choice a operation: "
      "\n[1] increase."
      "\n[2] decrease."
      "\n[3] double."
      "\n[4] half."
      "\n[5] Get out.")
wwcoin109.line()
while True:
    while True:
        option = str(input("Enter your choice: "))
        if option in "12345":
            break
    if option == "1":
        percent = int(input("How many percent of the value do you want increase? "))#n accept % after number
        print(f"--More {wwcoin.percent(percent)} in {wwcoin.coin(coin)} is {wwcoin109.increase(coin, percent, True)}")
    elif option == "2":
        percent = int(input("How many percent of the value do you want decrease? "))#n accept % after number
        print(f"--Less {wwcoin.percent(percent)} in {wwcoin.coin(coin)} is {wwcoin109.decrease(coin, percent, True)}")
    elif option == "3":
        print(f"--The double of {wwcoin.coin(coin)} is {wwcoin109.double(coin, True)}")
    elif option == "4":
        result = wwcoin.half(coin)
        print(f"--The half of {wwcoin.coin(coin)} is {wwcoin109.half(coin, True)}")
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
