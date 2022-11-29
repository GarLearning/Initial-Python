from datetime import date
print("---indication for the category---")
#age = int(input("type your age: "))
nas = int(input("type your date birth: "))
year = date.today().year
age = year - nas
if age <= 9:
    print("your category's little")
elif age <= 14:
    print("you category's childlike")
elif age <= 19:
    print("ypur category's junior")
elif age <= 25:
    print("your category's senior")
else:
    print("your category's master")
u = ('usar modulo data')