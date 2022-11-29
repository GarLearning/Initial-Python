def validator_of_float(inp):
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


def validator_of_response(inp):
    while True:
        stop = str(input(inp)).lower().strip()
        if stop not in "ny" or stop in "":
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            break
    return stop


def validator_of_int(inp):
    while True:
        number_int = str(input(inp))
        if number_int.isnumeric() is False or number_int in "":
            print("\033[31mThis isn't accept. try again!\033[m")
        else:
            break
    return int(number_int)
