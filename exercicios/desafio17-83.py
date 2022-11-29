lista = list()
phrase = str(input("Enter a phrase: ")).lower()
for phrase in phrase:
    lista.append(phrase)
left = lista.count("(")
right = lista.count(")")
if left == right:
    print("The parentheses are in correct order. ")
else:
    print(" The parentheses are in wrong order.")


#solução do guanabara
"""print(f"{'-'*10}")
expr = str(input("Enter a number: "))
pilha = []
for s in expr:
    if s == "(":
        pilha.append("(")
    elif s == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Your expression is valid.")
else:
    print("This expression is not valid.")"""