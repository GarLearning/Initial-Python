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


#abstract
def abstract(value=0, rate_above=0, rate_below=0):
    line()
    print(f"{'Abstract of value':^40}")
    line()
    print(f"{'Price analyze: ':<30}{coin(value)}")
    print(f"{f'Increase {percent(rate_above)}: ':<30}{increase(value, rate_above, True)}")
    print(f"{f'Decrease {percent(rate_below)}: ':<30}{decrease(value, rate_below, True)}")
    print(f"{'The double: ':<30}{double(value, True)}")
    print(f"{'The half: ':<30}{half(value, True)}")
