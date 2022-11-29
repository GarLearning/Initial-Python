from random import randint
from emoji import emojize
num = count = computer = player = 0
print("¨¨¨-¨¨¨Let's go EVEN OR ODD¨¨¨-¨¨¨")
while True:
    num = int(input("Enter a number: "))
    computer = randint(0, 10)
    player = str(input("EVEN OR ODD: [E/O]")).lower().strip()
    if (num + computer) % 2 == 0 and player == "e" or (num + computer) % 2 == 1 and player == "o":
        print("{}".format("Winner Winner chicken dinner"), f"\nThe computer play {computer} and you {num}.")
    if (num + computer) % 2 == 0 and player == "o" or (num + computer) % 2 == 1 and player == "e":
        break
    count += 1
print(emojize(f"You lose :grin: the computer typed {computer} and you {num}:cry:", use_aliases=True))
while player not in "eo":
   player = str(input("EVEN OR ODD: [E/O]")).lower().strip()[0]
#nesse caso enquanto a variavel player n for e ou o como resposta vai ficar em um loop até receber e ou o, o [0] no final faz um fatiamento so para a primeira letras