"""count = 0
table = ("Santos", "Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Corinthians", "Internacional",
"Athletico-PR", "Botafogo", "Bahia", "Ceará", "Goiás", "Grêmio", "Fortaleza",
"Vasco", "Cruzeiro", "Chapecoense", "Fluminense", "CSA", "Avaí")
for table in table:
    '''print(f"The word {table}, have the syllables", end=": ")
    count =1
    if "a" in table:
        print("a", end=" ")
    elif "e" in table:
        print("e", end=" ")
    elif "i" in table:
        print("i", end=" ")
    elif "o" in table:
        print("o", end=" ")
    elif "u" in table:
        print("u", end=" ")""""""
    else:
        print("Have 0 syllables, or the syllables have letters:\n-Capital letters\n-syllables with accent")
    if count != 0:
        print("\n")'''
#ta printando letas em listas (cadas letra é um termo da lista)
#    print(table)
    print(sorted(table))"""
a = (5, 5, 5)
b = (5, 5, 5)
if a == b:
    print("oi")
else:
    print("hello")