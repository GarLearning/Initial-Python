grade = {"Name": (str(input("Enter your name: "))), "Average": (float(input("Enter your average: ")))}
if grade["Average"] > 7:
    grade["Situation"] = "Approved"
elif grade["Average"] < 5:
    grade["Situation"] = "Disapproved"
else:
    grade["Situation"] = "Recovery"
print(".-." * 7)
for k, v in grade.items():
    print(f"{k} is {v}")
#abaixo de 7 recuperação
#abaixo de 5 reprovado
#+ 7 aprovado