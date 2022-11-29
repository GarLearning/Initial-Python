from random import randint
bigger = smaller = 0
sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#for sorte in sort: (printa sorta na quantidade de termos de sort)
print("\033[34mThe numbers typed are:\033[m")
for s in sort:
    print(s)
"""    print("\033[31m", sort)
    if bigger == 0 and smaller == 0:
        bigger = smaller = sort
    elif sort > bigger:
        bigger = sort
    elif sort < smaller:
        smaller = sort"""
print(f"\033[1;33mThe bigger number is {max(sort)} and the smaller number is {min(sort)}")