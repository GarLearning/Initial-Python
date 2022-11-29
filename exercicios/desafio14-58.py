from random import randint
couter = 0
#guess = int(input("Enter one number between 0 and 10: "))
compug = randint(0, 10)
guess = 11
while guess != compug:
    guess = int(input("Enter one number between 0 and 10: "))
    couter += 1
    if guess < compug:
        print("Is a number bigger.")
    elif guess > compug:
        print("Is a number smaller.")
print("The number whit computer selected was {}".format(compug))
print("You're right in the {} chance.".format(couter))