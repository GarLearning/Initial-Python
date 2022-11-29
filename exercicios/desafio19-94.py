register = {}
data_base = []
sun = 0
woman = []
while True:
    register["name"] = str(input("Enter your name: ")).lower()
    register["age"] = int(input("Enter your age: "))
    register["sex"] = str(input("Enter your sex [M/F]")).lower()[0]
    data_base.append(register.copy())
    #stop = str(input("You want continue [Y/N]? ")).lower()[0]
    #while stop not in "ny":#para aceitar n e y juntos é necessario in not alguma condicional
    #    print("Option not accept, try again.")
    #    stop = str(input("You want continue [Y/N]? ")).lower()[0]
    #opção alternativa sem 2 stop
    while True:
        stop = str(input("You want continue [Y/N]? ")).lower()[0]
        if stop in "yn":
            break
        print("Option not accept, try again.")
    if stop == "n":
        break
print(f"- Were register {len(data_base)} people.")
for s in data_base:
    sun += s["age"]
average = sun/len(data_base)
print(f"- The average of the ages are {average}.")
for f in data_base:
    if f["sex"] == "f":
        woman.append(f["name"])
print(f"- The woman register are: ", end="")
for w in woman:
    print(f"{w}", end=", " if w < woman[-1] else ".")
print(f"\n- The greater than average ages: ", end="")
for a in data_base:
    if a["age"] > average:
        print(f"{a['age']}", end=", " if a['age'] != data_base[-1]['age'] else ".")
#os prints de dicionarios dentro de listas sao equivalentes a printes de dicionario
#ao ivez de varios for podia-se colocar a soma das idades por exemplo dentro do while outros que tratavam de agentes do dicionario