pt = int(input("type the first term: "))
r = int(input("type the reason: "))
par = pt
print("the first 10 term of this PA is:")
for p in range(1, 11):
    print(par, end=" ")
    par += r
print("\n{:^30}".format("¨¨END¨¨"))