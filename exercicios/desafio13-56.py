sum = 0
lesst = 0
moreold = 0
nam = ""
for n in range(1, 6):
    print("{}ª person".format(n))
    name = str(input("Enter your name: ")).lower().strip()
    age = int(input("Enter your age: "))
    sex = str(input("Enter F for woman, or M for man:")).lower().strip()
    sum += age
    if sex == "m" and n == 1:
        moreold = age
        nam = name
    if moreold < age and sex == "m":
            moreold = age
            nam = name
    if sex == "f" and age < 20:
        lesst += 1
average = sum/5
print("The average from the age of group is {}.".format(average))
print("The man more old is {}.".format(nam))
print("In the group exist {} woman whit any less 20.".format(lesst))