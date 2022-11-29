from datetime import date
ant = date.today().year
print("-----type date with numbers-----")
ano = int(input('type the your year of birth? '))
#ant = int(input('type too the year you are? '))
mes = int(input('what month are you? '))
al = ano + 18
if ant == al and mes < 6:
    print("\033[4;33myou have to july of this year for your if enlistment\033[m")
elif ant < al:
    print("\033[34mare still missing {} for the enlistment\033[m".format(al - ant))
else:
    print("\033[1;31mthe date from enlistment already passed\033[m")
