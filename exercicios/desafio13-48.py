print("\033[1;37mThe multiples of 3 between 1 and 500:")
so = 0
cont = 0
for soma in range(1, 501):
    if soma%3==0:
        so += soma
        cont += 0
print("The sum of the numbers between 1 and 500 is {} \nWere added {} characters".format(so, cont))