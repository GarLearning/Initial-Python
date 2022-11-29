#fazer forma de pagamento com numeros negativos
#imports
from time import strftime
#variaveis
value = cedulas = resto = 0
hour = strftime("%H:%M, %p")
#execução/entradas
print("{:-^40}".format("\033[1mYour Bank\033[m"))
value = int(input("What withdrawal amount: "))
print("{:-^40}".format("\033[1mYou'll receive\033[m"))
if value > 50:
    cedulas = value // 50
    resto = value % 50
    value = resto
    print(f"-{cedulas} Banknotes of the $50.00.")
if value > 20:
    cedulas = value // 20
    resto = value % 20
    value = resto
    print(f"-{cedulas} Banknotes of the $20.00.")
if value > 10:
    cedulas = value // 10
    resto = value % 10
    value = resto
    print(f"-{cedulas} Banknotes of the $10.00.")
if value > 0:
    cedulas = value // 1
    print(f"-{cedulas} Banknotes of the $1.00.")
#saida
print("{:-^37}".format("\033[1mHave a good day!"))
print(f"{hour:>33}")