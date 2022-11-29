from random import randint
from time import sleep, strftime
print("-" * 30)
print(f"Number random for PowerBoll")
print("-" * 30)
powerboll = []
sort = []
game = 0
num = int(input("Want games you are sorted: "))
for n in range(1, num+1):
    for l in range(0, 6):
        luck = randint(1, 60)
        while luck in sort:
            luck = randint(1, 61)
        sort.append(luck)
    sort.sort()
    powerboll.append(sort[:])
#    print(f"Game {n}: {sort}")
    sort.clear()
for m in range(0, num):
    print(f"\nGame {game+1}: ", end="")
    for s in powerboll[game]:
        print(f"{s}", end=", " if s != powerboll[game][-1] else ".")
    sleep(1)
    game += 1
hour = strftime("%H:%M, %p")
print()
print(f"\n{'This are your games':^30}")
print(f"\n{'Good Luck!!!'}{hour:>19}")
