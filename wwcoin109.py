# functions of programs
def increase(value, rate, form=False):
    result = ((value * rate) / 100) + value
    return result if form is False else coin(result)


def decrease(value, rate, form=False):
    result = value - ((value * rate) / 100)
    return result if form is False else coin(result)


def double(value, form=False):
    result = value * 2
    return result if form is False else coin(result)


def half(value, form=False):
    result = value / 2
    return result if form is False else coin(result)


# line
def line():
    print("¨¨" * 20)


# print of values
def coin(value):
    return f"R${value:.2f}".replace(".", ",")


def percent(value):
    return f"{value}%"
