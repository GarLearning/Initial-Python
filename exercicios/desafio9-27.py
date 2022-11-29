nome = str(input('digite seu nome:')).strip()
n = nome.split()
print('seu 1 nome é {} e o seu ultimo nome {}, prazer!!! '.format(n[0], n[len(n)-1]))
