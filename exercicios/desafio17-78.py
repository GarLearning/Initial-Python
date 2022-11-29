c = 2
count2 = count3 = 0
numb = []
for n in range(0, 5):
    numb.append(int(input("Enter a number: ")))
nums = numb[:]
bigger = max(numb)
smaller = min(nums)

a = numb
b = numb[::-1]

if a != b:
    print(f"The bigger number is {max(numb)}", end="")
    big = numb.count(bigger)
    print(f" in the position(s) {numb.index(bigger)+1}", end="" if big > 1 else "\n")
    while big > 2:
        del numb[numb.index(bigger)]
        print(f", {numb.index(bigger)+c}", end="")
        big -= 1
        c += 1
    if big == 2:
        del numb[numb.index(bigger)]
        print(f" and {numb.index(bigger)+c}.")


    c = 2
    print(f"The smaller number is {min(nums)}", end="")
    smal = nums.count(smaller)
    print(f" in the position(s) {nums.index(smaller)+1}", end="" if smal > 1 else "\n")
    while smal > 2:
        del nums[nums.index(smaller)]
        print(f", {nums.index(smaller)+c}", end="")
        smal -= 1
        c += 1
    if smal == 2:
        del nums[nums.index(smaller)]
        print(f" and {nums.index(smaller)+c}.")
else:
    print(f"All terms typed are {numb[0]}")

"""
#tava tentando fazer assim
print(f"The smaller number is {smaller}", end='')
smal = num.count(smaller)
if smal > 1 or big > 1:
    print(f" in the position(s) {nums.index(smaller)+c}", end="")
    while smal > 2:
        c += 1
        del num[num.index(smaller)]
        print(f", {num.index(smaller)+c}", end="")
        c += 1
        smal -= 1
    if smal == 2:
        c += 1
        del num[num.index(smaller)]
        print(f" and {num.index(smaller)+c}")
else:
    print(f" in the position(s) {num.index(smaller) + 1}")"""


#for mais enumeric da para fazer caso aja numeros repitidos para indentificar suas respectivas posições