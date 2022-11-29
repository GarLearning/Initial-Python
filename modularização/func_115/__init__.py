from modularização.data import *


def line(size=42):
    print("\033[36m-\033[m" * size)


def menu(items_menu, size=42):
    cont = 1
    line()
    print(f"\033[1;32m{'Menu of the register':^{size}}\033[m")
    line()
    for item in items_menu:
        print(f"\033[33m{cont:>2}- \033[34m{item}\033[m")
        cont += 1
    line()


def print_list(name_doc):
    try:
        open_doc = open(name_doc, "r")
        count = 0
        line()
        print(f"\033[1;32m{'Register People':^42}\033[m")
        line()
        print(f"\033[32m{'  Name':<37}{'Age'}\033[m")
        for pos_line in open_doc.readlines():
            if count % 2 == 0:
                print(f"{f'{pos_line.strip():<35}':>37}", end="")
            else:
                print(f"{pos_line.strip()}")
            count += 1
        line()
        open_doc.close()
    except FileExistsError:
        open_doc = open(name_doc, "w")
        open_doc.close()
        print(f"File {name_doc} create.")
        print(f"Add names with option 2 for print the register.")


def entries(name_doc):
    name = validator_of_name("Your name [stop to out]: ")
    if name in "Stop":
        print(f"\033[31mOperation canceled.\033[m")
    else:
        age = validator_of_int("Your age: ")
        open_doc_r = open(name_doc, "r")
        for read in open_doc_r.readlines():
            while read.strip() == name:
                print(f"The name \033[31m{name}\033[m already exist.")
                print(f"Enter a surname or ID(alphanumeric) in the front name.")
                name = validator_of_name("Your name: ")
        open_doc_r.close()

        open_doc_a = open(name_doc, "a")
        open_doc_a.write(name + "\n")
        open_doc_a.write(str(age) + "\n")
        open_doc_a.close()


def delete(name_doc):
    while True:
        try:
            name = validator_of_name("Name [stop to out]: ")
            if name.lower() in "stop":
                break
            open_doc = open(name_doc, "r")
            word = []
            for c in open_doc.readlines():
                w = c.strip()
                word.append(w)
                open_doc.close()
            deleting = word.index(name)
            word.pop(deleting)
            word.pop(deleting)
            open_doc = open(name_doc, "w")
            for t in word:
                open_doc.write(f"{t}\n")
            open_doc.close()
            break
        except ValueError:
            print("\033[31mName not found. Try again!\033[m")
