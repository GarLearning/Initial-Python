num = int(input('digite um numero(entre 0 e 9999):'))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('O numero {} tem: \n {} unidades \n {} dezenas \n {} centemas \n {} milhar'.format(num, u, d, c, m))