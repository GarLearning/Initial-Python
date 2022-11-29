import math
ang = int(input('digite um angulo:'))
co = math.cos(math.radians(ang))
se = math.sin(math.radians(ang))
ta = math.tan(math.radians(ang))
print(' o seno é: {:.2f} \n o coseno: {:.2f} \n o tangente é: {:.2f}'.format(co, se, ta))
