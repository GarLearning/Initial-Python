from modularização.func_115 import *#ta importando tudo de modularização e de função
from time import sleep


while True:
    menu(["Print the register.", "Register the other name.", "Delete of the registers.", "Out the program."])
    while True:
        option = validator_of_int("Enter a option: ")
        if option not in (1, 2, 3, 4):
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            break

    if option == 1:
        print_list("list_names_age")
        sleep(1.5)

    elif option == 2:
        line()
        entries("list_names_age")
        line()
        sleep(1.5)

    elif option == 3:
        line()
        delete("list_names_age")
        line()
        sleep(1.5)

    elif option == 4:
        line()
        print(f"\033[1;32m{'Program Ends':^42}\033[m")
        line()
        break
#opção de admin: so ele deleta, escolhe trocar de lista