from random import randint
from time import sleep

number = []


def draw(rand):
    for n in range(0, 5):
        rand.append(randint(1, 9))
    print(f"The numbers drawn are: ")
    for num in rand:
        print(f"{num}", end=" ")
        sleep(0.5)


def sum_pair(lst):
    pair_list = []
    print()
    print("-" * 30)
    sun = cont = 0
    for pair in lst:
        if pair % 2 == 0:
            sun += pair
            cont += 1
            pair_list.append(pair)
    if cont > 1:
        print(f"The sum of the pair numbers ", end=" ")
        for p in pair_list:
            print(f"{p}", end=", " if p != pair_list[-1] else " ")
        print(f"are {sun}.")
    if cont == 1:
        print(f"The only value drawn pair is {sun}.")
    elif cont == 0:
        print(f"Not have none value pair.")


draw(number)
sum_pair(number)
