def bigger(*num):
    '''maior = cont = 0'''
    for n in num:
        print(f"{n}", end=" ")
        '''       if maior == 0:
                   cont = n
               else:
                   if n > cont:
                       cont = n
               maior += 1'''
    print(f"was the values informed.\nThe bigger among the {len(num)} is {max(num)}.")
    print("-=" * 20)


bigger(3, 51, 3, 4, 6, 78)
bigger(4, 3)
bigger(1000, 3, 700, 2)
