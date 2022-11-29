print("--type your grades--")
n1 = int(input("type your first grade: "))
n2 = int(input("type your second grade: "))
media = (n1 + n2) / 2
if media >= 7:
    print("the student's approved")
elif media < 5:
    print("the student's disapproved")
else:
    print("the student's of recovery")
print("For remember the grade maximum is 10 for test")
