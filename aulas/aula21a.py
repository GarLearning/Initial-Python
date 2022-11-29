#fiz no onenote: exemplos:
#2
'''def soma(a=0, b=0, c=0):
    """hi, test docs strings"""
    global s
    s = a + b + c


soma(4, 4)
print(s)
soma(3, 2, 5)
soma(3, 2)
help(soma)
print("¨" * 30)
print(input.__doc__)
'''

#4
"""num = [1, 2, 3, 4, 5]
n = 5


def number(n):
#    global num
    num = 2
    print(n)
    print(num)


number(num)
print(num)
print(n)"""

#5


"""def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(5, 5, 5)
r2 = soma(4, 4)
r3 = soma(3)
print(f"the sum are respective {r1}, {r2} the {r3}.")
print("¨" * 30)
print(soma(2, 2, 2))"""
"""
 return 
 grade = [73, 67, 38, 33]


def grades(grades):
    return [n if n < 38 or n % 5 < 3 else (n + 5 - (n % 5)) for n in grades]


r = grades(grade)
print(r)

 """