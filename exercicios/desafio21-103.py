def token(name="<unknown>", goals=0):
    print("¨¨" * 20)
#    if name == "":
#        name = "<unknown>"
#essas duas linhas n são necessarias se o parametro for declarado como unknown(mais é necessario o if do token, pq senao o name_player fica sem valor se n colocado nada)
    return f"The player {name} did {goals} goal(s) in the championship!!"


name_player = str(input("what the name of player: ")).strip().title()
goals_player = str(input("How many goals this player did: "))

if goals_player.isnumeric():
    goals_player = int(goals_player)
else:
    goals_player = 0

if name_player == "":
    print(token(goals=goals_player))
else:
    print(token(name_player, goals_player))
