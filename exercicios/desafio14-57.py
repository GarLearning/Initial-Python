print("----Inform the sex----\nF for female or M for male")
sex = str(input("insert on here:")).lower().strip()[0]
#while sex != "m" or sex != "f":
#while sex not in "fm":
while sex == "mf":
    sex = str(input("{} was the typed, isen't accepted\nEnter sex here: ".format(sex))).lower().strip()[0]
print(sex)