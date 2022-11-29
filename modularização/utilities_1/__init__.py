#functions of programs
def increase(value, rate):
    return ((value*rate) / 100) + value


def decrease(value, rate):
    return value - ((value*rate) / 100)


def double(value):
    return value*2


def half(value):
    return value/2


#line
def line():
    print("¨¨" * 20)


#print of values
def coin(value):
    return f"R${value:.2f}".replace(".", ",")


def percent(value):
    return f"{value}%"