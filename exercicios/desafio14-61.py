print("¨¨Calculating a PA¨¨")
first_term = int(input("Enter the fir term of PA: "))
reason = int(input("Enter the reason of the PA: "))
"""pa10 = first_term + (10 - 1) * reason
pa = first_term
sum = 0
while pa != pa10 + reason:
#for n in range(1, 11):
    print(pa, end="")
    print(", " if pa < pa10 else "", end="")
    sum += pa
    pa += reason
print("\nThe sum of the terms of PA is: {}.".format(sum))"""
pa = first_term
count = 1
sum = 0
while count <= 10:
    print(pa, end="")
    print(", " if count < 10 else "", end="")
    sum += pa
    pa += reason
    count += 1
print("\nThe sum of the terms of PA is: {}".format(sum))