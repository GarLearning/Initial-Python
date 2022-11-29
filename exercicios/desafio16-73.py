count = 0
table = ("Santos", "Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Corinthians", "Internacional",
"Athletico-PR", "Botafogo", "Bahia", "Ceará", "Goiás", "Grêmio", "Fortaleza",
"Vasco", "Cruzeiro", "Chapecoense", "Fluminense", "CSA", "Avaí")
print("{:-^40}".format("The top five teams are"))
for top in range(0, 5):
    count += 1
    print(count, table[top])
count = 0
print("{:-^40}".format("The last four are"))
for last in range(4, -1, -1):
    tl = table[:0:-1]
    print(table.index(tl[last])+1, tl[last])
print("{:-^40}".format("The teams in order"))
for alf in range(0, 20):
    orga = sorted(table)
    print(count + 1, orga[count])
    count += 1
print("The Chapecoense is in the {}ª position.".format(table.index("Chapecoense")+1))
#para colocar aspas dentro de aspas, como em um format(f""), basta colocar "" se a de fora for '' ou vice versa