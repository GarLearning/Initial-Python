from random import randint
print("=====jokenpo=====")
list = ["rock", "paper", "scissors"]
result = randint(0, 2)
print(" * For rock type 0 \n * For paper type 1 \n * For scissors type 2")
player = int(input("what's your choice? "))
#game = {"0": "rock", "1": "paper", "2": "scissors"}
#game = {}
#game["0"] = "rock"
#game["1"] = "paper"
#game["2"] = "scissors"
#value = game ["player"]
if result == 0:
    if player == 0:
        print("draw")
    elif player == 1:
        print("You win")
    elif player == 2:
        print("You lose")
    else:
        print("Input does't accept")
if result == 1:
    if player == 0:
        print("You lose")
    elif player == 1:
        print("draw")
    elif player == 2:
        print("You win")
    else:
        print("Input does't accept")
if result == 2:
    if player == 0:
        print("You win")
    elif player == 1:
        print("You lose")
    elif player == 2:
        print("draw")
    else:
        print("Input does't accept!")
if result == 0:
    print("The computer played rock!")
elif result == 1:
    print("The computer played paper!")
elif result == 2:
    print("The computer played scissor!")