age = countage = countm = countf = 0
sex = stop = ""
while True:
    age = int(input("Enter your age: "))
    sex = str(input("Enter your sex: [male/female]")).lower().strip()
    if age > 0 and sex == "male" or sex == "female":
        if age > 18:
            countage += 1
        if sex == "male":
            countm += 1
        if sex == "female" and age < 20:
            countf += 1
        stop = str(input("Do you wish to continue? [yes/no] ")).lower().strip()
    else:
        print("This option, of the sex, not is accept. try again! ")
    if stop != "yes":
            break
print(f"{countage} people over 18 years old.")
print(f"{countm} men was registered.")
print(f"{countf} women are under 20 years old.")
