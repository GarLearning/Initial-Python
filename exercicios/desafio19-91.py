from random import randint
from operator import itemgetter#modulo usado para ordenar valores em um dicionario, sendo key=itemgetter() a forma de chamar o modulo
# o 0 trata das chaves e 1 dos valores
from time import sleep
count = 1
dice = {"player1": 0, "player2": 0, "player3": 0, "player4": 0}
for d in dice.keys():
    rand = randint(1, 6)
    dice[d] = rand
for k, v in dice.items():
    print(f"The {k} took {v} in dice.")
    sleep(0.7)
print("=" * 30)
for k, v in sorted(dice.items(), key=itemgetter(1), reverse=True):
    print(f"{count}º place {k} with {v}.")
    count += 1
    sleep(1)