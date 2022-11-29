print("\033[1;30m       Analyze condition for home purchase:\033[m")
vc = float(input('\033[7;30mHow much the hose cost?\033[m '))
vs = float(input('\033[1mHow much do you earn?\033[m '))
mp = int(input('\033[7;30mHow years do you want to pay?\033[m '))
et = float(input('\033[1mHow much do you intend to pay?\033[m '))
#valor da prestação mensal, n pode utrapasar de 30% de seu salario(acrescenta ai uma entrada)
vm = (vc - et) / (mp*12)
print('')
if vm < vs * 30 /100:
    print('\033[1;46mAmount of monthly payment is: R${:.2f} \033[m'.format(vm))
else:
    print("\033[1;31mI'm sorry, but your salary doesn't pay the necessary monthly fee.\033[m")
