frase = str(input('digite um afrase:')).upper()
print('A letra a aparece {} vezes.'.format(frase.count('A')))
print('a primeira letra a apareceu {} posição'.format(frase.replace(' ', '').find('A') + 1))
print('a ultima letra a aparece na {} posição'.format(frase.replace(' ', '').rfind('A') + 1))
