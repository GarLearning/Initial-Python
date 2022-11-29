def validator_of_float_br(inp):
    while True:
        not_accept = comma_dot = 0
        resulte = str(input(inp)).strip()
        if resulte in "":
            print("try again")
            not_accept = 1
        for result in resulte:
            if result in ",." and comma_dot == 1:
                print("try again")
                not_accept = 1
                break
            if (result.isnumeric() or result in ",.") is False:
                print("try again")
                not_accept = 1
                break
            elif result in ",.":
                comma_dot = 1
        if not_accept == 0:
            break
    return float(resulte.replace(",", "."))


def validator_of_float_eua(inp):#refeito com tratamento de erro
    while True:
        try:
            result = float(input(inp))
        except ValueError:
            print(f"\033[31mThis isn't accept. try again!\033[m")
            continue
        else:
            return result


def validator_of_response(inp):
    while True:
        stop = str(input(inp)).lower().strip()
        if stop not in "ny" or stop in "":
            print("\033[31mThis isn't accept. try again!\033[m")
            continue
        else:
            return stop


def validator_of_int(inp):#refeito com tratamento de erro
    while True:
        try:
            number_int = int(input(inp))
        except ValueError:
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            return number_int


def validator_of_name(inp):
    while True:
        word_inp = str(input(inp)).lower().strip().title().replace(" ", "pus")
        if word_inp.isalpha() is False:
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            word_inp = word_inp.replace("pus", " ")
            return word_inp
