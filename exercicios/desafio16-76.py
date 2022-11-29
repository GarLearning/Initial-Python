#ver se da para definir todas as 1 letras de uma palavra como maiuscula ou minuscula
list = ("Mouse", 99.90, "Keyboard", 129.00, "Headset", 200.00, "Mouse pad", 76.90, "Monitor", 900.00)
print("{}".format("-" * 30))
print("{:-^30}".format("List from battle stage"))
print("{}".format("-" * 30))
for count in range(0, 10):
    if count % 2 == 0:
       print("{:-<20}".format(list[count]), end="")
    else:
        print("${:>7.2f}".format(list[count]))
print("{}".format("-" * 30))
