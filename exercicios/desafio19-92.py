from datetime import datetime
calculation = 0
register = dict()
register["Name"] = str(input("Enter your name: ")).lower().capitalize()
register["Sex"] = str(input("Enter your sex [M/F]: ")).upper()[0]
register["Age"] = int(input("Enter your birthday: "))
register["Work card"] = int(input("Enter your work card [0 case don't have]: "))
if register["Work card"] != 0:
    register["Hiring"] = int(input("Enter the year of your hiring: "))
    register["Salary"] = float(input("Enter your salary: "))
    time_stop = str(input("Was out for work over 1 year [Y/N]: ")).lower()[0]
    if time_stop == "y":
        calculation = int(input("For how many years: "))
    register["Age"] = datetime.now().year - (register["Age"])
    if register["Sex"] == "M":
        register["Sex"] = "Male"
        register["Retirement"] = 35 - (datetime.now().year - register["Hiring"]) + register["Age"] + calculation
    elif register["Sex"] == "F":
        register["Sex"] = "Female"
        register["Retirement"] = 30 - (datetime.now().year - register["Hiring"]) + register["Age"] + calculation
print("= " * 15)
for k, v in register.items():
    print(f"- {k} is {v}.")