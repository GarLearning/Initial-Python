harnessing = dict()
goals = list()
total = 0
harnessing["Name"] = str(input("Enter a name of a soccer player: "))
games = int(input("When games this player played? "))
for g in range(0, games):
    goals.append(int(input(f"How many goals did this player score, in the game {g+1}? ")))
harnessing["Goals"] = goals
for s in goals:
    total += s
harnessing["Total"] = total
print("", ("-=" * 29), "\n", harnessing, "\n", "-=" * 29)
for k, v in harnessing.items():
    print(f"The field {k} has a value {v}.")
print("", "-=" * 29)
print(f"The player {harnessing['Name']} played {games} games.")
for n, c in enumerate(harnessing["Goals"]):
    print(f"=> In the game {n+1}, did {c}.")
