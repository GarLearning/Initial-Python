print('teste cor e fundo')
print('\033[1;31;42mola mundo')
print('\033[4;34;47mola tudo bien\033[m')
print('\33[1;30mnormal')
print('\033[7;30minversao')
print('\033[7;31mincerso de vermelho\033[m')
print('-'*80)
print('\033[0;33;44mnormal')
print('\033[7;33;44minverso do anterior\033[m')
print('-'*80)
a = 3
b = 5
print('o valor 1 é de \033[32m{}\033[m e o 2 é de \033[34m{}\033[m!!!!'.format(a, b))
print('-'*80)
nome = 'gabriel'
print('nice to meet you, {}{}{}!!!!'.format('\033[4;35m', nome, '\033[m'))
print('-'*80)
nome = 'irineu vc n sabe nem eu!!'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
print('o seu nome é {}{}{}'.format(cores['pretobranco'], nome,cores['limpa']))
