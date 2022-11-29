price_p = total_spent = more_ot = count = 0
name_p = cheaper = stop = ""
while True:
    name_p = str(input("Name of the product: "))
    price_p = float(input("Price of the product: $"))
    total_spent += price_p
    if price_p > 1000:
        more_ot += 1
    if count == 0:
        count = price_p
        cheaper = name_p
    elif price_p < count:
        cheaper = name_p
    stop = str(input("You want continue the input products? [yes/no]")).strip().lower()
    if stop == "no":
        break
print(f"The total spend in your purchase was from {total_spent:.2f}")
if more_ot > 1:
    print(f"{more_ot} product costs more of the $1000.")
else:
    print(f"{more_ot} products costs more of the $1000.")
print(f"The product cheaper is {cheaper}")
