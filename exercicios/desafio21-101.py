"""def vote(birthday):
    from time import strftime
    year = strftime("%Y")
    ages = int(year) - birthday
    return ages


age = vote(int(input("year your birth? ")))
if 70 > age >= 18:
    print(f"You have {age} years and required your vote.")
elif age < 16:
    print(f"You have {age} years and can't vote.")
else:
    print(f"You have {age} years your vote is optional.")
"""

#resolução guanabara
def vote(birthday):
    from datetime import date
    ages = date.today().year
    age = int(ages) - birthday
    if 70 > age >= 18:
        return f"You have {age} years and required your vote."
    elif age < 16:
        return f"You have {age} years and can't vote."
    else:
        return f"You have {age} years your vote is optional."


#prog principal
print(vote(int(input("year your birth? "))))
