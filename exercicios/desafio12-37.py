num = int(input('type a number for desired base conversion:'))
#bis = str(input('''--binary--octal--hexadecimal--
#Which base you desire for conversion?'''))
print("""To base conversion desired, type:
[1]for binary base.
[2]for octal base.
[3]for hexadecimal base.
[4]for all bases above.""")
bis = (input("your option: "))
if bis == 1 or bis == 'binary':
    print('conversion de decimal para binary é {}'.format(bin(num)[2:]))
elif bis == 2 or bis == 'octal':
    print('conversion of decimal for octal is {}'.format(oct(num)[2:]))
elif bis == 3 or bis == 'hexadecimal':
    print('conversion of decimal for hexadecimal is {}'.format(hex(num)[2:]))
elif bis == 4 or bis == 'all bases':
    print("""conversion of all bases is:
    {} in binary
    {} in octal
    {} in hexadecimal""".format(bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('The base for conversion is not accepted.')
#n aceita binary e o numero 1