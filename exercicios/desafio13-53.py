phra = str(input("type the phrase: ")).strip().upper()
word = phra.split()
tog = "".join(word)
con = tog[:: -1]
#con = ""
#for letter in range (len(tog) -1, -1, -1):
#    con += tog[letter]
print("The word typed, no spaces, is \033[33m{}\033[m.\nThe your converse, no spaces, is \033[34m{}\033[m.".format(tog, con))
if tog == con:
    print("\033[1;32mThe word typed is a palindrome.")
else:
    print("\033[1;31mThis word not's palindrome.")