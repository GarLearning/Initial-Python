



#delete
"""name = str(input("name: "))
d = open("list_names_age", "r")
word = []
for c in d.readlines():
    w = c.strip()
    word.append(w)
    d.close()
delete = word.index(name)
word.pop(delete)
word.pop(delete)
d = open("list_names_age", "w")
for t in word:
    d.write(f"{t}\n")
d.close()
"""

"""name = str(input("name: "))
d = open("list_names_age", "r")
found = 0
for c in d.readlines():
    f = c.count(name)
    found += f
print(found)
d.close()
d = open("list_names_age", "w")
d.
"""

#print
"""d = open("list_names_age", "r")
count = 0
for c in d.readlines():
    if count % 2 == 0:
        print(f"{c.strip()}", end="    ")
    else:
        print(f"{c.strip()}")
    count += 1"""
