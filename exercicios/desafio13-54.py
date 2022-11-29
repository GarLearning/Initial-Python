from datetime import date
current = date.today().year
bigger = 0
smaller = 0
for i in range(1,8):
    ano = int(input("person {}ª type your year of birth: ".format(i)))
    age = current - ano
    if age >= 21:
        bigger += 1
    elif age < 21:
        smaller += 1
print("Follow below many people are bigger or smaller:\nbigger = {}.\nsmaller= {}.".format(bigger, smaller))
