print("¨¨Calculating a PA¨¨")
first_term = int(input("Enter the first term of PA: "))
reason = int(input("Enter the reason of the PA: "))
pa = first_term
count = 1
sum = 0
end = 1
term = 0
count2 = 0
while count < 10:
    print(pa if count == 1 else "", end="")
    print(", " if count < 10 else "", end="")
    sum += pa
    pa += reason
    count += 1
    print(pa, end="")
while end != 0:
    term = int(input("\nHow much more terms of the PA you want? "))
    if term != 0:
        mud_reason = str(input("You want change the reason? [yes, no] ")).lower().strip()
    if mud_reason == "yes":
       reason = int(input("Enter the new reason: "))
    count2 = 0
    end = term
    while count2 != term:
        pa += reason
        count2 += 1
        print(pa, end="")
        print(", " if count2 < term else "", end="")
        sum += pa
print("\nThe sum of the terms of PA is: {}".format(sum))