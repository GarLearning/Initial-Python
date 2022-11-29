harnessing_player = dict()
harnessing_team = list()
goals = list()
count = 0
while True:
    count += 1
    harnessing_player["Id"] = count
    harnessing_player["Name"] = str(input("Enter a name of a soccer player: "))
    games = int(input("When games this player played? "))
    print("How many goals this player score?")
    goals.clear()
    total = 0
    for g in range(0, games):
        goal_for_game = (int(input(f"   -In the game {g+1}? ")))
        total += goal_for_game
        goals.append(goal_for_game)
    harnessing_player["Goals"] = goals[:]
    harnessing_player["Total"] = total
    harnessing_player["Average"] = total / games
    harnessing_team.append(harnessing_player.copy())
    while True:
        stop = str(input("You want continue [Y/N]? ")).lower()[0]
        if stop in "yn":
            break
        print(f"this option not accept. try again!")
    if stop in "n":
        break
print("=" * 70)
for k in harnessing_team[0].keys():
    print(f"{k:<15}", end="")
for l in harnessing_team:
    print()
    for v in l.values():
        print(f"{str(v):<15}", end="")#unica forma de printar com lista(q esteja dentro de dic) dentro de um laço, e declarando ela como str
while True:
    more_information = int(input("\nType index of the other player [999 for exit the program]: "))
    if more_information == 999:
        break
    print("=" * 70)
    if more_information > harnessing_team[-1]["Id"]:
        print(f"Id not accept. try again!")
    for r in harnessing_team:
        if more_information == r["Id"]:
            print(f"Information of the player {r['Name']}.")
            for e, a in enumerate(r["Goals"]):
                print(f"    -In the game {e+1}, this player did {a} ", "goals." if r["Goals"] != 1 else "goal.")
            print(f"Your average of goals in the {len(r['Goals'])} games was the {r['Average']}.")
print(f"<<<END PROGRAM>>>")
