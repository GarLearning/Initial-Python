num = table = 0
print("{:-^36}\nfor stop type a negative number".format("MULTIPLICATION TABLE"))
while True:
    num = int(input("Enter the multiplication table: "))
    if num < 0:
        break
    for t in range(1, 11):
        print(f"{num} x {t:02} = {num*t}")
print("{:-^36}".format("END"))