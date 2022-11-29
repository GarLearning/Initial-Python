tabuada = int(input("type a number for table of multiplication: "))
print("""Choice one operation:
For sum [1]
For subtraction [2]
For division [3]
For multiplication [4]""")
ope = int(input("Your option of operation: "))
for t in range(0, 11):
#    if ope == 1:
 #       print('{} + {:2} = {}'.format(tabuada, t, tabuada + t))
#    elif ope == 2:
#        print('{} - {:2} = {}'.format(tabuada, t, tabuada - t))
 #   elif ope == 3:
  #      print('{} / {} = {:2}'.format(tabuada, t, tabuada % t))
 #       print("This is whole part of division ")
 #   if ope==4:
        print('{} x {:2} = {}'.format(tabuada, t, tabuada*t))
#    else:
#        print("This operation not's acceptd")
#COMENTEI TUDO PQ O RESTO E "INUTIL"