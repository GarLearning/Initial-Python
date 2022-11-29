bi = int(input('digite um ano:'))
#se = bi%4
#if se == 0:
#    if bi%100 != 0:
if bi % 4 == 0 and bi % 100 != 0 or bi % 400 == 0:
    print('o ano {} é bissexto'.format(bi))
else:
    print('o ano {} nao e bissexto'.format(bi))
