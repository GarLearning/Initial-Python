count = error = 0
print("Have 0 syllables, or the syllables have letters:\n-Capital letters\n-syllables with accent\n")
table = ("Santos", "Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Corinthians", "Internacional",
"Athletico-PR", "Botafogo", "Bahia", "Ceará", "Goiás", "Grêmio", "Fortaleza",
"Vasco", "Cruzeiro", "Chapecoense", "Fluminense", "CSA", "Avaí")
for table in table:
    print(f"The word {table}, have the syllables", end=": ")
    count = 1
    if "a" in table:
        error += 1
        print("a", end=" ")
    if "e" in table:
        error += 1
        print("e", end=" ")
    elif "i" in table:
        error += 1
        print("i", end=" ")
    if "o" in table:
        error += 1
        print("o", end=" ")
    if "u" in table:
        error += 1
        print("u", end=" ")
    if error == 0:
        print("Have 0 syllables, or the syllables have letters:\n-Capital letters\n-syllables with accent")
    if count != 0:
        print("\n")
    error = 0